FROM python:3.13-alpine
WORKDIR /app
COPY app.py .
USER 65534:65534
EXPOSE 8000
CMD ["python", "-u", "app.py"]
