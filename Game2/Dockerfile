# استخدم صورة بايثون رسمية خفيفة
FROM python:3.12-slim

# تحديث النظام وتثبيت مكتبات النظام المطلوبة لبناء الحزم
RUN apt-get update && apt-get install -y \
    build-essential cmake git \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev portaudio19-dev libpulse-dev \
    ffmpeg \
    libswscale-dev libavformat-dev libavcodec-dev libsmpeg-dev \
    libjpeg-dev libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# تعيين مجلد العمل داخل الصورة
WORKDIR /app

# نسخ ملف المتطلبات
COPY Game2/requirements.txt .

# تحديث pip وتثبيت الحزم
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي المشروع
COPY Game2/ .

# الأمر الافتراضي لتشغيل التطبيق GUI
CMD ["python3", "main.py"]
