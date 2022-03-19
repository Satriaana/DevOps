#/usr/bin/python3
from github import Github
from dotenv import dotenv_values
import yaml

config = dotenv_values(".env") 

def main():
    readYaml("./example.yml")
    #requestDetails("devOps")
    # call here

def requestDetails(repoName):
    allIssue = []
    gh = Github(config['GH_TOKEN'])
    repo = gh.get_repo(f"{config['ORG']}/{repoName}")
    open_issues = repo.get_issues(state='open')

    for issue in open_issues:
        issueUrl = f"https://github.com/{config['ORG']}/{repoName}/issues/{issue.number}"
        issueDict = { 'name': repoName, 'issueNumber': issue.number, 'url':issueUrl, 'title':issue.title }
        allIssue.append(issueDict)

    print(allIssue)


def readYaml(yamlfile):
    with open(yamlfile) as file:
        data = yaml.safe_load(file)
    Projects = data[config['ORG']]['Projects']

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


