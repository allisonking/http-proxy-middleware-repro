# http-proxy-middleware potential bug reproduction

Reproducing the error described [here](https://github.com/chimurai/http-proxy-middleware/discussions/726) for the [http-proxy-middleware library](https://github.com/chimurai/http-proxy-middleware).

## Overview of problem

When upgrading from node 14 to node 16, proxying now times out for partial response streams (i.e. streaming audio).

## Backend setup

I made both a Flask server and a Falcon server. This error actually only happens in the Falcon server, but I left the Flask server in just in case it's helpful in debugging.

```
# go to the server directory
cd server

# make a virtual env
python3 -m venv venv

# activate the virtual env
source venv/bin/activate

# install dependencies
pip3 intall -r requirements.txt

# start the server at port 5000
python3 falconaudiostream.py
```

## Frontend setup

```
# install dependencies
npm install

# start the express server at 3000 with proxy (3000 -> 5000)
node index.js
```

## Reproducing

- Start up the backend
- Start up the frontend
- Navigate to localhost:5000/api/play to hear the audio without a problem
- Navigate to localhost:3000/api/play. The audio will hang, and will not actually play until you ctrl+c the server

Try the same steps with node 14 instead of node 16. There will be no issue.
