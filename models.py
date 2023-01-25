from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean, Enum
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

# Models Untuk Users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(100))
    password = Column(String(100))
    is_active = Column(Boolean, default = True)
    role = Column(String(100), nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models untuk Master Fakultas
class Fakultas(Base):
    __tablename__ = 'master_fakultas'
    id_fakultas = Column(Integer, primary_key = True, index = True)
    nama_fakultas = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    fakultass = relationship("Prodi", back_populates = "prodis")
    
# Models untuk Master Prodi
class Prodi(Base):
    __tablename__ = 'master_prodi'
    id_prodi = Column(Integer, primary_key = True, index = True)
    kode_prodi = Column(String(10))
    nama_prodi = Column(String(100))
    fakultasID = Column(Integer, ForeignKey('master_fakultas.id_fakultas'))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    prodis = relationship("Fakultas", back_populates = "fakultass")
