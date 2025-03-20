#this is the module that will underly the notes API, etc.
from datetime import datetime

class Comment:
    def __init__(self, content:str):
        """initializes a comment with content and a date"""
        self.content = content
        self.time = str(datetime.now())

    def __str__(self):
        """returns a formatted string with the comments content and date"""
        return f"{self.content} at {self.time}"

class Note:
    def __init__(self, title : str, content : str):
        """initializes a note with a title, content, date, and a list to contain any comments"""
        self.title = title
        self.content = content
        self.comments = []
        self.time = datetime.now()

    def __str__(self):
        """returns a formatted string with the note's title and content"""
        return f"{self.title}: {self.content}"

    def get_title(self):
        """returns the note's title as a string"""
        return self.title

    def get_content(self):
        """returns the note's content as a string"""
        return self.content

    def get_comments(self):
        """returns the note's comments"""
        return self.comments

    def add_comment(self, content):
        """adds a new comment to a note"""
        self.comments.append(Comment(content))

class NotesApp:
    def __init__(self):
        """initializes the notes app, which is just a list that will contain notes"""
        self.list = []

    def list_all(self):
        """returns a list of all notes by title"""
        return self.list

    def add_note(self, title : str, content : str):
        """creates a new note with title and content, adds it to the list, and sends a message if its successfully added"""
        new_note = Note(title, content)
        self.list.append(new_note)
        if new_note in self.list:
            print("Note successfully added.")
            return "Note successfully added."
        else:
            print("Sorry, this note wasn't added.")
            return "Sorry, this note wasn't added."

    def return_note(self, title : str):
        """returns the content of a note given its title"""
        for note in self.list:
            if note.get_title() == title:
                print(note.get_content())
                return note.get_content()

    def search_notes(self, term : str):
        """returns a list of both the title and content of notes matching a search term"""
        #now somewhat problematic bc of the dates; like if you search for february you will get all comments and notes from february
        #maybe that's how you would want it to work idk
        found_list = []
        for note in self.list:
            title_list = note.get_title().split(" ")
            content_list = note.get_content().split(" ")
            comments_list = note.get_comments().split(" ")
            if term in title_list or term in content_list:
                found_list.append(str(note))
        return found_list

    def delete_note(self, title : str):
        """removes a note from the notesapp by title"""
        for note in self.list:
            if note.get_title() == title:
                self.list.remove(note)
                print("Note removed")

    def show_comments(self, title: str):
        "given a notes name, shows its comments"
        for note in self.list:
            if note.get_title() == title:
                return note.get_comments()
