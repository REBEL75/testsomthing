# PLUGIN MADE BY @Dark_IS_OP FOR DarkWeb
# KEEP CREDITS ELSE GAY

import random, re
from Dark.utils import admin_cmd
import asyncio
from telethon import events

@Dark.on(admin_cmd(pattern="baby1 ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""SUN TUU MERI ππJAANππ HAA MANA PYAR πΉπΉKIYA HAA KOI MAZAK NAHI. AJJ NIGHT π MAA TUU BHUT YAADππ AAA RAHI THE . TU BASS MERI πππ MERI JAAN HAA BASS MERIπ. I LOVE πYOU BABYππ""")