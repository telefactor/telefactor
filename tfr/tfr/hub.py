from functools import lru_cache

from github import Github

from .secret_store import Secrets


@lru_cache()
def login(gh_secrets: Secrets.GitHub) -> Github:
    return Github(gh_secrets.access_token)
