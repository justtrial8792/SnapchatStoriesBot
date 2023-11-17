import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "25222859"))
    API_HASH = os.environ.get("API_HASH", "b76d4fb1f5afc4a797b85c5e34b0f1ca")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6458225530:AAFhj-q7M-EdXi9UcB2r7tcq6vCTVSrE2cQ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Url_to_stream_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
