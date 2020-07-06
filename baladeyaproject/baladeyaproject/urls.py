
from django.contrib import admin
from django.conf import settings
from django.urls import path, include 
from django.conf.urls import handler404,handler500,handler403,handler400
from django.conf.urls.static import static

from website.views import (
        Home_view,#home_view
        News_view,Project_view, Decisions_view, Activity_view,Decisions_detail_view, Activity_detail_view, Project_detail_view,#news_view 
        Transactions_detail_view,Transactions_view,#transaction_view
        Rental_value_view, #rentalvalue_view
        Maalem_detail_view, Maalem_view,#maalem_view 
        Dalil_view, Dalil_detial_view,dalil_detail_detail_view,#dalil_view
        Response_view,Contactus_view,#contact_us_view
        About_view,#about_view
 )

handler404
urlpatterns = [

    path('admin/', admin.site.urls),#admin interface
    path('adminbaladeya/',include('baladeyaadmin.urls')),#member interface

    path('', Home_view, name='home'),#home_view

    path('news/', News_view, name='news'),#news_view

    path('decisions/', Decisions_view, name='decisions'),#decision_view
    path('decisions/<int:id>/', Decisions_detail_view, name='decisionsdetail'),#decision_detail_view

    path('project/', Project_view, name='project'),#project_view
    path('project/<int:id>/', Project_detail_view, name='projectdetail'),#projcet_detail_view

    path('about/', About_view, name='about'),#about_view

    path('contactus/', Contactus_view, name='contactus'),#contact_view
    path('response/<int:id>/', Response_view, name='response'),#response_view

    path('activity/', Activity_view, name='activity'),#activity_view
    path('activity/<int:id>/', Activity_detail_view, name='activitydetail'),#activity_detail_view

    path('transactions/', Transactions_view, name='transactions'),#transaction_view
    path('transactions/<int:id>/', Transactions_detail_view,name='transactionsdetail'),#transaction_detail_view

    path('rentalvalue/', Rental_value_view, name='rentalvalue'),#rental_value_view

    path('dalil/', Dalil_view, name='dalil'),#dalil_company_section_view
    path('dalil/<int:id>/', Dalil_detial_view, name='dalildetail'),#dalil_company_type_view
    path('dalil/<int:id>/<int:pk>/', dalil_detail_detail_view, name='dalildetaildetail'),#dalil_company_view

    path('maalem/', Maalem_view, name='maalem'),#maalem_view
    path('maalem/<int:id>/', Maalem_detail_view, name='maalemdetail'),#maalem_detail_view

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 ='website.views.page_not_found'
handler403 ='website.views.server_error'
handler400 ='website.views.permission_denied'
handler403 ='website.views.bad_request'
