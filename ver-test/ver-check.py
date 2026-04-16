import requests

url = "https://raw.githubusercontent.com/Lockmastern/test-versioning/refs/heads/main/version"

with open('version', 'r') as f:
    currentVersion = f.read()

githubVersion = requests.get(url).text.strip()

print(f'Current Version >> {currentVersion}\nGithub Version >> {githubVersion}')