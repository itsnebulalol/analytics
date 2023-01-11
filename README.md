# Analytics

Extremely simple anonymous analytics system written in Python.

# How to use

## Docker (recommended)

1. Run `cp config.example.json config.json` to create a config file
2. Modify `config.json`
    1. You'll need to generate a string which will be used as the secret token (for registering sites)
    2. You may change the port here
3. Run `docker compose up -d --build` in the cloned directory
4. Now running on port 7500 (or whatever it's modified to in `docker-compose.yml`)

## Standalone

1. Run `pip install -r requirements.txt` in the cloned directory
2. Run `cp config.example.json config.json` to create a config file
3. Modify `config.json`
    1. You'll need to generate a string which will be used as the secret token (for registering sites)
    2. You may change the port here
4. Then, run `python ./app.py` to run the server
5. Now running on port 7500 (or whatever it's modified to in config.yml)

# Sending requests

```bash
# Grab your secret token and replace AUTH_TOKEN with it
# Change port if needed
# Change the app name
curl -X POST -H "Authorization: Bearer AUTH_TOKEN" http://localhost:7500/register_app --data '{"app_name": "APP_NAME_HERE"}'

# Now, you can send a hit
# Secret token is not needed, this is meant to be public
curl -X POST http://localhost:7500/hit --data '{"app_name": "APP_NAME_HERE"}'
```
