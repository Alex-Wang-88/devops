from lib2to3.pgen2 import token
from github import Github
import yaml

# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object

data = yaml.safe_load(open('credentials.yml'))

# Extract the user and token from the data object
# 0. Complete these 2 lines below
user = 'Alex-Wang-88/devops'
token = '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'

# using an access token
g = Github(token)
repo = g.get_repo(user)

## Complete your tasks from here

# 1. Get all branches you have created for your public repo
list(repo.get_branches())

# 2. Get all pull requests you have created
pulls = repo.get_pulls(state='open', sort='created', base='master')
for pr in pulls:
    print(pr.number)

# 3. Get a list of commits you have created in your `main` branch.
#commit.getStatuses()
#commit = repo.get_commit(sha=sha)
#print(commit.commit.author.date)