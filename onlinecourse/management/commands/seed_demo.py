from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.timezone import localdate

from onlinecourse.models import Choice, Course, Lesson, Question


class Command(BaseCommand):
    help = "Add a Django course with two lessons and a practice exam."

    @transaction.atomic
    def handle(self, *args, **options):
        course, _ = Course.objects.get_or_create(
            name="Django Fundamentals",
            defaults={
                "description": "Learn to model relational data and route requests in a Django application.",
                "image": "course_images/django.png",
                "pub_date": localdate(),
            },
        )
        lesson_data = [
            (
                "Models and migrations",
                "Models describe your data. Migrations record and apply changes to the database schema.",
                "Which command applies migrations to the database?",
                4,
                [("python manage.py migrate", True), ("python manage.py makemigrations", False), ("python manage.py runserver", False)],
            ),
            (
                "URLs, views, and templates",
                "URL patterns route requests to views. Views can render templates with context data.",
                "Which tasks are handled by Django views? Select all that apply.",
                6,
                [("Handle incoming HTTP requests", True), ("Return an HTTP response", True), ("Create database schema migrations", False)],
            ),
        ]
        for order, (title, content, prompt, grade, choices) in enumerate(lesson_data):
            lesson, _ = Lesson.objects.get_or_create(
                course=course, title=title, defaults={"order": order, "content": content},
            )
            question, _ = Question.objects.get_or_create(
                lesson=lesson, question_text=prompt, defaults={"grade": grade},
            )
            for text, is_correct in choices:
                Choice.objects.get_or_create(
                    question=question, choice_text=text, defaults={"is_correct": is_correct},
                )
        self.stdout.write(self.style.SUCCESS(f"Course available at /onlinecourse/{course.pk}/"))
