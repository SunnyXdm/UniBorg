from collections import defaultdict, deque
import re

import regex
from telethon import events, utils
from telethon.tl import types, functions

@borg.on(events.NewMessage(pattern=r"#all", incoming=True))
async def _(event):
	if event.reply_to_msg_id:
		message_id = event.reply_to_msg_id
		await borg.send_message(
                    event.chat_id,
                    '@Akbarian_Ali94 @medevilofmelodies @Captain78 @DetApieZ',
                    reply_to=message_id,
                )
		await borg.send_message(
                    event.chat_id,
                    '[Alhan](tg://user?id=816826347) [Qb](tg://user?id=764492957) [Grany](tg://user?id=518879706)',
                    reply_to=message_id,
                )
		await borg.send_message(
                    event.chat_id,
                    '@Coccrhard @poison_ivy2  @Fereshhtee @A3peek',
                    reply_to=message_id,
                )
		await borg.send_message(
                    event.chat_id,
                    '@Nebsel @MedevilofMarvel @Mariameslami @Naeema_1998',
                    reply_to=message_id,
                )
		await borg.send_message(
                    event.chat_id,
                    '@Ruthlesskween @Heyiambita',
                    reply_to=message_id,
                )