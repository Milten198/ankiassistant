import genanki

from airtable_handler import update_flashcard_record_status

my_model = genanki.Model(
    1607392319,
    "Styled Model",
    fields=[
        {"name": "Front"},
        {"name": "Back"}
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Front}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Back}}",
        },
    ],
    css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
    """
)

spanish_deck = genanki.Deck(
    2059400110,
    "Anki Assistant"
)


def add_flashcards_to_deck(flashcards_to_add):
    for flashcard in flashcards_to_add:
        fields = flashcard.get('fields')
        record_id = fields['record_id']
        spanish_word = fields['spanish_word']
        example = fields['example']

        print(f"Adding flashcard {spanish_word}")
        note = genanki.Note(
            model=my_model,
            fields=[example, spanish_word]
        )
        spanish_deck.add_note(note)
        update_flashcard_record_status(record_id, True)

    genanki.Package(spanish_deck).write_to_file("spanish_vocab.apkg")
