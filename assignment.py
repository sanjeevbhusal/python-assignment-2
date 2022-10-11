def validate(data_dict, validator_dict):
    try:
        for key, value in data_dict.items():
            validators = validator_dict.get(key)
            if not validators:
                continue

            data_type_required = validators.get("data_type")
            if data_type_required == str:
                min_length_required = validators.get("min_length")
                max_length_required = validators.get("max_length")
                assert len(value) >= min_length_required
                assert len(value) <= max_length_required
            elif data_type_required == int:
                min_value_required = validators.get("min_value")
                max_value_required = validators.get("max_value")
                assert value >= min_value_required
                assert value <= max_value_required
            elif data_type_required == bool:
                value_required = validators.get("value")
                assert value == value_required
    except AssertionError:
        return False
    else:
        return True


data = {"id": 1, "name": "Sanjeev", "is_female": False}
validator = {"id": {"data_type": int, "min_value": 0, "max_value": 10},
             "name": {"data_type": str, "min_length": 1, "max_length": 100},
             "is_female": {"data_type": bool, "value": False}}


result = validate(data, validator)
print(result)