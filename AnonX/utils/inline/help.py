from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonX import app
from config import SUPPORT_GROUP


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Aԃɱιɳ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Aµƭɦ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="Bʅαƈƙʅιʂƚ",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Bɾσαԃƈαʂƚ",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="GႦαɳ",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="Lყɾιƈʂ",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Pιɳɠ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="Pʅαყ",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="Pʅαყʅιʂƚ",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Vιԃҽσƈԋαƚ",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="Sƚαɾƚ",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="Sυԃσ",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="Şนpp໐rt", url=f"{SUPPORT_GROUP}"
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
