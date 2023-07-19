import requests
import json

# Konfigurasi URL dan kredensial API Open edX
base_url = 'https://satu.icei.ac.id/api'
username = 'caesariost'
password = 'Satriatama155@'

# Endpoint API untuk mendapatkan data pengguna
endpoint = 'user/v1/accounts/'

try:
    # Mengirim permintaan autentikasi
    auth_response = requests.post(base_url + 'auth/login', json={'username': username, 'password': password})
    auth_response.raise_for_status()
    auth_token = auth_response.json().get('access_token')

    # Menambahkan token ke header permintaan
    headers = {'Authorization': 'Bearer ' + auth_token}

    # Mengirim permintaan untuk mendapatkan data pengguna
    data_response = requests.get(base_url + endpoint, headers=headers)
    data_response.raise_for_status()

    # Periksa kode status respons
    if data_response.status_code == 200:
        data = data_response.json()

        # Menyimpan data JSON ke file
        with open('openedx_user_data.json', 'w') as file:
            json.dump(data, file)
    else:
        print('Permintaan gagal. Kode status:', data_response.status_code)

except requests.exceptions.RequestException as e:
    print('Terjadi kesalahan saat melakukan permintaan:', str(e))
except json.decoder.JSONDecodeError as e:
    print('Terjadi kesalahan dalam dekode JSON:', str(e))
