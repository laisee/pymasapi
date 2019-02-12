FROM python:3

ADD /scripts/sample_api_call.py /
RUN pip install --upgrade pip
RUN pip install request

CMD [ "python", "./sample_api_call.py" ]
