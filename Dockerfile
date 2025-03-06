FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "uvicorn[standard]"
ENV SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7 \
    DB_NAME=appsec_db \
    DB_HOST=appsec-postgres \
    DB_PORT=5432 \
    DB_USER=postgres \
    DB_PASSWORD=postgres \
    FRONT_ORIGIN=http://appsec-frontend:80
EXPOSE 5000
CMD [ "uvicorn", "main:app" , "--host", "0.0.0.0", "--port", "5000"]