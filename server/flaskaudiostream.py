"""Simple flask server to stream audio. This seems to work fine."""

from http import HTTPStatus

from flask import Flask, Response

app = Flask(__name__)


@app.route("/api/play")
def stream():
    def generate():
        with open("data/convo.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)

    headers = {
        "Content-Type": "audio/mpeg",
        "Content-Range": "bytes 0-21313622/21313623",
        "Accept-Ranges": "bytes",
        "Content-Length": 21313623,
    }

    response = Response(generate(), HTTPStatus.PARTIAL_CONTENT)
    for k, v in headers.items():
        response.headers[k] = v
    return response


if __name__ == "__main__":
    app.run(debug=True)
