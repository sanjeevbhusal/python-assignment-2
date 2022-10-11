available_string_validators = ["sanjeev", "max_length"]
available_integer_validators = ["min_value", "max_value"]
available_boolean_validators = ["value"]


class IncorrectValidator(Exception):
    pass


def validate_string(string, validators):
    try:
        for validator in validators:
            if validator not in available_string_validators:
                raise IncorrectValidator

            if validator == "min_length":
                assert len(string) >= validators.get("min_length")

            elif validator == "max_length":
                assert len(string) <= validators.get("max_length")
    except AssertionError:
        raise AssertionError
    except IncorrectValidator:
        raise IncorrectValidator


def validate_integer(integer, validators):
    try:
        for validator in validators:
            if validator not in available_integer_validators:
                raise IncorrectValidator

            if validator == "min_value":
                assert integer >= validators.get("min_value")

            elif validator == "max_value":
                assert integer <= validators.get("max_value")
    except AssertionError:
        raise AssertionError
    except IncorrectValidator:
        raise IncorrectValidator


def validate_boolean(boolean, validators):
    try:
        for validator in validators:
            if validator not in available_boolean_validators :
                raise IncorrectValidator

            if validator == "value":
                assert boolean >= validators.get("value")
    except AssertionError:
        raise AssertionError
    except IncorrectValidator:
        raise IncorrectValidator


def validate(data_dict, validator_dict):
    for key, value in data_dict.items():
        validators = validator_dict.get(key)
        if not validators:
            continue
        try:
            data_type_required = validators["data_type"]
            del validators["data_type"]
            assert type(value) == data_type_required
            if data_type_required == str:
                validate_string(value, validators)
            elif data_type_required == int:
                validate_integer(value, validators)
            elif data_type_required == bool:
                validate_boolean(value, validators)
        except (AssertionError, IncorrectValidator, KeyError):
            return False
        else:
            return True


data = {"id": 1, "name": "Sanjeev", "is_female": False}
validator = {"id": {"data_type": int, "min_value": 1, "max_value": 10, },
             "name": {"data_type": str, "min_length": 1, "max_length": 100},
             "is_female": {"data_type": bool, "value": False}
             }


result = validate(data, validator)
print(result)