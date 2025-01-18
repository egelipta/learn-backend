# How to start
## 1. Clone & Setup Environment
a. Clone repository
```
khkhkk
```
b. Copy dan sesuaikan .env
```
cp env.txt .env
vim .env
```
c. Buat python virtualenv
```
python3.9 -m venv .venv
```
d. Aktifkan virtualenv
```
source .venv/bin/activate
```
e. Upgrade pip
```
pip install -U pip
```
## 2. Setup Database Server
a. Pastikan docker daemon berjalan, lalu jalankan MySQL+PHPMyAdmin dengan docker-compose
```
docker compose up -d
```
b. Login ke PHPMyAdmin dan import db.sql
## 3. Jalankan Backend
```
uvicorn app:app --reload --host 0.0.0.0 --port 8888
```

