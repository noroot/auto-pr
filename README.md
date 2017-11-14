# auto-pr

Automatic PR merge if commit are signed and formatted in special way.

## Configuration

API_KEY = "- PASTE YOUR KEY HERE -"

ORG_NAME = "organization name" 

USER_NAME = False # use if your have your own account, instead organization 

REPO_NAME = "repo-name"

FILENAME = "filename" # filename to check for signed commits 

REGEXP = re.compile("\|\s[^@]+@[^@]+\.[^@]+\|")

## Usage 

`python auto-pr.py`

