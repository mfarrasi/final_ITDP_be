from sqlalchemy import Column, String, Integer, Float, Boolean, Date, ForeignKey, Text, ARRAY, Enum, DateTime
from app.db import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String(50), nullable=False)

class Kantor(Base):
    __tablename__ = "kantor"

    kantor_id = Column(Integer, primary_key= True, autoincrement=True)
    cabang = Column(String(255), nullable=False)
    wilayah = Column(String(255), nullable=False)
    jumlah_total_npl = Column(Integer, nullable=True)

class Perusahaan(Base):
    __tablename__ = "perusahaan"

    cif = Column(String(50), primary_key=True)
    nama_perusahaan = Column(String(255), nullable=False)
    total_outstanding = Column(Integer)
    kantor_id = Column(Integer, ForeignKey("kantor.kantor_id"), nullable=False)

    kantor = relationship("Kantor", backref="perusahaan_list")

class Fasilitas(Base):
    __tablename__ = "fasilitas"

    deal_ref = Column(String(50), primary_key=True)
    cif = Column(String(50), ForeignKey("perusahaan.cif"), nullable=False)
    jenis_fasilitas = Column(String(100))
    jumlah_outstanding = Column(Integer)
    tanggal_mulai_macet = Column(Date)
    key_person_perusahaan = Column(String(255))
    progres_npl = Column(Text)
    restruktur_terakhir = Column(Date)
    ao_komersial = Column(Integer, ForeignKey("users.id"))
    ao_ppk = Column(Integer, ForeignKey("users.id"))
    jumlah_kredit_recovered = Column(Integer, default=0)

class Agunan(Base):
    __tablename__ = "agunan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    deal_ref = Column(String(50), ForeignKey("fasilitas.deal_ref"), nullable=False)
    jenis_agunan = Column(String(100))
    reappraisal_terakhir = Column(Integer)
    tanggal_reappraisal = Column(Date)
    status_agunan = Column(String(100))

class History(Base):
    __tablename__ = "history"

    event_history_id = Column(Integer, primary_key=True, autoincrement=True)
    deal_ref = Column(String(50), ForeignKey("fasilitas.deal_ref"))
    jenis_kegiatan = Column(String(255))
    ao_input = Column(Integer, ForeignKey("users.id"))
    keterangan_kegiatan = Column(Text)
    tanggal = Column(Date)
    status = Column(String(255), default='Berhasil')
    image = Column(Text)

class RoadmapPlan(Base):
    __tablename__ = "roadmap_plan"

    plan_id = Column(Integer, primary_key=True, autoincrement=True)
    deal_ref = Column(String(50), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(255), default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    cif = Column(String(50), ForeignKey("perusahaan.cif"))

    events = relationship("RoadmapEvent", back_populates="plan", cascade="all, delete")

class RoadmapEvent(Base):
    __tablename__ = "roadmap_event"

    event_id = Column(Integer, primary_key=True, autoincrement=True)
    plan_id = Column(Integer, ForeignKey("roadmap_plan.plan_id"), nullable=False)
    jenis_kegiatan = Column(String(255))
    ao_input = Column(Integer, ForeignKey("users.id"))
    cif = Column(String(50), ForeignKey("perusahaan.cif"))
    keterangan_kegiatan = Column(String)
    tanggal = Column(DateTime)
    update_terakhir = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    plan = relationship("RoadmapPlan", back_populates="events")
    ao = relationship("User", foreign_keys=[ao_input])