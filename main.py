from fastapi import FastAPI
import json
import time
from pddiktipy import api
import ssl
import requests

app = FastAPI()
ssl._create_default_https_context = ssl._create_unverified_context

@app.get("/search", response_model=dict)
def search_mahasiswa(names: str):
    pddikti = api()
    names_list = names.split(",")  # Memisahkan nama-nama mahasiswa berdasarkan koma

    results = []
    for name in names_list:
        result = pddikti.search_mahasiswa(name.strip())  # Menghapus spasi ekstra pada nama
        results.append(result)

    # Membuat nama file dengan timestamp
    timestamp = int(time.time())  # Mengambil timestamp saat ini
    file_name = f'output_{timestamp}.json'  # Menambahkan timestamp ke nama file

    # Menyimpan hasil ke file JSON
    with open(file_name, 'w') as f:
        json.dump(results, f)

    # Mengembalikan hasil pencarian dalam format JSON
    return {"message": "Search completed", "file_name": file_name, "results": results}

@app.get("/courses")
def get_courses():
    # Menentukan URL API Open edX untuk data course
    url = "https://satu.icei.ac.id/api/courses/v1/courses/"

    # Menentukan parameter yang dibutuhkan, seperti kunci API
    params = {
        "format": "json",
        "page_size": 100  # Jumlah maksimum course yang akan diambil
    }

    # Mengirim permintaan HTTP GET ke API Open edX untuk data course
    response = requests.get(url, params=params)

    # Memeriksa kode status respons untuk data course
    if response.status_code == 200:
        # Mengonversi respons JSON menjadi objek Python
        data = response.json()
        courses = []

        # Melakukan iterasi pada setiap course dalam respons course
        for course in data["results"]:
            course_id = course["id"]
            course_name = course["name"]
            course_number = course["number"]
            courses.append({
                "course_id": course_id,
                "course_name": course_name,
                "course_number": course_number
            })

        return courses
    else:
        return {"message": "Gagal mengambil data course. Kode status:", "status_code": response.status_code}

@app.get("/users")
def get_users():
    # Menentukan URL API Open edX untuk data user
    url = "https://satu.icei.ac.id/api/user/v1/accounts/"

    # Menentukan parameter yang dibutuhkan, seperti kunci API
    params = {
        "format": "json",
        "page_size": 100  # Jumlah maksimum user yang akan diambil
    }

    # Mengirim permintaan HTTP GET ke API Open edX untuk data user
    response = requests.get(url, params=params)

    # Memeriksa kode status respons untuk data user
    if response.status_code == 200:
        # Mengonversi respons JSON menjadi objek Python
        data = response.json()
        users = []

        # Melakukan iterasi pada setiap user dalam respons user
        for user in data["results"]:
            user_id = user["id"]
            user_username = user["username"]
            users.append({
                "user_id": user_id,
                "user_username": user_username
            })

        return users
    else:
        return {"message": "Gagal mengambil data user. Kode status:", "status_code": response.status_code}
