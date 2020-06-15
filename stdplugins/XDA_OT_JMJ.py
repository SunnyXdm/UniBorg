from collections import defaultdict, deque
import re

import regex
from telethon import events, utils
from telethon.tl import types, functions

@borg.on(events.NewMessage(pattern=r"#SOL_irl", incoming=True, chats=-1001055527387))
async def _(event):
	if event.reply_to_msg_id:
		message_id = event.reply_to_msg_id
		await borg.send_message(1284964960, "https://t.me/xdaofftopicgroup/{}".format(message_id))