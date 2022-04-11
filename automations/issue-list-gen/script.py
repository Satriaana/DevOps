# /usr/bin/python3
from github import Github
from dotenv import dotenv_values
import yaml
import pandas as pd

config = dotenv_values(".env")


def main():
    readYaml("./example.yml")
    """
    requestDetails("devOps")
    call here

    """


def requestDetails(repoName):
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
            allprojectDetails[projectmanager][id] = requestDetails(repo)

    return allprojectDetails


def highlight_max(s, color):
    return ['background-color: yellow' if s.name % 2 else '' for v in s]


def formatObject(userandissues, projectManager):

    for pm in userandissues:
        print(f"<h1> {pm} </h1>")
        if not userandissues[pm]:
            print("<code> no issues </code>")
        else:
            for info in userandissues[pm]:
                # printing usernmae
                print(f"<h4> <u> {info[0]['name']} </u> </h4>")
                df = pd.DataFrame(data=info)

                # embed the url inside a a tag
                df['url'] = '<a href=' + df['url'] + \
                    '><div>' + df['url'] + '</div></a>'
                df_print = df[['issueNumber', 'url', 'title']]

                # output the table
                print(df_print.style.apply(
                    highlight_max, color='green', axis=1).hide(axis='index').to_html(
                    escape=False,
                ))

        print("<hr>")


def readYaml(yamlfile):
    with open(yamlfile) as file:
        data = yaml.safe_load(file)

    Projects = data[config['ORG']]['Projects']

    for i in Projects:
        repos = Projects[i]['Repo-list']
        projectManager = Projects[i]['Project-Manager']
        mail_group = Projects[i]['mail-group']
        userandissues = DetailsHandler(repos, projectManager)
        formatObject(userandissues, projectManager)


if __name__ == "__main__":
    main()
