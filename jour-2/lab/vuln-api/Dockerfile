FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
RUN echo "m1secua-lab-hostname" > /etc/lab-hostname.txt
EXPOSE 5000
CMD ["python", "app.py"]
