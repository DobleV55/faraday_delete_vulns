import requests
import click

username = click.prompt('username')
password = click.prompt('password', hide_input=True)
server_address = click.prompt('Faraday Server URL', default='https://localhost:5985')
workspace = click.prompt('workspace')
severity = click.prompt('vuln_severity to delete', default='informational')

s = requests.Session()

login = s.post(server_address + '/_api/login', json={'email':username, 'password':password})
if login.status_code == 401:
    print('Invalid Credentials') 

delete_vuln = 'https://staging.faradaysec.com/_api/v2/ws/'+workspace+'/vulns/bulk_delete/'

delete = s.delete(delete_vuln,json={'severities':[severity]})
print(delete.status_code)
print(delete.text)