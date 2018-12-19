from django.contrib import admin
from api.models import Company, Secretary, Director, Subsidiary


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'security_code', 'country', 'phone',
                    'npwp', 'ipo_date', 'board', 'sector', 'sub_sector')
    search_fields = ('company_name',)
    ordering = ('company_name',)


@admin.register(Secretary)
class SecretaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'company')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'company')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Subsidiary)
class SubsidiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'total_asset', 'percentage', 'company')
    search_fields = ('name',)
    ordering = ('name',)


# end of file
