🧠 APA ITU DATASET BERKUALITAS?

Dataset berkualitas = dataset yang membuat model belajar pola yang BENAR, bukan kebiasaan yang KEBETULAN sering muncul.

Bukan sekadar:

> “jawabannya benar”



tapi:

> “cara sampai ke jawaban itu dapat digeneralisasi.”




---

I. SYARAT DASAR (WAJIB)

Tanpa ini, dataset rusak.

1️⃣ Ground Truth Benar (No Silent Error)

Jawaban pasti benar

Tidak ambigu

Tidak ada kontradiksi internal


❌ Buruk:

> Soal punya 2 jawaban benar
Reasoning tidak cocok dengan answer



✅ Baik:

> Satu soal → satu jawaban → reasoning mendukung




---

2️⃣ Konsistensi Internal

Semua bagian harus sinkron:

Elemen	Harus

Question	Mendefinisikan masalah jelas
Reasoning	Langkah logis
Answer	Konsisten dengan reasoning
Options	Hanya satu yang benar


❌ Dataset kamu sebelumnya gagal di sini (contoh: nilai tidak ada di opsi)


---

3️⃣ Tidak Ada Shortcut Statistik

Model tidak boleh bisa menjawab tanpa berpikir.

❌ Contoh fatal:

Jawaban sering = A

Kata “maka” → biasanya benar

Angka terbesar → sering benar


Ini disebut spurious correlation.


---

II. KUALITAS STRUKTURAL (INI YANG MEMBEDAKAN DATASET “BANYAK” vs “PINTAR”)

4️⃣ Distribusi Jawaban Seimbang

Untuk pilihan ganda:

Huruf	Ideal

A	~25%
B	~25%
C	~25%
D	~25%


Kalau tidak seimbang:

> model belajar menebak, bukan berpikir




---

5️⃣ Variasi Bentuk Soal (Anti Template)

Jangan selalu:

“Hitung…”

“Tentukan…”


Campur:

Mengapa

Mana pernyataan salah

Pilih argumen paling kuat

Koreksi kesalahan


❌ Dataset template → model hafalan
✅ Dataset variatif → model reasoning


---

6️⃣ Reasoning ≠ Jawaban Disamarkan

Reasoning harus:

eksplisit

berurutan

bisa dipakai ulang


❌ Buruk:

> “Jelas terlihat bahwa…”



✅ Baik:

> “Langkah 1…, Langkah 2…”




---

III. KUALITAS KOGNITIF (INILAH INTI “MODEL PINTAR”)

7️⃣ Mengajarkan Pola, Bukan Kasus

Soal harus:

mewakili kelas masalah

bukan kasus unik


❌ Buruk:

> Hitung integral super-spesifik tanpa makna



✅ Baik:

> Soal yang bisa digeneralisasi (rekurensi, simetri, identitas)




---

8️⃣ Progressive Difficulty (Curriculum)

Dataset bagus itu berjenjang:

1. Dasar (definisi)


2. Menengah (kombinasi)


3. Sulit (abstraksi)



Kalau langsung lompat ke berat:

> model bingung, bukan belajar




---

9️⃣ Negative Examples (SANGAT PENTING)

Model harus melihat:

reasoning salah

asumsi keliru

kesimpulan palsu


Ini melatih error detection.

Tanpa ini:

> model mudah halusinasi




---

IV. KUALITAS TEKNIS (SERING DIABAIKAN, PADAHAL KRUSIAL)

🔟 Bebas Leakage

Dataset tidak boleh bocor:

❌ Soal:

> “Gunakan rumus berikut…”



❌ Reasoning:

> “Seperti pada soal sebelumnya…”



Model akan menghafal, bukan memahami.


---

1️⃣1️⃣ Token-Efficient tapi Informative

Reasoning cukup

Tidak bertele-tele

Tidak kosong


Ideal:

> minimum token, maximum signal




---

1️⃣2️⃣ Noise Terkontrol

Noise kecil (variasi bahasa) baik
Noise besar (typo, salah konsep) merusak


---

V. KUALITAS META (LEVEL LANJUT – JARANG ORANG SADAR)

1️⃣3️⃣ Anti Overfitting Bahasa

Jangan selalu:

gaya formal

kalimat panjang

struktur sama


Campur:

ringkas

padat

variasi simbol



---

1️⃣4️⃣ Evaluability

Dataset bagus:

bisa diuji

bisa diaudit

bisa diperbaiki


Kalau manusia tidak bisa memverifikasi → model juga tidak.


---

1️⃣5️⃣ Alignment dengan Tujuan

Dataset harus jelas:

mau melatih apa?


Tujuan	Dataset

Hitung cepat	Banyak numerik
Reasoning	Langkah logis
Verifikasi	Salah vs benar
Kreatif	Open-ended



---

VI. KESIMPULAN KERAS (INI PENTING)

> 10.000 sample buruk < 300 sample berkualitas tinggi



Model besar tetap bodoh kalau:

data bias

reasoning rusak

shortcut dibiarkan


Model kecil bisa sangat pintar jika:

data bersih

struktur tepat

pola benar
