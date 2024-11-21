import anthropic
from typing import Iterable

from data_model import ChatMessage, State
import mesop as me

def call_claude_sonnet(input: str, history: list[ChatMessage]) -> Iterable[str]:
    state = me.state(State)
    client = anthropic.Anthropic(
        api_key=state.claude_api_key,
        base_url="https://api.x.ai"
    )
    
    messages = [
        {
            "role": "assistant" if message.role == "model" else message.role,
            "content": message.content,
        }
        for message in history
    ] + [{"role": "user", "content": input}]

    with client.messages.stream(
        max_tokens=1024,
        system="You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy.",
        messages=messages,
        model="grok-beta",
    ) as stream:
        for text in stream.text_stream:
            yield text
