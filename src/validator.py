def validate_input(value):
    if value is None:
        return False
    return len(value) > 0
