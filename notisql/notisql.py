import os
import notion_client
from termcolor import colored
from .page import PageInformation

# Prevent error when running on windows
if os.name == "nt": os.system("color")


class Notisql:
    def __init__(self, api_key: str):
        self.client = notion_client.Client(auth=api_key)

    def version(self):
        version = "0.0.1"
        print(colored(f"[-] Notisql Version: {version}", "green"))

    def page_information(self, database_id: str):
        return PageInformation(client=self.client, database_id=database_id)