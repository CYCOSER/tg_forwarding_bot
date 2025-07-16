def clipSpace64(text: str, max_bytes: int = 64) -> str:
    words = text.split()
    result = ""

    for word in words:
        candidate = f"{result} {word}".strip()
        if len(candidate.encode("utf-8")) > max_bytes:
            break
        result = candidate

    return result
