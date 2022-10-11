import re


class IncorrectValidator(Exception):
    pass


class Validate:
    @classmethod
    def validate(cls, value, validator_dict):
        try:
            for key, rule_value in validator_dict.items():
                if key == "data_type":
                    assert cls.convert_data_type_to_string(type(value)) == rule_value
                if key == "min_value":
                    assert value >= rule_value
                elif key == "max_value":
                    assert value <= rule_value
                elif key == "min_length":
                    assert len(value) >= rule_value
                elif key == "max_length":
                    assert len(value) <= rule_value
                elif key == "value":
                    assert value == rule_value
        except (AssertionError, IncorrectValidator):
            return False

        return True

    @classmethod
    def convert_data_type_to_string(cls, data_type):
        return re.search("'.*'", str(data_type)).group()[1:-1]


def validate(data_dict, validator_dict):
    for key, rule in validator_dict.items():
        # make sure all keys present in validator_dict are also present in data_dict
        if key not in data_dict:
            return False

        # get the value of that key from data_dict
        value = data_dict[key]
        answer = Validate.validate(value, rule)
        if answer is False:
            return answer

    return True


validator = {"id": {"data_type": "int", "min_value": 1, "max_value": 10},
             "name": {"data_type": "str", "min_length": 1, "max_length": 100},
             "is_female": {"data_type": "bool", "value": False}
             }
data_list = [
    {"id": 1, "name": "Sanjeev", "is_female": False},
    {"id": 10, "name": "John", "is_female": False},
    {"id": 0, "name": "Sanjeev", "is_female": True},
]

for data in data_list:
    result = validate(data, validator)
    print(result)
