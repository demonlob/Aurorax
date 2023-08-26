from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
     buttons = [
         [
             InlineKeyboardButton(
                 text="Sҽƚƚιɳɠʂ", callback_data="settings_helper"
             ),
         ],
      ]
     return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aԃԃ ɱҽ ƚσ ɠɾσυρ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hҽʅρ",
                callback_data="settings_back_helper",
            ),
        ],
     ]
    return buttons
