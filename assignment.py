available_string_validators = ["min_length", "max_length", "data_type"]
available_integer_validators = ["min_value", "max_value", "data_type"]
available_boolean_validators = ["value", "data_type"]


class IncorrectValidator(Exception):
    pass


def validate_string(string, validators_dict):
    # check for every possible string validators
    try:
        for validator in validators_dict:
            # check if any non-expected validators are supplied in validators_dict
            if validator not in available_string_validators:
                raise IncorrectValidator

            if validator == "min_length":
                assert len(string) >= validators_dict.get("min_length")

            elif validator == "max_length":
                assert len(string) <= validators_dict.get("max_length")
    except AssertionError:
        raise AssertionError
    except IncorrectValidator:
        raise IncorrectValidator


def validate_integer(integer, validators_dict):
    # check for every possible integer validators
    try:
        for validator in validators_dict:
            # check if any non-expected validators are supplied in validators_dict
            if validator not in available_integer_validators:
                raise IncorrectValidator

            if validator == "min_value":
                assert integer >= validators_dict.get("min_value")

            elif validator == "max_value":
                assert integer <= validators_dict.get("max_value")
    except AssertionError:
        raise AssertionError
    except IncorrectValidator:
        raise IncorrectValidator


def validate_boolean(boolean, validators_dict):
    # check for every possible boolean validators
    try:
        for validator in validators_dict:
            # check if any non-expected validators are supplied in validators_dict
            if validator not in available_boolean_validators :
                raise IncorrectValidator

            if validator == "value":
                assert boolean >= validators_dict.get("value")
    except AssertionError:
        raise AssertionError
    except IncorrectValidator:
        raise IncorrectValidator

def data_type_from_string(data_type):
    if data_type == "int":
        return int
    elif data_type == "str":
        return str
    elif data_type == "boolean":
        return bool



def validate(data_dict, validator_dict):
    # make sure all keys present in validator_dict are also present in data_dict
    for key in validator_dict.keys():
        if key not in data_dict:
            return False

    for key, value in data_dict.items():
        # get the corresponding validator for each key. If validator does not exist, move on
        validators = validator_dict.get(key)
        if not validators:
            continue

        try:
            # data type mentioned in validator_dict should match data type supplied in data_dict
            data_type_required = data_type_from_string(validators["data_type"])
            assert type(value) == data_type_required

            # based upon the data type supplied in data_dict, run the corresponding function
            if data_type_required == str:
                validate_string(value, validators)
            elif data_type_required == int:
                validate_integer(value, validators)
            elif data_type_required == bool:
                validate_boolean(value, validators)
        except (AssertionError, IncorrectValidator, KeyError):
            return False

    return True


data_list = [
    {"id": 1, "name": "Sanjeev", "is_female": False},
    {"id": 10, "name": "John", "is_female": False},
    {"id": 0, "name": "Sanjeev", "is_female": True},
]

validator = {"id": {"data_type": "int", "min_value": 1, "max_value": 10, },
             "name": {"data_type": "str", "min_length": 1, "max_length": 100},
             "is_female": {"data_type": "boolean", "value": False}
             }

for data in data_list:
    result = validate(data, validator)
    print(result)