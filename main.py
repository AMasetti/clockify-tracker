import requests
import datetime

from constants import HOLIDAYS_ENDPOINT, USER_ID, WORKSPACE_NIMBLE_LA
from helper import add_entry_endpoint

year = f'{datetime.datetime.now():%Y}'
data = requests.get(f'{HOLIDAYS_ENDPOINT}{year}').json()
print(f'Este año habra {len(data)} feriados')
print(data)
print(f"{datetime.datetime.now():%Y-%m-%d}")

x = requests.post(add_entry_endpoint(WORKSPACE_NIMBLE_LA,USER_ID), headers=)
