#!/usr/bin/env python3

import requests
import json

# defining the configs
WORKFRONT_API_URL = "https://{domain}.my.workfront.com"
WORKFRONT_API_VERSION = "/attask/api/v10.0"
WORKFRONT_API_KEY = "{You Api Key}"

WORKFRONT_EXAMPLE = 'Workfront API Example 2019-08-19'

def get_header():
    return {
        'Content-Type': 'application/json',
        'Accept':'application/json',
        'apiKey': WORKFRONT_API_KEY
    }


def handle_response(action, response):
    if response.status_code != 200:
        raise Exception(f'Error {action}: {response.text}')

    results = response.json()
    return results['data']


def search(objCode, searchFilter):
    response = requests.get(url=f'{WORKFRONT_API_URL}{WORKFRONT_API_VERSION}/{objCode}/search',
                            headers=get_header(),
                            params=searchFilter)
    return handle_response(f'{objCode} search', response)


def put(objCode, id, body):
    response = requests.put(url=f'{WORKFRONT_API_URL}{WORKFRONT_API_VERSION}/{objCode}/{id}',
                            headers=get_header(),
                            data=json.dumps(body))
    return handle_response(f'{objCode} put', response)


def post(objCode, body):
    response = requests.post(url=f'{WORKFRONT_API_URL}{WORKFRONT_API_VERSION}/{objCode}',
                             headers=get_header(),
                             data=json.dumps(body))
    return handle_response(f'{objCode} post', response)

def delete(objCode, id):
    response = requests.delete(url=f'{WORKFRONT_API_URL}{WORKFRONT_API_VERSION}/{objCode}/{id}',
                             headers=get_header())
    return handle_response(f'{objCode} delete', response)

def add_fields():
    parameter1 = post('PARAM', {
        'name': 'DropDown Example',
        'extRefID': WORKFRONT_EXAMPLE,
        'dataType': 'TEXT',
        'displayType': 'SLCT',
        'parameterOptions':[
            {
                'label': 'Option 1',
                'value': '1',
                'displayOrder': 1,
                'isDefault': 'true'
            },
            {
                'label': 'Option 2',
                'value': '2',
                'displayOrder': 2
            },
            {
                'label': 'Option 3',
                'value': '3',
                'displayOrder': 3
            }
        ]
    })
    parameter2 = post('PARAM', {
        'name': 'Radio Button Example',
        'extRefID': WORKFRONT_EXAMPLE,
        'dataType': 'TEXT',
        'displayType': 'RDIO',
        'parameterOptions':[
            {
                'label': 'Option A',
                'value': 'A',
                'displayOrder': 1,
            },
            {
                'label': 'Option B',
                'value': 'B',
                'displayOrder': 2
            },
            {
                'label': 'Option C',
                'value': 'C',
                'displayOrder': 3
            }
        ]
    })
    parameter3 = post('PARAM', {
        'name': 'CheckBox Example',
        'extRefID': WORKFRONT_EXAMPLE,
        'dataType': 'TEXT',
        'displayType': 'CHCK',
        'parameterOptions':[
            {
                'label': 'Option 1',
                'value': '1',
                'displayOrder': 1,
            },
            {
                'label': 'Option 2',
                'value': '2',
                'displayOrder': 2
            },
            {
                'label': 'Option 3',
                'value': '3',
                'displayOrder': 3
            }
        ]
    })
    parameter4 = post('PARAM', {
        'name': 'Radio Data Number Example',
        'extRefID': WORKFRONT_EXAMPLE,
        'dataType': 'NMBR',
        'displayType': 'RDIO',
        'parameterOptions':[
            {
                'label': '100',
                'value': '100',
                'displayOrder': 1,
            },
            {
                'label': '200',
                'value': '200',
                'displayOrder': 2
            },
            {
                'label': '300',
                'value': '300',
                'displayOrder': 3
            }
        ]
    })
    parameter5 = post('PARAM', {
        'name': 'Multi-DropDown Example',
        'extRefID': WORKFRONT_EXAMPLE,
        'dataType': 'TEXT',
        'displayType': 'MULT',
        'parameterOptions':[
            {
                'label': 'Option 1',
                'value': 'Option 1',
                'displayOrder': 1,
            },
            {
                'label': 'Option 2',
                'value': 'Option 2',
                'displayOrder': 2
            },
            {
                'label': 'Option 3',
                'value': 'Option 3',
                'displayOrder': 3
            }
        ]
    })
    parameter6 = post('PARAM', {
        'name': 'Text Example',
        'extRefID': WORKFRONT_EXAMPLE,
        'dataType': 'TEXT',
        'displayType': 'TEXT'
    })

    parameter7 = post('PARAM', {
        'name': 'Calculated Example',
        'extRefID': WORKFRONT_EXAMPLE,
        'dataType': 'TEXT',
        'displayType': 'CALC',
    })
    
    return [parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7]

def add_sections():
    parameterGroup1 = post('PGRP', {
        'name': "Section Break 1",
        'extRefID': WORKFRONT_EXAMPLE,
        'description': 'First section'
    })
    parameterGroup2 = post('PGRP', {
        'name': "Section Break 2",
        'extRefID': WORKFRONT_EXAMPLE,
        'description': 'Second section'
    })
    parameterGroup3 = post('PGRP', {
        'name': "Section Break 3",
        'extRefID': WORKFRONT_EXAMPLE,
        'description': 'Third section'
    })
    parameterGroup4 = post('PGRP', {
        'name': "Section Break 4",
        'extRefID': WORKFRONT_EXAMPLE,
        'description': 'Fourth section'
    })
    parameterGroup5 = post('PGRP', {
        'name': "Section Break 5",
        'extRefID': WORKFRONT_EXAMPLE,
        'description': 'Fifth section'
    })
    
    return [parameterGroup1, parameterGroup2, parameterGroup3, parameterGroup4, parameterGroup5]

def add_custom_form(parameters, parameterGroups):
    parameterName = parameters[0]['name']
    category1 = post('CTGY', {
        'name': "Task Custom Form Example",
        'extRefID': WORKFRONT_EXAMPLE,
        'catObjCode': "TASK",
        'categoryParameters': [
            {
                'displayOrder': 1,
                'parameterID': parameters[0]['ID'],
                'parameterGroupID': parameterGroups[0]['ID']
            },
            {
                'displayOrder': 2,
                'parameterID': parameters[1]['ID'],
                'parameterGroupID': parameterGroups[1]['ID']
            },
            {
                'displayOrder': 3,
                'parameterID': parameters[2]['ID'],
                'parameterGroupID': parameterGroups[2]['ID']
            },
            {
                'displayOrder': 4,
                'parameterID': parameters[3]['ID'],
                'parameterGroupID': parameterGroups[3]['ID']
            },
            {
                'displayOrder': 5,
                'parameterID': parameters[4]['ID'],
                'parameterGroupID': parameterGroups[3]['ID']
            },
            {
                'displayOrder': 6,
                'parameterID': parameters[5]['ID'],
                'parameterGroupID': parameterGroups[4]['ID'],
                'securityLevel': 'A', # Admin access
                'viewSecurityLevel': 'ELU' # Manage access
            },
            {
                'displayOrder': 7,
                'parameterID': parameters[6]['ID'],
                'parameterGroupID': parameterGroups[4]['ID'],
                'customExpression': f'CONCAT(Name, {parameterName})',
                'securityLevel': 'A', # Admin access
                'viewSecurityLevel': 'ELU' # Manage access
            }
        ],
        'categoryCascadeRules': [
            # Display `Radio Button Example` if `Drop Down Example` `Option 1`is selected
            {
                'nextParameterID': parameters[1]['ID'],
                'ruleType': 'DISPLAY',
                'categoryCascadeRuleMatches': [
                    {
                        'parameterID': parameters[0]['ID'],
                        'value': '1',
                        'matchType': 'EXIST'
                    }
                ]
            },
            # Display `Multi-DropDown Example` if `CheckBox Example` `Option 2` is selected AND `Radio Data Number Example` `300` is selected
            {
                'nextParameterID': parameters[4]['ID'],
                'ruleType': 'DISPLAY',
                'categoryCascadeRuleMatches': [
                    {
                        'parameterID': parameters[2]['ID'],
                        'value': '2',
                        'matchType': 'EXIST'
                    },
                    {
                        'parameterID': parameters[3]['ID'],
                        'value': '300',
                        'matchType': 'EXIST'
                    }
                ]
            },
            # Display `Section Break 5` if `CheckBox Example` `Option 3` is selected
            {
              'nextParameterGroupID': parameterGroups[4]['ID'],
                'ruleType': 'DISPLAY',
                'categoryCascadeRuleMatches': [
                    {
                        'parameterID': parameters[2]['ID'],
                        'value': '3',
                        'matchType': 'EXIST'
                    }
                ]
            },
            # if `Multi-DropDown Example` selects any value, skip to `End of form`
            {
                'otherwiseParameterID': parameters[4]['ID'],
                'ruleType': 'SKIP',
                'toEndOfForm': 'true'
            }
        ]
    })

    return category1

# search existing examples
existingParameters = search('PARAM', {'extRefID': WORKFRONT_EXAMPLE})
existingParameterGroups = search('PGRP', {'extRefID': WORKFRONT_EXAMPLE})
existingCategories = search('CTGY', {'extRefID': WORKFRONT_EXAMPLE})

# edit parameter's description
# existingParameters = search('PARAM', {'extRefID': WORKFRONT_EXAMPLE})
# for existingParameter in existingParameters:
#     put('PARAM', existingParameter['ID'], {'description': 'editing description'})

# delete all existing examples
for existingCategory in existingCategories:
    delete('CTGY', existingCategory['ID'])
for existingParameterGroup in existingParameterGroups:
    delete('PGRP', existingParameterGroup['ID'])
for existingParameter in existingParameters:
    delete('PARAM', existingParameter['ID'])

# create custom form
parameters = add_fields()
parameterGroups = add_sections()
category = add_custom_form(parameters, parameterGroups)
print('Category has been created with ID of ' + category['ID'])
