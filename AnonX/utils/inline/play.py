import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from AnonX import app

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < anon < 3:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 3 <= anon < 4:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 4 <= anon < 5:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 6 <= anon < 7:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 7 <= anon < 8:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 9 <= anon < 10:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 11 <= anon < 12:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 12 <= anon < 13:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 13 < anon < 14:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 14 <= anon < 15:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|😇 "
    elif 15 <= anon < 16:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 16 <= anon < 17:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 17 <= anon < 18:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 18 <= anon < 19:
        bar = " ⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳| "
    elif 19 <= anon < 20:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 20 <= anon < 21:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 21 <= anon < 22:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 22 <= anon < 23:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 23 <= anon < 24:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 24 <= anon < 25:
        bar = " ⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳| "
    elif 25 <= anon < 26:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 26 <= anon < 27:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 27 <= anon < 28:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 28 <= anon < 29:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 29 <= anon < 30:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 30 <= anon < 31:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 31 <= anon < 32:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 32 <= anon < 33:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 33 <= anon < 34:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 34 <= anon < 35:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 35 <= anon < 36:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 36 <= anon < 37:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 37 <= anon < 38:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 38 <= anon < 39:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 39 <= anon < 40:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 40 <= anon < 41:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 41 <= anon < 42:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 42 <= anon < 43:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 43 <= anon < 44:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 44 < anon < 45:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 45 <= anon < 46:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 46 <= anon < 47:
        bar = " 🥀𝚃𝙷𝙴_𝚅𝙸𝙿_𝙱𝙾𝚈🥀 "
    elif 47 <= anon < 48:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 48 <= anon < 49:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 49 <= anon < 50:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 50 <= anon < 51:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 51 <= anon < 52:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 52 <= anon < 53:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 53 <= anon < 54:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 54 <= anon < 55:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 55 <= anon < 56:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 56 <= anon < 57:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 57 <= anon < 58:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 58 <= anon < 59:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 59 <= anon < 60:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 60 <= anon < 61:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 61 <= anon < 62:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 62 <= anon < 63:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 63 <= anon < 64:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 64 <= anon < 65:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 65 <= anon < 66:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 66 <= anon < 67:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 67 <= anon < 68:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 68 <= anon < 69:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 69 <= anon < 70:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 70 <= anon < 71:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 71 <= anon < 72:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 72 <= anon < 73:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 73 <= anon < 74:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 74 <= anon < 75:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 75 <= anon < 76:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 76 < anon < 77:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 77 <= anon < 78:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 78 <= anon < 79:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 79 <= anon < 80:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 80 <= anon < 81:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 81 <= anon < 82:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 82 <= anon < 83:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 83 <= anon < 84:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 84 <= anon < 85:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 85 <= anon < 86:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 86 <= anon < 87:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 87 <= anon < 88:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 88 <= anon < 89:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 89 <= anon < 90:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 90 <= anon < 91:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 91 <= anon < 92:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 92 <= anon < 93:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 93 <= anon < 94:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 94 <= anon < 95:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 95 <= anon < 96:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 96 <= anon < 97:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 97 <= anon < 98:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 98 <= anon < 99:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    else:
        bar = " 🍷ѕσ ¢ιтє ѕσηg🍷 "
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < anon < 3:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 3 <= anon < 4:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 4 <= anon < 5:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 6 <= anon < 7:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 7 <= anon < 8:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 9 <= anon < 10:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 11 <= anon < 12:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 12 <= anon < 13:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 13 < anon < 14:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 14 <= anon < 15:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 15 <= anon < 16:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 16 <= anon < 17:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 17 <= anon < 18:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 18 <= anon < 19:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 19 <= anon < 20:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 20 <= anon < 21:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 21 <= anon < 22:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 22 <= anon < 23:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 23 <= anon < 24:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 24 <= anon < 25:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 25 <= anon < 26:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 26 <= anon < 27:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 27 <= anon < 28:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 28 <= anon < 29:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 29 <= anon < 30:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 30 <= anon < 31:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 31 <= anon < 32:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 32 <= anon < 33:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 33 <= anon < 34:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 34 <= anon < 35:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 35 <= anon < 36:
        bar = " ⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳| "
    elif 36 <= anon < 37:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 37 <= anon < 38:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 38 <= anon < 39:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 39 <= anon < 40:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 40 <= anon < 41:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 41 <= anon < 42:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 42 <= anon < 43:
        bar = " ⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳| "
    elif 43 <= anon < 44:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 44 < anon < 45:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 45 <= anon < 46:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 46 <= anon < 47:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 47 <= anon < 48:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 48 <= anon < 49:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 49 <= anon < 50:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 50 <= anon < 51:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 51 <= anon < 52:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 52 <= anon < 53:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 53 <= anon < 54:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 54 <= anon < 55:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 55 <= anon < 56:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 56 <= anon < 57:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 57 <= anon < 58:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 58 <= anon < 59:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 59 <= anon < 60:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 60 <= anon < 61:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 61 <= anon < 62:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 62 <= anon < 63:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 63 <= anon < 64:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 64 <= anon < 65:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 65 <= anon < 66:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 66 <= anon < 67:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 67 <= anon < 68:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 68 <= anon < 69:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 69 <= anon < 70:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 70 <= anon < 71:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 71 <= anon < 72:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 72 <= anon < 73:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 73 <= anon < 74:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 74 <= anon < 75:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 75 <= anon < 76:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 76 < anon < 77:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 77 <= anon < 78:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 78 <= anon < 79:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 79 <= anon < 80:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 80 <= anon < 81:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 81 <= anon < 82:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 82 <= anon < 83:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 83 <= anon < 84:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 84 <= anon < 85:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 85 <= anon < 86:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 86 <= anon < 87:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 87 <= anon < 88:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 88 <= anon < 89:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 89 <= anon < 90:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 90 <= anon < 91:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 91 <= anon < 92:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 92 <= anon < 93:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 93 <= anon < 94:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    elif 94 <= anon < 95:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥 "
    elif 95 <= anon < 96:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 96 <= anon < 97:
        bar = " 🥀⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🥀 "
    elif 97 <= anon < 98:
        bar = " 🔥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|🔥 "
    elif 98 <= anon < 99:
        bar = " 💥⏤͟͟͞͞✘ 𓆩𝙆 𝙍 𝙄 𝙎 𝙃 𝙉 𝘼𓆪|🇮🇳|💥  "
    else:
        bar = " 🍷ℓσνєℓу ѕσηg🍷 "

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [  
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons
