import requests

# Menentukan URL API Open edX untuk data pengguna
url = "https://satu.icei.ac.id/api/user/v1/accounts/"

# Menentukan parameter yang dibutuhkan, seperti kunci API
params = {
    "format": "json",
    "page_size": 100  # Jumlah maksimum pengguna yang akan diambil
}

# Mengirim permintaan HTTP GET ke API Open edX untuk data pengguna
response = requests.get(url, params=params)

# Memeriksa kode status respons
if response.status_code == 200:
    # Mengonversi respons JSON menjadi objek Python
    data = response.json()

    # Melakukan iterasi pada setiap pengguna dalam respons
    for user in data["results"]:
        user_id = user["id"]
        user_username = user["username"]
        user_email = user["email"]
        print(f"User ID: {user_id}")
        print(f"Username: {user_username}")
        print(f"Email: {user_email}")
else:
    print("Gagal mengambil data pengguna. Kode status:", response.status_code)
