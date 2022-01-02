#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import asyncio
import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
from config import Config
from translation import Translation
import os
# filters for auto post
FILTER_TEXT = bool(os.environ.get("FILTER_TEXT", True))
FILTER_AUDIO = bool(os.environ.get("FILTER_AUDIO", True))
FILTER_DOCUMENT = bool(os.environ.get("FILTER_DOCUMENT", True))
FILTER_PHOTO = bool(os.environ.get("FILTER_PHOTO", True))
FILTER_STICKER = bool(os.environ.get("FILTER_STICKER", True))
FILTER_VIDEO = bool(os.environ.get("FILTER_VIDEO", True))
FILTER_ANIMATION = bool(os.environ.get("FILTER_ANIMATION", True))
FILTER_VOICE = bool(os.environ.get("FILTER_VOICE", True))
FILTER_VIDEO_NOTE = bool(os.environ.get("FILTER_VIDEO_NOTE", True))
FILTER_CONTACT = bool(os.environ.get("FILTER_CONTACT", True))
FILTER_LOCATION = bool(os.environ.get("FILTER_LOCATION", True))
FILTER_VENUE = bool(os.environ.get("FILTER_VENUE", True))
FILTER_POLL = bool(os.environ.get("FILTER_POLL", True))
FILTER_GAME = bool(os.environ.get("FILTER_GAME", True))
files_count = 0

#===================Run Function===================#

@Client.on_message(filters.private & filters.command(["run"]))
async def run(bot, message):
    global SKIP
    global FROM
    global TO
    global LIMIT
    fromid = await bot.ask(message.chat.id, Translation.FROM_MSG)
    if fromid.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    elif not fromid.text.startswith('@'):
        return await message.reply(Translation.USERNAME)
    toid = await bot.ask(message.chat.id, Translation.TO_MSG)
    if toid.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    skipno = await bot.ask(message.chat.id, Translation.SKIP_MSG)
    if skipno.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    limitno = await bot.ask(message.chat.id, Translation.LIMIT_MSG)
    if limitno.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    buttons = [[
        InlineKeyboardButton('Yes', callback_data='start_public'),
        InlineKeyboardButton('No', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        text=Translation.DOUBLE_CHECK.format(fromid.text),
        reply_markup=reply_markup
    )
    SKIP = skipno.text
    FROM = fromid.text
    TO = toid.text
    LIMIT = limitno.text
    if re.match('-100\d+', TO):
        TO = int(TO)
