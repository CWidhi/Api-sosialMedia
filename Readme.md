# Api-sosialMedia

Api-sosialMedia adalah sebuah RESTful API berbasis Django dan Django REST Framework yang dirancang untuk mendukung fungsionalitas sosial media sederhana. Pengguna dapat membuat postingan, memberi komentar, serta memberikan like/unlike pada postingan.

## Fitur Utama

- Autentikasi pengguna menggunakan JWT
- CRUD untuk Post dan Komentar
- Fungsi Like & Unlike untuk:
  - Postingan
- Endpoint RESTful yang rapi dan terstruktur

---

## Struktur Direktori
- infoKoding/
  - posts/ # Aplikasi untuk mengelola postingan
  - comments/ # Aplikasi untuk mengelola komentar
  - likes/ # Aplikasi untuk fitur suka
  - users/ # Aplikasi autentikasi pengguna
  - manage.py
  - README.md

---

## Autentikasi (JWT)

| Method | Endpoint             | Deskripsi                           |
|--------|----------------------|-------------------------------------|
| POST   | `/api/token/`        | Mendapatkan akses & refresh token   |
| POST   | `/api/token/refresh/`| Menyegarkan access token            |
| POST   | `/api/register/`        | Mendaftarkan akun baru/membuat user baru     |

---

## Enpoint User

| Method | Endpoint             | Deskripsi                           |
|--------|----------------------|-------------------------------------|
| GET   | `/api/users/`        | Mendapatkan list user yang terdaftar   |
| POST   | `/api/users/`| Mendaftarkan akun baru/membuat user baru            |
| GET   | `/api/users/{id}`        | Mendapatkan data user yang terdaftar berdasarkan id user   |
| PUT/PATCH   | `/api/users/{id}`        | Mengedit data user yang terdaftar berdasarkan id user(hanya dapat dilakukan oleh yang memiliki akun tersebut)   |
| DELETE   | `/api/users/{id}`        | Menghapus data user yang terdaftar berdasarkan id user(hanya dapat dilakukan oleh yang memiliki akun tersebut)   |

---

## Endpoint Postingan

| Method | Endpoint            | Deskripsi                        |
|--------|---------------------|----------------------------------|
| GET    | `/posts/`       | Menampilkan semua postingan     |
| POST   | `/posts/`       | Membuat postingan baru          |
| GET    | `/posts/{id}/`  | Menampilkan detail postingan    |
| PUT    | `/posts/{id}/`  | Memperbarui postingan           |
| DELETE | `/posts/{id}/`  | Menghapus postingan             |

---

## Endpoint Komentar

| Method | Endpoint                          | Deskripsi                          |
|--------|-----------------------------------|------------------------------------|
| GET    | `/comment/posts/{post_id}/comments/`  | Menampilkan komentar pada postingan|
| POST   | `/comment/posts/{post_id}/comments/`  | Menambah komentar baru             |
| GET    | `/comment/posts/{post_id}/comment/{id}`             | Melihat komentar                   |
| PUT    | `/comment/posts/{post_id}/comment/{id}`             | Memperbarui komentar               |
| DELETE | `/comment/posts/{post_id}/comment/{id}`             | Menghapus komentar                 |

---

## Like Postingan

| Method | Endpoint                    | Deskripsi                          |
|--------|-----------------------------|------------------------------------|
| GET    | `/like/posts/{post_id}/likes/`    | Daftar user yang menyukai post     |
| POST   | `/like/posts/{post_id}/likes/`    | Menyukai post                      |
| DELETE | `/like/posts/{post_id}/likes/`    | Batal menyukai post                |

---
## swagger
1. bisa mengakses semua endpoint di atas dan mencobanya di tampilan swagger dengan mengakses endpoint
    ```bash
    http://localhost:8000/swagger/

## Teknologi yang Digunakan

- Python 3.10
- Django 5.2
- Django REST Framework
- SQLite (default dev)
- JWT Authentication

## Instalasi

1. Clone repositori:
   ```bash
   git clone https://github.com/CWidhi/Api-sosialMedia.git
   cd infoKoding
   python -m venv env
   # Ubuntu : source env/bin/activate  
   # Windows: env\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver