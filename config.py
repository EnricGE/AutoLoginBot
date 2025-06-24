from typing import Dict, TypedDict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig(TypedDict):
    username: Optional[str]
    password: Optional[str]
    url: Optional[str]

CONFIGS: Dict[str, BotConfig] = {
    "github": {
        "username": os.getenv("GITHUB_USERNAME"),
        "password": os.getenv("GITHUB_PASSWORD"),
        "url": os.getenv("GITHUB_URL")
    },
    "quotes": {
        "username": os.getenv("QUOTES_USERNAME"),
        "password": os.getenv("QUOTES_PASSWORD"),
        "url": os.getenv("QUOTES_URL")
    }
}
