# oficjalny obraz Pythona
FROM python:3.13.3-slim
# Skopiuj pliki projektu do kontenera
COPY . /usr/src/app
# Ustaw katalog roboczy
WORKDIR /usr/src/app
# Zainstaluj zależności Pythona
RUN pip install --upgrade pip && pip install -r requirements.txt
# Domyślna komenda uruchamiająca serwer
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]