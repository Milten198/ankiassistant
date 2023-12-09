from dropbox_manager import get_file_by_name
from open_ai_helper import extract_words_from_file

base64_image = get_file_by_name("IMG20231209094211")

words = extract_words_from_file(base64_image)

list_of_words = words.json()['choices'][0]['message']['content']

print(list_of_words)