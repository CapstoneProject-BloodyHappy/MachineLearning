from flask import request

from app import app,APP_ROOT
from app.process import predictImage

@app.route('/')
def home():
    return 'Hellso, world'

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    if request.method == 'POST':
        request_data = request.get_json()
        file_link = request_data["file_link"]
        x=predictImage(file_link)
        return x