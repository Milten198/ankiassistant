from dropbox_manager import get_file_by_name
from open_ai_helper import extract_words_from_file, format_extracted_words, create_flashcard
from airtable_handler import add_flashcard_records, get_flashcards_to_create

# base64_image = get_file_by_name("IMG20231209094211")
#
# words = extract_words_from_file(base64_image)
#
# list_of_words = words.json()['choices'][0]['message']['content']
#
# formatted_words = format_extracted_words(list_of_words)
#
# flashcards = create_flashcard(formatted_words)
#
# add_flashcard_records(flashcards)

get_flashcards_to_create()