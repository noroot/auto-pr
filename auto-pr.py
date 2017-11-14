from github import Github
import re
import sys

API_KEY = "- PASTE YOUR KEY HERE -"
ORG_NAME = "organization name" 
USER_NAME = False # use if your have your own account, instead organization 
REPO_NAME = "repo-name"
FILENAME = "filename" # filename to check for signed commits 
REGEXP = re.compile("\|\s[^@]+@[^@]+\.[^@]+\|")

g = Github(login_or_token=API_KEY)
if USER_NAME:
    org = g.get_user(USER_NAME)
else:
    org = g.get_organization(ORG_NAME)
    
r = org.get_repo(REPO_NAME)

is_matched = False
issues = r.get_pulls('open')
print("Found {} opened pull requests".format(len(list(issues))))
for issue in issues:
    commits = issue.get_commits()
    for c in commits:
        files = c.raw_data['files']
        verified = c.raw_data['commit']['verification']['verified']
        if not verified:
            print("Not verified {}".format(c.sha))
            continue
        for f in files:
            if f['filename'] == FILENAME:
                is_matched = True
                matched = f['patch'].split('+')
                if len(matched) > 0:
                    diff = matched[2]
                    if REGEXP.match(diff):
                        try:
                            issue.merge()
                            print("Merged. {}".format(c.sha))
                        except:
                            print("Unexpected error: {}".format(sys.exc_info()[0]))
                            # TODO: Errors handling
                            pass
                    else:
                        print("No rules matched for {}".format(c.sha))
                break
