from django.contrib import admin

from apps.quizzes.models import Answer, Category, Favorite, Question, Quiz

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Favorite)
