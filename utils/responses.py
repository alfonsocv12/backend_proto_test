import json
from fastapi import Response
from typing import Any
from google.protobuf.json_format import MessageToDict


class BinaryResp(Response):
    media_type = "plain/text"

    content = None

    def render(self, content: str) -> bytes:
        return content


def response_format(format: str, object: Any):
    format_options = {
        'json': lambda: json.dumps(MessageToDict(object)).encode('utf-8'),
        'buffer': lambda: object.SerializeToString()
    }
    resp = format_options.get(
        format, format_options['buffer']
    )()
    return BinaryResp(resp)