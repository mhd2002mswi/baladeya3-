from django import forms
from .models import Question, QuestionType, Email, RentalValue
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


# ------------------------------------------------------ QuestionForm Section ------------------------------------
class QuestionForm(forms.ModelForm):#design the field in this model
    Question_full_name = forms.CharField(
        max_length=60, label='الأسم الثلاثي', required=False,widget=forms.TextInput(attrs={'placeholder': 'الإسم الثلاثي - إختياري ', 'class': 'form-control '}))

    Question_email = forms.EmailField(label='بريدك الألكتروني - إختياري', required=False, widget=forms.EmailInput(
        attrs={'placeholder': 'البريد الألكتروني- إختياري ', 'class': 'form-control '}))

    Question_phone = forms.CharField(
        max_length=15, label=' رقم الهاتف - إختياري', required=False, widget=forms.TextInput(attrs={'placeholder': 'رقم الهاتف - إختياري', 'class': 'form-control '}))

    Question_title = forms.CharField(max_length=100, label='عنوان السؤال', widget=forms.TextInput(attrs={'placeholder': 'عنوان الموضوع  ', 'class': 'form-control '}))

    Question_text = forms.CharField(
        max_length=2500, label='الموضوع', widget=forms.Textarea(attrs={'class': 'form-control ', "id": 'validationTextarea', 'required': '', 'placeholder': 'الموضوع', }))

    Question_principal_image = forms.ImageField(
        label='أرفق صورة - إختياري', required=False, widget=forms.FileInput(attrs={"class": "custom-file-input", "id": "customFile"}))
#add_google_recaptcha to the code
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
        'data-theme': 'dark',
    }))

    class Meta():
        model = Question
#design_the_type_input
        widgets = {
            'Question_type': forms.Select(attrs={"class": "custom-select my-1 mr-sm-2", "id": "inlineFormCustomSelectPref"}),
        }
#select_the_field_on_the_form
        fields = [
            'Question_full_name',
            'Question_email',
            'Question_phone',
            'Question_title',
            'Question_text',
            'Question_principal_image',
            'Question_type',
        ]


# ------------------------------------------------------ EmailForm Section ------------------------------------
# class EmailForm(forms.ModelForm):
#     email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
#                              'name': 'emailsubsicribe', 'type': 'text', 'class': "form-control ", "placeholder": "بريدك الألكتروني", 'style': 'width=100%'}))
#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
#         'data-theme': 'dark',
#     }))

#     class Meta():
#         model = Email
#         fields = ['email']


# ------------------------------------------------------ RentalValue Section ------------------------------------
class RentalValueForm(forms.ModelForm):#design each field on the form
    rental_value_realty_number = forms.CharField(required=False,max_length=6, widget=forms.TextInput(
        attrs={'name': 'realtynumber', 'class': 'form-control m-1', 'placeholder': '  العقار'}))
    rental_vlaue_section = forms.CharField(required=False,max_length=2, widget=forms.TextInput(
        attrs={'name': 'sectonnumber', 'class': 'form-control m-1', 'placeholder': 'القسم'}))
    rental_value_block_number = forms.CharField(required=False,max_length=2, widget=forms.TextInput(
        attrs={'name': 'blocknumber', 'class': 'form-control m-1', 'placeholder': 'البلوك'}))
    rental_value_additional_code = forms.CharField(required=False,max_length=20,widget=forms.TextInput(
        attrs={'name': 'additionalcode', 'class' :'form-control m-1', 'placeholder':'Your IQ'},
    ))
    #add_google_recaptcha_to_the_form
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
        'data-theme': 'dark',
    }))    

    class Meta():
        model = RentalValue
        #form_field
        fields = [
            'rental_value_realty_number',
            'rental_value_block_number',
            'rental_vlaue_section',
            'rental_value_additional_code'
        ]


# ------------------------------------------------------ Response Section ------------------------------------
class ResponseForm(forms.Form):
    special_code = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={ 'class': 'form-control m-1', 'placeholder': '  الكود'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
        'data-theme': 'dark',
        'class': 'mx-auto',
    }))