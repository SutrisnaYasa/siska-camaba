from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Form, Depends, UploadFile

# Membuat Pilihan Untuk Role
class Roles(str, Enum):
    user = "user",
    admin = "admin"

# Schemas Untuk Users
class User(BaseModel):
    username: str
    password: str
    role: Roles
    is_active: bool = True

class ShowUser(BaseModel):
    username: str
    is_active: bool = True
    role: Roles

    class Config():
        orm_mode = True
# End Schemas Untuk User


# Schemas Untuk Login
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
# End Schemas Untuk Login


# Schemas Untuk Master Fakultas
class FakultasBase(BaseModel):
    nama_fakultas: str

class Fakultas(FakultasBase):
    class Config():
        orm_mode = True

class ShowFakultas(BaseModel):
    id_fakultas : int
    nama_fakultas: str

    class Config():
        orm_mode = True
# End Schemas Master Fakultas


# Schemas Untuk Master Prodi
class ProdiBase(BaseModel):
    kode_prodi: str
    nama_prodi: str
    fakultasID: int

class Prodi(ProdiBase):
    class Config():
        orm_mode = True

class ShowProdi(BaseModel):
    id_prodi: int
    kode_prodi: str
    nama_prodi: str
    prodis: ShowFakultas

    class Config():
        orm_mode = True
# End Schemas Master Prodi


# Schemas Untuk Biodata
class BiodataBase(BaseModel):
    nama: str = Form(...)

class Biodata(BiodataBase):
    class Config():
        orm_mode = True

class ShowBiodata(BaseModel):
    nama: str
    nama_file: str

    class Config():
        orm_mode = True
# End Schemas Biodata
