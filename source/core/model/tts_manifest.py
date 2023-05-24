from core.model.game_piece import card_deck
from core.model import tts_asset

import json
import re
import os
import shutil

REMOTE_REGEX = r'http[s]*:\/\/[^(\"|\')]{2,200}'

class TTSManifest:
    def __init__(self, mod, manifest):
        self.manifest_text = manifest
        self.manifest = json.loads(manifest)
        self.mod = mod

    def parse_locations(self):
        return [location for location in re.findall(REMOTE_REGEX, self.manifest_text) if not 'api.tabletopsimulator.com' in location]

    def write_assets(self, assets):
        for k,v in assets.items():
            asset = tts_asset.TTSAsset(self.mod, v['path'], v['local_id'], k, v['extension'])
            if not os.path.isfile(asset.local_path):
                shutil.move(asset.cache_path, asset.local_path)

    def parse_full(self):
        self.decks = []
        for state in self.manifest['ObjectStates']:
            if state['Name'] == 'DeckCustom':
                deck_info = state['CustomDeck'][state['CustomDeck'].keys()[0]]
                payload = {
                    'name': state['Nickname'],
                    'description': state['Description'],
                    'front_location': deck_info['FaceURL'],
                    'back_location': deck_info['BackURL'],
                    'columns': deck_info['NumWidth'],
                    'rows': deck_info['NumHeight'],
                    'unique_back': deck_info['UniqueBack']
                }
                self.decks.append(card_deck.CardDeck(payload))
        return {
            'decks': self.decks
        }