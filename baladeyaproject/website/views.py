from django.shortcuts import render
from django.contrib import messages
from .forms import QuestionForm,RentalValueForm,ResponseForm#,EmailForm,
from .models import( 
    NewsDecisions, NewsFileDecisions,NewsProjects,NewsActivity,NewsFileProjects,NewsFileActivity,
    QuestionType, Question, Response, ResponseFile, 
    Email,
    Transactions ,
    RentalValue,RentalValueBill,
    Maalem,MaalemImage,
    CompanyType,Company,CompanySection
    )
from django.core.mail import send_mail,EmailMessage
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory,modelformset_factory
from django import forms
from django.forms import formset_factory
from django.template.loader import render_to_string
from baladeyaproject.settings import MUNICIPALITY_NAME,EMAIL_HOST_USER


#-------------------------------------------------Home Section  --------------------------------------------------
def Home_view(request):
    context = {
        'NewsDecisions':    NewsDecisions.objects.order_by('-news_date')[0:3],
        'NewsProjectFinish':    NewsProjects.objects.filter(news_projects_finish=1).order_by('-news_date')[0:1],
        'NewsProjectNotFinish': NewsProjects.objects.filter(news_projects_finish=0).order_by('-news_date')[0:1],
        'NewsActivity':     NewsActivity.objects.order_by('-news_date')[0:3],
        'Maalem':           Maalem.objects.all().order_by('-maalem_date')[0:10],
    } 
    return render(request, 'Home_view.html', context)


#-------------------------------------------------NewsDecisions Section  --------------------------------------------------
def Decisions_view(request):
    decisionmore=None
    showmore=request.GET.get('showmore')
    showless=request.GET.get('showless')
    decision=NewsDecisions.objects.order_by('-news_date')[0:10]
    if showless:
        showmore=0
    if showmore :
        if NewsDecisions.objects.all().count()>10:
            decisionmore=NewsDecisions.objects.order_by('-news_date')[10:80]
        else:
            messages.warning(request,'لا يوجد المزيد من القرارات و التعاميم')
        
    context = {
        'showmore':showmore,
        'NewsDecisions':decision ,
        'NewsDecisionsmore':decisionmore
    }
    return render(request, 'Decisions/Decisions_view.html', context)

def Decisions_detail_view(request,id):
    try:
        thedecision=NewsDecisions.objects.get(id=id)
    except :
        messages.warning(request,'حدث خطأ')
    newsfiledecision=NewsFileDecisions.objects.filter(relation=thedecision)
    context = {
        'NewsModel': thedecision,
        'NewsFileModel': newsfiledecision,
    }
    return render(request, 'Decisions/Decisions_detail_view.html', context)


#-------------------------------------------------News Section  --------------------------------------------------
def News_view(request):
    context = {
        'NewsDecisions': NewsDecisions.objects.order_by('-news_date')[0:6],
        'NewsProjectFinish': NewsProjects.objects.filter(news_projects_finish=1).order_by('-news_date')[0:3],
        'NewsProjectNotFinish': NewsProjects.objects.filter(news_projects_finish=0).order_by('-news_date')[0:3],
        'NewsActivity': NewsActivity.objects.order_by('-news_date')[0:6],

    }   
    return render(request, 'News_view.html',context)


#-------------------------------------------------Project Section  --------------------------------------------------
def Project_view(request):
    projectsmore=None
    showmore=request.GET.get('showmore')
    showless=request.GET.get('showless')
    finish=request.GET.get('finish')
    if finish == None:
        finish='1'
    if showless:
        showmore=0
    if finish== '0':
        projects=NewsProjects.objects.filter(news_projects_finish=0).order_by('-news_date')[0:10]
        if showmore:
            if NewsProjects.objects.filter(news_projects_finish=0).count()>10:
                projectsmore=NewsProjects.objects.filter(news_projects_finish=0).order_by('-news_date')[2:80]
            else:
                messages.warning(request,'لا يوجد المزيد من المشاريع ')
    else :
        projects=NewsProjects.objects.filter(news_projects_finish=1).order_by('-news_date')[0:10]
        if showmore:
            if NewsProjects.objects.filter(news_projects_finish=1).count()>10:
                projectsmore=NewsProjects.objects.filter(news_projects_finish=1).order_by('-news_date')[10:80]
            else:
                messages.warning(request,'لا يوجد المزيد من المشاريع ')
    
    context = {
    'showmore':showmore,
    'Project':projects,
    'Projectmore':projectsmore,
    'finish':finish
    }
    return render(request, 'Project/Project_view.html', context)

def Project_detail_view(request,id):
    try:
        theproject=NewsProjects.objects.get(id=id)
    except :
        messages.warning(request,'حدث خطأ')
    newsfileproject=NewsFileProjects.objects.filter(relation=theproject)
    context = {
        'NewsModel': theproject,
        'NewsFileModel': newsfileproject,
        'projectfinish':theproject.news_projects_finish,
    }
    return render(request, 'Project/Project_detail_view.html', context)


#-------------------------------------------------About Section  --------------------------------------------------
def About_view(request):
    context={
      
    }
    return render(request, 'About/About_view.html',context)


#-------------------------------------------------Contact us Section  --------------------------------------------------
def Contactus_view(request):
    #email_form = EmailForm()
    question_form = QuestionForm()
    last_question = Question.objects.last()

    if request.method == 'POST':
     #   email_form = EmailForm(request.POST or None)
        question_form = QuestionForm(request.POST or None,request.FILES or None)
        email_in_question =request.POST.get('Question_email')        

        if question_form.is_valid():
            obj=question_form.save(commit=False)
            if obj.Question_principal_image:
                if obj.Question_principal_image.size >5242880:#verify the size of the image is small than 5mb 
                    obj.delete()
                    messages.warning(request,'الحد الأقصى للصورة المرفقة 5 ميجابايت')
                else:
                    obj.save()
            else:
                obj.save()
                
            last_question = Question.objects.last()
            last_question_id = last_question.id
            last_question_date = last_question.Question_date
    
            if email_in_question:
                special_code = last_question.specialcode
                date = str(last_question_date)
                questiontype_in_question = request.POST.get('Question_type')
                fullname_in_question =request.POST.get('Question_full_name')
                subject = MUNICIPALITY_NAME
                message = f''
                email_from = EMAIL_HOST_USER
                email_recipient = [email_in_question,EMAIL_HOST_USER]
                try:
                    send_mail(
                        subject,
                        message,
                        email_from,
                        email_recipient,
                        fail_silently=False,
                        html_message = render_to_string('email/questionemail.html', {'special_code': special_code,'last_question_id':last_question_id,'date':date})
                            )
                    messages.success(request,'تم ارسال رسالة الى البريد الالكتروني الخاص بكم لمتابعة الاجابة')
                except:
                    messages.warning(request,'فشل بأرسال رسالة الى البريد الالكتروني الخاص بكم')
            messages.success(request,'شكرا لتواصلكم ')
            question_form = QuestionForm()
        else:
            messages.warning(request,'لم تنجح محاولة الإتصال بنا ')

    Lastquestion = Question.objects.order_by('-Question_date')[0:99]
    result=''
    query =request.GET.get("search")
    if query:
        Lastquestion=Question.objects.filter(Question_text__icontains=query).order_by('-Question_date')[0:99]
        result=query
    context = {
        'result':result,
        'Question': Question.objects.all(),
        'QuestionType': QuestionType.objects.all(),
        'QuestionForm': question_form,
        #'EmailForm': email_form,
        'Response': Response.objects.all(),
        'LastQuestion':Lastquestion,
    }
    

    return render(request, 'Contactus_view.html', context)


#-------------------------------------------------Activity Section  --------------------------------------------------
def Activity_view(request):
    activitymore=None
    showmore=request.GET.get('showmore')
    showless=request.GET.get('showless')
    activity=NewsActivity.objects.order_by('-news_date')[0:10]
    if showless:
        showmore=0
    if showmore :
        if NewsProjects.objects.all().count()>10:
            activitymore=NewsActivity.objects.order_by('-news_date')[10:80]
        else:
            messages.warning(request,'لا يوجد المزيد من النشاطات ')
        
    context = {
        'showmore':showmore,
        'Newsactivity':activity ,
        'Newsactivitymore':activitymore
        }
    return render(request, 'Activity/Activity_view.html', context)

def Activity_detail_view(request,id):
    try:
        theactivity=NewsActivity.objects.get(id=id)
    except :
        messages.warning(request,'حدث خطأ')
    newsfileactivity=NewsFileActivity.objects.filter(relation=theactivity)
    context = {
        'NewsModel': theactivity,
        'NewsFileModel': newsfileactivity
    }
    return render(request, 'Activity/Activity_detail_view.html', context)


#-------------------------------------------------Transactions Section  --------------------------------------------------
def Transactions_view(request):
    q=0
    query =request.GET.get("search")
    Transaction_list= Transactions.objects.all()
    if query:
        Transaction_list=Transaction_list.filter(transactions_title__icontains=query)
        if not Transaction_list.last():
            messages.warning(request,'لا يوجد نتيجة لبحثكم')
            q=1
    context = {
        'Transactions': Transaction_list,
        'q':q,
        'query':query,
    }
    return render(request, 'Transactions/Transactions_view.html', context)

def Transactions_detail_view(request,id):
    try:
        transaction=Transactions.objects.get(id=id)
    except :
        messages.warning(request,'حدث خطأ')
    context = {
        'Transactions': transaction
    }
    return render(request, 'Transactions/Transactions_detail_view.html', context)


#-------------------------------------------------Rental Value Section  --------------------------------------------------
def Rental_value_view(request):
    RentalVlaueList=1
    RentalVlaueBillList=RentalValueBill.objects.all()
    rental_value_form = RentalValueForm()   
    a=0#for verifie the data input if true , if true the response show by giving the variabla a value 'True' 
    if request.method == 'POST':
        rental_value_form = RentalValueForm(request.POST or None) 
        blocknumber = request.POST.get('rental_value_block_number')
        realtynumber = request.POST.get('rental_value_realty_number')
        sectionnumber = request.POST.get('rental_vlaue_section')
        additionalcode = request.POST.get('rental_value_additional_code')

        
        if rental_value_form.is_valid():
            if blocknumber == '':blocknumber=None
            if realtynumber == '':realtynumber=None
            if sectionnumber == '':sectionnumber=None
            if additionalcode == '':additionalcode=None
          
            c=0# if this variable is True this mean the first try to get the object by the (block and section and realty number) fail so
           
            try:
                RentalVlaueList=get_object_or_404(RentalValue,
                                                    rental_value_block_number = blocknumber,
                                                    rental_vlaue_section=sectionnumber,
                                                    rental_value_realty_number=realtynumber,
            )
                a=1# here we know the data is verfied so a =1 so the result should show
            except:
                c=1
            # here come the next try to find the object by the (realty number and additional code) and befor do that we should make sure the first try is fail because if the first try success and the second try success by a 2 different value that mean the problem exist
            try:
                if c:
                    RentalVlaueList=get_object_or_404(RentalValue,
                                                        rental_value_realty_number = realtynumber,
                                                        rental_value_additional_code=additionalcode
                )    
                    a=1# here we know the data is verfied so a =1 so the result should show            
            except:
                #here the two try fail so a message should be raise to the user
                if c:
                    messages.warning(request,'حدث خطأ الرجاء التأكد من المعلومات المدخلة , في حال تكرر الخطأ الرجاء التواصل معنا')
        else:
            messages.warning(request,'الرجاء التأكد من المعلومات المدخلة')    
        rental_value_form = RentalValueForm()
  
    context={
        'RentalVlaueList':RentalVlaueList,
        'RentalVlaueBillList':RentalVlaueBillList,
        'rental_value_form':rental_value_form,
        'a':a,
    }

    return render(request,'Rental_value_view.html',context)


#-------------------------------------------------Maalem Section  --------------------------------------------------
def Maalem_view(request):
    maalemmore=None
    showmore=request.GET.get('showmore')
    showless=request.GET.get('showless')
    maalem=Maalem.objects.order_by('-maalem_date')[0:10]
    if showless:
        showmore=0
    if showmore :
        if Maalem.objects.all().count()>10:
            maalemmore=Maalem.objects.order_by('-maalem_date')[10:80]
        else:
            messages.warning(request,'لا يوجد المزيد من المعالم')
    
    context = {
        'Maalem': maalem,
        'maalemmore':maalemmore,
        'showmore':showmore,
        'showless':showless,
    }
    return render(request, 'maalem/Maalem_view.html', context)

def Maalem_detail_view(request,id):
    try:
        maalem=Maalem.objects.get(id=id)
    except :
        messages.warning(request,'حدث خطأ')
    context = {
        'Maalem': maalem,
        'MaalemImage': MaalemImage.objects.all()
    }
    return render(request, 'maalem/Maalem_detail_view.html', context)


#-------------------------------------------------Dalil Section  --------------------------------------------------
def Dalil_view(request):
    context ={
        'CompanySection':CompanySection.objects.all(),

    }
    return render(request,'dalil/dalil_view.html',context)

def Dalil_detial_view(request,id):
    q=0
    query =request.GET.get("search")
    Companylist = Company.objects.all()
    try:
        thecompanysection=CompanySection.objects.get(id=id)
    except :
        messages.warning(request,'حدث خطأ')
    types=CompanyType.objects.filter(section=thecompanysection)
    if query:
        types=types.filter(company_type_title__icontains=query)
        if not types.last():
            messages.warning(request,'لا يوجد نتيجة لبحثكم')
            q=1
    try:
        companysection=CompanySection.objects.get(id=id)
    except :
        messages.warning(request,'حدث خطأ')
    context = {
        'q':q,
        'query':query,
        'CompanySection':companysection,
        'CompanyType':types,
    }
    return render(request,'dalil/dalil_detail_view.html',context)

def dalil_detail_detail_view(request,id,pk):
    q=0
    query =request.GET.get("search")
    try:
        thetype=CompanyType.objects.get(id=pk)
    except :
        messages.warning(request,'حدث خطأ')
    companys=Company.objects.filter(type=thetype)
    if query:
        companys=companys.filter(company_title__icontains=query)
        if not companys.last():
            messages.warning(request,'لا يوجد نتيجة لبحثكم')
            q=1
    context={
        'q':q,
        'query':query,
        'companys':companys,
        'thetype':thetype,

    }
    return render(request,'dalil/dalil_detail_detail_view.html',context)


#------------------------------------------------- Response Section  --------------------------------------------------
def Response_view(request,id):
    exactquestion=0
    exactresponse=0
    a=0#if the user is a real user should put the right special code if the verification of the code success so a=1 when a=1 the question show and if its a response the response show with extra file if its available
    theresponsefile=0
    responseform=ResponseForm()
    if request.method == 'POST':
        responseform = ResponseForm(request.POST or None)   
        specialcode = request.POST.get('special_code')
        try:
            exactquestion=Question.objects.get(id=id)
        except :
            messages.warning(request,' الرابط خطأ ')

        if responseform.is_valid():
            if exactquestion.specialcode==specialcode:
                a=1
                try:
                    exactresponse=Response.objects.get(response_question = exactquestion)
                    theresponsefile=ResponseFile.objects.filter(response_response=exactquestion)
                except Response.DoesNotExist:
                    messages.warning(request, 'الإجابة غير متوفرة فور جهوزها سيتم التواصل معك عبر البريد الالكتروني')
                responseform=ResponseForm()
            else:
                messages.warning(request,'رجاء استخدم الكود المناسب للرابط المرسل اليك')
  
    context={
        'Question': exactquestion,
        'ResponseForm':responseform,
        'a':a,
        'Response':exactresponse,
        'theresponsefile':theresponsefile
    }
    return render(request,'response_view.html',context)

def page_not_found(request,exception):
    messages.warning(request,'Page not found ,الصفحة غير موجودة')
    context={}
    return render(request,'error/404.html',context)

def server_error(reqeust):
    messages.warning(request,'Server error ,خلل في الخادم')
    context={}
    return render(request,'error/500.html',context)

def permission_denied(reqeust,exception):
    messages.warning(request,'Permission denied ,طلب الاذن مرفوض')
    context={}
    return render(request,'error/403.html',context)

def bad_request(reqeust,exception):
    messages.warning(request,'Bad request ,خطأ في الطلب')
    context={}
    return render(request,'error/400.html',context)
