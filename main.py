
from typing import Any,Dict,List
from argparse import ArgumentParser
from dotenv import load_dotenv
import os
import requests

load_dotenv()
PERSONAL_ACCESS_TOKEN:str = os.getenv('GITHUB_TOKEN')

def get_user_activity(username:str)->None:

    url:str = f'https://api.github.com/users/{username.username}/events'
    headers:Dict[str,str]= {"Authorization":f"Bearer {PERSONAL_ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers)

    data:List[Dict[str,Any]]= response.json()

    for event in data:
        commits:List[Dict[str,Any]] | None= event.get('payload').get('commits')
        repo_name:str = event.get('repo').get('name')
        if commits:
            print(f'Pushed {len(commits)} to {repo_name}')


def main() -> None:
    parser:ArgumentParser = ArgumentParser(prog='github-activity')

    parser.add_argument('username',help='Provide a username to show all the activities.')

    args = parser.parse_args()
    
    get_user_activity(args)

    




