from django.contrib import admin

from .models import Inquirer, Questions,Answers, UserAnswers, UserInquirer

# Register your models here.

admin.site.register(Inquirer)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(UserAnswers)
admin.site.register(UserInquirer)