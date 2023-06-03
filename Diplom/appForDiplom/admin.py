from django.contrib import admin
from .models import *
# Register your models here.  
admin.site.register(Videos)
admin.site.register(Teacher)
admin.site.register(Lessons)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Test_Question)
admin.site.register(Teacher_Lessons_Test)
admin.site.register(Teacher_Lessons_Video)
admin.site.register(Practice)
admin.site.register(User)
admin.site.register(User_Test)

