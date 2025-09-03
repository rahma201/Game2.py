# استخدم صورة بايثون رسمية خفيفة
FROM python:3.12-slim

# تحديث النظام وتثبيت المكتبات اللازمة لـ PyGame و PyAudio
RUN apt-get update && apt-get install -y \
    build-essential \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libsmpeg-dev \
    libjpeg-dev \
    libfreetype6-dev \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# إعداد مجلد العمل داخل الصورة
WORKDIR /app

# نسخ ملف المتطلبات وتحديث pip
COPY Game2/requirements.txt .
RUN python3 -m pip install --upgrade pip setuptools wheel

# تثبيت مكتبات Python المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي المشروع داخل الصورة
COPY Game2/ .

# أمر التشغيل الافتراضي
CMD ["python3", "main.py"]
