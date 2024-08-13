import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def safe_getenv_int(var_name, default):
    value = getenv(var_name)
    if value is None:
        return default
    return int(value)

def safe_getenv_bool(var_name, default):
    value = getenv(var_name)
    if value is None:
        return default
    return value.lower() in ["true", "1", "yes"]

# Get this value from my.telegram.org/apps
API_ID = safe_getenv_int("API_ID", 8186557)
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = safe_getenv_int("DURATION_LIMIT", 2001)

# Chat id of a group for logging bot's activities
LOGGER_ID = safe_getenv_int("LOGGER_ID", -1002053793790)

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = safe_getenv_int("OWNER_ID", 1895219306)

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Hjwad/fixx")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN")  # Fill this variable if your upstream repository is private
CH_US = getenv("CH_US", "mmmsc")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/mmmsc")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/mmmsc")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = safe_getenv_bool("AUTO_LEAVING_ASSISTANT", False)

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = safe_getenv_int("PLAYLIST_FETCH_LIMIT", 25)

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = safe_getenv_int("TG_AUDIO_FILESIZE_LIMIT", 104857600)
TG_VIDEO_FILESIZE_LIMIT = safe_getenv_int("TG_VIDEO_FILESIZE_LIMIT", 1073741824)
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/1bccb452031ac902596bf.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/1bccb452031ac902596bf.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
STATS_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/1bccb452031ac902596bf.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
