# بلاكثون
# يمنع منعاً باتاً تصور الملف خليتك كرامه ولتسرقة
من  jepthon  import  jepiq
من  telethon . TL . وظائف . استيراد الرسائل  GetHistoryRequest 
من  telethon . TL . وظائف . استيراد القنوات  JoinChannelRequest 
من  telethon . TL . وظائف . استيراد الرسائل  ImportChatInviteRequest 
 طلبات الاستيراد
استيراد  asyncio
من  أحداث الاستيراد telethon  
ج  =  الطلبات . جلسة ()
bot_username  =  "@ t06bot"
jepthon  = [ 'نعم' ]


@ jepiq . في ( admin_cmd ( pattern = "(نجب | نجبيت )" ))
غير متزامن  def  _ ( حدث ):
    إذا كان  jepthon [ 0 ] ==  "نعم" :
        انتظر  الحدث . تحرير ( "** ᯽︙سيتم تجميع النقاط ، قبل كل شي تأكد من انك قمت بلانظمام قنوات قنوات الاجباري للبوت ).
        channel_entity  =  انتظر  jepiq . get_entity ( bot_username )
        انتظر  جيبيك . send_message ( '@ t06bot' ، '/ start' )
        في انتظار  أسينسيو . ينام ( 5 )
        msg0  =  انتظار  jepiq . get_messages ( '@ t06bot' ، الحد = 1 )
        في انتظار  msg0 [ 0 ]. انقر ( 2 )
        في انتظار  أسينسيو . ينام ( 5 )
        msg1  =  انتظار  jepiq . get_messages ( '@ t06bot' ، الحد = 1 )
        في انتظار  msg1 [ 0 ]. انقر ( 0 )

        chs  =  1
        لأني  في  النطاق  ( 100 ) :
            إذا كان  jepthon [ 0 ] ==  'لا' :
                استراحة
            في انتظار  أسينسيو . ينام ( 5 )

            list  =  انتظار  jepiq ( GetHistoryRequest ( الند = channel_entity ، الحد = 1 ،
                                                   offset_date = لا شيء ، offset_id = 0 ، max_id = 0 ، min_id = 0 ، add_offset = 0 ، التجزئة = 0 ))
            msgs  =  قائمة . الرسائل [ 0 ]
            إذا  الرسائل . رسالة . find ( 'لا يوجد قنوات في الوقت الحالي ، قم يتجميع النقاط بطريقه مختلفه' ) ! =  - 1 :
                انتظر  جيبيك . send_message ( event . chat_id ، f "** لاتوجد قنوات للبوت **" )
                استراحة
            url  =  الرسائل . reply_markup . صفوف [ 0 ]. أزرار [ 0 ]. عنوان url
            جرب :
                جرب :
                    في انتظار  جيبيك ( JoinChannelRequest ( url ))
                باستثناء :
                    بوت  =  عنوان url . انقسام ( '/' ) [ - 1 ]
                    انتظار  jepiq ( ImportChatInviteRequest ( بوت ))
                msg2  =  انتظار  jepiq . get_messages ( '@ t06bot' ، الحد = 1 )
                في انتظار  msg2 [ 0 ]. انقر ( نص = "تحقق" )
                chs  + =  1
                انتظر  جيبيك . send_message ( "me" ، f "تم بخدمة في { chs } قناة" )
            باستثناء :
                انتظر  جيبيك . send_message ( event . chat_id ، f "** خطأ، ممكن تبندت **" )
                استراحة
        انتظر  جيبيك . send_message ( event . chat_id ، "** تم الانتهاء من التجميع! **" )

    آخر :
        انتظر  الحدث . تحرير ( "يجب الدفع لاستعمال هذا الامر!" )
