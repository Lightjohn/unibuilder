import os


def is_git_url(uri: str):
    # If uri looks like an git url
    if uri.startswith("http"):
        return True
    if uri.startswith("git@"):
        return True
    return False


def is_local_uri(uri: str):
    # If local folder exist and is populated
    if os.path.isdir(uri):
        files = os.listdir(uri)
        if len(files) > 0:
            return True
    return False
