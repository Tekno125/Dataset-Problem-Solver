# HARD-Datasets

**HARD — High-level Abstract Reasoning Datasets**

HARD-Datasets adalah kumpulan dataset yang dirancang untuk melatih dan mengevaluasi **kemampuan reasoning tingkat tinggi**, **intelektualitas**, dan **general intelligence** pada model AI. Dataset ini secara eksplisit menghindari soal-soal **formulaik** dan **berbasis hafalan**, serta menekankan *deep reasoning*, *generalization*, dan *structured thinking*.

---

## Tujuan Utama

Sebagian besar dataset publik saat ini masih dapat diselesaikan model dengan:

* menghafal rumus tetap,
* mencocokkan pola token,
* atau melakukan lookup implisit dari data latih.

**HARD-Datasets** bertujuan untuk melampaui batas tersebut dengan menyajikan soal yang:

* tidak memiliki solusi satu-langkah,
* menuntut justifikasi dan pembuktian,
* memerlukan perencanaan multi-langkah,
* dan menguji ketahanan model terhadap kesalahan pola.

Jika sebuah soal gagal diselesaikan tanpa *reasoning eksplisit*, maka soal tersebut **berhasil**.

---

## Filosofi Desain

Prinsip utama dalam HARD-Datasets:

1. **Non-formulaic by design**
   Soal yang dapat diselesaikan hanya dengan mengingat rumus tertutup dianggap *tidak layak*.

2. **Reasoning over results**
   Proses berpikir lebih penting daripada jawaban akhir.

3. **Structural difficulty > Numerical difficulty**
   Kompleksitas berasal dari struktur masalah, bukan angka besar.

4. **Controlled ambiguity**
   Beberapa soal sengaja memiliki lebih dari satu solusi yang sah, selama disertai argumen yang benar.

5. **Self-correction friendly**
   Soal ideal memungkinkan analisis kesalahan dan perbaikan solusi.

---

## 📂 Kategori Soal

HARD-Datasets mencakup (namun tidak terbatas pada) kategori berikut:

* Debugging & Code Comprehension
* Non-trivial Pattern Discovery
* Multi-constraint Story Problems
* Mathematical Proof & Formal Reasoning
* High-level Algorithm Design
* Formal Logic & First-Order Logic (FOL)
* Probabilistic & Bayesian Reasoning
* Combinatorics & Discrete Optimization
* Logic Puzzles & Adversarial Problems
* Natural Language Ambiguity Resolution
* Causal Reasoning & Thought Experiments
* Conceptual Physics & Modeling
* Theory of Computation & Formal Languages
* Cryptography & Security Reasoning
* Meta-reasoning & Self-debugging

Detail kategori dan prinsip penulisan soal dapat dilihat pada dokumen desain internal repository.

---

## 🧩 Struktur Dataset (Rencana)

```text
HARD-Datasets/
├── train/
├── reasoning/
├── algorithms/
├── math-proof/
├── logic/
├── probability/
├── puzzles/
├── meta-reasoning/
└── README.md
```

---

## 🧪 Format Data (Harus)

Contoh skema JSONL:

```json
{
  "question": "...",
  "options":{"A":"","B":"","C":"","D":""},"reasoning":"","answer":"","output":""}
}
```

---

## 🚫 Contoh Soal yang Dihindari

* Jumlah deret dengan rumus tertutup tanpa pembuktian
* Soal yang hanya membutuhkan substitusi langsung
* Masalah yang dapat diselesaikan dengan satu pola token tetap

Soal-soal ini mungkin terlihat sulit bagi manusia, tetapi **mudah bagi model** dan tidak meningkatkan kemampuan reasoning.

---

## ✅ Contoh Soal yang Diutamakan

* Pembuktian matematis dengan variasi kondisi
* Pola yang memiliki beberapa interpretasi sah
* Masalah algoritmik dengan trade-off desain
* Soal yang meminta analisis kesalahan solusi sendiri
