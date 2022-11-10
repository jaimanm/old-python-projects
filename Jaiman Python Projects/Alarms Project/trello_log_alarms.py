from trello import TrelloClient

client = TrelloClient(
    api_key = '1db4391d5c6ec50d3491ebea1be700aa',
    token = '3287ce13a5dfb9252d9ac961ff1e73343ed1bc439b7c839202884ff3b027c1f3'
    )

all_boards = client.list_boards()
last_board = all_boards[-1]
print(last_board.name)

my_list = last_board.list_lists()

for card in my_list.list_cards():
    print(card.name)
