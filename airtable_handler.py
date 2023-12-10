from pyairtable import Api
import os

base_id = 'appfU86I12dbN941Y'
table_name = 'Flashcards'

AIRTABLE_KEY = os.getenv('AIRTABLE_KEY', 'API key not found')

airtable = Api(AIRTABLE_KEY)
tab = airtable.table(base_id, table_name)


def add_flashcard_records(flashcards):
    for flashcard in flashcards:
        print(f"Adding record for flashcard:\n {flashcard}")
        record = tab.create(
            {"file_name": "test_file_2", "spanish_word": f"{flashcard['spanish']}",
             "polish_word": f"{flashcard['polish']}",
             "example": f"{flashcard['example']}",
             "flashcard_created": False})
        print(f"Added record:\n {record}")


def get_flashcards_to_create():
    formula = "flashcard_created = FALSE()"
    to_create = tab.all(formula=formula)
    print(to_create)
    return to_create


def update_flashcard_record_status(record_id, is_created):
    tab.update(record_id, {"flashcard_created": is_created})
