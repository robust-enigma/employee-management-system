from django.contrib import admin
from .models import Employee, Role, Department
# Register your models here.
#To acess admin portal u have to create super user 
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department) 