from pyrogram import Client, Filters, Message
from config import CONFIG, DotDict

firewatch_list = [DotDict(i) for i in CONFIG.firewatch.watch]


def match_id(id, id_list):
    return (id in id_list) or ("any" in id_list)


@Client.on_message(Filters.group, group=0)
async def watch(c: Client, m: Message):
    for i in firewatch_list:
            if not m.service and match_id(m.chat.id, i.chat_id):
                if m.from_user:
                    if match_id(m.from_user.id, i.target_id):
                        await m.forward(i.dest_chat_id)
