import subprocess



def main():
    command = input("Enter custom 'git' command")
    match command:
        case 'push':
            exe_push()
        case _:
            print('Please try')

def exe_push():
    placeholder = input("Enter the comment for the commit: ")
    placeholder = '"' + placeholder + '"'

    PUSH = [
        ["git","add", ".", ],
        ["git", "commit", "-m", placeholder],
        ["git", "branch", "-M", "main"],
        ["git", "push", "-u", "origin", "main"]
        ]    
    loop_actions(PUSH)
    

def loop_actions(command):
    for actions in command:
        print(actions)
        result = subprocess.run(actions, shell=True, capture_output=True, text=True)
        print(result.stdout)    

if __name__ == '__main__':
    main()