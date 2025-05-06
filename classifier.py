from pydantic import BaseModel,Field
from typing import Literal

class MessageClassifier(BaseModel):
    message_type:Literal["emotional","logical"] = Field(
        ...,
        description="Classify if the message requires and emotional (therapist) or logical response"
    )
    