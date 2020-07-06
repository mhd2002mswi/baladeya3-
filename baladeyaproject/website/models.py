#All import
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
import random

#------------------------------------------------------------------------------- News Section

#Decision_Model 
class NewsDecisions(models.Model):
    news_title=                     models.CharField(max_length=128)                                                                            
    news_description=               models.TextField()
    news_principale_image=          models.ImageField(upload_to='News/Decision/Principal/Image/')
    news_date=                      models.DateTimeField(default=datetime.now,blank=True,null=True)
    madetby=models.ForeignKey(settings.AUTH_USER_MODEL ,blank=True,null=True,on_delete=models.CASCADE,related_name='decision')

    def __str__(self):#return the title of object when i call the object
        return self.news_title

    def delete(self, *args,**kwargs):#delete the file from the directory
        self.news_principale_image.delete()        
        super().delete(*args, **kwargs)
#Decision_File_Model      
class NewsFileDecisions(models.Model):
    news_file=                      models.FileField(upload_to='News/Decision/Second/File/',blank=True,null=True)
    news_image=                     models.ImageField(upload_to='News/Decision/Second/Image/',blank=True,null=True)
    relation=                      models.ForeignKey(NewsDecisions,on_delete=models.CASCADE,related_name='decisionfile',blank=True, null=True)
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.news_file.delete()
        self.news_image.delete()        
        super().delete(*args, **kwargs)


#Activity_Model
class NewsActivity(models.Model):
    news_title=                     models.CharField(max_length=128)
    news_description=               models.TextField()
    news_principale_image=          models.ImageField(upload_to='News/Activity/Principal/Image/')
    news_date=                      models.DateTimeField(default=datetime.now,blank=True,null=True)
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='activity')

    def __str__(self):#return the title of object when i call the object
        return self.news_title

    def delete(self, *args,**kwargs):#delete the file from the directory
        self.news_principale_image.delete()
        super().delete(*args, **kwargs)     
#Activity_File_model
class NewsFileActivity(models.Model):
    news_file=                      models.FileField(upload_to='News/Activity/Second/File/',blank=True,null=True)
    news_image=                     models.ImageField(upload_to='News/Activity/Second/Image/',blank=True,null=True)
    relation=                       models.ForeignKey(NewsActivity,on_delete=models.CASCADE,related_name='activityfile',blank=True, null=True)
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.news_file.delete()
        self.news_image.delete()
        super().delete(*args, **kwargs)
    

#Project_Model
class NewsProjects(models.Model):
    news_title=                     models.CharField(max_length=128)
    news_description=               models.TextField()
    news_principale_image=          models.ImageField(upload_to='News/Projects/Principal/Image/')
    news_date=                      models.DateTimeField(default=datetime.now,blank=True,null=True)
    news_projects_finish=          models.BooleanField()
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='projects')
    def __str__(self):#return the title of object when i call the object
        return self.news_title
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.news_principale_image.delete()
        super().delete(*args, **kwargs)
#Project_File_Model
class NewsFileProjects(models.Model):
    news_file=                      models.FileField(upload_to='News/Projects/Second/File/',blank=True,null=True)
    news_image=                     models.ImageField(upload_to='News/Projects/Second/File/',blank=True,null=True)
    relation=                       models.ForeignKey(NewsProjects,on_delete=models.CASCADE,related_name='projectfile',blank=True, null=True)
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.news_file.delete()
        self.news_image.delete()
        super().delete(*args, **kwargs)

#------------------------------------------------------------------------------- Contact Us Section

#Question_Type_Model
class QuestionType(models.Model):
    Question_type = models.CharField(max_length=128, blank=True, null=True)
    
    def __str__(self):#return the title of object when i call the object
        return self.Question_type
#Question_Model
class Question(models.Model):
    Question_full_name =            models.CharField(max_length=128, blank=True, null=True)
    Question_email =                models.EmailField(blank=True, null=True)
    Question_phone =                models.CharField(max_length=15, blank=True, null=True)
    Question_title =                models.CharField(max_length=128, blank=True, null=True)
    Question_text =                 models.TextField(blank=True, null=True)
    Question_principal_image =      models.ImageField(upload_to='Contactus/Question/Principal/Image/', blank=True, null=True)
    Question_date =                 models.DateTimeField(blank=True, null=True, default=datetime.now)
    Question_type =                 models.ForeignKey(QuestionType, on_delete=models.CASCADE,  blank=True, null=True,related_name='question')
    Question_show =                 models.BooleanField(default=False)
    specialcode=                    models.CharField(max_length=20,null=True, blank=True)  
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='question')
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.Question_principal_image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):#return the title of object when i call the object
        return self.Question_title
    def save(self, *args, **kwargs):
        self.specialcode = random.randint(1000,9999)
        super(Question, self).save(*args, **kwargs) 


#Response_Model
class Response(models.Model):
    response_question =              models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, related_name='response')
    response_title =                models.CharField(max_length=128, blank=True, null=True)
    response_description =          models.TextField()
    response_date =                 models.DateTimeField(default=datetime.now, blank=True, null=True)
    response_principal_image =      models.ImageField(upload_to='Contactus/Response/Principal/Image', blank=True, null=True)
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='response')
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.response_principal_image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):#return the title of object when i call the object
        return self.response_title
#Response_File_Model
class ResponseFile(models.Model):
    response_image =                models.ImageField(upload_to='Contactus/Response/Second/Image/', blank=True, null=True)
    response_file =                 models.FileField(upload_to='Contactus/Response/Second/File/', blank=True, null=True)
    response_response =             models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, related_name='file')
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.response_image.delete()
        self.response_file.delete()
        super().delete(*args, **kwargs)



#------------------------------------------------------------------------------- Dalil Section

#Company_Section_Model
class CompanySection(models.Model):
    company_section_title =         models.CharField(max_length=128)
    company_section_date =                 models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):#return the title of object when i call the object
        return self.company_section_title
#Company_Type_Model
class CompanyType(models.Model):
    company_type_title =            models.CharField(max_length=128)
    section =                       models.ForeignKey(CompanySection,  on_delete=models.CASCADE, null=True, blank=True,related_name='type')
    company_type_date =                 models.DateTimeField(default=datetime.now, blank=True, null=True)
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='companytype')

    def __str__(self):#return the title of object when i call the object
        return self.company_type_title
#Company_Model
class Company(models.Model):
    company_title =                 models.CharField(max_length=128)
    company_location =              models.CharField(max_length=200, default='municipality location')
    company_tell =                  models.CharField(max_length=128, blank=True, null=True)
    type =                          models.ForeignKey(CompanyType,  on_delete=models.CASCADE, null=True, blank=True,related_name='company')
    company_date =                 models.DateTimeField(default=datetime.now, blank=True, null=True)
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='company')

    def __str__(self):#return the title of object when i call the object
        return self.company_title

#------------------------------------------------------------------------------- Other Model Section

#Email_Model
class Email(models.Model):
    email =                         models.EmailField()
    timestamp =                     models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date =                 models.DateTimeField(default=datetime.now,blank=True,null=True)

    def __str__(self):#return the title of object when i call the object
        return self.email


#Transaction_Model
class Transactions(models.Model):
    transactions_title =            models.CharField(max_length=200)
    transactions_descriptions =     models.TextField(blank=True, null=True)
    transactions_file =             models.FileField(upload_to='Transactions/Principal/')
    transaction_date =                 models.DateTimeField(default=datetime.now, blank=True, null=True)
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='transaction')
    def __str__(self):#return the title of object when i call the object
        return self.transactions_title
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.transactions_file.delete()
        super().delete(*args, **kwargs)


#RentalValue_Model
class RentalValue(models.Model):
    rental_value_realty_number =    models.CharField(max_length=10, null=True,blank=True)
    rental_value_block_number =     models.CharField(max_length=10, null=True,blank=True)
    rental_vlaue_section =          models.CharField(max_length=10, null=True,blank=True)
    rental_value_additional_code =  models.CharField(max_length=100, null=True,blank=True)
    rental_value_total =            models.CharField(max_length=10, null=True,blank=True)

    def __str__(self):#return the title of object when i call the object
        return self.rental_value_realty_number
#RentalValueBill_Model
class RentalValueBill(models.Model):
    rental_value_bill_rental_value= models.ForeignKey(RentalValue,  on_delete=models.CASCADE,related_name='bill',null=True, blank=True)
    rental_value_bill_date =        models.DateField()
    rental_value_bill_value =       models.CharField(max_length=20)


#Maalem_Model
class Maalem(models.Model):
    maalem_title =                  models.CharField(max_length=50)
    maalem_descriptions =           models.TextField()
    maalem_principal_image =        models.ImageField(upload_to='Maalem/Principal/')
    maalem_loaction =               models.CharField(max_length=128, default='haret hreik')
    maalem_date =                 models.DateTimeField(default=datetime.now, blank=True, null=True)
    madetby=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='maalem')
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.maalem_principal_image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):#return the title of object when i call the object
        return self.maalem_title
#Mallem_File(Image)_Model
class MaalemImage(models.Model):
    maalem_image_maalem =           models.ForeignKey(Maalem,  on_delete=models.CASCADE,related_name='image',blank=True, null=True)
    maalem_image_image =            models.ImageField(upload_to='Maalem/Second/')
    def delete(self, *args,**kwargs):#delete the file from the directory
        self.maalem_image_image.delete()
        super().delete(*args, **kwargs)
