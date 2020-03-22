from github import Github

from . import secret_store


def login(gh_secrets: secret_store.GitHub) -> Github:
    return Github(gh_secrets.access_token)
