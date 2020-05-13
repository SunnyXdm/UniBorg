from collections import defaultdict, deque
import re

import regex
from telethon import events, utils
from telethon.tl import types, functions

@borg.on(events.NewMessage(pattern=r"#SOL_irl", incoming=True))
async def _(event):
	if event.reply_to_msg_id:
		message_id = event.reply_to_msg_id
		await borg.send_message(
                    event.chat_id,
                    '@shinigaminokaicho @Kirito_Kiri @spearwolf @piyushsharmaxyz',
                    reply_to=message_id,
                )
		await borg.send_message(
                    event.chat_id,
                    '[JMJ](tg://user?id=1284964960)',
                    reply_to=message_id,
                )
		await borg.send_message(
                    event.chat_id,
                    '@artificialHuman @Wtfstalker @Kochiro @medevilofmelodies ',
                    reply_to=message_id,
                )
		await borg.send_message(
                    event.chat_id,
                    '@LordPeng @spookyenvy @drakxtor',
                    reply_to=message_id,
                )