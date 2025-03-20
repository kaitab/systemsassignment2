#this contains the fast api code

#import statements
from fastapi import FastAPI
import notesapp
from pydantic import BaseModel

#initialize an instance of the fast api
app = FastAPI()

#initialize an instance of our notesapp
our_notes = notesapp.NotesApp()

@app.get("/")
async def root():
    """returns a string with a mini tutorial on how to use the notes app API"""
    return{"tutorial": "to use the notes app, navigate to one of the URLs below:",
                       "/list" : "returns a list of all notes by title",
                       "/find?term={term}" : "returns list of notes that contain a search term",
                       "/note/{note_name}" : "returns the content of a note",
                       "/add" : "adds a new note from json format/dictionary or a file"}

@app.get("/list")
async def get_list():
    """returns a list of the titles of all notes"""
    note_objs = our_notes.list_all() #NTS: remember this returns a list of note *objects*
    return {"all notes" : [note.get_title() for note in note_objs]}

#make a route for search
@app.get("/find")
async def search_notes(term : str):
    """returns a list of titles of notes that match a search term"""
    return {"we found" : our_notes.search_notes(term)}

@app.get("/note/{note_name}")
async def get_note(note_name : str):
    """returns the content of a note given its name"""
    return {note_name : our_notes.return_note(note_name)}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

class NewNote(BaseModel):
    name : str
    content : str

@app.post("/add")
async def add_note(note:NewNote):
    """tries to add a new note and sends a message indicating if successful"""
    return our_notes.add_note(note.name, note.content)
