import os
import sys

CMD_OK = 0
INVALID_INPUT = -1
MISSING_DEPS = -2
CMD_INVALID_RETURN = -3
INVALID_SYSTEM = -4
INVALID_BUILD_TOOLS = -5


def clone_or_pull_git(uri, destination):
    if not destination:
        destination = uri.split("/")[-1].replace(".git", "")
    if not os.path.isdir(destination):
        print("Cloning", uri)
        status = os.system(f"git clone {uri} {destination}")
    else:
        print("Folder, already exist. Updating existing repo")
        status = os.system(f"cd {destination} && git pull")
    if status != CMD_OK:
        print("Invalid command return detected:", status)
        sys.exit(CMD_INVALID_RETURN)
