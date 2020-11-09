import string


def replace_not_important_with_others(name):
    to_replace = {'Rev', 'Col', 'Major', 'Capt', 'Dona', 'Don', 'Sir', 'Jonkheer', 'Countess', 'Lady'}
    return 'Others' if name in to_replace else name


def get_age_by_title(value):
    title_dict = {'Master': 5, 'Miss': 22, 'Mr': 32, 'Mrs': 37, 'Others': 45, 'Dr': 44}
    return title_dict[value] if not isinstance(value, float) else value


def extract_ticket_type(value):
    for c in string.punctuation:
        value = value.replace(c, "")

    chunks = value.strip().split(' ')
    if len(chunks) == 1 and chunks[0].isnumeric():
        return 'NO'

    value = "".join(chunks[:-1]).upper()

    if 'TON' in value:
        return 'SOTON'
    elif 'PC' in value:
        return 'PC'
    elif 'CA' in value:
        return 'CA'
    elif 'A5' in value or 'A4' in value:
        return 'A'
    elif 'WC' in value:
        return 'WC'

    return 'OTHER_TICKET'

