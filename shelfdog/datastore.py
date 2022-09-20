# -*- coding: utf-8 -*-

"""
shelfdog's database schema
"""
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
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

    bibAudn = Column(String(1))
    bibAuthor = Column(String)
    bibIsBio = Column(Boolean, nullable=False)
    bibCatDate = Column(Date)
    bibIsCritWork = Column(Boolean, nullable=False)
    bibItemForm = Column(String(1))
    bibLiteraryForm = Column(String(1))
    bibPhysicalDesc = Column(String)
    bibLang = Column(String(3))
    bibSubjects = Column(String)
    bibSubjectPerson = Column(String)
    bibTitle = Column(String)
    bibType = Column(String(1))
    bibIsWorldLang = Column(Boolean, nullable=False)

    callAssigned = Column(String)
    callPredicted = Column(String)
    callResearch = Column(String)
    callFormat = Column(String(5))
    callAudn = Column(String(1))
    callIsWorldLang = Column(Boolean, nullable=False)
    callType = Column(String(5))
    callHasCutter = Column(Boolean, nullable=False)
    callDewey = Column(String)

    # bib may not have any orders attached so all columns below
    # should not be enforced
    ordAudn = Column(String(1))
    ordFormat = Column(String(1))
    ordLang = Column(String(3))
    ordIsWorldLang = Column(Boolean)
    ordLocations = Column(String)
    ordShelveCodes = Column(String)
    ordVenNotes = Column(String)
