import requests
import os.path
from os import path

session = requests.Session()
session.auth = ('rw', 'jQ4AmRNz')

session.verify = False

x = input()
rotavapor_ip = '169.254.149.76'
base_url = f"https://{rotavapor_ip}/api/v1"
process_endpoint = base_url + "/process"
set_type_msg = { 'program' : { 'type' : x }} #Das Programm "Trocknen" oder "Manuell" wird ausgewählt
set_type_resp = session.put(process_endpoint, json=set_type_msg)
process_endpoint = base_url + "/settings"
if x == 'Dry':
    set_lift_msg = { 'lift' : { 'immerseOnStart' : False }}
    set_lift_resp = session.put(process_endpoint, json=set_lift_msg)
else:
    set_lift_msg = { 'lift' : { 'immerseOnStart' : True }}
    set_lift_resp = session.put(process_endpoint, json=set_lift_msg)