import json
import time
from pddiktipy import api
from pprint import pprint

a = api()
result = a.dump_all_univ()


# Membuat nama file dengan timestamp
timestamp = int(time.time())  # Mengambil timestamp saat ini
file_name = f'output_{timestamp}.json'  # Menambahkan timestamp ke nama file

# Menyimpan hasil ke file JSON
with open(file_name, 'w') as f:
    json.dump(result, f)