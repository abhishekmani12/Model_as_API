FROM python:3.9

WORKDIR /home/abshk/Desktop/app
COPY . .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
