# استخدم صورة بايثون رسمية خفيفة
FROM python:3.12-slim

# تحديث النظام وتثبيت المكتبات اللازمة لبناء الحزم الخاصة بـ PyGame, PyAudio, OpenCV وغيرها
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
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
    libpulse-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# تعيين مجلد العمل داخل الصورة
WORKDIR /app

# نسخ ملف المتطلبات وتحديث pip
COPY Game2/requirements.txt .
RUN python3 -m pip install --upgrade pip setuptools wheel

# تثبيت مكتبات Python المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي المشروع داخل الصورة
COPY Game2/ .

# تعريف بورت التطبيق (مثلاً واجهة ويب على 5000)
EXPOSE 5000

# تعيين الأمر الافتراضي لتشغيل التطبيق
CMD ["python3", "main.py"]
