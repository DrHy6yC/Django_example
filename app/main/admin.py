from django.contrib import admin

from main.models import User, UserQuize, UserLevel, UserAnswer, QuizeAnswer, \
QuizeQuestion, QuizeStatus, Constant, QuizeTrueAnswer, Quize, Acces


admin.site.register(User)
admin.site.register(UserQuize)
admin.site.register(UserLevel)
admin.site.register(UserAnswer)
admin.site.register(QuizeAnswer)
admin.site.register(QuizeQuestion)
admin.site.register(QuizeStatus)
admin.site.register(Constant)
admin.site.register(QuizeTrueAnswer)
admin.site.register(Quize)
admin.site.register(Acces)
