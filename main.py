from typing import Any,Dict,List
from argparse import ArgumentParser,Namespace
from dotenv import load_dotenv
import os
import requests
import redis 
import json

load_dotenv()
PERSONAL_ACCESS_TOKEN:str = os.getenv('GITHUB_ACCESS_TOKEN')
r = redis.Redis(host='localhost',port=6379,decode_responses=True)



def get_user_activity(username:str | Namespace)->None:
    if PERSONAL_ACCESS_TOKEN is None:
        print('Please provide a personal access token')
        return

    username_str:str = username.username
    url:str = f'https://api.github.com/users/{username_str}/events'
    headers:Dict[str,str]= {"Authorization":f"Bearer {PERSONAL_ACCESS_TOKEN}"}

    data:List[Dict[str,Any]] = []

    if r.exists(username_str):
        print('Getting the data from the cache')
        data = json.loads(r.get(username_str))
    else:
        print('The data wasn\'t in the cache')
        response = requests.get(url, headers=headers)
        data = response.json()
        print('Saving the data in the cache...')
        r.set(username_str,json.dumps(data)) 

    try:
        for event in data:
            commits:List[Dict[str,Any]] | None = event.get('payload').get('commits')
            repo_name:str = event.get('repo').get('name')
            if commits:
                print(f'Pushed {len(commits)} to {repo_name}')
    except Exception as e:
        print('No commits found')
        print(e)


def main() -> None:
    parser:ArgumentParser = ArgumentParser(prog='github-activity')

    parser.add_argument('username',help='Provide a username to show all the activities.')

    args = parser.parse_args()
    
    get_user_activity(args)
    

    




