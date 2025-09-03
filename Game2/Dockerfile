FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential cmake git \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libsmpeg-dev \
    libjpeg-dev libfreetype6-dev portaudio19-dev libpulse-dev ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY Game2/requirements.txt .
RUN python3 -m pip install --upgrade pip setuptools wheel

# تثبيت الحزم مع عرض التفاصيل إذا فشل
RUN pip install --no-cache-dir -r requirements.txt || (cat /root/.pip/pip.log && exit 1)

COPY Game2/ .

EXPOSE 5000
CMD ["python3", "main.py"]
