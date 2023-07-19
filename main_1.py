from fastapi import FastAPI
import requests

app = FastAPI()

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
