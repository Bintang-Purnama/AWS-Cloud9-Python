# ☁️ AWS Re/Start: Python Learning on Cloud9

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Environment](https://img.shields.io/badge/AWS-Cloud9-orange.svg)
![Status](https://img.shields.io/badge/Status-Educational-green.svg)

## 📝 Deskripsi Project

Repository ini berisi kumpulan kode Python yang saya kerjakan selama mengikuti program **AWS Re/Start**. Semua kode di sini ditulis dan dijalankan menggunakan lingkungan pengembangan berbasis cloud, **AWS Cloud9**.

Repository ini mendokumentasikan perjalanan belajar saya mulai dari dasar-dasar sintaks Python, manipulasi tipe data, hingga teknik debugging dan penanganan file JSON.

## 📚 Topik & Struktur File

Berikut adalah pemetaan file berdasarkan materi yang dipelajari:

### 1. Dasar Pemrograman (Basics)
* `hello-world.py`: Program pertama "Hello, World!".
* `numeric.py`: Pengenalan tipe data numerik (integer, float, complex).
* `String-Data-Type.py`: Manipulasi string.
* `Conditional.py`: Penggunaan logika `if`, `else`, dan `elif`.
* `categorize-value.py`: Latihan mengkategorikan nilai menggunakan loop dan kondisi.

### 2. Struktur Data (Data Structures)
* `list-tuples-dictionary.py`: Memahami perbedaan List, Tuple, dan Dictionary.
* `composite-data.py`: Bekerja dengan tipe data komposit (membaca data dari CSV `car_fleet.csv`).

### 3. Logika & Algoritma
* `caesar-cipher.py`: Implementasi algoritma enkripsi klasik Caesar Cipher (membuat fungsi enkripsi/dekripsi sederhana).
* `net-charge.py`: Perhitungan muatan bersih (net charge) insulin (studi kasus bioinformatika).

### 4. File Handling & JSON
* `jsonFileHandler.py`: Membaca dan menulis file format JSON.
* `calc_weight_json.py`: Menghitung berat molekul dari data JSON (`insulin.json`).
* `string-insulin.py` & `preproinsulin-seq*.txt`: Memproses data sekuens insulin dari file teks.

### 5. Debugging Practice
* `debugger.py`: Latihan dasar menggunakan debugger.
* `debug-caesar-1.py`, `2.py`, `3.py`: Latihan memperbaiki *bug* pada kode Caesar Cipher.

## 🛠️ Teknologi & Tools
* **Bahasa**: Python 3
* **IDE**: AWS Cloud9 (Linux-based environment)
* **Library**: `os`, `json`, `csv` (Standard Libraries)

## 🚀 Cara Menjalankan

Karena kode ini dibuat di lingkungan Cloud9, Anda bisa menjalankannya di terminal Linux/Mac atau Command Prompt Windows asalkan sudah terinstall Python.

1.  **Clone repository:**
    ```bash
    git clone [https://github.com/username/aws-cloud9-python.git](https://github.com/username/aws-cloud9-python.git)
    ```

2.  **Masuk ke folder:**
    ```bash
    cd aws-cloud9-python
    ```

3.  **Jalankan salah satu file (contoh Caesar Cipher):**
    ```bash
    python caesar-cipher.py
    ```

## 🤝 Kontribusi
Repository ini adalah dokumentasi pembelajaran pribadi. Namun, jika Anda melihat ada cara penulisan kode yang lebih efisien, silakan buat *Pull Request*!

## 📄 Lisensi
Project ini dilindungi di bawah lisensi [MIT](LICENSE).
