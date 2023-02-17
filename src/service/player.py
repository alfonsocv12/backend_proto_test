import json
from  src.domain.player_pb2 import PlayerEntity
from src.outgoing.player import PlayerOutgoing
from google.protobuf import json_format
from google.protobuf.timestamp_pb2 import Timestamp

class PlayerService:
    player_outgoing = PlayerOutgoing()
    
    def get_player(self) -> list[PlayerEntity]:
        players_raw = self.player_outgoing.get_players()
        
        players = []
        for player in players_raw:
            player_entity = PlayerEntity()
            player_entity.id = player['id']
            player_entity.name = player['name']
            player_entity.height = player['height']
            player_entity.country_id = player['country_id']
            player_entity.created_at.FromDatetime(player['created_at'])
            players.append(player_entity)
            
        return players