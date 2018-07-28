from decouple import config

import requests

default_params = {
    'key': config('TRELLO_KEY'),
    'token': config('TRELLO_TOKEN')
}
api_root = 'https://api.trello.com/1'
default_board_id = config('DEFAULT_BOARD_ID')

def get_card_id_from_title(title):
    default_params['fields'] = 'name,id'
    url = f'{api_root}/boards/{default_board_id}/cards'
    response = requests.get(url, params=default_params).json()
    card_id = [
        card['id'] for card in response
        if card['name'] == title
    ][0]
    return card_id

def add_and_mark_checklist(card_id, text, checked=False):
    # Set the checklist variables
    default_params['name'] = 'Things to do'
    default_params['pos'] = 'top'
    default_params['idCard'] = card_id
    url = f'{api_root}/checklists'

    # Send them
    response_checklist = requests.post(url, params=default_params).json()
    
    # Get the checklist
    checklist_id = response_checklist.get('id')

    # Set the checklist item variables
    default_params['name'] = text
    default_params['checked'] = 'true' if checked else 'false'
    
    # And finally send them
    return requests.post(f'{url}/{checklist_id}/checkItems', params=default_params)

def get_board_id_from_title(username, title):
    """ Little helper to get our board ID easily """
    url = f'{api_root}/members/{username}/boards'
    response = requests.get(url, params=default_params).json()
    board_id = [
        board['id'] for board in response
        if board['name'] == title
    ][0]
    return board_id
