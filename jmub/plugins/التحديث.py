
استيراد  asyncio
استيراد  سياق النص
استيراد  نظام التشغيل
استيراد  النظم
من  أسينسيو . استثناءات  استيراد  CancelledError

استيراد  heroku3
استيراد  urllib3
من  بوابة  الاستيراد  الريبو
من  بوابة . باستثناء  استيراد  GitCommandError و InvalidGitRepositoryError و NoSuchPathError

من  استيراد jmub  HEROKU_APP ، UPSTREAM_REPO_URL ، jmub 

من .. تكوين  استيراد  التكوين
من .. الأساسية . تسجيل استيراد  المسجل 
من .. الأساسية . يقوم المديرون  باستيراد  edit_delete و edit_or_reply
من .. sql_helper . استيراد global_collection  (
    add_to_collectionlist ،
    del_keyword_collectionlist ،
    get_collectionlist_items ،
)

cmdhd  =  التكوين . COMMAND_HAND_LER
ENV  =  منطقي ( بيئة نظام التشغيل . get ( "ENV" ، False ))
LOGS  =  التسجيل . getLogger ( __name__ )

HEROKU_APP_NAME  =  التكوين . HEROKU_APP_NAME  أو  لا شيء
HEROKU_API_KEY  =  التكوين . HEROKU_API_KEY  أو  لا شيء
Heroku  =  heroku3 . from_key ( التكوين . HEROKU_API_KEY )
heroku_api  =  "https://api.heroku.com"

UPSTREAM_REPO_BRANCH  =  التكوين . UPSTREAM_REPO_BRANCH

REPO_REMOTE_NAME  =  "اسم مؤقت"
IFFUCI_ACTIVE_BRANCH_NAME  =  "رئيسي"
NO_HEROKU_APP_CFGD  =  "لم يتم العثور على تطبيق heroku ، ولكن تم إعطاء المفتاح؟ 😕"
HEROKU_GIT_REF_SPEC  =  "HEAD: refs / heads / master"
RESTARTING_APP  =  "إعادة بدء تطبيق heroku"
IS_SELECTED_DIFFERENT_BRANCH  = (
    "يشبه الفرع المخصص {Branch_name}"
    "قيد الاستخدام: \ n "
    "في هذه الحالة ، يتعذر على المحدث تحديد الفرع المراد تحديثه."
    "يرجى التحقق من الفرع الرسمي ، وإعادة تشغيل التحديث."
)


# - نهاية الثوابت - #

أورليب 3 . تعطيل_ تحذيرات ( urllib3 . استثناءات . InsecureRequestWarning )

المتطلبات_المسار  =  نظام التشغيل المسار . انضم (
    نظام التشغيل . المسار . اسم الدليل ( مسار نظام التشغيل . اسم الدليل (مسار نظام التشغيل. اسم الدليل ( __ ملف__ ) ) ) ، " requirements.txt"
)


غير متزامن  def  gen_chlog ( ريبو ، فرق ):
    d_form  =  "٪ d /٪ m /٪ y"
    العودة  "" . انضم (
        و "• { ج . ملخص } ( { ج . وقت_التزام . strftime ( d_form ) } ) < { c . author } > \ n "
        ل  ج  في  الريبو . iter_commits ( فرق )
    )


غير متزامن  def  print_changelogs ( حدث ، ac_br ، سجل التغيير ):
    changelog_str  = (
        f "** • توفر تحديث جديد للفـرت [ { ac_br } ]: \ n \ n التغييرات: ** \ n` { changelog } ` "
    )
    إذا كان  len ( changelog_str ) >  4096 :
        انتظر  الحدث . تم وضعه في ملف ** " ) التغييرات كثيرة جدًا.
        مع  فتح ( "output.txt" ، " w +" ) كملف  :
            ملف . الكتابة ( changelog_str )
        انتظر  الحدث . العميل . send_file (
            حدث . chat_id ،
            "output.txt" ،
            reply_to = حدث . معرف ،
        )
        نظام التشغيل . إزالة ( "output.txt" )
    آخر :
        انتظر  الحدث . العميل . send_message (
            حدث . chat_id ،
            changelog_str ،
            reply_to = حدث . معرف ،
        )
    عودة  صحيح


 التحديث غير  المتزامن update_requirements ():
    reqs  =  str ( requirements_path )
    جرب :
        العملية  =  انتظار  عدم التزامن . create_subprocess_shell (
            "" . انضم ([ sys . قابل للتنفيذ ، "-m" ، "نقطة" ، "تثبيت" ، "-r" ، reqs ]) ،
            stdout = أسينسيو . عملية فرعية . الأنابيب ،
            stderr = أسينسيو . عملية فرعية . الأنابيب ،
        )
        انتظار  العملية . التواصل ()
         عملية العودة . رمز الإرجاع
    باستثناء  الاستثناء  كـ  e :
        إعادة  rep ( هـ )


async  def  update_bot ( event ، repo ، ups_rem ، ac_br ):
    جرب :
        ups_rem . سحب ( ac_br )
    باستثناء  GitCommandError :
        الريبو . بوابة . إعادة تعيين ( "- Hard" ، "FETCH_HEAD" )
    في انتظار  update_requirements ()
    بلاكثون  =  انتظار  الحدث . تعديل ( "** • تم بنجاح التحديث جار إعادة التشغيل الان **" )
    انتظر  الحدث . العميل . إعادة تحميل ( بلاكثون )


 نشر غير  متزامن ( حدث ، الريبو ، ups_rem ، ac_br ، txt ):
    لو   كانت  HEROKU_API_KEY بلا :
        يعود  انتظار  الحدث . تعديل ( "** • يرجى وضع فار HEROKU_API_KEY للتحديث **" )
    هيروكو  =  heroku3 . from_key ( HEROKU_API_KEY )
    heroku_applications  =  heroku . تطبيقات ()
    لو   كانت  HEROKU_APP_NAME بلا :
        انتظر  الحدث . تحرير (
            "** • يرجى وضع يرجى وضع فار HEROKU_APP_NAME **  " لتتمكن من تحديث السورس "
        )
        الريبو . __del__ ()
        يعود
    heroku_app  =  التالي (
        ( التطبيق  للتطبيق  في heroku_applications إذا كان اسم التطبيق == _       كان HEROKU_APP_NAME
        لا شيء ،
    )

    إذا كان  heroku_app  هو  لا شيء :
        انتظر  الحدث . تحرير ( f " { txt } \ n "  "** • خطأ في التعرف على تطبيق هيروكو **" )
        إعادة  الريبو . __del__ ()
    jmthon  =  انتظار  الحدث . يحرر (
        "** • جار اعادة تشغيل الدينو الان يرجى الانتظار من 2-5 دقائق **"
    )
    يحاول :
        ulist  =  get_collectionlist_items ()
        لأني  في ulist _   :
            إذا  كنت  ==  "إعادة تشغيل_تحديث" :
                del_keyword_collectionlist ( "reset_update" )
    باستثناء  الاستثناء  كـ  e :
        السجلات . خطأ ( هـ )
    جرب :
        add_to_collectionlist ( "reset_update" ، [ jmthon . chat_id ، jmthon . id ])
    باستثناء  الاستثناء  كـ  e :
        السجلات . خطأ ( هـ )
    ups_rem . إحضار ( ac_br )
    الريبو . بوابة . إعادة تعيين ( "- Hard" ، "FETCH_HEAD" )
    heroku_git_url  =  heroku_app . git_url . استبدال (
        "https: //" ، f "https: // api: { HEROKU_API_KEY } @"
    )

    إذا كان  "heroku"  في  الريبو . أجهزة التحكم عن بعد :
        بعيد  =  الريبو . بعيد ( "heroku" )
        بعيد . set_url ( heroku_git_url )
    آخر :
        بعيد  =  الريبو . create_remote ( "heroku" ، heroku_git_url )
    جرب :
        بعيد . push ( refspec = "HEAD: refs / head / master" ، force = True )
    باستثناء  استثناء  كخطأ  _ :
        انتظر  الحدث . تحرير ( f " { txt } \ n ** تقرير الخطأ: ** \ n` { error ` ")
        إعادة  الريبو . __del__ ()
    build_status  =  heroku_app . يبني ( order_by = "created_at" ، الفرز = "desc" ) [ 0 ]
    إذا  build_status . الحالة  ==  "فشل" :
        العودة  تنتظر  edit_delete (
            حدث ، "** • تحديث التحديث ** \ n "  "يبدو أنه تم الغاءه أو حصل حصل ما"
        )
    جرب :
        بعيد . push ( "master: main" ، force = True )
    باستثناء  الاستثناء  كخطأ  : _
        انتظر  الحدث . تحرير ( f " { txt } \ n ** تقرير الخطأ: ** \ n` { error } " )
        إعادة  الريبو .__del__ ()
    انتظر  الحدث . تحرير ( "** • فشل التحديث ارسل **` .اعادة تشغيل` ** للتحديث ** " )
    مع  سياق النص . قمع ( CancelledError ):
        انتظر  الحدث . العميل . قطع الاتصال ()
        إذا  لم يكن HEROKU_APP  بلا :  
            HEROKU_APP . إعادة ()


@ jmub . ar_cmd ( pattern = "تحديث (| الان)؟ $" )
غير متزامن  def  المنبع ( حدث ):
    أسيوط  =  حدث . تطابق_نمط . مجموعة ( 1 ).يجرد ()
    الحدث  =  انتظار  التحرير أو الرد (
        حدث _ "** • جار البحث عن التحديثات يرجى الانتظار قليلا **"
    )
    off_repo  =  UPSTREAM_REPO_URL
    force_update  =  خطأ
    إذا كانت  ENV  و ( HEROKU_API_KEY  لا  شيء  أو  HEROKU_APP_NAME  لا  شيء ):
        العودة  في انتظار  edit_or_reply (
            الحدث ، "** • عليك وضع فارات هير مارك للتحديث **"
        )
    جرب :
        txt  =  "فشل في التحديث لسورس بلاكثون"  +  "** • حدث خطأ ما: ** \ n "

        الريبو  =  الريبو ()
    باستثناء  NoSuchPathError  كخطأ  : _
        انتظر  الحدث . تحرير ( f " { txt } \ n المجلد { خطأ } لم يتم أيجاده" )
        إعادة  الريبو . __del__ ()
    باستثناء  GitCommandError  كخطأ  : _
        انتظر  الحدث . تحرير ( f " { txt } \ n فشل مبكر { error } " )
        إعادة  الريبو . __del__ ()
    باستثناء  InvalidGitRepositoryError  كخطأ  : _
        إذا كان  conf  هو  لا شيء :
            عودة  انتظار  الحدث . تحرير (
                f "** • للأسف المجلد { error } لا يبدة انه خاص لسورس معين. \ n يمكنك اصلاح هذه المشكلة بأرسال.` .تحديث التنصيب` "
            )

        الريبو  =  الريبو . الحرف الأول ()
        الأصل  =  الريبو . create_remote ( "upstream" ، off_repo )
        الأصل . جلب ()
        force_update  =  صحيح
        الريبو . create_head ( "master" ، origin . refs . master )
        الريبو . رؤساء . سيد . set_tracking_branch ( الأصل . المراجع . master )
        الريبو . رؤساء . سيد . الخروج ( صحيح )
    ac_br  =  الريبو . active_branch . اسم
    إذا كان  ac_br  ! =  UPSTREAM_REPO_BRANCH :
        انتظر  الحدث . تحرير (
            "** [التحديث]: ** \ n "
            و "يبدو أنك تستخدم فرع أخر: ( { ac_br } )."
            "في هذه الحالة غير قادر على التحديث"
            "لملفات الفرع الخاص بك."
            "يرجى استخدام الفرغ الاساسي"
        )
        إعادة  الريبو . __del__ ()
    مع  سياق النص . قمع ( BaseException ):
        الريبو . create_remote ( "upstream" ، off_repo )
    ups_rem  =  ريبو . بعيد ( "المنبع" )
    ups_rem . إحضار ( ac_br )
    changelog  =  await  gen_chlog ( repo ، f "HEAD..upstream / { ac_br } " )
    # حالة خاصة للنشر
    إذا كان  التغيير ==  "  "  وليس  force_update : 
        انتظر  الحدث . تحرير (
            " \ n ** • سورس بلاكثون محدث الى أخر اصدار **"
            f "** \ n الفـرع: { UPSTREAM_REPO_BRANCH } ** \ n "
        )
        إعادة  الريبو . __del__ ()
    if  conf  ==  "  " وليس  force_update : 
        في انتظار  print_changelogs ( حدث ، ac_br ، سجل التغيير )
        انتظر  الحدث . حذف ()
        عودة  انتظار  الحدث . رد (
            f "** • ارسل **` { cmdhd } حدث` لتحديث سورس بلاكثون "
        )

    إذا  فرض_التحديث :
        انتظر  الحدث . تعديل ( "** • التحديث الاجباري الى اخر اصدار انتظر قليلا **" )
    إذا  أسيوط  ==  "الان" :
        انتظر  الحدث . تحرير ( "** • جار تحديث سورس بلاكثون أنتظر قليلا **" )
        في انتظار  update_bot ( event ، repo ، ups_rem ، ac_br )
    يعود


@ jmub . ar_cmd (
    نمط = "حدث $" ،
)
غير متزامن  def  المنبع ( حدث ):
    إذا كان  ENV :
        إذا كانت  HEROKU_API_KEY بلا  أو لم تكن HEROKU_APP_NAME بلا :     
            العودة  في انتظار  edit_or_reply (
                حدث _ "** •
            )
     نظام elif . المسار . موجود ( "config.py" ):
        العودة  تنتظر  edit_delete (
            حدث _
            f "** • انت تستخدم التنصيب يدويا يرجى ارسال امر **` { cmdhd } حدث` " ،
        )
    event  =  wait  edit_or_reply ( event ، "** - جار جلب ملفات السورس يرجى الانتظار قليلا **" )
    off_repo  =  "https://github.com/ZEKO124/gibthon"
    نظام التشغيل . chdir ( "/ التطبيق" )
    جرب :
        txt  =  "** • لقد حدث خطأ اثناء التحديث **"  +  "** لقد حدث خطأ ما ** \ n "

        الريبو  =  الريبو ()
    باستثناء  NoSuchPathError  كخطأ  : _
        انتظر  الحدث . تحرير ( f " { txt } \ n • المجلد   { error } لم يتم العثور عليه" )
        إعادة  الريبو . __del__ ()
    باستثناء  GitCommandError  كخطأ  : _
        انتظر  الحدث . تحرير ( f " { txt } \ n • فشل فشل الخطا: { error } " )
        إعادة  الريبو . __del__ ()
    باستثناء  InvalidGitRepositoryError :
        الريبو  =  الريبو . الحرف الأول ()
        الأصل  =  الريبو . create_remote ( "upstream" ، off_repo )
        الأصل . جلب ()
        الريبو . create_head ( "master" ، origin . refs . master )
        الريبو . رؤساء . سيد . set_tracking_branch ( الأصل . المراجع . master )
        الريبو . رؤساء . سيد . الخروج ( صحيح )
    مع  سياق النص . قمع ( BaseException ):
        الريبو . create_remote ( "upstream" ، off_repo )
    ac_br  =  الريبو . active_branch . اسم
    ups_rem  =  ريبو . بعيد ( "المنبع" )
    ups_rem . إحضار ( ac_br )
    انتظر  الحدث . تحرير ( "** • جار الان التحديث أنتظر قليلا **" )
    في انتظار  النشر ( event ، repo ، ups_rem ، ac_br ، txt )
تذييل
حقوق النشر © لعام 2023 لشركة GitHub، Inc.
التنقل في التذييل
شروط
خصوصية
حماية
حالة
المستندات
اتصل بـ GitHub
التسعير
API
تمرين
مدونة
عن
