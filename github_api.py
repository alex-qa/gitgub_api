import requests

class GitHubAPI:
    
    def __init__(self, base_uri='https://api.github.com'):
        self.base_uri = base_uri
        
    def try_login(self, login, password):
        r = requests.get(self.base_uri, auth=(login, password))
        if r.status_code == 200:
            return True
        else:
            return False

if __name__ == '__main__':
    github = GitHubAPI()
    github.try_login('user', 'password')           # Negative
    github.try_login('alex-qa', 'Password2017$@')  # Positive