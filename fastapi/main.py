from fastapi import FastAPI
from enum import Enum
app = FastAPI()


class TopicNames(str,Enum):
    limit = "fun"
    derivatives = "easy to deal with"
    integral = "fuck sake"


@app.get("/")
def root():
    return {"Main":"Calculus Topics"}
@app.get("/math/{topic}")
def read_item(topic:str):
    if topic is TopicNames.limit:
        return {"Topic":topic,"message":TopicNames[topic].value}

    if topic is TopicNames.derivatives:
        return {"Topic":topic,"message":TopicNames[topic].value}

    return {"Topic":topic ,"message":TopicNames[topic].value}
