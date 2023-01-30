from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File, Form
import schemas, database, models, auth
from sqlalchemy.orm import Session
from repository import biodata
from fastapi.responses import FileResponse
from os import getcwd

router = APIRouter(
    prefix = "/biodata",
    tags = ['Biodata']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowBiodata], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return biodata.get_all_biodata(db)

# @router.post('/', status_code = status.HTTP_201_CREATED)
# def create(nama: str = Form(), file: UploadFile = File(...), db: Session = Depends(get_db)):
#     return biodata.create(nama, file, db)

@router.post('/', status_code = status.HTTP_201_CREATED)
async def create(request: schemas.Biodata = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    data_options = request.dict()
    return biodata.create(request, file, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return biodata.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Biodata, db: Session = Depends(get_db)):
    return biodata.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowBiodata)
def show(id: int, db: Session = Depends(get_db)):
    return biodata.show(id, db)


@router.get("/download/{name_file}")
def download_file(name_file: str):
    return FileResponse(path=getcwd() + "/images/" + name_file, media_type='application/octet-stream', filename=name_file)

@router.get("/file/{name_file}")
def get_file(name_file: str):
    return FileResponse(path=getcwd() + "/images/" + name_file)
