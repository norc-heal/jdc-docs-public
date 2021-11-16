''' 
code to format, copy, or make or append any necessary 
files for JDC documentation with mkdocs.

this includes the mkdocs.yml config file or making
actual markdown files
'''
import pandas as pd
import tabulate
import os
import re
from io import StringIO
import hashlib
import requests

from gen3.auth import Gen3Auth
from gen3.submission import Gen3Submission
from gen3.index import Gen3Index
import numpy as np

from pathlib import Path
import yaml
from jsonpath_ng import parse
import json 

from collections.abc import Iterable

import glob
# get variable categories of core measures
credentials_path = Path('credentials.json')
endpoint = 'https://jcoin.datacommons.io'
auth = Gen3Auth(refresh_file=credentials_path.as_posix())
index = Gen3Index(endpoint, auth)
sub = Gen3Submission(auth)

def get_dictionary(endpoint,node_type):
    api_url = f"{endpoint}/api/v0/submission/_dictionary/{node_type}"
    output = requests.get(api_url).text
    data = json.loads(output)
    return data

def get_possible_values(prop_name,prop):
    ''' 
    get a human-readble description of possible values 
    -- this will be either be a restricted list of values
    from the enum parameter or a type of value (eg string)
    from the type value.

    for similar gen3 data-portal fxn to form DD table: 
        see getType fxn in data-portal/src/DataDictionary/utils.js
    
    ''' 
    if 'enum' in prop:
        #enums are lists -- add to flat list
        return {prop_name:prop['enum']}
    elif 'type' in prop:
        #type is a string
        return {prop_name:prop['type']}
    elif 'oneOf' in prop:
        #get list of types
        one_of_types = [
            match.value 
            for match in parse('$..type').find(prop)
            if match 
        ]
        #get enum and flatten multiple enum lists
        one_of_enum = [
            match.value
            for match in parse('$..enum[*]').find(prop)
            if match 
        ]
        return {prop_name:one_of_enum+one_of_types}
        
    elif 'anyOf' in prop:
        #get the properties json parse object with properties dictionary
        #note -- for some reason these properties were duplicated (hence the anyOf[0])..not sure why
        any_of_props = parse("$.anyOf[0]..properties").find(prop)[0].value
        items = {}
        for anyof_prop_name,anyof_prop in any_of_props.items():
            items.update(get_possible_values(f"{prop_name}.{anyof_prop_name}",anyof_prop))
        return items
    else:
        return {prop_name:["UNDEFINED"]}


def get_description(prop_name,prop):
    ''' 
    get human readable description of property. 

    Descriptions are either added directly to node 
    property or referenced via __terms or __definition 
    "hidden" nodes.

    Theoretically, there could be more than one description
    if in node properties and also in hidden node so this accounts
    for that scenario by returning all matches from json expression

    if node is a link, then collect all these descriptions
    ''' 
    
    if 'anyOf' in prop:
        #get the properties json parse object with properties dictionary
        #note -- for some reason these properties were duplicated (hence the anyOf[0])..not sure why
        any_of_props = parse("$.anyOf[0]..properties").find(prop)[0].value
        items = {}
        for anyof_prop_name,anyof_prop in any_of_props.items():
            items.update(get_description(f"{prop_name}.{anyof_prop_name}",anyof_prop))
        return items
    else:
        description_json = parse("$..description").find(prop)
        descriptions = [match.value for match in description_json if match]
    
        if descriptions:
            return {prop_name:descriptions}
        else:
            return {prop_name:["No description"]}

#TODO: Relationship to Core measures document

def make_data_dictionary(endpoint,node_list=None):
    ''' iterate through the entire dictionary and get possible values and descriptions
    (only if dictionary item is a node (ie has properties)), returning a data dictionary 
    as a dataframe with node name, property name, property description, and possible values

    Can specify a given set of nodes
    '''
    dictionary = get_dictionary(endpoint,'_all')
    nodes = []
    if not node_list:
        node_list = dictionary.keys()

    for node_name,props in dictionary.items():

        format_title = lambda x: x.replace("_"," ").title()
        node_title = props.get('title',format_title(node_name))
        node_description = props.get('description','No description')
        system_properties = props.get("systemProperties",[])

        is_in_props = 'properties' in props
        is_in_node_list = node_name in node_list
        is_not_system_prop = node_name not in system_properties

        if is_in_props and is_in_node_list and is_not_system_prop:
            possible_values = {}
            descriptions = {}
            for prop_name,prop in props['properties'].items():
                possible_values.update(get_possible_values(prop_name,prop))
                descriptions.update(get_description(prop_name,prop))
                #TODO: return dictioanry instead of df
            node_properties = pd.DataFrame(
                {'possible_values':possible_values,
                'descriptions':descriptions}
            )
            # append the overall list with the node info and formmated property tbl
            ## leaving out dictionary entries without properties            
            nodes.append({
                'name':node_name,
                'title':node_title,
                'description':node_description,
                'properties_tbl':node_properties
            })
    return nodes 


def get_node_list():
    return yaml.safe_load(open('config.yaml','r'))['nodes']

data_dictionaries = make_data_dictionary(endpoint,get_node_list())

# TODO: make a mkdocs_json and populate OEPS and JCOIN measure pages
## for minimum viable value - hardcoded json/yaml

# mkdocs_json = {
#     "site_name": "JCOIN Data Commons",
#     "site_url": "https://example.com",
#     "nav":[],
#     "use_directory_urls": True,
#     "markdown_extensions": [{"toc": {"permalink": "##"}}],
#     "plugins":["search","mermaid2"]
# }

mkdocs_json = {'JCOIN Variables':[]}
for node in data_dictionaries:
    
    dd = node['properties_tbl'] #dd=data_dictionary

    #format data dictionary for html table to be inserted into makrdown file
    #note, markdown tables were causing issues with special characters so 
    # decided to just insert the html version of table which seems to be rendering correctly
    dd_md = (
        dd[['descriptions','possible_values']]
        .rename(
            columns={'descriptions':'Description','possible_values':'Possible Values'}
        )
        .rename_axis('Variable Name')
        .applymap(lambda x: '<br>'.join(x) if type(x) is list else x)
        .applymap(lambda x: x.replace('\n','') if type(x) is str else x)
        .reset_index()

        # update: explicitly encoding md files as utf-8 allows decoding of these characters
        #  
        #the weird quotes are giving a utf-8 encoding error so replacing with regular quotes
        #alternatively, could put the html codes in for these values &#8220; and &#8221	
        #.applymap(lambda x: x.replace('“','"').replace("”",'"').replace("–","-") if type(x) is str else x)
    )
    # if node['name']=='baseline_demographics':
    #     test_df = dd_md
    doc_dir = f"docs/nodes/{node['name']}.md"
    mkdocs_json['JCOIN Variables'].append({node['title']:doc_dir})

    with open(doc_dir,'w',encoding='utf-8') as f:
        node_description = (
            f"# {node['title']} Variables\n\n{node['description']}\n\n"
        )
        f.write(node_description)

        #escape=False to allow <br> tag for table cells --
        #  may want to allow others to be escaped but need to manually code
        f.write(dd_md.to_html(escape=False,index=False))
    

# OEPS
# get markdown docs from gen3

# TODO: extract info from Core Measure Document 

# make the mkdocs.yml file
