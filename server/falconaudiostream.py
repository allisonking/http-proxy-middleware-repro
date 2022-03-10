"""Simple Falcon server to stream audio. This does not work fine."""
from wsgiref.simple_server import make_server

import falcon


class PlaybackResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        def generate():
            with open("data/whistling.mp3", "rb") as fwav:
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
        resp.stream = generate()
        resp.status = falcon.HTTP_PARTIAL_CONTENT
        resp.set_headers(headers)
        return resp


app = falcon.App()
app.add_route("/api/play", PlaybackResource())

if __name__ == "__main__":
    with make_server("", 5000, app) as httpd:
        print("Serving on port 5000...")

        # Serve until process is killed
        httpd.serve_forever()
