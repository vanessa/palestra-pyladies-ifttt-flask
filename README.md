# Flask + IFTTT
Exemplo dado na palestra do PyLadies Recife (28/07/2018) sobre [automatização de tarefas com Python e IFTTT](http://bit.ly/auto-py), utilizando Flask.

## Rodando
1. Crie um ambiente virtual e o ative
1. Instale as dependências com `pip install -r requirements.txt`
1. Crie um arquivo `.env` com as seguintes variáveis obrigatórias:
    ```
    TRELLO_KEY='sua_key_aqui'
    TRELLO_TOKEN='seu_token_aqui'
    DEFAULT_BOARD_ID='board_id_aqui'
    ```
    - `TRELLO_KEY`: Sua developer API key do Trello, [pegue neste link](https://trello.com/app-key)
    - `TRELLO_TOKEN`: Sua API token do Trello, você pode pegá-la no mesmo link acima, clicando em *Token*
    - `DEFAULT_BOARD_ID`: O id do seu quadro do Trello, você pode usar o helper `get_board_id_from_title()` para descobri-lo facilmente
1. Para utilizar o Flask localmente, exporte as variáveis de ambiente abaixo:
    ```bash
    $ EXPORT FLASK_ENV=development
    $ EXPORT FLASK_DEBUG=1
    $ EXPORT FLASK_APP=app.py
    ```
1. Rode o servidor do Flask com `flask run`

## Utilizando com IFTTT
1. Instale e rode o [ngrok](https://ngrok.com) (lembre-se de apontar para a porta do seu servidor do Flask, que geralmente é 5000)
1. Crie um novo applet com o IFTTT, onde:
    1. Seu *THIS* será o gatilho escolhido, pode ser o **Button widget > Press button**
    1. Seu *THAT* será um **Webhook Request > Make a web request** onde você só precisará preencher o campo URL
1. Salve o applet e tente rodá-lo!