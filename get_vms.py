#!/usr/sbin/python3

import requests
import cred
import json
from base64 import b64encode

username = cred.username
password = cred.password
encoded_credentials = b64encode(bytes(f"{username}:{password}", encoding="ascii")).decode("ascii")
auth_header = f"Basic {encoded_credentials}"


NUTANIX_URL = ('https://' + cred.server_url + ':9440/api/nutanix/v3/vms/list')
HEADERS = {
    "Content-Type": "application/json", 
    "Authorization": f"{auth_header}", 
    "cache-control": "no-cache"}


REQUEST = {}
REQUEST["kind"] = "vm"

NUTANIX_DATA = requests.post(NUTANIX_URL, headers=HEADERS, verify=False, data=json.dumps(REQUEST))

print(NUTANIX_DATA.text)