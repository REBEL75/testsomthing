# Thanks to @D3_krish
# Porting in DARKDarkWeb
import asyncio
from telethon import version

from DarkWeb import ALIVE_NAME, DARKversion
from DarkWeb.cmdhelp import CmdHelp
from DarkWeb.Config.DARK_Config import Config
from DarkWeb.utils import admin_cmd, sudo_cmd
from DarkWeb import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK WEB"

ludosudo = Config.SUDO_USERS

sudou = "True" if ludosudo else "False"
DARK = bot.uid

edit_time = 1
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b765c0daec4a63c286e34.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**π₯π₯πππππ πππ  ππ ππππππ₯π₯**__\n\n" + "**ββββββββββββββββββββββ**\n\n"


pm_caption += (
    f"                π°α°α©ΥTα΄απ°\n      **γ[{DEFAULTUSER}](tg://user?id={DARK})γ**\n\n"
)
pm_caption += "ββββββββββββββ\n"
pm_caption += f"β£β’β³β   `α΄α΄Κα΄α΄Κα΄Ι΄:` `{version.__version__}` \n"
pm_caption += f"β£β’β³β  `α΄ α΄ΚsΙͺα΄Ι΄:` `{DARKversion}`\n"
pm_caption += f"β£β’β³β  `sα΄α΄α΄:` `{sudou}`\n"
pm_caption += "β£β’β³β  `α΄Κα΄Ι΄Ι΄α΄Κ:` [α΄α΄ΙͺΙ΄](https://t.me/DarkWeb_SUPPORT)\n"
pm_caption += "β£β’β³β  `α΄Κα΄α΄α΄α΄Κ:` [Κα΄Κα΄Κ](https://t.me/DARK_IS_OP)\n"
pm_caption += "β£β’β³β  `sα΄α΄α΄α΄Κα΄α΄Κ:` [sα΄α΄α΄α΄Κα΄](https://t.me/DARKSSUPPORT)\n"
pm_caption += "ββββββββββββββββ\n"
pm_caption += " [π₯ππ΄πΏπΎπ₯](https://github.com/TEAMDARKS/DarkWeb) πΉ [ππ»πππππππ](https://github.com/TEAMDARKS/DarkWeb/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1, caption=pm_caption)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command("alive", None, "To check am i alive").add_command(
    "DARK", None, "To check am i alive with your favorite alive pic"
).add()
