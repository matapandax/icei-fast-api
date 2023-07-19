import requests
import json
import os
from datetime import datetime

# Menentukan URL API Open edX
url = "https://satu.icei.ac.id/api/courses/v1/courses/"

# Menentukan parameter yang dibutuhkan, seperti kunci API
params = {
    "format": "json",
    "page_size": 100  # Jumlah maksimum kursus yang akan diambil
}

# Mengirim permintaan HTTP GET ke API Open edX
response = requests.get(url, params=params)

# Memeriksa kode status respons
if response.status_code == 200:
    # Mengonversi respons JSON menjadi objek Python
    data = response.json()

    # Melakukan iterasi pada setiap kursus dalam respons
    for course in data["results"]:
        course_id = course["id"]
        course_name = course["name"]
        course_number = course["number"]
        print(f"Course ID: {course_id}")
        print(f"Course Name: {course_name}")
        print(f"Course Number: {course_number}")

    # Menentukan nama file untuk ekspor JSON
    file_name = "courses.json"
    if os.path.exists(file_name):
        # Jika file sudah ada, tambahkan nomor unik atau tanda waktu ke dalam nama file baru
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"courses_{timestamp}.json"

    # Menulis data ke file JSON
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Data kursus berhasil diekspor ke {file_name}")
else:
    print("Gagal mengambil data kursus. Kode status:", response.status_code)
