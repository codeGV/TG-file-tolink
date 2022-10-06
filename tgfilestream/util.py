
from typing import Tuple, Union

from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import TypeInputPeer, InputPeerChannel, InputPeerChat, InputPeerUser
from aiohttp import web

from .config import trust_headers

pack_bits = 32
pack_bit_mask = (1 << pack_bits) - 1

group_bit = 0b01
channel_bit = 0b10
chat_id_offset = 2
msg_id_offset = pack_bits + chat_id_offset


def pack_id(evt: events.NewMessage.Event) -> int:
    file_id = 0
    if evt.is_group:
        file_id |= group_bit
    if evt.is_channel:
        file_id |= channel_bit
    file_id |= evt.chat_id << chat_id_offset
    file_id |= evt.id << msg_id_offset
    return file_id


def unpack_id(file_id: int) -> Tuple[TypeInputPeer, int]:
    is_group = file_id & group_bit
    is_channel = file_id & channel_bit
    chat_id = file_id >> chat_id_offset & pack_bit_mask
    msg_id = file_id >> msg_id_offset & pack_bit_mask
    if is_channel:
        peer = InputPeerChannel(channel_id=chat_id, access_hash=0)
    elif is_group:
        peer = InputPeerChat(chat_id=chat_id)
    else:
        peer = InputPeerUser(user_id=chat_id, access_hash=0)
    return peer, msg_id


def get_file_name(message: Union[Message, events.NewMessage.Event]) -> str:
    if message.file.name:
        return message.file.name
    ext = message.file.ext or ""
    return f"{message.date.strftime('%Y-%m-%d_%H:%M:%S')}{ext}"


def get_requester_ip(req: web.Request) -> str:
    if trust_headers:
        try:
            return req.headers["X-Forwarded-For"]
        except KeyError:
            pass
    peername = req.transport.get_extra_info('peername')
    if peername is not None:
        return peername[0]
