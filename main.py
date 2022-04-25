import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uvicorn
import point
import filter

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


@app.post("/filter/gaussian_blur", response_class=FileResponse)
async def root(file: UploadFile = File(...), x: int = 5):
    with open(f'uploads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "./uploads/"+file.filename
    image = filter.gaussian_blur(path, x)
    point.export_image(image, "exports/"+file.filename)
    res = "exports/"+file.filename
    return res

@app.post("/filter/laplacian", response_class=FileResponse)
async def root(file: UploadFile = File(...), k: int = 3):
    with open(f'uploads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    path = "./uploads/"+file.filename
    image = filter.laplacian(path, k)
    point.export_image(image, "exports/"+file.filename)
    res = "exports/"+file.filename
    return res

if __name__ == '__main__':
    uvicorn.run("app.main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                )