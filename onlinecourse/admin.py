from django.contrib import admin
from django.forms.models import BaseInlineFormSet

from .models import Choice, Course, Instructor, Learner, Lesson, Question, Submission


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class LessonQuestionFormSet(BaseInlineFormSet):
    def save_new(self, form, commit=True):
        form.instance.course_id = self.instance.course_id
        return super().save_new(form, commit=commit)


class QuestionInline(admin.TabularInline):
    formset = LessonQuestionFormSet
    exclude = ("course",)
    model = Question
    extra = 1
    show_change_link = True


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ("name", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["name", "description"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ("title", "course", "order")
    list_filter = ["course"]
    search_fields = ["title"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ("question_text", "course", "lesson", "grade")
    list_filter = ["course"]
    search_fields = ["question_text"]


admin.site.register(Choice)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
