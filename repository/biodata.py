from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status, UploadFile, File, Form
import shutil

def get_all_biodata(db: Session):
    biodata_all = db.query(models.Biodata).all()
    return biodata_all

# def create(nama, file, db: Session):
#     with open(f'{file.filename}', "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     new_biodata = models.Biodata(nama = nama, nama_file = file.filename)
#     db.add(new_biodata)
#     db.commit()
#     db.refresh(new_biodata)
#     return new_biodata

def create(request, file, db: Session):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    new_biodata = models.Biodata(nama = request.nama, nama_file = file.filename)
    db.add(new_biodata)
    db.commit()
    db.refresh(new_biodata)
    return new_biodata

def destroy(id: int, db: Session):
    biodata = db.query(models.Biodata).filter(models.Biodata.id_biodata == id)
    if not biodata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Biodata dengan id {id} tidak ditemukan")
    biodata.delete(synchronize_session = False)
    db.commit()
    return 'Data Biodata Berhasil di Hapus'

def update(id: int, request: schemas.Biodata, db: Session):
    biodata = db.query(models.Biodata).filter(models.Biodata.id_biodata == id)
    if not biodata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Biodata dengan id {id} tidak ditemukan")
    biodata.update(request.dict())
    db.commit()
    return 'Data Biodata Berhasil di Update'

def show(id: int, db: Session):
    biodata = db.query(models.Biodata).filter(models.Biodata.id_biodata == id).first()
    if not biodata:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Biodata dengan id {id} tidak ditemukan")
    return biodata
