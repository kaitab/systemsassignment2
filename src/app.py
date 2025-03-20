#this contains the flask code
from flask import Flask, request, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from src import model, app, db
import datetime

our_notes = model.Note

#TODO: add ability to delete notes
@app.route("/", methods=["GET", "POST"])
def main_page():
    """generates the main page"""
    notes = db.session.execute(db.select(our_notes).order_by(our_notes.title)).scalars()
    return render_template("mainpage.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    """adds a note and sends a success message"""
    title = request.form["title"]
    content = request.form["content"]
    if title and content:
        this_note = model.Note(title=title, content=content, time=datetime.datetime.now())
        db.session.add(this_note)
        db.session.commit()
        return render_template("addpage.html")
    else:
        return render_template("errorpage.html")

#TODO : add capability to search comments
@app.route("/find")
def search_results():
    """displays search results"""
    term = request.args["term"]
    return render_template("searchpage.html", results=our_notes.search_notes(term))

#TODO: display comments
#TODO: add ability to add comments
@app.route("/note/<note_name>")
def get_note(note_name):
    """displays a note given its name"""
    this_note = our_notes.query.filter_by(title=note_name)[0]
    body = this_note.body
    comments = this_note.comments
    return render_template("notepage.html", name=note_name, note_body=body, note_comments=comments)

@app.route("/del/<note_id>", methods = ["POST"])
def del_note(note_id):
    if request.method == "POST":
        try:
            this_note = db.get_or_404(model.Note, note_id)
            db.session.delete(this_note)
            db.session.commit()
            return redirect(url_for("/"))
        except IntegrityError:
            db.session.rollback()
            db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
