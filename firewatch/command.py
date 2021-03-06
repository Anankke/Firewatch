from pyrogram import Client, Filters, Message
from config import CONFIG


@Client.on_message(Filters.user(CONFIG.firewatch.trusted_op_id) & Filters.text, group=1)
async def firewatch(c: Client, m: Message):
    if m.text.startswith("/firewatch "):
        text_list = m.text.split(" ")

        # /firewatch dump @heipchat/or_it's_chat_id @someone/or_it's_user_id dest_chat_id [optional]offset_id
        if text_list[1] == "dump":
            chat_id = 0
            user_id = 0
            dst_id = 0
            try:
                chat_id = (await c.get_chat(text_list[2])).id
                user_id = (await c.get_users(text_list[3])).id
                dst_id = (await c.get_chat(text_list[4])).id
                try:
                    offset_id = int(text_list[5])
                except:
                    offset_id = 0
            except:
                await m.reply(
                    "Error occurred while parsing ids, check your input.\n"
                    "Chat ID: {}, User ID: {}, DST ID: {}".format(chat_id, user_id, dst_id)
                )
                return

            counter = 0
            all_history = c.iter_history(chat_id=chat_id, offset_id=offset_id, reverse=True)
            if user_id == "any":
                async for i in all_history:
                    if not i.service:
                        await i.forward(dst_id)
                        counter += 1
            else:
                async for i in all_history:
                    if not i.service and i.from_user:
                        if i.from_user.id == user_id:
                            await i.forward(dst_id)
                            counter += 1
            await m.reply("{} messages dumped successfully.".format(counter))
