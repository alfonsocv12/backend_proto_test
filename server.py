import uvicorn
from fastapi import FastAPI
from src.incoming.players.http_handler import router as player_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(player_router, tags=['players'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == '__main__':
    uvicorn.run(
        "server:app", host="0.0.0.0", port=8000,
        reload=True
    )