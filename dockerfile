FROM python:3.9.6-alpine3.13 as dev

WORKDIR /work
RUN apk add curl
RUN curl -fsSL https://platform.activestate.com/dl/cli/onb01/install.sh | sh

RUN cd /bin && ln -s /root/.local/ActiveState/StateTool/release/bin/state
FROM python:3.9.6-alpine3.13 as debugging

FROM dev as runtime
WORKDIR /app
COPY ./src/ /app

RUN pip install -r requirements.txt
ENV FLASK_APP=apphttp.py

CMD flask run -h 0.0.0 -p 5000
#ENTRYPOINT ["python", "/app/app.py"]