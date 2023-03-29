def is_empty_name(value: str) -> bool:
    return value is None or value.strip() == ''


def is_valid_name(value: str) -> bool:
    # допустимы только пробелы и буквы
    return value.replace(' ', '').isalpha()


def prepare_name(value: str) -> str:
    return value.strip().lower()