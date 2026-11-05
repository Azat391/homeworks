FROM python:3.12.14-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install \
    --no-cache-dir \
    -r requirements.txt

COPY . .

CMD ["python", "-m", "pytest", "-m", "smoke", "-q", "--alluredir=allure-results"]