FROM python:3.9

COPY . .


RUN pip3 install -r requirements.txt


CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000