import requests

result = requests.get('https://raw.githubusercontent.com/waferdp/python-intro/refs/heads/main/README.md')

if result.ok:
    print(result.content)
else:
    print(f'{result.status_code}: {result.reason}' )