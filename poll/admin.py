# poll/admin.py

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Poll, Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin view for Questions, allowing inline editing of Choices."""
    list_display = ('question_text', 'poll')
    search_fields = ('question_text', 'poll__title')

    class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 2

    inlines = [ChoiceInline]


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """Admin view for Polls with a direct link to the results page."""

    class QuestionInline(admin.TabularInline):
        model = Question
        extra = 1
        show_change_link = True

    # This tuple DEFINES the columns that appear in the admin list.
    # The string 'view_results_link' MUST match the method name below.
    list_display = (
        'title',
        'start_date',
        'created_by',
        'is_active',
        'view_results_link' # This is the custom column
    )
    
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'created_by__username')
    inlines = [QuestionInline]

    def view_results_link(self, obj):
        """
        This method is called for each poll in the list.
        It generates a safe HTML link to the front-end results page.
        """
        # This uses the name='poll_results' from your poll/urls.py
        url = reverse('poll_results', args=[obj.pk])
        return format_html('<a href="{}" target="_blank">View Results</a>', url)

    # This sets the title for our custom column in the admin header.
    view_results_link.short_description = 'Results Page'