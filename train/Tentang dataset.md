# Catatan Desain Dataset

## Dataset untuk Model dengan IQ, Intelektual, dan Logika Tinggi

Dokumen ini berisi **kategori pertanyaan** dan **prinsip desain soal** untuk membangun dataset yang benar-benar melatih *reasoning*, *generalization*, dan *problem solving*, bukan sekadar menghafal rumus atau pola tetap.

---

## Prinsip Umum (WAJIB)

1. **Hindari soal formulaik murni**
   Contoh buruk: `1² + 2² + ... + n²` → model cukup mengingat rumus.
   Contoh baik: *buktikan*, *variasikan*, atau *ubah tujuan* (estimasi, generalisasi, kontra-contoh).

2. **Utamakan proses, bukan hasil akhir**
   Soal ideal meminta:

   * langkah penalaran
   * justifikasi
   * analisis kesalahan

3. **Berikan ruang ambiguitas terkontrol**
   Soal boleh memiliki lebih dari satu solusi **asal disertai alasan**.

4. **Naikkan kesulitan secara struktural, bukan numerik**
   Tambah constraint, variabel, atau aturan — bukan hanya angka besar.

---

## Kategori Soal (15 Kategori Utama)

### 1. Debugging & Code Comprehension

**Fokus:** memahami kode, menemukan bug, reasoning semantik.

* Cari bug logika / race condition / edge case
* Jelaskan *mengapa* bug terjadi
* Perbaiki dengan perubahan minimal

---

### 2. Pola Bilangan & Pola Simbolik Kompleks

**Fokus:** generalisasi pola non-trivial.

* Pola dengan banyak kemungkinan interpretasi
* Wajib menyertakan justifikasi
* Boleh meminta beberapa kemungkinan jawaban

---

### 3. Soal Cerita Multi-Langkah (Constraint Reasoning)

**Fokus:** perencanaan & pemenuhan syarat.

* Jadwal
* Penugasan
* Logika eksklusi

---

### 4. Matematika Pembuktian & Reasoning Formal

**Fokus:** pembuktian, bukan hitung cepat.

* Induksi
* Kontradiksi
* Konstruksi

---

### 5. Desain Algoritma Tingkat Tinggi

**Fokus:** abstraksi & efisiensi.

* Rancang algoritma
* Analisis kompleksitas
* Proof of correctness

---

### 6. Logika Formal & First-Order Logic (FOL)

**Fokus:** simbolisasi & inferensi.

* Bahasa alami → logika
* Validitas argumen
* Counterexample

---

### 7. Probabilitas & Statistik Reasoning

**Fokus:** pemahaman probabilistik.

* Bayesian reasoning
* Interpretasi data
* Menghindari bias intuitif

---

### 8. Kombinatorika & Optimisasi Diskrit

**Fokus:** counting & strategi optimal.

* Dynamic Programming
* Greedy + bukti
* Bijection

---

### 9. Puzzle Logika & Adversarial Problems

**Fokus:** solusi kreatif & non-obvious.

* Puzzle timbangan
* Puzzle strategi
* Minimal langkah

---

### 10. Bahasa Alami Kompleks & Ambiguitas

**Fokus:** tracking entitas & konteks.

* Referensi silang
* Temporal reasoning
* Resolusi ambiguitas

---

### 11. Penalaran Kausal & Eksperimen Pikiran

**Fokus:** sebab–akibat.

* Korelasi vs kausalitas
* Confounder
* Desain eksperimen

---

### 12. Fisika Konseptual & Pemodelan

**Fokus:** modeling & estimasi.

* Order of magnitude
* Asumsi eksplisit
* Translasi dunia nyata → matematika

---

### 13. Teori Komputasi & Bahasa Formal

**Fokus:** batas kemampuan komputasi.

* Automata
* Regex
* Bahasa non-regular

---

### 14. Kriptografi & Security Reasoning

**Fokus:** asumsi & serangan.

* Mengapa skema aman/tidak
* Threat model
* Proof sketch

---

### 15. Meta-Reasoning & Self-Debugging

**Fokus:** refleksi & koreksi diri.

* Identifikasi kesalahan solusi sendiri
* Counterexample
* Perbaikan argumen

---

## Catatan Penting tentang Soal "Terlihat Sulit tapi Sebenarnya Mudah"

Beberapa soal tampak sulit bagi manusia karena:

* perhitungan panjang
* manipulasi simbol

Namun bagi model, soal ini **mudah** karena:

* memiliki rumus tetap
* sering muncul di data latih

⚠️ **Soal seperti ini TIDAK meningkatkan kecerdasan model.**

Solusi:

* ubah soal menjadi pembuktian
* tambahkan constraint baru
* minta generalisasi atau variasi

---

## Tujuan Akhir Dataset

Dataset ini bertujuan melatih model agar:

* tidak sekadar menjawab benar
* tetapi **berpikir benar**
* mampu menjelaskan, mengoreksi, dan menggeneralisasi

Jika model gagal tanpa rumus eksplisit, maka soal tersebut **berhasil**.

---

## Rekomendasi Tambahan

* Simpan **rubrik penilaian**, bukan hanya jawaban
* Tandai soal dengan metadata: `reasoning_depth`, `ambiguity_level`, `multi-solution`
* Campur soal deterministik & open-ended

---

> "Model cerdas bukan yang paling cepat menjawab, tetapi yang paling tahan terhadap kesalahan pola."
