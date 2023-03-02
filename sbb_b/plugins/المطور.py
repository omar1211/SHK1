import random
import re
import time
from platform import python_version

from telethon import version, Button
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from sbb_b import StartTime, sbb_b, JMVERSION

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

@sbb_b.ar_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    CAT_IMG = " https://telegra.ph/file/351833e9422b1b7e8ac55.jpg "
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"هـذا هـو مـطـور سـورس القرش\n"
        cat_caption += f"✛━━━[𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊˼](https://t.me/L_H_V)━━━✛\n\n"
        cat_caption += f"⎊ قـناة الـسـورس :  [『 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊』➯](https://t.me/L_H_V)\n\n"
        cat_caption += f"⎊ جـروب الـسـورس  : [『 𝐒𝐇𝐀𝐑𝐊 𝐆𝐑𝐎𝐔𝐏𖥢』➯](https://t.me/QW_PN)\n\n"
        cat_caption += f"⎊ مـبرمج الـسورس : [『 ★⃝➼3𝕄𝕆ℝ𝕐🜪 . 🕷 ˼ 』➯](https://t.me/T_3_A)\n\n"
        cat_caption += f"✛━━━[𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊](https://t.me/L_H_V)━━━✛\n\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
#semo
