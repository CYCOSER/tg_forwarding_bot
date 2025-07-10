def clip64(text: str) -> str:
    encoded = text.encode('utf-8')
    if len(encoded) <= 64:
        return text

    # Обрезаем по байтам — побайтово назад до подходящей длины
    while len(encoded) > 64:
        text = text[:-1]
        encoded = text.encode('utf-8')

    return text


def clipSpace64(text: str, max_bytes: int = 64) -> str:
    words = text.split()
    result = ""

    for word in words:
        candidate = f"{result} {word}".strip()
        if len(candidate.encode("utf-8")) > max_bytes:
            break
        result = candidate

    return result
