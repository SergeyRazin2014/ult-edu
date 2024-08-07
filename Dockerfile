FROM python:3.11-slim


RUN pip install poetry
COPY . .
RUN poetry config virtualenvs.create false --local
RUN poetry install
CMD ["sh", "-c", "python manage.py migrate && python manage.py initialize_db && python manage.py runserver 0.0.0.0:8000"]
