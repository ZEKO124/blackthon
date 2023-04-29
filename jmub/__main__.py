import sys

import jepthon

from jepthon import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config

from .core.logger import logging

from .core.session import jepiq

from .utils import (

    add_bot_to_logger_group,

    install_externalrepo,

    ipchange,

    load_plugins,

    setup_bot,

    mybot,

    startupmessage,

    verifyLoggerGroup,

    saves,

)

LOGS = logging.getLogger("jepthon")

print(jepthon.__copyright__)

print("Licensed under the terms of the " + jepthon.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:

    LOGS.info("جارِ بدء بوت بلاكتون ✓")

    jepiq.loop.run_until_complete(setup_bot())

    LOGS.info("تم اكتمال تنصيب البوت ✓")

except Exception as e:

    LOGS.error(f"{str(e)}")

    sys.exit()

try:

    LOGS.info("يتم تفعيل وضع الانلاين")

    jepiq.loop.run_until_complete(mybot())

    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")

except Exception as jep:

    LOGS.error(f"- {jep}")

    sys.exit()    

class CatCheck:

    def __init__(self):

        self.sucess = True

Catcheck = CatCheck()

async def startup_process():

    check = await ipchange()

    if check is not None:

        Catcheck.sucess = False

        return

    await verifyLoggerGroup()

    await load_plugins("plugins")

    await load_plugins("assistant")

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    print("᯽︙بـوت بلاكتون يعـمل بـنجاح ")

    print(

        f"تم تشغيل الانلاين تلقائياً ارسل {cmdhr}الاوامر لـرؤيـة اوامر السورس\

        \nللمسـاعدة تواصـل  https://t.me/xl444"

    )

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    
