FROM python:3.9
SHELL ["/bin/bash", "-c"]
RUN pip install pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock /app/
RUN pipenv install
COPY . /app
ENV PYTHONUNBUFFERED 1
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
