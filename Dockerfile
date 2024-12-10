FROM python:3.12

RUN useradd -m -u 1000 user
WORKDIR /app

COPY --chown=user . /app
RUN pip install --no-cache-dir --upgrade .

CMD ["python", "-m", "tgbot"]