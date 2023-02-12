FROM python:3.10.6-alpine
WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app/app.py"]