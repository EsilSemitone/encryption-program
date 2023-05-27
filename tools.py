"""Toold for encrypt"""


def delete_in_text(text: str, low=False, sumbols=None) -> str:

    if sumbols:
        for i in sumbols:
            text = text.replace(f'{i}', '')
    if low:
        text = text.lower()

    return text


def delete_duplicates(string: str) -> str:

    duplicates = []
    new_str = ''
    for i in string:
        if string.count(i) > 1:
            if not (i in duplicates):
                duplicates.append(i)
                new_str += i
        else:
            new_str += i
    return new_str


def split_text(text: str | list, length=3) -> list:
    return [text[i:i + length] for i in range(0, len(text), length)]
