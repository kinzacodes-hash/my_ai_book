from sqlalchemy import Column, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import UUID
import uuid

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    progress = Column(JSON, default={}) # map of module IDs to completion status
    background_profile = Column(String) # e.g., "AI engineer", "student"

    # Define a relationship to track which books a user is associated with if needed
    # For now, progress stores module IDs directly.

class Book(Base):
    __tablename__ = "books"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True)
    modules = Column(JSON, default=[]) # array of module objects, each with id, title, chapters

    modules_rel = relationship("Module", back_populates="book_rel")

class Module(Base):
    __tablename__ = "modules"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True)
    book_id = Column(PG_UUID(as_uuid=True), ForeignKey("books.id"))

    book_rel = relationship("Book", back_populates="modules_rel")
    chapters_rel = relationship("Chapter", back_populates="module_rel")

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True)
    content = Column(String) # using String for now, could be Text for larger content
    module_id = Column(PG_UUID(as_uuid=True), ForeignKey("modules.id"))

    module_rel = relationship("Module", back_populates="chapters_rel")
