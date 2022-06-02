"""
Details
"""
from github import Github
from dotenv import dotenv_values

config = dotenv_values(".env")


def RequestDetails(repoName):
    allIssue = []
    gh = Github(config['GH_TOKEN'])
    repo = gh.get_repo(f"{config['ORG']}/{repoName}")
    open_issues = repo.get_issues(state='open')

    for issue in open_issues:
        issueUrl = f"https://github.com/{config['ORG']}/{repoName}/issues/{issue.number}"
        issueDict = {'name': repoName, 'issueNumber': issue.number,
                     'url': issueUrl, 'title': issue.title}
        allIssue.append(issueDict)

    return allIssue


def DetailsHandler(repos, projectmanager):
    allprojectDetails = {}

    """
    Project
    {"senali" : {issues}}
    """

    allprojectDetails[projectmanager] = repos

    if not repos:
        print()
    else:
        for id, repo in enumerate(repos):
            allprojectDetails[projectmanager][id] = RequestDetails(repo)

    return allprojectDetails
