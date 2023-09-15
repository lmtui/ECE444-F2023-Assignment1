import subprocess

def get_current_git_branch():
    try:
        return subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode("utf-8")
    except subprocess.CalledProcessError:
        return None

if __name__ == "__main__":
    current_branch = get_current_git_branch()

    if current_branch == "develop":
        print("Hello World, 3 Years at Uoft")
    else:
        print(f"Run this on the develop branch")
