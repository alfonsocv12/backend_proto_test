player_list: list[dict] = [
    {
        'id': 'd20f83b1-29b0-4d24-81bf-7d06000395f1',
        'name': 'Sophi',
        'height': 1.70,
        'country_id': '1'
    },
    {
        'id': '9dd844d3-9059-4b0a-affe-20b12f29e3d0',
        'name': 'Alfonso',
        'height': 1.80,
        'country_id': '1'
    },
    {
        'id': '34f18fb4-f1ab-4838-bccf-ce8a20ff2864',
        'name': 'Boby',
        'height': 1.70,
        'country_id': '1'
    }
]

class PlayerOutgoing:
    
    def get_players(self):
        return player_list
