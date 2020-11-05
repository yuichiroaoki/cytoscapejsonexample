FROM python:3.8.3

WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PORT '8081'

# add and install requirements
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8081
CMD [ "python", "main.py", "--host=0.0.0.0" ]