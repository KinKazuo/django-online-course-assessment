# Online Course Assessment

This Django application extends the [IBM Skills Network starter project](https://github.com/ibm-developer-skills-network/final-cloud-app-with-database) with course exams, weighted scoring, and per-question results.

## Run locally

Use Python 3.11 or later. Create and activate a virtual environment, then run:

```sh
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Open [the course catalog](http://127.0.0.1:8000/onlinecourse/). Sign up, enroll in Django Fundamentals, and open **Start exam**. Choose every correct answer for each question and submit. Each question earns its full weight when the selected answers exactly match the answer key. A score above 80% passes the mock exam.

In the [Django admin](http://127.0.0.1:8000/admin/), edit a lesson to add questions, then edit a question to add choices and mark correct answers. Each submission is associated with an enrollment, so learners can only open their own results.
