from django.db import migrations, models
import django.db.models.deletion


def backfill_question_course(apps, schema_editor):
    Question = apps.get_model("onlinecourse", "Question")
    Lesson = apps.get_model("onlinecourse", "Lesson")
    db = schema_editor.connection.alias
    course_for_lesson = Lesson.objects.using(db).filter(pk=models.OuterRef("lesson_id")).values("course_id")
    Question.objects.using(db).update(course_id=models.Subquery(course_for_lesson))


class Migration(migrations.Migration):
    dependencies = [("onlinecourse", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="question",
            name="course",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.course"),
        ),
        migrations.RunPython(backfill_question_course, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="question",
            name="course",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.course"),
        ),
        migrations.AlterField(
            model_name="question",
            name="lesson",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.lesson"),
        ),
    ]
