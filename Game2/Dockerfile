# استخدم صورة بايثون رسمية خفيفة
FROM python:3.12-slim

# تثبيت مكتبات النظام اللازمة لـ PyGame و PyAudio
RUN apt-get update && apt-get install -y \
    build-essential cmake git \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev portaudio19-dev libpulse-dev \
    ffmpeg \
    libswscale-dev libavformat-dev libavcodec-dev libsmpeg-dev \
    libjpeg-dev libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# تعيين مجلد العمل
WORKDIR /app

# نسخ المتطلبات
COPY Game2/requirements.txt .

# تثبيت الحزم
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# نسخ المشروع كامل (يشمل src/cocos2d)
COPY Game2/ .

# الأمر الافتراضي لتشغيل اللعبة
CMD ["python3", "main.py"]
