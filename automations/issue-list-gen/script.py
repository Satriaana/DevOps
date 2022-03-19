#/usr/bin/python3
from github import Github
from dotenv import dotenv_values
import yaml

config = dotenv_values(".env") 
allprojectDetails = {}

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

    return allIssue


def DetailsHandler(repos, projectmanager, mail_group, project):

    """
    Project

    mailgroup , projectmanager
    repo -> all issues 

    projectname -> repo[issues] , pm , mailgroup
    """

    allprojectDetails[projectmanager] = repos

    if not repos:
        print("nah")
    else:
        for id, repo in enumerate(repos):
            allprojectDetails[projectmanager][id] = requestDetails(repo)

    print(allprojectDetails)


def readYaml(yamlfile):
    with open(yamlfile) as file:
        data = yaml.safe_load(file)

    Projects = data[config['ORG']]['Projects']

    for i in Projects:
        repos = Projects[i]['Repo-list']
        projectManager = Projects[i]['Project-Manager']
        mail_group = Projects[i]['mail-group']
        DetailsHandler(repos , projectManager, mail_group, i )


if __name__ == "__main__":
    main()


