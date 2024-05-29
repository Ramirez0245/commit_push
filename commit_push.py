import subprocess

placeholder = input("Enter the comment for the commit: ")
placeholder = '"' + placeholder + '"'
ACTIONS = [
    ["git","add", ".", ],
    ["git", "commit", "-m", placeholder],
    ["git", "branch", "-M", "main"],
    ["git", "push", "-u", "origin", "main"]
    ]

for command in ACTIONS:
    print(command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

