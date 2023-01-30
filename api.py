from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
import pandas as pd
import shutil as st
import str_time
import os
import filetype
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

url = "http://127.0.0.1:8000/uploadfile"
myobj = {'somekey': 'somevalue'}
x = requests.post(url, json = myobj)

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# df = df.to_json()

time = str_time.now_utc()
dir_name = str_time.str_yyyy_mm_dd(time)
file_name = str_time.get_time()



# @app.post("/")
# async def root(file: UploadFile = File(...)):
#   with open(f'{file_name}', 'wb') as alex:
#     st.copyfileobj(file.file, alex)
#   return {'file_name': alex}

@app.post("/uploadfile/")
async def upload_file(files: List[UploadFile] = File(...)):
  for file_in_list in files:
    dir_path = "upload/" + str_time.str_yyyy_mm_dd(time)
    str_time.create_path("upload")
    str_time.create_path(dir_path)
    file_path = dir_path + "/" + f'{file_name}.wav'
    file_bytes = file_in_list.file.read()
    str_time.upload_file_bytes(file_bytes, file_path)
    # with open(f'{file_path}', 'wb') as alex:
    #     st.copyfileobj(file_in_list.file, alex)
    return {'file name': 'Good'}
    
@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})