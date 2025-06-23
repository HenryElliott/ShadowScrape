# utils/limiter.py
from aiolimiter import AsyncLimiter

_domain_limiters = {}

def get_limiter(domain: str, rate: int = 5, period: int = 60):
    """
    Returns a rate limiter for a given domain.
    Prevents IP bans and respects site limits.
    """
    if domain not in _domain_limiters:
        _domain_limiters[domain] = AsyncLimiter(rate, period)
    return _domain_limiters[domain]
