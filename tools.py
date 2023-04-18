"""Инструменты для шифровки"""


def delete_in_text(text: str, low=False, other=None) -> str:
    """Тут все понятно"""
    if other:
        for i in other:
            text = text.replace(f'{i}', '')
    if low:
        text = text.lower()

    return text


def delete_duplicates(string: str) -> str:
    """Функция  для удаления дубликатов в ключе"""
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
    """Разделение текста на списки"""
    return [text[i:i + length] for i in range(0, len(text), length)]
