
#!/usr/bin/env python3

import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--group', required=True, help="Group to add to")
parser.add_argument('--file', required=True, help="File to read users from")

ORG_URL = 'https://api.github.com'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_USER = os.environ.get('GITHUB_USER')
GITHUB_ORG = os.environ.get('GITHUB_ORG')

repos = []


def main():
    args = parser.parse_args()

    repos_file = args.file
    group = args.group
    if not os.path.exists(repos_file):
        raise Exception("Could not find file {}".format(member_file))
    with open(repos_file) as repos_file_in:
        repos = repos_file_in.read().split()


    if not os.environ.get('GITHUB_TOKEN'):
        raise ValueError('You must set GITHUB_TOKEN')
    if not os.environ.get('GITHUB_USER'):
        raise ValueError('You must set GITHUB_TOKEN')

    print("Adding {} repos to {}".format(len(repos), group))
    group_exists = requests.get(ORG_URL+ '/teams/{}/repos'.format(group), auth=(GITHUB_USER, GITHUB_TOKEN))
    group_exists.raise_for_status()
    headers = {'Accept': 'application/vnd.github.hellcat-preview+json'}
    
    for repo in repos:

        print("Adding {} to group {} ".format(repo,org,group))
        team_url = ORG_URL+ '/teams/{}/repos/{}/{}'.format(group, repo)
        r = requests.put(team_url, data='{"permission": "push"}', headers=headers, auth=(GITHUB_USER, GITHUB_TOKEN)) #read/write access 
    if r.status_code == 422:
        pass
    else:
        r.raise_for_status()
        print(r.status_code)

main()
