import os
import notion_client
from termcolor import colored

# Prevent error when running on windows
if os.name == "nt":
    os.system("color")


class Notisql:
    def __init__(self, notion_token: str):
        self.client = notion_client.Client(auth=notion_token)

    def version(self):
        version = "0.0.1"
        print(colored(f"[-] Notisql Version: {version}", "green"))
