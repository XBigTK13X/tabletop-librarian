class CardDeck:
    def __init__(self, deck_info):
        self.deck_info = deck_info
        self.name = deck_info['name']
        self.description = deck_info['description']
        self.face_location = deck_info['face_location']
        self.back_location = deck_info['back_location']
        self.columns = deck_info['columns']
        self.rows = deck_info['rows']
        self.unique_back = deck_info['unique_back']