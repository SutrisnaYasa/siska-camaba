from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    prodi_all = db.query(models.Prodi).all()
    return prodi_all

def create(request: schemas.Prodi, db: Session):
    new_prodi = models.Prodi(kode_prodi = request.kode_prodi, nama_prodi = request.nama_prodi, fakultasID = request.fakultasID)
    db.add(new_prodi)
    db.commit()
    db.refresh(new_prodi)
    return new_prodi

def destroy(id: int, db: Session):
    prodi = db.query(models.Prodi).filter(models.Prodi.id_prodi == id)
    if not prodi.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Prodi dengan id {id} tidak ditemukan")
    prodi.delete(synchronize_session = False)
    db.commit()
    return 'Data Prodi Berhasil di Hapus'

def update(id: int, request: schemas.Prodi, db: Session):
    prodi = db.query(models.Prodi).filter(models.Prodi.id_prodi == id)
    if not prodi.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Prodi dengan id {id} tidak ditemukan")
    prodi.update(request.dict())
    db.commit()
    return 'Data Prodi Berhasil di Update'

def show(id: int, db: Session):
    prodi = db.query(models.Prodi).filter(models.Prodi.id_prodi == id).first()
    if not prodi:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Prodi dengan id {id} tidak ditemukan")
    return prodi
