FROM python:3.9-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY . .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .
# ENTRYPOINT ["python", "src/load_model.py"] 
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8000", "src.wsgi:app" ]