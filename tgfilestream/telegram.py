
import logging

from telethon import TelegramClient, events
from telethon.sessions import StringSession

from .paralleltransfer import ParallelTransferrer
from .config import (
    session_name,
    api_id,
    api_hash,
    public_url,
    start_message,
    group_chat_message
)
from .util import pack_id, get_file_name

log = logging.getLogger(__name__)

client = TelegramClient(StringSession(session_name), api_id, api_hash)
transfer = ParallelTransferrer(client)


@client.on(events.NewMessage)
async def handle_message(evt: events.NewMessage.Event) -> None:
    if not evt.is_private:
        await evt.reply(group_chat_message)
        return
    if not evt.file:
        await evt.reply(start_message)
        return
    url = public_url / str(pack_id(evt)) / get_file_name(evt)
    await evt.reply(f"Link to download file: {url}")
    log.info(f"Replied with link for {evt.id} to {evt.from_id} in {evt.chat_id}")
    log.debug(f"Link to {evt.id} in {evt.chat_id}: {url}")
