import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import point

app = FastAPI()


@app.post("/point/reverse", response_class=FileResponse)
async def root(file: UploadFile = File(...)):
    with open(f'uploads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "./uploads/"+file.filename
    image = point.reverse_image(path)
    point.export_image(image, "exports/"+file.filename)
    res = "exports/"+file.filename
    return res


@app.post("/point/threshold", response_class=FileResponse)
async def root(file: UploadFile = File(...), a: int = 0, b: int = 100):
    with open(f'uploads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "./uploads/"+file.filename
    image = point.threshold(path, a, b)
    point.export_image(image, "exports/"+file.filename)
    res = "exports/"+file.filename
    return res


@app.post("/point/log", response_class=FileResponse)
async def root(file: UploadFile = File(...), c: float = 2):
    with open(f'uploads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "./uploads/"+file.filename
    image = point.log_transformation(path, c)
    point.export_image(image, "exports/"+file.filename)
    res = "exports/"+file.filename
    return res

@app.post("/point/hist", response_class=FileResponse)
async def root(file: UploadFile = File(...)):
    with open(f'uploads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "./uploads/"+file.filename
    image = point.hist(path)
    point.export_image(image, "exports/"+file.filename)
    res = "exports/"+file.filename
    return res
