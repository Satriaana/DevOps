#/usr/bin/python3
from github import Github
from dotenv import dotenv_values


def main():
    print("main")
    # call here

def requestDetails():
    config = dotenv_values(".env") 
    gh = Github(config['token'])

    repo = gh.get_repo("Satriaana/DevOps")
    open_issues = repo.get_issues(state='open')

    for issue in open_issues:
        print(issue)


if __name__ == "__main__":
    main()


