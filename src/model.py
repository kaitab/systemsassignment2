from typing import List
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from src import db


class Base(DeclarativeBase):
    pass

class Note(Base):
    """initializes a note as a database table"""
    __tablename__ = "note"
    id: Mapped[int] = mapped_column(primary_key=True)
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="parent", cascade = "all, delete-orphan")
    title = db.Column(db.String(100), unique = False, nullable = False)
    content = db.Column(db.String(280), unique = False, nullable = False)
    time = db.Column(db.String(40), unique=False, nullable=False)


    def __repr__(self):
        """returns a formatted string with the content and title of the note"""
        return f"{self.title}: {self.content}"

class Comment(Base):
    """initializes a comment table"""
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id = mapped_column(sqlalchemy.ForeignKey("note.id"), nullable = False)
    parent: Mapped["Note"] = relationship("Note", back_populates="comments")
    content = db.Column(db.String(280), unique = False, nullable = False)
    time = db.Column(db.String(40), unique = False, nullable = False)

    def __repr__(self):
        """returns a formatted string with the content and time of the comment"""
        return f"{self.content} at {self.time}"
