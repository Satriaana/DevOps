#/usr/bin/python3
from github import Github
from dotenv import dotenv_values
import yaml

config = dotenv_values(".env") 


def main():
    readYaml("./example.yml")
    #requestDetails("devOps")
    # call here

def requestDetails(repo):
    gh = Github(config['GH_TOKEN'])
    repo = gh.get_repo(f"Satriaana/{repo}")
    open_issues = repo.get_issues(state='open')

    for issue in open_issues:
        print(issue)


def readYaml(yamlfile):
    with open(yamlfile) as file:
        data = yaml.safe_load(file)
    Projects = data['Satriaana']['Projects']

    for i in Projects:
        repos = Projects[i]['Repo-list']

        if not repos:
            print("nah")
        else:
            for repo in repos:
                print(repo)
                requestDetails(repo)

if __name__ == "__main__":
    main()


