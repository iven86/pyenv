    # Python automation for environment variables V2.0.
    #
    # Copyright (C) 2020  Iven Leni Fernandez
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as
    # published by the Free Software Foundation, either version 3 of the
    # License, or (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU Affero General Public License for more details.
    #
    # You should have received a copy of the GNU Affero General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

from numpy.lib import index_tricks
import requests
import json
import pandas as pd
from pandas import DataFrame
import cfg as cfg


from base64 import b64encode
from nacl import encoding, public


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


url = f"https://api.github.com/repos/{cfg.GITHUB_USER}/{cfg.REPO_NAME}/actions/secrets"
kurl = f"https://api.github.com/repos/{cfg.GITHUB_USER}/{cfg.REPO_NAME}/actions/secrets/public-key"


payload={}
headers = {
  'Authorization': f'Bearer {cfg.GITHUB_TOKEN}'
}

#########################
#   List project keys   #
#########################
def get_public_key_id():

    response = requests.request("GET", kurl, headers=headers, data=payload)
    lpv = json.loads(response.text)
    return lpv

#########################
#   BUILD ENV PAYLOAD   #
#########################
def build_env_payload():

    pp = get_public_key_id()

    with open(cfg.env_file,'r') as f:
        ss=f.read()
    rr=ss.split('\n')
    payload=[]
    for r in rr: 
        tk=r.split('=')
        if len(tk)!=2:
            continue
        payload.append({'secrets_name': tk[0],'key_id':pp['key_id'],'encrypted_value': encrypt(pp['key'], tk[1])})

    return payload

payload = build_env_payload()

##########################
#   CREATE ENV PAYLOAD   #
##########################
def create_Secrets(payload):
    for index in range(len(payload)):
        surl = (url + '/' + payload[index]['secrets_name'])
        sec_dic = {"key_id" : payload[index]['key_id'], "encrypted_value" : payload[index]['encrypted_value']}
        response = requests.request('PUT', surl, headers=headers, json=sec_dic)
        print('Secret: ', payload[index]['secrets_name'], ' Created successfully')
    print('Project repository secrets created successfully')


#########################
# List project Secrets#
#########################
def list_Secrets():

    response = requests.request("GET", url, headers=headers)
    lpv = json.loads(response.text)
    dic = lpv['secrets']
    name_list = []
    for i in dic:
        name_list.append(i['name'])
    return name_list

###########################
# Update project Secrets#
###########################
def update_Secrets(payload):

    pdata = {}
    response = requests.request("GET", kurl, headers=headers, data=pdata)
    ppp = json.loads(response.text)


    slist = pd.DataFrame(list_Secrets())
    print(slist)
    print("Choose variable ID to update")
    variable_id = int(input("Enter variale ID: "))
    print(slist[0][variable_id])
    variable_value = input("Enter new variale: ")
    

    for index in range(len(payload)):
        if payload[index]['secrets_name'] == slist[0][variable_id]:
            surl = (url + '/' + payload[index]['secrets_name'])
            sec_dic = {"key_id" : payload[index]['key_id'], "encrypted_value" : encrypt(ppp['key'], variable_value)}
            requests.request('PUT', surl, headers=headers, json=sec_dic)
    print('Secret: ', slist[0][variable_id], ' Updated successfully')


###########################
# Delete project Secrets#
###########################
def delete_Secrets(payload):

    key_range = len(payload)
    key_list = key_range - 1
    for index in range(key_range):
        durl = f"https://api.github.com/repos/{cfg.GITHUB_USER}/{cfg.REPO_NAME}/actions/secrets/" + payload[key_list]
        response = requests.request("DELETE", durl, headers=headers)
        print(payload[key_list], '-> Deleted')
        key_list = key_list - 1

    print('Project secrets Secrets deleted successfully')
