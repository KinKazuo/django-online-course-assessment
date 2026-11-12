from django.contrib import admin

from .models import Choice, Course, Instructor, Learner, Lesson, Question, Submission


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class QuestionInline(admin.TabularInline):
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
    list_display = ("question_text", "lesson", "grade")
    list_filter = ["lesson__course"]
    search_fields = ["question_text"]


admin.site.register(Choice)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
