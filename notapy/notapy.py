import os
import notion_client
from termcolor import colored

# Prevent error when running on windows
if os.name == "nt": os.system("color")


class Notapy:
    def __init__(self, api_key: str):
        self.client = notion_client.Client(auth=api_key)

    def version(self):
        version = "0.0.1"
        print(colored(f"[-] Notapy Version: {version}", "green"))
