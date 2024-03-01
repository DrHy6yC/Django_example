from django.contrib import admin

from main.models import User, UserQuize, LevelUser, UserAnswer, QuizeAnswer, \
QuizeQuestion, StatusQuize, Constant, QuizeTrueAnswer, Quize, AccesUser


admin.site.register(User)
admin.site.register(UserQuize)
admin.site.register(LevelUser)
admin.site.register(UserAnswer)
admin.site.register(QuizeAnswer)
admin.site.register(QuizeQuestion)
admin.site.register(StatusQuize)
admin.site.register(Constant)
admin.site.register(QuizeTrueAnswer)
admin.site.register(Quize)
admin.site.register(AccesUser)
