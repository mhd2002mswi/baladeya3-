from django import forms
from website.models import( 
    NewsDecisions, NewsFileDecisions,NewsProjects,NewsActivity,NewsFileProjects,NewsFileActivity,
    QuestionType, Question, Response, ResponseFile, 
    Email,
    Transactions ,
    RentalValue,RentalValueBill,
    Maalem,MaalemImage,
    CompanyType,Company,CompanySection
    )

#response_form
class ResponseForm(forms.ModelForm):
    class Meta():
        model=Response
        fields=[
            'response_title',
            'response_description',
            'response_principal_image',
            'response_question',
        ]
        widgets = {
            'response_question': forms.Select(attrs={"class": "custom-select my-1 mr-sm-2", "id": "inlineFormCustomSelectPref"}),
        }
#response_file_form
class ResponseFileForm(forms.ModelForm):
    class Meta():
        model=ResponseFile
        fields=[
            'response_image',
            'response_file',
            'response_response',
        ]
    
#question_form(for the question madet by the client and want to be updated by the municipality member)
class QuestionForm1(forms.ModelForm):
    class Meta():
        model=Question
        fields=[
  
            'Question_show',    
        ]  
#question_form(regular)
class QuestionForm(forms.ModelForm):
    class Meta():
        model=Question
        fields=[
            'Question_title',
            'Question_text',
            'Question_type',    
            'Question_show',    
        ]  


#company_type_form
class ConpanyTypeForm(forms.ModelForm):
    class Meta():
        model=CompanyType
        fields=[
            'company_type_title',
            'section',
        ]
#company_form
class ConpanyForm(forms.ModelForm):
    class Meta():
        model=Company
        fields=[
            'company_title',
            'company_location',
            'company_tell',
            'type',
        ]

#activity_form
class ActivityForm(forms.ModelForm):

    class Meta():
        model=NewsActivity
        fields=[
            'news_title',
            'news_description',
            'news_principale_image',
            'news_date',
        ]
#activity_file_form
class ActivityFileForm(forms.ModelForm):
    class Meta():
        model=NewsFileActivity
        fields = [
            'news_file',
            'news_image',
            'relation',
            'id',
        ]

#decision_form      
class DecisionsForm(forms.ModelForm):
    class Meta():
        model=NewsDecisions
        fields=[
            'news_title',
            'news_description',
            'news_principale_image',
            'news_date',
        ]
#decision_file_form
class DecisionsFileForm(forms.ModelForm):
    class Meta():
        model=NewsFileDecisions
        fields = [
            'news_file',
            'news_image',
            'relation',
            'id',
        ]

#project_form        
class ProjectsForm(forms.ModelForm):
    class Meta():
        model=NewsProjects
        fields=[
            'news_title',
            'news_description',
            'news_principale_image',
            'news_projects_finish',
            'news_date',
        ]
#project_file_form
class ProjectsFileForm(forms.ModelForm):
    class Meta():
        model=NewsFileProjects
        fields = [
            'news_file',
            'news_image',
            'relation',
            'id',
        ]

#maalem_form        
class MaalemForm(forms.ModelForm):
    class Meta():
        model=Maalem
        fields = [
            'maalem_title',
            'maalem_descriptions',
            'maalem_principal_image',
            'maalem_loaction',
            'id',
        ]
#maalem_file_form        
class MaalemFileForm(forms.ModelForm):
    class Meta():
        model=MaalemImage
        fields = [
            'maalem_image_image',
            'maalem_image_maalem',
            'id',
        ]

#transaction_form        
class TransactionForm(forms.ModelForm):

    class Meta():
        model=Transactions
        fields = [
            'transactions_title',
            'transactions_descriptions',
            'transactions_file',
        ]
        
