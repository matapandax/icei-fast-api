import requests
import json
import os
from datetime import datetime

# Menentukan URL API Open edX
url_courses = "https://satu.icei.ac.id/api/courses/v1/courses/"
url_users = "https://satu.icei.ac.id/api/user/v1/accounts/"

# Menentukan parameter yang dibutuhkan, seperti kunci API
params = {
    "format": "json",
    "page_size": 100  # Jumlah maksimum kursus yang akan diambil
}

# Mengirim permintaan HTTP GET ke API Open edX untuk data kursus
response_courses = requests.get(url_courses, params=params)

# Memeriksa kode status respons untuk data kursus
if response_courses.status_code == 200:
    # Mengonversi respons JSON kursus menjadi objek Python
    data_courses = response_courses.json()

    # Melakukan iterasi pada setiap kursus dalam respons kursus
    for course in data_courses["results"]:
        course_id = course["id"]
        course_name = course["name"]
        course_number = course["number"]
        print(f"Course ID: {course_id}")
        print(f"Course Name: {course_name}")
        print(f"Course Number: {course_number}")

        # Mengirim permintaan HTTP GET ke API Open edX untuk data pengguna kursus
        url_course_users = f"{url_courses}{course_id}/users/"
        response_users = requests.get(url_course_users, params=params)

        # Memeriksa kode status respons untuk data pengguna kursus
        if response_users.status_code == 200:
            # Mengonversi respons JSON pengguna kursus menjadi objek Python
            data_users = response_users.json()

            # Memeriksa apakah kunci "results" ada dalam respons pengguna kursus
            if "results" in data_users:
                # Melakukan iterasi pada setiap pengguna dalam respons pengguna kursus
                for user in data_users["results"]:
                    user_id = user["id"]
                    user_username = user["username"]
                    print(f"User ID: {user_id}")
                    print(f"Username: {user_username}")
            else:
                print(f"Tidak ada data pengguna dalam respons pengguna kursus.")
        else:
            print(f"Gagal mengambil data pengguna kursus. Kode status: {response_users.status_code}")
else:
    print(f"Gagal mengambil data kursus. Kode status: {response_courses.status_code}")
