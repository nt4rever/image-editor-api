from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import point
import filter
import segment
from pydantic import BaseModel
from typing import Optional
from utils import str_id, export_image
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


class Image(BaseModel):
    uri: str
    name: str
    x: Optional[int] = None
    k: Optional[int] = None
    a: Optional[int] = None
    b: Optional[int] = None
    c: Optional[int] = None


@app.post("/point/reverse")
async def reverse(image: Image):
    img = point.reverse_image(image.uri)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/point/threshold")
async def threshold(image: Image):
    img = point.threshold(image.uri, image.a, image.b)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/point/log")
async def log_transformation(image: Image):
    img = point.log_transformation(image.uri, image.c)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/point/hist")
async def hist(image: Image):
    img = point.hist(image.uri)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/filter/gaussian-blur")
async def gaussian_blur(image: Image):
    img = filter.gaussian_blur(image.uri, image.x)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/filter/laplacian")
async def laplacian(image: Image):
    img = filter.laplacian(image.uri, image.k)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/segment/kmean")
async def kmean(image: Image):
    img = segment.kmean(image.uri, image.k)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/segment/grahp-cut")
async def grahp_cut(image: Image):
    img = segment.grahp_cut(image.uri)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.post("/segment/meanshift")
async def meanshift(image: Image):
    img = segment.mean_shift(image.uri)
    name = str_id()+image.name
    export_image(img, "exports/"+name)
    return {"filename": name}


@app.get("/exports/{filename}")
def get_file(filename: str):
    return FileResponse("exports/"+filename)
