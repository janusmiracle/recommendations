import os

# CLIENT_ID & CLIENT_SECRET set in environment variables (held in .zshrc)
def get_client_id() -> str:
    return os.environ["CLIENT_ID"]

def get_client_secret() -> str:
    return os.environ["CLIENT_SECRET"]

