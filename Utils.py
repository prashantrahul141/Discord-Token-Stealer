import requests
from logger import logger
import json
from constants import TOKENS_FILE_NAME, DISCORD_TOKEN_CHECK_URL


def verifyToken(token: str) -> bool:
    logger.info(f"verifying token : {token}")
    response = requests.get(DISCORD_TOKEN_CHECK_URL, headers={"Authorization": token})
    return response.status_code == 200


def saveToken(newToken: str) -> bool:
    logger.info(f"saving token : {newToken}")
    json_data = {"TOKENS": [newToken]}
    try:
        logger.info("trying to load old file.")
        with open(TOKENS_FILE_NAME, "r") as file:
            json_data = json.loads(file.read())
            json_data["TOKENS"].append(newToken)

        logger.info("saving new token")
        with open(TOKENS_FILE_NAME, "w") as file:
            json.dump(json_data, file)

    except:
        logger.error("failed to read file creating a new file with new token")
        with open(TOKENS_FILE_NAME, "w") as file:
            json.dump(json_data, file)


def readTokens(fileName: str = "tokens.pickle"):
    logger.info("reading tokens file")
    try:
        with open(TOKENS_FILE_NAME, "r") as file:
            jsonObj = json.loads(file.read())
            tokens = jsonObj["TOKENS"]
            print(tokens)

    except Exception as e:
        logger.error(f"failed to read file : {file}\nError :{e}")
