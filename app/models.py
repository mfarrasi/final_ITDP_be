from sqlalchemy import Column, String, Integer, Float, Boolean, Date, ForeignKey, Text, ARRAY, Enum
from app.db import Base
from sqlalchemy.orm import relationship

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

# # 6. Event Roadmap Table
# class EventRoadmap(Base):
#     __tablename__ = "event_roadmap"

#     event_roadmap_id = Column(Integer, primary_key=True, autoincrement=True)
#     jenis_kegiatan = Column(String(255))
#     ao_input = Column(Integer, ForeignKey("users.uid"))
#     cif = Column(String(50), ForeignKey("perusahaan.cif"))
#     deal_ref = Column(String(50), ForeignKey("fasilitas.deal_ref"))
#     keterangan_kegiatan = Column(Text)
#     tanggal = Column(Date)
#     update_terakhir = Column(TIMESTAMP)
#     status_diterima = Column(Boolean)

# # 7. History Table
# class History(Base):
#     __tablename__ = "history"

#     event_history_id = Column(Integer, primary_key=True, autoincrement=True)
#     deal_ref = Column(String(50), ForeignKey("fasilitas.deal_ref"))
#     jenis_kegiatan = Column(String(255))
#     ao_input = Column(Integer, ForeignKey("users.uid"))
#     keterangan_kegiatan = Column(Text)
#     tanggal = Column(Date)

# # 8. Deal Ownership Table (Many-to-Many)
# class UserDeals(Base):
#     __tablename__ = "user_deals"

#     uid = Column(Integer, ForeignKey("users.uid"), primary_key=True)
#     deal_ref = Column(String(50), ForeignKey("fasilitas.deal_ref"), primary_key=True)