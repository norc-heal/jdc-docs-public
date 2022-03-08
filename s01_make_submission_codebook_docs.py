''' 
Generates documentation
based on the Table Schema and 
other metadata. 

Work in progress

Switched from html to markdown to support mkdocs

Given this should live in jdc-docs, migrating this code over to jdc-docs repo.

'''
from jsonpath_ng.jsonpath import Fields
from frictionless import Schema

# Overall objective

# File format and naming

#Box upload instead of gen3-client 


#submission visual workflow
def add_submission_workflow(mermaid_str):
    #see https://mermaid-js.github.io/mermaid/#/
    #and to quickly create - use live editor: 
    #https://mermaid.live/
    mermaid_script = (
        '<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>'
        '<script>mermaid.initialize({startOnLoad:true});</script>'
    )
    mermaid_class = f'<div class="mermaid">{mermaid_str}</div>'
    return r'\n'.join([mermaid_script,mermaid_class])

title_template = '''
### {title}
'''
#title
def add_title(field):
    title = field.get('title',None)
    if title:
        return title_template.format(title=title.title())
    else:
        return ''

def add_core_measure(field):
    core_measure_exp = Fields("custom").child(Fields("jcoin:core_measure_id"))
    core_measure = core_measure_exp.find(field)
    if core_measure:
        return  core_measure[0].value.capitalize()
    else:
        return  'Not in core measures'

#descriptions
def add_description(field):
    return field.get('description','NO DESCRIPTION')

#variable name
def add_variable_name(field):
    return field.get('name',"NO VARIABLE NAME")

#variable values
def add_enums(field):
    enum_exp = Fields("constraints").child(Fields("enum"))
    enum_list = enum_exp.find(field)
    if enum_list:
        # enum_list_html = [f"<li>{enum}</li>" for enum in enum_list]
        # enum_title = "<p><strong>Possible Values:</strong></p>"
        # return enum_title + f"<ul>{enum_list_html}</ul>"
        return ','.join(enum_list[0].value)
    else:
        return "Any of the fields type and other constraints"

def add_type(field):
    type_str = field.get('type','NO TYPE SPECIFIED')
    return type_str.title()

#note
def add_note(field):
    note_exp = Fields('custom').child(Fields('note'))
    note = note_exp.find(field)
    if note:
        return note[0].value
    else:
        return ""

def add_examples(examples):
    return examples


def add_core_measure_question(field):
    question_exp = Fields('custom').child(Fields("jcoin:core_measure_question"))
    question = question_exp.find(field)

    if question:
        return question[0].value
    else:
        return ''

#make an ordered dict of mappings
field_md_template = ''' 

--------------------------------------------
{title}
 |               |                          |
----------------- | --------------------------
|**Variable name** | `{variable_name}`|
|**JCOIN Core Measure Question Text** | {question} |
|**Description:** | {description} |
|**Variable type** | {type}|
|**Possible values** | {enums}|
'''
def make_field_md(field):
    field_md = field_md_template.format(
        title=add_title(field),
        question=add_core_measure_question(field),
        core_measure=add_core_measure(field),
        description=add_description(field),
        variable_name=add_variable_name(field),
        enums=add_enums(field),
        type=add_type(field),
    )
    notes = add_note(field)

    if notes:
        field_md+=f"**Notes | {notes}"
    
    return field_md

section_md_template = '''
----------
## **{section}**
----------
'''
def get_section(field,first_level='custom',second_level='jcoin:core_measure_section'):
    json_section = Fields(first_level).child(Fields(second_level)).find(field)
    if json_section:
        section = json_section[0].value
    else:
        section = "Other"
    return section_md_template.format(section=section)

baseline_schema_path = r"C:\Users\kranz-michael\projects\frictionless-jcoin\hubs\metadata\table_schemas\table-schema-baseline.json"
timepoint_schema_path = r"C:\Users\kranz-michael\projects\frictionless-jcoin\hubs\metadata\table_schemas\table-schema-time-points.json"
schemas = [Schema(baseline_schema_path),Schema(timepoint_schema_path)]
# Field Codebook
for schema in schemas:
    field_md_list = []
    section = '' #initiate section name
    for field in schema.fields:
        #compare this section with last section and add section header to markdown if new
        if section!=get_section(field):
            field_md_list.append(get_section(field))
        section = get_section(field)

        field_md_list.append(make_field_md(field))
        
    fields_mds = '\n\n'.join(field_md_list)
    schema_description = schema.get('description','No description')
    schema_file_name = schema_description.split(":")[0].lower().replace(" ","_")
    overall_md = f"# {schema_description}"
    overall_md+=fields_mds
    with open(f"docs/submission/{schema_file_name}.md",'w') as f:
        f.write(overall_md)


