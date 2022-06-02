"""
utils
"""
import pandas as pd


def highlight_max(s, color):
    return ['background-color: yellow' if s.name % 2 else '' for v in s]


def formatObject(userandissues, projectManager):
    payload = ""

    for pm in userandissues:
        payload += f"<h1> {pm} </h1>"
        if not userandissues[pm]:
            payload += ("<code> no issues </code>")
        else:
            for info in userandissues[pm]:
                # printing usernmae
                payload += (f"<h4> <u> {info[0]['name']} </u> </h4>")
                df = pd.DataFrame(data=info)

                # embed the url inside a a tag
                df['url'] = '<a href=' + df['url'] + \
                    '><div>' + df['url'] + '</div></a>'
                df_print = df[['issueNumber', 'url', 'title']]

                # output the table
                payload += (df_print.style.apply(
                    highlight_max, color='green', axis=1).hide(axis='index').to_html(
                    escape=False,
                ))

        payload += "<hr>"
        return payload
