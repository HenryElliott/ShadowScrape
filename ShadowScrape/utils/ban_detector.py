# utils/ban_detector.py

def is_banned(content: str, status: int) -> bool:
    """
    Detects if a request has been blocked or banned.
    """
    ban_keywords = ["access denied", "blocked", "verify you are human", "captcha"]

    if status in [403, 429, 503]:
        return True

    content_lower = content.lower()
    return any(keyword in content_lower for keyword in ban_keywords)
