# Class Based View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.views.generic.base import TemplateView,TemplateResponseMixin,ContextMixin
from django.template.loader import render_to_string
#for email
from baladeyaproject.settings import MUNICIPALITY_NAME,EMAIL_HOST_USER

#Form
from .forms import (
    QuestionForm,
    QuestionForm1,
    ResponseForm,ResponseFileForm,ConpanyTypeForm,
    ConpanyForm,ActivityForm,ActivityFileForm,DecisionsFileForm,
    DecisionsForm,ProjectsFileForm,ProjectsForm,MaalemForm,MaalemFileForm ,
    TransactionForm
    )
#Formset
from django.forms import formset_factory,modelformset_factory,inlineformset_factory
#Email
from django.core.mail import send_mail
#django Function Based view
from django.urls import reverse
from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect,
                              redirect)
# THe user stuf
from django.contrib.auth.decorators import login_required
from django.contrib import  auth
from django.contrib.auth.models import User
#Models
from website.models import ( 
    NewsDecisions, NewsFileDecisions,NewsProjects,NewsActivity,NewsFileProjects,NewsFileActivity,
    QuestionType, Question, Response, ResponseFile, 
    Email,
    Transactions ,
    RentalValue,RentalValueBill,
    Maalem,MaalemImage,
    CompanyType,Company,CompanySection
    )
#Other
from django.contrib import messages
from django.utils.decorators import method_decorator
#______________________________________________ Authonticate _____________________________________________________________________

#the login view
def login_view(request):
    if request.method =='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            messages.success(request,f'Login by {request.user} success ,welcome , for any help contact us (mmcoding)')
            return redirect('adminhome')
        else:
            messages.warning(request,'Login faild wrong username or password')
            return render(request,'admin/authonticate/login.html',{'error':'Hey Somthing is wrong'})
    else:
        return render(request,'admin/authonticate/login.html')

#just logout methode for logout the user and direct him tho the login view
def logout(request):
    if request.method == 'POST':
        user=request.user
        auth.logout(request)
        messages.success(request,f'Logout by {user} success')
        return redirect('adminhome')

#for the class based view inhert this class to be able to (force login befor to enter to the page)
class LoginRequeiredMixin(object):
    @classmethod
    def as_view(cls,**kwargs):
        view = super(LoginRequeiredMixin,cls).as_view(**kwargs)
        return login_required(view)

#user activity view (the user can view all the activity,on )
#
#this code can be dowet by another way much better
@login_required            
def user_view(request):
    x=1
    #identify the user
    user=request.user
    #get the name of category and store it in x varible
    x=request.GET.get('category')
    category=0
    if x =='9':#------>activity
        category=user.activity.all()
    elif x=='1':#------>projects
        category=user.projects.all()
    elif x=='2':#------>decision
        category=user.decision.all()
    elif x=='4':#------>question
        category=user.question.all()
    elif x=='5':#------>response
        category=user.response.all()
    elif x=='3':#------>transaction
        category=user.transaction.all()
    elif x=='6':#------>maalem
        category=user.maalem.all()
    elif x=='7':#------>company
        category=user.company.all()
    elif x=='8':#------>company type
        category=user.companytype.all()

    context={
            'category':category,
            'x':x,
            }
    return render(request,'admin/authonticate/activity.html',context)

#______________________________________________ Transactions ____________________________________________________________

#transaction field
transactionsfield=[
    'transactions_title',
    'transactions_descriptions',
    'transactions_file',       
]   
#transaction model
transactionsmodel=Transactions
#transactions_detail_view
class TransactionsDetailView(LoginRequeiredMixin,DetailView):
    model=transactionsmodel
    template_name='admin/Transactions/detail.html'
#transactions_list_view
class TransactionsListView(LoginRequeiredMixin,ListView):
    model=transactionsmodel    
    template_name='admin/Transactions/list.html'
#transactions_create
@login_required
def transaction_create(request):
    createform=TransactionForm()
    if request.method == 'POST':
        createform=TransactionForm(request.POST or None , request.FILES or None)
        if createform.is_valid():
            obj1=createform.save(commit=False)
            obj1.madetby=request.user
            obj1.save()
            messages.success(request,f'create transaction by {request.user} success ')
            return redirect('transactionslist')
        else:
            messages.warning(request, f'create transaction by {request.user} fail , if this problem repeated pleas contact us from the home page')
    context = {
        'form':createform
    }
    return render(request,'admin/transactions/create.html',context)
#transactions_update
@login_required
def transaction_update(request,pk):
    thetransaction=Transactions.objects.get(id=pk)
    updateform=TransactionForm(instance=thetransaction)
    if request.method == 'POST':
        updateform=TransactionForm(request.POST or None , request.FILES or None, instance=thetransaction)
        if updateform.is_valid():
            obj1=updateform.save(commit=False)
            obj1.save()
            messages.success(request,f'Transaction updated by {request.user} Success')
            return redirect('transactionslist')
        else:
            messages.warning(request, f'Update transaction by {request.user} fail , if this problem repeated pleas contact us from the home page')
    context = {
        'form':updateform
    }
    return render(request,'admin/transactions/update.html',context)
#transactions_delete
class TransactionsDeleteView(LoginRequeiredMixin,DeleteView):
    model=transactionsmodel
    template_name=f'admin/Transactions/delete.html'   

    def get_success_url(self):
        messages.success(self.request,f'Delete Transaction by {self.request.user} succes')
        return reverse('transactionslist')

#______________________________________________ Activity ____________________________________________________________

activityfield=[
    'news_title',
    'news_description',
    'news_principale_image',       
]   
activitymodel=NewsActivity
activitytemplate='activity'
activitylist='activitylist'
#activity_detail
@login_required
def activity_detail(request,pk):
    theactivity=NewsActivity.objects.get(id=pk)
    thefileactivity=NewsFileActivity.objects.filter(relation=theactivity)
    context={
        'object':theactivity,
        'extrafile':thefileactivity
    }
    return render(request,'admin/activity/detail.html',context)
#activity_list
class ActivityListView(LoginRequeiredMixin,ListView):
    model=activitymodel
    ordering = ['-news_date']   
    template_name=f'admin/{activitytemplate}/list.html'
#activity_create
@login_required
def activity_create( request):
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0
    createform=ActivityForm()
    createformset=formset_factory(ActivityFileForm,extra=int(x),max_num=6)
    formset=createformset()
    if request.method =="POST":
        createform=ActivityForm(request.POST or None ,request.FILES or None)
        formset=createformset(request.POST or None ,request.FILES or None)

        if createform.is_valid() and formset.is_valid():
            obj1=createform.save(commit=False)
            obj1.madetby=request.user
            obj1.save()
            lastactivity=NewsActivity.objects.last()
            for form in formset:
                obj=form.save(commit=False)
                obj.relation=lastactivity                
                obj.save()
            messages.success(request,f'Activity create by {request.user} success')
            return redirect('activitylist')
        else:
            messages.warning(request, f'Create activity by {request.user} fail , if this problem repeated pleas contact us from the home page')
        
    context={
        'formset':formset,
        'form':createform,
        'x':x
    }
    return render(request,'admin/activity/create.html',context)
#activity_update
@login_required
def activity_update_view(request, pk): 
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0
    theactivity= NewsActivity.objects.get(id=pk)
    activityform = ActivityForm(instance = theactivity) 
    activityfile=NewsFileActivity.objects.filter(relation=theactivity)
    ActivityFormSet=modelformset_factory(
                                        NewsFileActivity,
                                        fields=['relation','news_file','news_image','id'],
                                        extra=int(x),                                       
                                        )
    formset=ActivityFormSet(queryset=activityfile)   
 
    if request.method=="POST":
        activityform = ActivityForm(request.POST or None,request.FILES or None , instance = theactivity) 
        formset=ActivityFormSet(request.POST or None,request.FILES or None)   
        if activityform.is_valid() and formset.is_valid() :                     
            obj1=activityform.save(commit=False)
            obj1.save()
            for form in formset:
                obj = form.save(commit=False)
                obj.relation=theactivity
                obj.madetby=request.user
                obj.save()
            
            messages.success(request,f'Activity Update by {request.user} success')
            return redirect('activitylist')
        else:
            messages.warning(request, f'Update activity by {request.user} fail , if this problem repeated pleas contact us from the home page')

    
    context={
        'object':theactivity,
        'form':activityform,
        'formset':formset,
        'x':x
    }
    return render(request, "admin/activity/update.html", context) 
#activity_delete
@login_required
def activity_delete(request,pk):
    theactivity=NewsActivity.objects.get(id=pk)
    thefielactivity=theactivity.activityfile.all()
    if request.method =='POST':
        for file in thefielactivity:
            file.delete()
        theactivity.delete()
        messages.success(request,f'activity delete by {request.user} success')
        return redirect('activitylist')
    context = {
        'object':theactivity
    }
    return render(request,'admin/activity/delete.html',context)
#______________________________________________ Company ____________________________________________________________

#company_list
@login_required
def company_list_view(request,pks,pk):
    thesection=CompanySection.objects.get(id=pks)
    thetype=CompanyType.objects.get(id=pk)
    companys=Company.objects.filter(type=thetype)
    context = {
        'thesection':thesection,
        'thetype':thetype,
        'companys':companys,
    }
    return render(request,'admin/company/list.html',context)

#company_detail
@login_required
def company_detail(request, pks,pkc,pk):
    thecompany=Company.objects.get(id=pkc)
    context = {
        'thecompany':thecompany,
    }
    return render(request,'admin/company/detail.html',context)
    
#company_create
@login_required
def company_create(request,pks,pk):
    thecompanyform=ConpanyForm()
    thetype=CompanyType.objects.get(id=pk)
    if request.method=="POST":
        thecompanyform=ConpanyForm(request.POST or None)
        if thecompanyform.is_valid():
            obj=thecompanyform.save(commit=False)
            obj.type=thetype
            obj.madetby=request.user
            obj.save()
            messages.success(request,f'Company create by {request.user} success')
            return HttpResponseRedirect('../')
            
        else:
            messages.warning(request, f'Create Company by {request.user} fail , if this problem repeated pleas contact us from the home page')
    context = {
        'thetype':thetype,
        'thecompanyform':thecompanyform,
        'pk':pk,
    }
    return render(request, 'admin/company/create.html', context)

#company_update
@login_required
def company_update(request,pks,pk,pkc):
    thecompanytype=CompanyType.objects.get(id=pk)
    thecompany=Company.objects.get(id=pkc)    
    updatecompany=ConpanyForm(instance=thecompany)
    if request.method =="POST":
        updatecompany=ConpanyForm(request.POST or None,instance=thecompany)
        if updatecompany.is_valid():
            obj = updatecompany.save(commit=False)
            obj.type = thecompanytype
            obj.save()
            messages.success(request,f'Company Update by {request.user} success')
            return HttpResponseRedirect('../../')
        else:
            messages.warning(request, f'Update Company by {request.user} fail , if this problem repeated pleas contact us from the home page')

    context = {
        'updatecompany':updatecompany,
        'thecompanytype':thecompanytype,
        'object':thecompany,
    }
    
    return render(request, 'admin/company/update.html', context)

#company_delete
@login_required
def company_delete(request,pk,pks,pkc):
    thecompany=Company.objects.get(id=pkc)    
    if request.method =='POST':
        thecompany.delete()
        messages.success(request,f'company delete by {request.user} success')
        return HttpResponseRedirect('../../')
    
    context={
        'thecompany':thecompany
    }
    return render(request,'admin/company/delete.html',context)


#______________________________________________ Company Type ____________________________________________________________

companytypefield=[
    'company_secion_title',
    'section',
]   
companytypemodel=CompanyType
companytypetemplate='company/type'
companytypelist='companytypelist'

#company_type_list
class CompanyTypeListView(LoginRequeiredMixin,ListView):
    model=companytypemodel
    template_name=f'admin/{companytypetemplate}/list.html'

#company_type_detail
class CompanyTypeDetailView(LoginRequeiredMixin,DetailView):
    model=companytypemodel
    template_name=f'admin/{companytypetemplate}/detail.html'

#company_type_create
@login_required
def company_type_create(request,pks):
    createform=ConpanyTypeForm()
    thesection=CompanySection.objects.get(id=pks)

    if request.method=="POST":
        createform=ConpanyTypeForm(request.POST or None)
        if createform.is_valid():
            obj=createform.save(commit=False)
            obj.section=thesection
            obj.madetby=request.user
            obj.save()
            messages.success(request,f'Compnay Type Create by {request.user} success')
            return HttpResponseRedirect('../')
        else:
            messages.warning(request, f'Create Company Type by {request.user} fail , if this problem repeated pleas contact us from the home page')

    context={
        'createform':createform,
    }
    return render(request,'admin/company/type/create.html',context)

#company_type_update
@login_required
def company_type_update(request,pks,pk):
    thecompanytype=CompanyType.objects.get(id=pk)
    thesection=CompanySection.objects.get(id=pks)    
    updatecompanytype=ConpanyTypeForm(instance=thecompanytype)
    if request.method =="POST":
        updatecompanytype=ConpanyTypeForm(request.POST or None,instance=thecompanytype)
        if updatecompanytype.is_valid():
            obj = updatecompanytype.save(commit=False)
            obj.section=thesection
            obj.save()
            messages.success(request,f'Company Type update by {request.user} success')
            return HttpResponseRedirect('../../')
            messages.success(request,'conpany type updated')
    context = {
        'updatecompanytype':updatecompanytype,
        'object':thecompanytype,
    }
    
    return render(request, 'admin/company/type/update.html', context)
        
#company_type_delete
@login_required
def company_type_delete(request,pk,pks):
    thecompanytype=CompanyType.objects.get(id=pk)
    if request.method =='POST':
        thecompanytype.delete()
        messages.success(request,f'Company Type Delete by {request.user} success')
        return HttpResponseRedirect('../../')
    context={
        'thecompanytype':thecompanytype
    }
    return render(request,'admin/company/type/delete.html',context)


#______________________________________________ Company Section ____________________________________________________________

companysectionfield=[
    'company_section_title',
      
]   
companysectionmodel=CompanySection
companysectiontemplate='company/section'
companysectionlist='companysectionlist'

#company_secion_list
class CompanySectionListView(LoginRequeiredMixin,ListView):
    model=companysectionmodel
    template_name=f'admin/{companysectiontemplate}/list.html'

#company_secion_detail
@login_required
def company_section_detail(request,pks):
    thesection=CompanySection.objects.get(id=pks)
    types=CompanyType.objects.filter(section=thesection)
    context = {
        'object':thesection,
        'types':types,
    }
    return render(request, 'admin/company/section/detail.html', context)

#company_secion_create
class CompanySectionCreateView(LoginRequeiredMixin,CreateView):
    model=companysectionmodel
    fields=companysectionfield
    def get_success_url(self):
        messages.success(self.request,f'Company Section Create by {self.request.user} success')
        return reverse(companysectionlist)
    template_name=f'admin/{companysectiontemplate}/create.html'

#company_secion_update
class CompanySectionUpdateView(LoginRequeiredMixin,UpdateView):
    model=companysectionmodel
    fields=companysectionfield
    def get_success_url(self):
        messages.success(self.request,f'Company Section update by {self.request.user}')
        return reverse(companysectionlist)
    template_name=f'admin/{companysectiontemplate}/update.html'

#company_secion_delete
class CompanySectionDeleteView(LoginRequeiredMixin,DeleteView):
    model=companysectionmodel
    template_name=f'admin/{companysectiontemplate}/delete.html'
    def get_success_url(self):
        messages.success(self.request,f'Company Section delete by {self.request.user} success')
        return reverse(companysectionlist)


#_________________________________________________ newsDecisions _____________________________________________________________________

newsdecisionsfield=[
    'news_title',
    'news_description',
    'news_principale_image',


]   
newsdecisionsmodel=NewsDecisions
newsdecisionstemplate='decisions'
newsdecisionslist='decisionslist'

#decision_list
class NewsDecisionsListView(LoginRequeiredMixin,ListView):
    model=newsdecisionsmodel
    ordering = ['-news_date']
    template_name=f'admin/{newsdecisionstemplate}/list.html'

#decision_detail
@login_required
def decisions_detail(request,pk):
    thedecisions=NewsDecisions.objects.get(id=pk)
    thefiledecisions=NewsFileDecisions.objects.filter(relation=thedecisions)
    context={
        'object':thedecisions,
        'extrafile':thefiledecisions
    }
    return render(request,'admin/decisions/detail.html',context)

#decision_create
@login_required
def decisions_create( request):
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0
    createform=DecisionsForm()
    createformset=formset_factory(DecisionsFileForm,extra=int(x),max_num=6)
    formset=createformset()
    if request.method =="POST":
        createform=DecisionsForm(request.POST or None ,request.FILES or None)
        formset=createformset(request.POST or None ,request.FILES or None)

        if createform.is_valid() and formset.is_valid():
            obj1=createform.save()
            obj1.madetby=request.user
            obj1.save()
            lastdecisions=NewsDecisions.objects.last()
            for form in formset:
                obj=form.save(commit=False)
                obj.relation=lastdecisions
                obj.save()
            messages.success(request,f'Decision create by {request.user} success')
            return redirect('decisionslist')
        else:
            messages.warning(request, f'Create Decision by {request.user} fail , if this problem repeated pleas contact us from the home page')
        
    context={
        'formset':formset,
        'form':createform,
        'x':x
    }
    return render(request,'admin/decisions/create.html',context)
#decision_update
@login_required
def decisions_update_view(request, pk): 
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0

    thedecisions= NewsDecisions.objects.get(id=pk)
    decisionsform = DecisionsForm(instance = thedecisions) 
    decisionsfile=NewsFileDecisions.objects.filter(relation=thedecisions)
    DecisionsFormSet=modelformset_factory(
                                        NewsFileDecisions,
                                        fields=['relation','news_file','news_image','id'],
                                        extra=int(x),                                    
                                        )
    formset=DecisionsFormSet(queryset=decisionsfile)   
 
    if request.method=="POST":
        decisionsform = DecisionsForm(request.POST or None,request.FILES or None , instance = thedecisions) 
        formset=DecisionsFormSet(request.POST or None,request.FILES or None)   
        if decisionsform.is_valid() and formset.is_valid() :                     
            obj1=decisionsform.save()
            obj1.save()
            for form in formset:
                obj = form.save(commit=False)
                obj.relation=thedecisions
                obj.save()
            
            messages.success(request,f'Decision Update by {request.user} success ')
            return redirect('decisionslist')
        else:
            messages.warning(request, f'Create Company Type by {request.user} fail , if this problem repeated pleas contact us from the home page')

    
    context={
        'object':thedecisions,
        'form':decisionsform,
        'formset':formset,
        'x':x
    }
    return render(request, "admin/decisions/update.html", context) 
#decision_delete
@login_required
def decision_delete(request,pk):
    thedecision=NewsDecisions.objects.get(id=pk)
    thefieldecision=thedecision.decisionfile.all()
    if request.method =='POST':
        for file in thefieldecision:
            file.delete()
        thedecision.delete()
        messages.success(request,f'decision delete by {request.user} success')
        return redirect('decisionslist')
    context = {
        'object':thedecision
    }
    return render(request,'admin/decisions/delete.html',context)
#_________________________________________________ Maalem _____________________________________________________________________

maalemfield=[
    'maalem_title',
    'maalem_descriptions',
    'maalem_principal_image',
    'maalem_loaction',
      
]   
maalemmodel=Maalem
maalemtemplate='maalem'
maalemlist='maalemlist'

#maalem_list
class MaalemListView(LoginRequeiredMixin,ListView):
    model=maalemmodel
    ordering = ['-maalem_date']
    template_name=f'admin/{maalemtemplate}/list.html'

#maalem_detail
@login_required
def maalem_detail(request,pk):
    themaalem=Maalem.objects.get(id=pk)
    thefilemaalem=MaalemImage.objects.filter(maalem_image_maalem=themaalem)
    context={
        'object':themaalem,
        'extrafile':thefilemaalem
    }
    return render(request,'admin/maalem/detail.html',context)
#maalem_Create
@login_required
def maalem_create( request):
    
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0
    createform=MaalemForm()
    createformset=formset_factory(MaalemFileForm,extra=int(x),max_num=6)
    formset=createformset()
    if request.method =="POST":
        createform=MaalemForm(request.POST or None ,request.FILES or None)
        formset=createformset(request.POST or None ,request.FILES or None)

        if createform.is_valid() and formset.is_valid():
            obj1=createform.save(commit=False)
            obj1.madetby=request.user
            obj1.save()
            
            lastmaalem=Maalem.objects.last()
            for form in formset:
                obj=form.save(commit=False)
                obj.maalem_image_maalem=lastmaalem
                obj.save()
            messages.success(request,f'Create maalem by {request.user} success')
            return redirect('maalemlist')
        else:
            messages.warning(request, f'Create Maalem by {request.user} fail , if this problem repeated pleas contact us from the home page')

        
    context={
        'x':x,
        'formset':formset,
        'form':createform
    }
    return render(request,'admin/maalem/create.html',context)
#maalem_update
@login_required
def maalem_update_view(request, pk): 
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0

    themaalem= Maalem.objects.get(id=pk)
    maalemform = MaalemForm(instance = themaalem) 
    maalemfile=MaalemImage.objects.filter(maalem_image_maalem=themaalem)
    MaalemFormSet=modelformset_factory(
                                        MaalemImage,
                                        fields=[            'maalem_image_image','maalem_image_maalem','id',],
                                        extra=int(x),                                        
                                        )
    formset=MaalemFormSet(queryset=maalemfile)   
  
    if request.method=="POST":
        maalemform = MaalemForm(request.POST or None,request.FILES or None , instance = themaalem) 
        formset=MaalemFormSet(request.POST or None,request.FILES or None)   
        if maalemform.is_valid() and formset.is_valid() :                     
            obj1=maalemform.save(commit=False)
            obj1.save()

            for form in formset:
                obj = form.save(commit=False)
                obj.maalem_image_maalem=themaalem
                obj.save()
            
            messages.success(request,f'Update maalem by {request.user} success')
            return redirect('maalemlist')
        else:
            messages.warning(request, f'Update Maalem by {request.user} fail , if this problem repeated pleas contact us from the home page')


    
    context={
        'object':themaalem,
        'form':maalemform,
        'formset':formset,
        'x':x
    }
    return render(request,'admin/maalem/update.html',context)

#maalem_delete
@login_required
def maalem_delete(request,pk):
    themaalem=Maalem.objects.get(id=pk)
    themaalemfile=themaalem.image.all()
    if request.method == 'POST':
        for malam in themaalemfile:
            malam.delete()
        themaalem.delete()
        messages.success(request,f'maalem delete by {request.user} success')
        return redirect('maalemlist')
    context={
        'object':themaalem
    }
    return render(request,'admin/maalem/delete.html',context)

#_________________________________________________ Project _____________________________________________________________________

projectsfield=[
    'news_title',
    'news_description',
    'news_principale_image',
    'news_projects_finish',
      
]   
projectsmodel=NewsProjects
projectstemplate='projects'
projectslist='projectslist'

#project_list
class NewsProjectsListView(LoginRequeiredMixin,ListView):
    model=projectsmodel
    ordering = ['-news_date']
    template_name=f'admin/{projectstemplate}/list.html'

#project_detail
@login_required
def projects_detail(request,pk):
    theprojects=NewsProjects.objects.get(id=pk)
    thefileprojects=NewsFileProjects.objects.filter(relation=theprojects)
    context={
        'object':theprojects,
        'extrafile':thefileprojects
    }
    return render(request,'admin/projects/detail.html',context)

#project_Create
@login_required
def projects_create( request):
    
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0
    createform=ProjectsForm()
    createformset=formset_factory(ProjectsFileForm,extra=int(x),max_num=6)
    formset=createformset()
    if request.method =="POST":
        createform=ProjectsForm(request.POST or None ,request.FILES or None)
        formset=createformset(request.POST or None ,request.FILES or None)

        if createform.is_valid() and formset.is_valid():
            obj1=createform.save(commit=False)
            obj1.madetby=request.user
            obj1.save()
            lastprojects=NewsProjects.objects.last()
            for form in formset:
                obj=form.save(commit=False)
                obj.relation=lastprojects
                obj.save()
            messages.success(request,f'Create project by {request.user} success')
            return redirect('projectslist')
        else:
            messages.warning(request, f'Create project by {request.user} fail , if this problem repeated pleas contact us from the home page')

        
    context={
        'x':x,
        'formset':formset,
        'form':createform
    }
    return render(request,'admin/projects/create.html',context)
#project_update
@login_required
def projects_update_view(request, pk): 
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0

    theprojects= NewsProjects.objects.get(id=pk)
    projectsform = ProjectsForm(instance = theprojects) 
    projectsfile=NewsFileProjects.objects.filter(relation=theprojects)
    ProjectsFormSet=modelformset_factory(
                                        NewsFileProjects,
                                        fields=['relation','news_file','news_image','id'],
                                        extra=int(x),
                                        )
    formset=ProjectsFormSet(queryset=projectsfile)   

  
    if request.method=="POST":
        projectsform = ProjectsForm(request.POST or None,request.FILES or None , instance = theprojects) 
        formset=ProjectsFormSet(request.POST or None,request.FILES or None)   
        if projectsform.is_valid() and formset.is_valid() :                     
            obj1=projectsform.save(commit=False)
            obj1.save()
            for form in formset:
                obj = form.save(commit=False)
                obj.relation=theprojects
                obj.save()
            
            messages.success(request,f'Update project by {request.user} success ')
            return redirect('../..')
        else:
            messages.warning(request, f'Update project by {request.user} fail , if this problem repeated pleas contact us from the home page')

    
    context={
        'object':theprojects,
        'form':projectsform,
        'formset':formset,
        'x':x
    }
    return render(request,'admin/projects/update.html',context)
#project_delete
@login_required
def project_delete(request,pk):
    theproject=NewsProjects.objects.get(id=pk)
    theprojectfile=theproject.projectfile.all()
    if request.method == 'POST':
        for projectfile in theprojectfile:
            projectfile.delete()
        theproject.delete()
        messages.success(request,f'project delete by {request.user} success')
        return redirect('projectslist')
    context={
        'object':theproject
    }
    return render(request,'admin/projects/delete.html',context)
#_________________________________________________ Question _____________________________________________________________________

questionfield=[
    'Question_full_name',     
    'Question_email',     
    'Question_phone',     
    'Question_title',     
    'Question_text',     
    'Question_principal_image',     
    'Question_type',     
    'Question_show',     
]   
questionmodel=Question
questiontemplate='question'
questionlist='questionlist'

#question_list_view (show the list of question and separete them if its responded or no , filter the question by type or by respond or by search)
@login_required
def question_list_view(request):
    questionlist=Question.objects.all().order_by('-Question_date')   
    quetiontype=QuestionType.objects.all()
    
    checkbox = 0
    checkbox =request.GET.get("checkbox")
    respondedquestion=0
    if checkbox:
        respondedquestion=1
    selection =request.GET.get("type")
    if selection == '1':
        type=QuestionType.objects.get(Question_type='شكوى')
        questionlist=questionlist.filter(Question_type=type )
    elif selection == '2':
        type=QuestionType.objects.get(Question_type='سؤال')
        questionlist=questionlist.filter(Question_type=type )
    elif selection == '3':
        type=QuestionType.objects.get(Question_type='استفسار')
        questionlist=questionlist.filter(Question_type=type )
    else:
        type=0

    query=0
    query=request.GET.get('search')
    if query:
        questionlist=questionlist.filter(Question_title__icontains=query )
    context={
        'object_list':questionlist,
        'respondedquestion':respondedquestion,
        'query':query,
        'type':selection,
    }
    return render(request,'admin/question/list.html',context)

#question_detail(show the question and the response if its available)  
@login_required
def question_detail_view(request,pk):
    response=0
    responsefile=0
    thequestion= Question.objects.get(pk=pk)   
    try :
        response = get_object_or_404(Response, response_question=thequestion) 
    except :
        messages.warning(request,'no response available')
    try :
        responsefile = ResponseFile.objects.filter( response_response=thequestion) 
    except :
        messages.warning(request,'no response addtional file exist')
    
    context = {
        'object':thequestion,
        'theresponse':response,
        'theresponsefile':responsefile,
        
    }
    return render(request,'admin/question/detail.html',context)

#question_create(here we should edit the question model and add the madit by field)
def question_create_view(request):
    form=QuestionForm()
    if request.method=="POST":
        form=QuestionForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.madetby=request.user
            obj.save()
            messages.success(request,f'Question create by {request.user} success')
            return redirect(questionlist)
        else:
            messages.warning(request, f'Create Question by {request.user} fail , if this problem repeated pleas contact us from the home page')
    context = {
        'form':form
    }
    return render(request,'admin/question/create.html',context)

#question_update (schow Question or no)
@login_required
def question_update(request,pk):
    thequestion=Question.objects.get(id=pk)
    form=QuestionForm1(instance=thequestion)        
    if thequestion.madetby :
        form=QuestionForm(instance=thequestion)    
    if request.method=="POST":
        form=QuestionForm1(request.POST or None,request.FILES or None,instance=thequestion)
        if thequestion.madetby :
            form=QuestionForm(request.POST or None,request.FILES or None,instance=thequestion)
        if form.is_valid():

            obj=form.save(commit=False)
            obj.save()
            messages.success(request,f'Question Update by {request.user} success')
            return redirect(questionlist)
        else:
            messages.warning(request, f'Create Question by {request.user} fail , if this problem repeated pleas contact us from the home page')
    context = {'form':form}
    return render(request,'admin/question/update.html',context)

#question_delete
@login_required
def question_delete(request, pk):
    thequestion=Question.objects.get(id=pk)
    if request.method=='POST':
        if thequestion.madetby:
            thequestion.delete()
            messages.success(request,f'delete question by {request.user} success')
            return redirect('questionlist')
        else:
            messages.warning(request,f'delete question by {request.user} faild because this question is madet by a user,if its neccesary contact us on mm-coding.com or from your home page')
    context={
        'object':thequestion
    }
    return render(request,'admin/question/delete.html',context)
#_________________________________________________ Response _____________________________________________________________________

#response view
@login_required
def response_view(request,pk):
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0
    thequestion= Question.objects.get(pk=pk)
    ResponseFormSet=formset_factory(ResponseFileForm,extra=int(x),max_num=6)
    formset=ResponseFormSet()
    responseform=ResponseForm()

    
    if request.method == 'POST':
        responseform=ResponseForm(request.POST or None,request.FILES or None)
        formset=ResponseFormSet(request.POST or None,request.FILES or None)

        if responseform.is_valid() and formset.is_valid():            
            obj = responseform.save(commit=False)
            obj.response_question=thequestion
            obj.madetby=request.user
            obj.save()
            for form in formset:
                obj = form.save(commit=False)
                obj.response_response=thequestion
                obj.save()
            
            if thequestion.Question_email :
                special_code = thequestion.specialcode
                subject = MUNICIPALITY_NAME
                message = f''
                email_from = EMAIL_HOST_USER
                email_recipient = [thequestion.Question_email,EMAIL_HOST_USER]
                try:
                    send_mail(
                            subject,
                            message,
                            email_from,
                            email_recipient,
                            fail_silently=False,
                            html_message = render_to_string('email/responseemail.html', {'special_code': special_code,'last_question_id':thequestion.id,'date':thequestion.Question_date})
                                )
                    messages.success(request,f'send by {request.user} email success')
                except :
                    messages.warning(request,f'sending by {request.user} email faild')

            messages.success(request,f'The Question is responded by {request.user} success')
            return redirect('questionlist')
        else:
            messages.warning(request, f' The Response by {request.user} fail , if this problem repeated pleas contact us from the home page')        
    
    context={
        'responseform':responseform,
        'formset':formset,
        'object':thequestion,
        'x':x
        
    }
    
    return render(request,'admin/question/response/response.html',context)

#update view
@login_required            
def response_update_view(request, pk): 
    x=0
    x=request.GET.get('extra')
    if not x:
        x=0

    thequestion= Question.objects.get(pk=pk)

    responseformobj = get_object_or_404(Response, response_question=thequestion) 
    responseform = ResponseForm(instance = responseformobj) 
    responsefile=ResponseFile.objects.filter(response_response=thequestion)
    ResponseFormSet=modelformset_factory(
                                        ResponseFile,
                                        fields=['response_image','response_file','response_response','id'],
                                        extra=int(x),
                                        )
    formset=ResponseFormSet(queryset=responsefile)   

    if request.method=="POST":
        responseform = ResponseForm(request.POST or None,request.FILES or None , instance = responseformobj) 
        formset=ResponseFormSet(request.POST or None,request.FILES or None)   

        if responseform.is_valid() and formset.is_valid() :                     
            obj = responseform.save(commit=False)
            obj.response_question=thequestion
            obj.madetby=request.user
            obj.save()
            for form in formset:
                obj = form.save(commit=False)
                obj.response_response=thequestion
                obj.save()
            if thequestion.Question_email :
                special_code = thequestion.specialcode
                subject = MUNICIPALITY_NAME
                message = f''
                email_from = EMAIL_HOST_USER
                email_recipient = [thequestion.Question_email,EMAIL_HOST_USER]
                try:
                    send_mail(
                            subject,
                            message,
                            email_from,
                            email_recipient,
                            fail_silently=False,
                            html_message = render_to_string('email/updateresponseemail.html', {'special_code': special_code,'last_question_id':thequestion.id,'date':thequestion.Question_date})
                                )
                    messages.success(request,f'email send by {request.user} success')
                except :
                    messages.warning(request,f'faild sending email by {request.user}')
            
            messages.success(request,f'Update Response by {request.user} success')
        else:
            messages.warning(request, f'Update Response by {request.user} fail , if this problem repeated pleas contact us from the home page')
        return redirect('questionlist')

    
    context={
        'responseform':responseform,
        'formset':formset,
        'object':thequestion,
        'x':x
    }
    return render(request, "admin/question/response/update.html", context) 


#_________________________________________________ Home _____________________________________________________________________
#home_view
@login_required            
def home_view(request):
    x=0


    allquestion=Question.objects.all()
    for question in allquestion:
        if  question.response.last():
            x=0
        else:
            x=1
            break     
    if  x:
        messages.warning(request,'hey ther you should response on the question !!!')
        
    if request.method =='POST':
        y=request.POST.get('message')
        subject = MUNICIPALITY_NAME
        message = f'the message :{y} User:{request.user}'
        email_from = EMAIL_HOST_USER
        email_recipient = ['mmcoding@gmail.com',EMAIL_HOST_USER]
        try:
            send_mail(
                            subject,
                            message,
                            email_from,
                            email_recipient,
                            fail_silently=False,
                                )
            messages.success(request,'email send success')
        except:
            messages.warning(request,'sending email faild')

      
    return render(request,'admin/home.html',{'x':x,'user':request.user})
#_________________________________________________ user _____________________________________________________________________
