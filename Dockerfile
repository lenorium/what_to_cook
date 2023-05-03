FROM python:3.10

ARG API_PORT
ENV API_PORT $API_PORT

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/
COPY . /usr/src/app/

#бд не всегда успевает подняться перед запуском приложения, поэтому ждем
#RUN #git clone https://github.com/vishnubob/wait-for-it.git
#RUN #chmod +x ./wait-for-it/wait-for-it.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $API_PORT

#ENTRYPOINT ["./wait-for-it/wait-for-it.sh", "$POSTGRES_HOST:$POSTGRES_PORT", "--", "python", "app.py"]
ENTRYPOINT ["python", "app.py"]