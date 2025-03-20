import streamlit as st
import notesapp

#saving the notes app to the streamlit session
#NTS: this puts our app in a dictionary function and it should be accessed that way
if 'our_notes' not in st.session_state:
    st.session_state['our_notes'] = notesapp.NotesApp()

#setting up some formatting and text
st.set_page_config(layout="wide")
st.title("Welcome to NotesApp!")

#implementing search function
st.markdown("Search all notes:")
with st.form("search"):
    term = st.text_input("term")
    submit = st.form_submit_button("search")

if submit:
    st.markdown(f'{st.session_state['our_notes'].search_notes(term)}')

#implementing adding a new note
st.markdown("Add a new note:")
with st.form("add"):
    title = st.text_input("title")
    body = st.text_input("body")
    submit2 = st.form_submit_button("add")

if submit2:
    st.markdown(f'{st.session_state['our_notes'].add_note(title, body)}')

#implementing list all AND show note function
st.markdown("List of all notes(click to see content):")
for note in st.session_state['our_notes'].list_all():
    note_title = note.get_title()
    if st.button(note_title):
        st.write(st.session_state['our_notes'].return_note(note_title))



