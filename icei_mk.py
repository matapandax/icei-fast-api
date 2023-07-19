import requests
import json

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
        course_number= course["number"]
        print(f"Course ID: {course_id}")
        print(f"Course Name: {course_name}")
        print(f"Course Number: {course_number}")

    # Menulis data ke file JSON
    with open("courses.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("Data kursus berhasil diekspor ke courses.json")
else:
    print("Gagal mengambil data kursus. Kode status:", response.status_code)
