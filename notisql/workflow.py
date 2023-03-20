# TEST FILE OF GITHUB WORKFLOW
# print("TEST FILE OF GITHUB WORKFLOW")

import os
from dotenv import load_dotenv
from Notisql import version

# Load .env vaiables
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_TOKEN = os.getenv("DATABASE_TOKEN")
PAGE_TOKEN = os.getenv("PAGE_TOKEN")

# Print version
version()
