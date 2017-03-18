import pytest
import csv
from github_api import GitHubAPI

positive_creds = list(csv.reader(open('positive_logins.csv'), delimiter='\t', quotechar="'"))[1:]
negative_creds = list(csv.reader(open('negative_logins.csv'), delimiter='\t', quotechar="'"))[1:]
github = GitHubAPI()

@pytest.mark.parametrize("login,password", positive_creds)
def test_positive_login(login, password):
    assert github.try_login(login, password)
    
@pytest.mark.parametrize("login,password", negative_creds)
def test_negative_login(login, password):
    assert not github.try_login(login, password)
