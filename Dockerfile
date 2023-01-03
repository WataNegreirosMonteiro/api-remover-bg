FROM bitnami/python:3.10-debian-11

WORKDIR /app

COPY . .
RUN pip install Flask
RUN pip install pillow
RUN pip install rembg

EXPOSE 5000

CMD ["python", "api_bgremover.py"]
