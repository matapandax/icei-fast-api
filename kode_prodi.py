import json
import time
from pddiktipy import api
from pprint import pprint
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


a = api()
result = a.dump_all_prodi()


# Membuat nama file dengan timestamp
timestamp = int(time.time())  # Mengambil timestamp saat ini
file_name = f'output_{timestamp}.json'  # Menambahkan timestamp ke nama file

# Menyimpan hasil ke file JSON
with open(file_name, 'w') as f:
    json.dump(result, f)
