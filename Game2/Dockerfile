# استخدم صورة رسمية لـ Python
FROM python:3.12-slim

# تثبيت مكتبات نظام ضرورية لتشغيل Pygame و PyAudio
RUN apt-get update && apt-get install -y \
    python3-pygame \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libfreetype6-dev \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى الحاوية
COPY Game2/ /app

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# تعيين البورت (اختياري لو البرنامج يفتح سيرفر)
EXPOSE 5000

# أمر التشغيل
CMD ["python", "main.py"]
