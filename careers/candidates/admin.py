from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Candidate, CandidateJobMap,Job



class CandidateResource(resources.ModelResource):
    class Meta:
        model=Candidate

class CandidateAdmin(ImportExportModelAdmin):
 
    list_display = ('Name', 'Email_id','Years_of_Experience',)
    list_filter = ('Email_id','Years_of_Experience','Expected_hourly_rate')
    #list_filter = ('Role',)
    

class All_CandidatesAdmin(admin.ModelAdmin):
    list_display=('Name','Email_id','Expected_hourly_rate','Req_Id','status')
    list_editable=('status',)

    
class CandidateInline(admin.TabularInline):
    model = CandidateJobMap
class JobAdmin(admin.ModelAdmin):
    inlines=(CandidateInline,)
    list_display=('Req_Id','Job_title',)


# Register your models here.
admin.site.register(Job,JobAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CandidateJobMap, All_CandidatesAdmin)
