from src.incoming.players import http_responses_pb2
from utils.responses import BinaryResp, response_format
from fastapi import APIRouter, Header
from src.service.player import PlayerService


router = APIRouter(prefix="/players")
service = PlayerService()


@router.get("", response_class=BinaryResp)
def get_players(format: str = Header(default='')):
    players = http_responses_pb2.GetPlayers(
        players=service.get_player()
    )
    return response_format(format, players)