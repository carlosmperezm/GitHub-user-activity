# Github User Activity
This is a solution of [roadmap.sh](https://roadmap.sh) project [Github User Activity](https://roadmap.sh/projects/github-user-activity)
This project just fetch the recently user activity on github by introducing the username through the comman line.

## Set up
Just clone the repo
```
git clone https://github.com/carlosmperezm/Github-user-activity.git
```
Then run the followin command to install all the dependencies
```
pip install -e .
```

## How to use it
Just use the command [github-activity] and the name of the [username] you want to fetch the data.
```
github-activity username 
```
## Note 
You should have a github api token set in you enviroment variables in order to fetch the users's data corretly
otherwise the github api will reject the request.
