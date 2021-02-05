from django.contrib import admin
from .models import DocInfo


admin.site.site_header = 'Panel del Administrador'
change_list_template = 'newData.html'


admin.site.register(DocInfo)


# Register your models here.
