import requests
import os.path
from os import path

session = requests.Session()
session.auth = ('rw', 'jQ4AmRNz')

session.verify = False

rotavapor_ip = '169.254.149.76'
base_url = f"https://{rotavapor_ip}/api/v1"
process_endpoint = base_url + "/process"

stop_rotation_msg = { 'rotation' : { 'running' : False }}
set_stop_rotation_msg = session.put(process_endpoint, json=stop_rotation_msg)