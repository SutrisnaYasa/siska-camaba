from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    fakultas_all = db.query(models.Fakultas).all()
    return fakultas_all

def create(request: schemas.Fakultas, db: Session):
    new_fakultas = models.Fakultas(nama_fakultas = request.nama_fakultas)
    db.add(new_fakultas)
    db.commit()
    db.refresh(new_fakultas)
    return new_fakultas

def destroy(id: int, db: Session):
    fakultas = db.query(models.Fakultas).filter(models.Fakultas.id_fakultas == id)
    if not fakultas.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Fakultas dengan id {id} tidak ditemukan")
    fakultas.delete(synchronize_session = False)
    db.commit()
    return 'Data Fakultas Berhasil di Hapus'

def update(id: int, request: schemas.Fakultas, db: Session):
    fakultas = db.query(models.Fakultas).filter(models.Fakultas.id_fakultas == id)
    if not fakultas.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Fakultas dengan id {id} tidak ditemukan")
    fakultas.update(request.dict())
    db.commit()
    return 'Data Fakultas Berhasil di Update'

def show(id: int, db: Session):
    fakultas = db.query(models.Fakultas).filter(models.Fakultas.id_fakultas == id).first()
    if not fakultas:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Fakultas dengan id {id} tidak ditemukan")
    return fakultas
