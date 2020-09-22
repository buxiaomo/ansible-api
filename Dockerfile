FROM python:3.7-alpine

COPY requirements.txt /usr/local/ansible-api/requirements.txt

RUN apk add --no-cache curl \
    && pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r /usr/local/ansible-api/requirements.txt

COPY . /usr/local/ansible-api

WORKDIR /usr/local/ansible-api

EXPOSE 5000

CMD ["python3", "run.py", "runserver", "-h", "0.0.0.0"]