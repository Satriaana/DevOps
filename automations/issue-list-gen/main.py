# /usr/bin/python3
from dotenv import dotenv_values
import yaml

from details import requestDetails, DetailsHandler
from utils import highlight_max, formatObject
from sendmail import SendMail

config = dotenv_values(".env")


def main():
    readYaml("./.data/example.yml")
    """
    requestDetails("devOps")
    call here

    """


def readYaml(yamlfile):
    with open(yamlfile) as file:
        data = yaml.safe_load(file)

    Projects = data[config['ORG']]['Projects']

    for i in Projects:
        repos = Projects[i]['Repo-list']
        projectManager = Projects[i]['Project-Manager']
        mail_group = Projects[i]['mail-group']
        userandissues = DetailsHandler(repos, projectManager)
        payload = formatObject(userandissues, projectManager)
        SendMail("z9fr@protonmail.com", payload, projectManager)


if __name__ == "__main__":
    main()
