from django.contrib import admin
from .models import Poll, Question, Choice

# This inline allows you to add Choices when editing a Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Provides 3 blank slots for new choices

# This is the key part for adding choices to a question.
# It tells the Question's admin page to include the ChoiceInline.
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# --- Inlines for the Poll page ---
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1 # Provides 1 blank slot for a new question

class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'start_date', 'end_date', 'created_by')
    list_filter = ['start_date', 'end_date']
    search_fields = ['title']


# --- Registration ---
admin.site.register(Poll, PollAdmin)

# This line is CRUCIAL. It connects the Question model to its special admin view.
# If this is missing or just says `admin.site.register(Question)`, you won't see the options.
admin.site.register(Question, QuestionAdmin)