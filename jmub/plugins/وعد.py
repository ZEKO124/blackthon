import logging
import time
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events
# -

sython.start()
c = requests.session()
bot_username = '@KBKBOT'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'



@sython.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''**
SYTHON TAMOEL IS WORKING
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
- VERSION : 2.0
- DEVLOBER : SOMY TEAM
- CHANNEL : @SAYTHONH
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
ارسـل '.اوامر التجميع' لفتح الاوامر الخاصة بالسورس
**''')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اوامر التجميع"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''**
تجميع نقاط بوت المليار » `.تجميع المليار`
تجميع نقاط بوت الجوكر » `.تجميع الجوكر`
تجميع نقاط بوت العقاب » `.تجميع العقاب`
**''')
    


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("**حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء**")
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@KBKBOT', '**جاري التجميع بواسطة | SOMY TEAM**')
        channel_entity = await sython.get_entity(bot_username)
        await sython.send_message('@KBKBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@KBKBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@KBKBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@KBKBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")


##################


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("**حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء**")
        channel_entity = await sython.get_entity(bot_usernamee)
        await sython.send_message('@A_MAN9300BOT', '**جاري التجميع بواسطة | SOMY TEAM**')
        channel_entity = await sython.get_entity(bot_usernamee)
        await sython.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

############
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العقاب"))
async def _(event):
        await event.edit("**حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء**")
        channel_entity = await sython.get_entity(bot_usernameee)
        await sython.send_message('@MARKTEBOT', '**جاري التجميع بواسطة | SOMY TEAM**')
        channel_entity = await sython.get_entity(bot_usernameee)
        await sython.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython(ImportChatInviteRequest(bott))
                msg2 = await sython.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython.send_message(event.chat_id, "تم الانتهاء من التجميع !")





print("- sython Userbot Running ..")
sython.run_until_disconnected()


# t.me/zeko124
@jmub.ar_cmd(pattern="بخشيش وعد (.*)")
async def baqshis(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jmub.send_message(chat, "بخشيش")
        await asyncio.sleep(605)


@jmub.ar_cmd(pattern="راتب وعد (.*)")
async def ratb(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jmub.send_message(chat, "راتب")
        await asyncio.sleep(605)


# none
@jmub.ar_cmd(pattern="كلمات وعد (.*)")
async def waorwaad(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jmub.send_message(chat, "كلمات")
        await asyncio.sleep(0.5)
        masg = await jmub.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=3)[3:])).split(" ", 2)
        if len(masg) == 2:
            msg = masg[0]
            await jmub.send_message(chat, msg)
        else:
            msg = masg[0] + " " + masg[1]
            await jmub.send_message(chat, msg)


@jmub.ar_cmd(pattern="استثمار وعد (.*)")
async def _(event):
    await event.edit(
        "**- تم تفعيل الاستثمار ببوت وعد بنجاح لأيقافه ارسل \n`.استثمار وعد 1`"
    )
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jmub.send_message(chat, "فلوسي")
        await asyncio.sleep(0.5)
        masg = await jmub.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
        msg = masg[0]
        if int(msg) > 500000000:
            await jmub.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(10)
            mssag2 = await jmub.get_messages(chat, limit=1)
            await mssag2[0].click(text="اي ✅")
        else:
            await jmub.send_message(chat, f"استثمار {msg}")
        await asyncio.sleep(1210)
