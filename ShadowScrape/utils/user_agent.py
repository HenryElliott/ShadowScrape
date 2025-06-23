# utils/user_agent.py
from fake_useragent import UserAgent

def get_random_user_agent() -> str:
    ua = UserAgent()
    return ua.random
