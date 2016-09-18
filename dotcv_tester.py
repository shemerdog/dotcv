import re

testObject = {
    'personalDetails': {
        'fullName': {
            'firstName': "Yehuda",
            'middleName': None,
            'lastName': "Gerstle"
        },
        'dateOfBirth': {
            'gregorianDate': '08/04/1984',
            'hebrewDate': '06/01/5744'
        },
        'address': {
            'city': 'Talmon',
            'street': 'Yehoshua Bin-Noon',
            'number': 2,
            'apartment': 3,
            'zipCode': 71937
        },
    },

    'contactDetails': {
        'email': "Yehuda.G@LBD.co.il",
        'secondaryEmail': None,
        'phone': [
            {
                'countryCode': 972,
                'number': 523531113,
                'mobile': True,
                'work': None
            }, {
                'countryCode': 972,
                'number': 26281081,
                'mobile': False,
                'work': False
            }
        ]
    }
}

requiredFields = {
    'personalDetails': {
        'fullName': {
            'firstName': True,
            'middleName': False,
            'lastName': True
        },
        'dateOfBirth': {
            'gregorianDate': True,
            'hebrewDate': False
        },
        'address': {
            'city': True,
            'street': True,
            'number': True,
            'apartment': False,
            'zipCode': False
        },
    },

    'contactDetails': {
        'email': False,
        'secondaryEmail': False,
        'phone': True
    }
}

regexRules = {
    'personalDetails': {
        'fullName': {
            'firstName': '\w+',
            'middleName': False,
            'lastName': True
        },
        'dateOfBirth': {
            'gregorianDate': True,
            'hebrewDate': False
        },
        'address': {
            'city': True,
            'street': True,
            'number': True,
            'apartment': False,
            'zipCode': False
        },
    },

    'contactDetails': {
        'email': False,
        'secondaryEmail': False,
        'phone': True
    }
}

dictionaryPath = []


def check_if_in_format(field_name, field_value):
    if re.match(regexRules['personalDetails']['fullName'][field_name], field_value):
        return True
    return False


def loop_through_object(cv_object):
    for key, value in cv_object.iteritems():
        # print "looping through"
        # print key, value
        dictionaryPath.append(key)
        if isinstance(value, dict):
            # print "starting recursion"
            # print dictionaryPath
            loop_through_object(value)
            dictionaryPath.pop()
        else:
            test_format = check_if_in_format(key, value)
            is_required = requiredFields[dictionaryPath[0]]
            if dictionaryPath and isinstance(is_required, dict):
                for key in dictionaryPath:
                    try:
                        is_required = is_required[key]
                    except KeyError:
                        continue
            print dictionaryPath, is_required
            dictionaryPath.pop()


loop_through_object(testObject)
