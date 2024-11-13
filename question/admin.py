from django.contrib import admin

from question.models import Question, QuestionLike, Answer, AnswerLike, Profile, Tag


admin.site.register(Question)
admin.site.register(QuestionLike)
admin.site.register(Answer)
admin.site.register(AnswerLike)
admin.site.register(Profile)
admin.site.register(Tag)