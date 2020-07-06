
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import( 
    NewsDecisions, NewsFileDecisions,NewsProjects,NewsActivity,NewsFileProjects,NewsFileActivity,
    QuestionType, Question, Response, ResponseFile, 
    Email,
    Transactions ,
    RentalValue,RentalValueBill,
    Maalem,MaalemImage,
    CompanyType,Company,CompanySection
    )

admin.site.site_header='mmcoding admin page'
admin.site.site_title='mmcoding'
admin.site.index_title='baladeya super admin by mmcoding'

#register the rental valure to import and export
@admin.register(RentalValue)
class TestModal(ImportExportModelAdmin):
    pass
#register all models to control the data base
admin.site.register(NewsDecisions)
admin.site.register(NewsFileDecisions)
admin.site.register(NewsActivity)
admin.site.register(NewsProjects)
admin.site.register(NewsFileProjects)
admin.site.register(NewsFileActivity)
admin.site.register(QuestionType)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(ResponseFile)
admin.site.register(Email)
admin.site.register(Transactions)
admin.site.register(RentalValueBill)
admin.site.register(Maalem)
admin.site.register(MaalemImage)
admin.site.register(CompanyType)
admin.site.register(Company)
admin.site.register(CompanySection)
