from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['text']
    list_display = ('text', 'date')
    list_filter = ['date']
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
