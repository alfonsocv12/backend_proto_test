import json
import src.domain.player_pb2 as player_pb2
from src.outgoing.player import PlayerOutgoing
from google.protobuf import json_format

class PlayerService:
    player_outgoing = PlayerOutgoing()
    
    def get_player(self) -> list[player_pb2.PlayerEntity]:
        players_raw = self.player_outgoing.get_players()
        
        players = []
        for player in players_raw:
            player_entity = player_pb2.PlayerEntity()
            json_format.Parse(json.dumps(player), player_entity)
            players.append(player_entity)
            
        return players