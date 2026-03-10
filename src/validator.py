def validate_input(value):
    if value is None:
        return False

    if not isinstance(value, str):
        return False

    return len(value.strip()) > 0
