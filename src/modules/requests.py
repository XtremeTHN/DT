import json

class Requests:
    FILE='FILE'
    DATA='DATA'

    END="END"

    @staticmethod
    def format_request(req: str, data_length: int):
        return json.dumps({
            "request": req,
            "bytes-length": data_length
        }).encode()
