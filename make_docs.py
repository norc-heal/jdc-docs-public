''' 
code to format, copy, or make or append any necessary 
files for JDC documentation with mkdocs.

this includes the mkdocs.yml config file or making
actual markdown files
'''
import pandas as pd
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
    ''' 

    if 'oneOf' in prop:
        items = {}
        for prop_name,prop in props['oneOf']:
            items.update(get_description(prop_name,prop))
        return items
    else:
        description_json = parse("$..description").find(prop)
        descriptions = [match.value for match in description_json if match]
    
        if descriptions:
            return {prop_name:descriptions}
        else:
            return {prop_name:["No description"]}



#TODO: Relationship to Core measures document

# iterate through the entire dictionary and get possible values and descriptions
# only if dictionary item is a node (ie has properties)
dictionary = get_dictionary(endpoint,'_all')

nodes = []
for node_name,props in dictionary.items():
    if 'properties' in props:
        possible_values = {}
        descriptions = {}
        for prop_name,prop in props['properties'].items():
            possible_values.update(get_possible_values(prop_name,prop))
            descriptions.update(get_description(prop_name,prop))
        
        node_df = pd.DataFrame(
            {'possible_values':possible_values,
            'descriptions':descriptions}
        )
        node_df['node'] = node_name
        nodes.append(node_df)

        

### get possible values and convert to pd.Series
### get descriptions and convert ot pd.Series
### join on property name
### name series the name of node

# concatenate nodes together for one large data dictionary



# OEPS
# get markdown docs from gen3

# JDC Graph Model
# get node properties from gen3
# TODO: extract info from Core Measure Document and join to JDC info