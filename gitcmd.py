import subprocess

def run_git_status():
    subprocess.run(["git", "status"])

def run_git_add():
    subprocess.run(["git", "add", "."])

def run_git_commit():
    commit_message = input("Enter commit message: ")
    subprocess.run(["git", "commit", "-m", commit_message])

def run_git_push():
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    run_git_status()
    run_git_add()
    run_git_commit()
    run_git_push()
