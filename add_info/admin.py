# -*- coding: utf-8 -*-
from django.contrib import admin
from add_info.models import Declaration, Company, Judcase, Lawyer, Plea

class DeclarationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Декларации', {'fields': [
            'num_dec',  
            'num_con',    
            'num_ship',    
            'date_coming',    
            'name_goods',    
            'place_point',   
            'date_output',   
            'kts',    
            'notes',
            'comp',
    ]}),
    #    ('', {'fields': ['']}),
    ]
    search_fields = [
            'num_dec',  
            'num_con',
    ]
    list_filter = [
            'num_dec',  
            'num_con',
    ]

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Комании', {'fields': [
            'name',    
            'cheef',   
            'law_adr',   
            'pay_OGRN',    
            'pay_INN',  
            'pay_KPP',    
            'pay_OKPO',    
            'pay_RASCH',   
            'pay_KORR',    
            'pay_BIK',    
            'data_end_cert',
    ]}),
    #    ('', {'fields': ['']}),
    ]

class JudcaseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Судебные дела', {'fields': [
            'dec',
            'type_of_case',
            'reason = models.TextField',
            'data_to_lawyer',
            'data_pay_order',
            'data_jud_sit',
            'num_judmnt',
            'data_judmnt',
            'result_path',
    ]}),
    #    ('', {'fields': ['']}),
    ]

class LawyerAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Юристы', {'fields': [
        'judcase', 
        'num_treaty',
        'data_treary',
        'num_pay',
        'summ_pay',
        'data_pay',
        'num_pay_order',
        'data_pay_order',
        'data_to_lawyer',
        'result_path',
    ]}),
    #   ('', {'fields': ['']}),
    ]

class PleaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Жалобы', {'fields': [
            'dec',
            'reason',
            'inspector',
            'data_of_plea',
            'data_response',
            'notes',
            'result_path',    
    ]}),
    #   ('', {'fields': ['']}),
    ]   
admin.site.register(Declaration, DeclarationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Judcase, JudcaseAdmin)
admin.site.register(Lawyer, LawyerAdmin)
admin.site.register(Plea, PleaAdmin)
# Register your models here.
