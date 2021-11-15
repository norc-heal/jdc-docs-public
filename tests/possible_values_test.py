from jsonpath_ng import jsonpath, parse
import json

node_json = r'''{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "additionalProperties": false,
    "category": "clinical",
    "description": "Data for the characterization of the participant by means of segementing the population (e.g., characterization by age, sex, or race).\n",
    "id": "demographic",
    "links": [
        {
            "backref": "demographics",
            "label": "describes",
            "multiplicity": "one_to_one",
            "name": "participants",
            "required": true,
            "target_type": "participant"
        }
    ],
    "namespace": "https://jcoin.datacommons.io/dd",
    "program": "*",
    "project": "*",
    "properties": {
        "D4a": {
            "description": "What was your sex at birth? \n",
            "enum": [
                "Male",
                "Female"
            ]
        },
        "D4b": {
            "description": "What is your gender identity? \n",
            "enum": [
                "Male",
                "Female",
                "Transgender",
                "Gender nonconforming",
                "Not reported"
            ]
        },
        "D4c": {
            "description": "Sexual Orientation. Do you think of yourself as . . . \n",
            "enum": [
                "Straight or heterosexual",
                "Lesbian or gay",
                "Bisexual",
                "Queer, pansexual, and/or questioning",
                "Something else (SPECIFY _________)"
            ]
        },
        "D4c_specify": {
            "description": "Sexual Orientation. Do you think of yourself as . . .not matching one of the enumerated racial categories.\n",
            "type": [
                "string"
            ]
        },
        "D4d": {
            "description": "Have you ever been pregnant?\n",
            "enum": [
                "Never been pregnant",
                "Currently pregnant",
                "Previously pregnant, had a child",
                "Previously pregnant, did not have a child"
            ]
        },
        "D5": {
            "description": "What is your marital status?\n",
            "enum": [
                "Married [GO TO D6]",
                "Widowed",
                "Divorced",
                "Separated",
                "Never married"
            ]
        },
        "D5a": {
            "description": "Are you currently living as married with a romantic partner?\n",
            "enum": [
                "Yes, I am living as married with partner",
                "No, I am not living as married with partner"
            ]
        },
        "D6": {
            "description": "What is the highest grade or level of school you have completed or the highest degree you have received?  \n",
            "enum": [
                "Did not complete high school. HIGHEST GRADE COMPLETED ________",
                "GED or equivalent",
                "Regular high school diploma",
                "Some college credit, but less than 1 year of college credit",
                "1 or more years of college credit, but no degree",
                "Associate’s Degree (e.g., AA or AS)",
                "Graduate degree (MSW, MA, MS, JD, MD, DSW, EdD, Ph.D, etc.)",
                "Other (specify)"
            ]
        },
        "D6_1": {
            "description": "HIGHEST GRADE COMPLETED\n",
            "type": [
                "string"
            ]
        },
        "D6_2": {
            "description": "What is the highest grade or level of school you have completed or the highest degree you have received, not matching one of the enumerated categories.\n",
            "type": [
                "string"
            ]
        },
        "Death_records_using_admin_data": {
            "description": "tbd\n",
            "type": [
                "string"
            ]
        },
        "O1": {
            "description": "What sex was originally listed on your birth certificate?\n",
            "enum": [
                "Male",
                "Female",
                "Decline to answer"
            ]
        },
        "O2_2_gender_identity_specify": {
            "description": "Additional gender category (or other) \n",
            "type": [
                "string"
            ]
        },
        "O2_gender_identity": {
            "description": "Do you think of yourself as...\n",
            "enum": [
                "Male",
                "Female",
                "Transgender man/trans man/female-to-male (FTM)",
                "Transgender woman/trans woman/male-to-female (MTF)",
                "Genderqueer/gender nonconforming/neither exclusively male nor female",
                "Additional gender category (or other)",
                "Not reported"
            ]
        },
        "age": {
            "description": "About how old are you?\n",
            "type": [
                "integer"
            ]
        },
        "created_datetime": {
            "oneOf": [
                {
                    "format": "date-time",
                    "type": "string"
                },
                {
                    "type": "null"
                }
            ],
            "term": {
                "description": "A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]\n"
            }
        },
        "date_and_cause_of_death_per_ICD_10_codes": {
            "description": "tbd\n",
            "type": [
                "string"
            ]
        },
        "electronic_health_record": {
            "description": "tbd\n",
            "type": [
                "string"
            ]
        },
        "gender": {
            "description": "What is your gender identity? \n",
            "enum": [
                "Male",
                "Female",
                "Transgender",
                "Gender nonconforming",
                "Something else",
                "Not reported"
            ]
        },
        "hispanic": {
            "description": "Are you of Hispanic, Latino, or Spanish origin?\n",
            "enum": [
                "Yes",
                "No",
                "Not reported"
            ]
        },
        "id": {
            "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
            "systemAlias": "node_id",
            "term": {
                "description": "A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.\n",
                "termDef": {
                    "cde_id": "C54100",
                    "cde_version": null,
                    "source": "NCIt",
                    "term": "Universally Unique Identifier",
                    "term_url": "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&version=16.02d&ns=NCI_Thesaurus&code=C54100"
                }
            },
            "type": "string"
        },
        "jewish": {
            "description": "Whether a participant describes him or herself as Jewish.\n",
            "enum": [
                "Yes",
                "No",
                "Unknown"
            ]
        },
        "other_race": {
            "description": "Racial designation not matching one of the enumerated racial categories.\n",
            "type": [
                "string"
            ]
        },
        "participants": {
            "anyOf": [
                {
                    "items": {
                        "additionalProperties": true,
                        "maxItems": 1,
                        "minItems": 1,
                        "properties": {
                            "id": {
                                "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
                                "term": {
                                    "description": "A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.\n",
                                    "termDef": {
                                        "cde_id": "C54100",
                                        "cde_version": null,
                                        "source": "NCIt",
                                        "term": "Universally Unique Identifier",
                                        "term_url": "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&version=16.02d&ns=NCI_Thesaurus&code=C54100"
                                    }
                                },
                                "type": "string"
                            },
                            "submitter_id": {
                                "type": "string"
                            }
                        },
                        "type": "object"
                    },
                    "type": "array"
                },
                {
                    "additionalProperties": true,
                    "properties": {
                        "id": {
                            "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
                            "term": {
                                "description": "A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.\n",
                                "termDef": {
                                    "cde_id": "C54100",
                                    "cde_version": null,
                                    "source": "NCIt",
                                    "term": "Universally Unique Identifier",
                                    "term_url": "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&version=16.02d&ns=NCI_Thesaurus&code=C54100"
                                }
                            },
                            "type": "string"
                        },
                        "submitter_id": {
                            "type": "string"
                        }
                    },
                    "type": "object"
                }
            ]
        },
        "principal_tribe_community": {
            "description": "Principal tribe or community not matching one of the enumerated racial categories.\n",
            "type": [
                "string"
            ]
        },
        "project_id": {
            "term": {
                "description": "Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement.\n"
            },
            "type": "string"
        },
        "race": {
            "description": "What is your race? SELECT ALL THAT APPLY\n",
            "enum": [
                "White",
                "Black or African American",
                "American Indian or Alaska Native (SPECIFY principal tribe or community)",
                "Native Hawaiian or Other Pacific Islander",
                "Asian",
                "Some other race (SPECIFY)",
                "Not reported"
            ]
        },
        "state": {
            "default": "validated",
            "downloadable": [
                "uploaded",
                "md5summed",
                "validating",
                "validated",
                "error",
                "invalid",
                "released"
            ],
            "oneOf": [
                {
                    "enum": [
                        "uploading",
                        "uploaded",
                        "md5summing",
                        "md5summed",
                        "validating",
                        "error",
                        "invalid",
                        "suppressed",
                        "redacted",
                        "live"
                    ]
                },
                {
                    "enum": [
                        "validated",
                        "submitted",
                        "released"
                    ]
                }
            ],
            "public": [
                "live"
            ],
            "term": {
                "description": "The current state of the object.\n"
            }
        },
        "submitter_id": {
            "type": [
                "string",
                "null"
            ]
        },
        "type": {
            "type": "string"
        },
        "updated_datetime": {
            "oneOf": [
                {
                    "format": "date-time",
                    "type": "string"
                },
                {
                    "type": "null"
                }
            ],
            "term": {
                "description": "A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]\n"
            }
        },
        "vital_statistics_for_count_of_overdose_deaths": {
            "description": "tbd\n",
            "type": [
                "string"
            ]
        },
        "year_of_birth": {
            "term": {
                "description": "Numeric value to represent the calendar year in which an individual was born.\n",
                "termDef": {
                    "cde_id": 2896954,
                    "cde_version": 1,
                    "source": "caDSR",
                    "term": "Year Birth Date Number",
                    "term_url": "https://cdebrowser.nci.nih.gov/CDEBrowser/search?elementDetails=9&FirstTimer=0&PageId=ElementDetailsGroup&publicId=2896954&version=1.0"
                }
            },
            "type": [
                "number",
                "null"
            ]
        }
    },
    "required": [
        "submitter_id",
        "type",
        "participants",
        "gender",
        "race",
        "hispanic"
    ],
    "submittable": true,
    "systemProperties": [
        "id",
        "project_id",
        "state",
        "created_datetime",
        "updated_datetime"
    ],
    "title": "Demographic",
    "type": "object",
    "uniqueKeys": [
        [
            "id"
        ],
        [
            "project_id",
            "submitter_id"
        ]
    ],
    "validators": null
}'''
node_dict = json.loads(node_json)

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
        return [
            get_possible_values(f"{prop_name}.{anyof_prop_name}",anyof_prop)
            for anyof_prop_name,anyof_prop in any_of_props.items()
        ]
    else:
        return {prop_name:["UNDEFINED"]}

props = [
    get_possible_values(prop_name, prop)
    for prop_name,prop in node_dict['properties'].items()
]
