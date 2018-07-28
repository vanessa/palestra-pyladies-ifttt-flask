from flask import Flask, request
from helpers import get_card_id_from_title, add_and_mark_checklist, \
                    get_board_id_from_title

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    card_id = get_card_id_from_title('Example card')
    add_and_mark_checklist(card_id, 'Dar a primeira palestra de programação da vida')
    return "Done!"

@app.route('/ifttt-working', methods=['GET'])
def ifttt_working():
    card_id = get_card_id_from_title('Example card')
    add_and_mark_checklist(card_id, 'Mostrar o IFTTT funcionando', checked=True)
    return "Done!"

@app.route('/board-id/<username>/<title>', methods=['GET'])
def get_board_id(username, title):
    board_id = get_board_id_from_title(username, title)
    return board_id