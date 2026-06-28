from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Repository(BaseModel):
    name: str


class Pusher(BaseModel):
    name: str


class HeadCommit(BaseModel):
    message: str


class GithubWebhook(BaseModel):
    repository: Repository
    pusher: Pusher
    head_commit: HeadCommit


@app.post("/webhook")
async def github_webhook(payload: GithubWebhook):

    print("=" * 50)
    print("Repository :", payload.repository.name)
    print("Author     :", payload.pusher.name)
    print("Commit     :", payload.head_commit.message)

    return {"status": "success",
            "slklsmlc" :"some_value"}