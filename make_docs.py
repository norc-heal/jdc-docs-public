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

from gen3.auth import Gen3Auth
from gen3.submission import Gen3Submission
from gen3.index import Gen3Index
import numpy as np

from pathlib import Path
import yaml
#from jsonpath_ng import parse

from collections.abc import Iterable


# TODO: extract info from Core Measure Document and join to JDC info


# get variable categories of core measures
credentials_path = Path('credentials.json')
endpoint = 'https://jcoin.datacommons.io'
auth = Gen3Auth(refresh_file=credentials_path.as_posix())
index = Gen3Index(endpoint, auth)
sub = Gen3Submission(auth)


def get_possible_values(df):

    df = df.copy().fillna('') #replace nans with blank string
    convert_to_str = lambda x: ','.join([str(y) for y in x]) if type(x) is list else str(x).title()
    if 'enum' in df and 'type' in df:
        possible_values = df['enum'].apply(convert_to_str) + df['type'].apply(convert_to_str)
    elif 'enum' in df:
        possible_values = df['enum'].apply(convert_to_str)
    elif 'type' in df:
        possible_values = df['type'].apply(convert_to_str)
    else:
        raise Exception("BAD POSSIBLE VALUE")
    return possible_values

def make_human_readable_table(node_name):

    node = sub.get_dictionary_node(node_name)

    #human readable node-level properties
    if 'title' in node:
        node_title = node['title']
    else:
        node_title = node_name.replace('_',' ').title()

    #variable level details
    if 'properties' in node:
        df = pd.DataFrame(node['properties']).T
        df['node_name'] = node_name
        df['node_title'] = node_title
        df['possible_values'] = df.pipe(get_possible_values)
        # Description of variable (ie property)
        if 'description' not in df:
            df['description'] = None

        if 'term' in df:
            #if there are some properties with a ref to the __term yaml, replace with the term description
            replace_desc_with_term_desc = lambda x: x['description'] if 'description' in x else ''
            df['description'].fillna(df['term'].apply(replace_desc_with_term_desc),inplace=True)

        #TODO: Relationship to Core measures document
        # return pd.DataFrame(data={
        #     "Variable Category":df['node_title'],
        #     "JDC Variable Category (or 'node') Name":df['node_name'],
        #     "JDC Variable Description":df['description'],
        #     "Possible JDC Variable Values": df['possible_values']
        # })
        return df
    else:
        return None
#%%
make_human_readable_table('participant')
#%%
nodes_df = pd.concat(
    [make_human_readable_table(key) for key,_ in sub.get_dictionary_all().items()]
)

