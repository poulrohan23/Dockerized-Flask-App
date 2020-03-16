1. FROM python:3.6.1-alpine
2. WORKDIR /project
3. ADD . /project
4. RUN pip install -r requirements.txt
5. CMD ["python","app_flask.py"]
