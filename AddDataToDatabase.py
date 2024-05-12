import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendencerealtime-e3d59-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "203047":
        {
            "name": "Harsh Kumar Singh",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "203030":
        {
            "name": "Chashmeet Singh Sehgal",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 1,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "203050":
        {
            "name": "Himanshu Kansal",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 2,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)