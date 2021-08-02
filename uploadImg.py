import pyrebase

def fetchData():
    config = {
        "apiKey": "AIzaSyCHFa3Xe1_OT7CSlcihnr8qkkp8nMOqxho",
        "authDomain": "uploadimg-d9f60.firebaseapp.com",
        "projectId": "uploadimg-d9f60",
        "databaseURL": "xxxxxx",
        "storageBucket": "uploadimg-d9f60.appspot.com",
        "messagingSenderId": "103516727890",
        "appId": "1:103516727890:web:cc47badd32d43a3d108d8b",
        "measurementId": "G-GPK6D1ZZQP"
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()

    employee = "Joshua Jerez"
    path_on_cloud = "images/" + employee +".jpg"
     # path_local = "Capture.jpg"

    # Uploading Image
    # storage.child(path_on_cloud).put(path_local)

    # Downloading Image
    storage.child(path_on_cloud).download("ImagesAttendance/" + employee+ ".jpg")