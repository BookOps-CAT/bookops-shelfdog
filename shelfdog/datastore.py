# -*- coding: utf-8 -*-

"""
shelfdog's database schema
"""
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class File(Base):
    __tablename__ = "file"

    sid = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow())
    handle = Column(String, nullable=False)
    libraryId = Column(Integer, ForeignKey("library.sid"), nullable=False)


class Library(Base):
    __tablename__ = "library"

    sid = Column(Integer, primary_key=True)
    code = Column(String(3), unique=True)


class Bib(Base):
    __tablename__ = "bib"
    __table_arg__ = UniqueConstraint("sierraId", "libraryId")

    sid = Column(Integer, primary_key=True)
    libraryId = Column(Integer, ForeignKey("library.sid"), nullable=False)
    sierraId = Column(Integer, nullable=False)

    audn = Column(String(1))
    author = Column(String)
    bibType = Column(String(1))
    callNoResearch = Column(String)
    callNoSuggested = Column(String)
    callNoFormat = Column(String(5))
    callNoAudn = Column(String(1))
    callNoWl = Column(Boolean, nullable=False)
    callNoType = Column(String(5))
    callNoCutter = Column(Boolean, nullable=False)
    callNoDewey = Column(String)
    catDate = Column(Date)
    critWork = Column(Boolean, nullable=False)
    itemForm = Column(String(1))
    physicalDesc = Column(String)
    primaryLang = Column(String(3))
    subjects = Column(String)
    subjectPerson = Column(Boolean, nullable=False)
    title = Column(String(25), nullable=False)
    worldLang = Column(Boolean, nullable=False)
