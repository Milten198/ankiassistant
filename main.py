from airtable_handler import add_flashcard_records, list_files_in_table, get_flashcards_to_create
from dropbox_manager import get_file_by_name, list_files_in_folder
from open_ai_helper import extract_words_from_file, format_extracted_words, create_flashcard

files_in_dropbox = list_files_in_folder()
files_in_airtable = list_files_in_table()


def get_list_of_db_unprocessed_files(dropbox_files, airtable_files):
    return [file for file in dropbox_files if file not in airtable_files]


def create_flashcard_records(files_with_words):
    for file in files_with_words:
        base64_image = get_file_by_name(file)
        words = extract_words_from_file(base64_image)
        list_of_words = words.json()['choices'][0]['message']['content']
        formatted_words = format_extracted_words(list_of_words)
        flashcards = create_flashcard(formatted_words)
        add_flashcard_records(flashcards, file)


files_to_process = get_list_of_db_unprocessed_files(files_in_dropbox, files_in_airtable)

create_flashcard_records(files_to_process)


# get_flashcards_to_create()
