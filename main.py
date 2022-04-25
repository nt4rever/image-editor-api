from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import point
import filter
import utils
from utils import uploads, remove_file, remove_files, str_id
app = FastAPI()

origins = ["*"]
exports_folder = "exports/*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/point/reverse")
async def root(file: UploadFile = File(...)):
    remove_files(exports_folder)
    file.filename = str_id()+file.filename
    path = uploads(file)
    image = point.reverse_image(path)
    point.export_image(image, "exports/"+file.filename)
    remove_file(path)
    return {"filename": file.filename}


@app.post("/point/threshold")
async def root(file: UploadFile = File(...), a: int = 0, b: int = 100):
    remove_files(exports_folder)
    file.filename = str_id()+file.filename
    path = uploads(file)
    image = point.threshold(path, a, b)
    point.export_image(image, "exports/"+file.filename)
    remove_file(path)
    return {"filename": file.filename}


@app.post("/point/log")
async def root(file: UploadFile = File(...), c: float = 2):
    remove_files(exports_folder)
    file.filename = str_id()+file.filename
    path = uploads(file)
    image = point.log_transformation(path, c)
    point.export_image(image, "exports/"+file.filename)
    remove_file(path)
    return {"filename": file.filename}


@app.post("/point/hist")
async def root(file: UploadFile = File(...)):
    remove_files(exports_folder)
    file.filename = str_id()+file.filename
    path = uploads(file)
    image = point.hist(path)
    point.export_image(image, "exports/"+file.filename)
    remove_file(path)
    return {"filename": file.filename}


@app.post("/filter/gaussian_blur")
async def root(file: UploadFile = File(...), x: int = 5):
    remove_files(exports_folder)
    file.filename = str_id()+file.filename
    path = uploads(file)
    image = filter.gaussian_blur(path, x)
    point.export_image(image, "exports/"+file.filename)
    remove_file(path)
    return {"filename": file.filename}


@app.post("/filter/laplacian")
async def root(file: UploadFile = File(...), k: int = 3):
    remove_files(exports_folder)
    file.filename = str_id()+file.filename
    path = uploads(file)
    image = filter.laplacian(path, k)
    point.export_image(image, "exports/"+file.filename)
    remove_file(path)
    return {"filename": file.filename}


@app.get("/exports/{filename}")
def get_file(filename: str):
    return FileResponse("exports/"+filename)
