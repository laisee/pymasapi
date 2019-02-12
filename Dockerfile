FROM python:3

ADD sample_api_call.py /

RUN pip install request

CMD [ "python", "./sample_api_call.py" ]
