from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events
from help import *
c = requests.session()
bot_username = '@KBKBOT'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت المليار"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit(KBKBOT)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.جمع"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sedthon.get_entity(bot_username)
        await sedthon.send_message('@KBKBOT', '/start')
        await asyncio.sleep(0)
        msg0 = await sedthon.get_messages('@KBKBOT', limit=1)
        await msg0[0].click(0)
        await asyncio.sleep(0)
        msg1 = await sedthon.get_messages('@KBKBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(0)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f"خطأ , ممكن تبندت")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")



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
