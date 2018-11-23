# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    """
    Наследование от admin.StackedInline - выведет формы для добавления в несколько строк, одну за другой
    Наследование от admin.TabularInline - выведет формы для добавления в одну строку, одну за другой
    """
    model = Choice
    # Кол-во форм для добавления новых
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    Структурирование формы администрарования Question
    """
    # Порядок отображения полей на экране деталей Question, в виде блоков строк
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),
        ('Date information', {
            'fields': ['pub_date']
        })
    ]
    # fields = ['pub_date', 'question_text']
    # Добавляем в вывод с привязкой к Question
    inlines = [ChoiceInline]

    # Оформление вывода Question на экране списка всех Question
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Добавляет блок фильтрации вывода по данному полю
    list_filter = ['pub_date']

    # Добавляет блок поиска по указанным полям. Использует LIKE в запросе
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)