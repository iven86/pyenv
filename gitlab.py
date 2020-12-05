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


import requests
import json
import pandas as pd
from pandas import DataFrame
import cfg as cfg
import inquirer

headers = {
    'PRIVATE-TOKEN': cfg.private_token,
    'Content-Type': cfg.content_type
}

#########################
#   BUILD ENV PAYLOAD   #
#########################
def build_env_payload():

    with open(cfg.env_file,'r') as f:
        ss=f.read()
    rr=ss.split('\n')
    payload=[]
    for r in rr: 
        tk=r.split('=')
        if len(tk)!=2:
            continue
        payload.append({'variable_type': 'env_var','key':tk[0],'value':tk[1],'protected': 'true','masked': 'false','environment_scope': '*'})

    return payload

##########################
#   CREATE ENV PAYLOAD   #
##########################
def create_variables(payload):
    for index in range(len(payload)):
        response = requests.request('POST', cfg.url, headers=headers, json=payload[index])
        print(response.text.encode('utf8'))
    print('Project CI / CD variables created successfully')
    list_variables()


#########################
# List project variables#
#########################
def list_variables():
    response = requests.request('GET', cfg.url, headers=headers)
    lpv = json.loads(response.text)
    return pd.DataFrame(lpv)

###########################
# Update project variables#
###########################
def update_variables():


    print(list_variables()['key'])
    print("Choose variable ID to update")
    variable_id = int(input("Enter variale ID: "))
    variable_value = input("Enter new variale: ")

    durl = (cfg.url + "/" + list_variables()['key'][variable_id] + '?value=' + variable_value)
    response = requests.request("PUT", durl, headers=headers)
    print(response.text)
    if list_variables()['value'][variable_id] == variable_value:
        print(list_variables()['key'][variable_id], '--> Updated')

    print('Project CI / CD variable updated successfully')


###########################
# Delete project variables#
###########################
def delete_variables(payload):

    key_range = len(payload)
    key_list = key_range - 1
    for index in range(key_range):
        durl = cfg.url + "/" + payload[key_list]
        response = requests.request("DELETE", durl, headers=headers)
        print(payload[key_list], '-> Deleted')
        key_list = key_list - 1

    print('Project CI / CD variables deleted successfully')