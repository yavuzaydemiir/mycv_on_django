# 1. Python'un resmi ve hafif sürümünü taban alıyoruz
FROM python:3.12-slim

# 2. Konteyner içindeki çalışma klasörümüzü belirliyoruz
WORKDIR /app

# 3. Malzeme listemizi konteynere kopyalayıp kurulumları yapıyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Projedeki tüm kodlarımızı konteynere aktarıyoruz
COPY . .

# 5. Django'nun dışarıya yayın yapacağı portu açıyoruz
EXPOSE 8000

# 6. Konteyner ayağa kalktığında sunucuyu çalıştıracak o meşhur komut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]