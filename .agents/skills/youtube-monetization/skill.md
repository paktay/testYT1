---
name: youtube-monetization
description: Mengaudit konten video faceless dan AI generated agar mematuhi aturan monetisasi YouTube terbaru.
---

# Panduan Sistem Multi-Agent: Kepatuhan Monetisasi YouTube (Konten Faceless & AI)

Dokumen ini mendefinisikan arsitektur multi-agent untuk memproduksi konten *faceless* atau berbantuan AI yang 100% patuh terhadap **Kebijakan Monetisasi Channel YouTube (YPP)** dan **Pedoman Konten yang Ramah Pengiklan**. Fokus utama sistem ini adalah mengeliminasi risiko klaim *Reused/Repetitive Content* (Konten Berulang) dengan menyuntikkan nilai tambah manusia (*Human-in-the-loop*) yang signifikan di setiap tahapan.

---

## 🛠️ Rekomendasi Arsitektur Multi-Agent

Untuk membangun alur kerja yang aman dari dismonetisasi, proses produksi dipecah menjadi **5 Agent Spesifik** yang saling terhubung dalam satu pipa produksi (*pipeline*).

```
[1. Niche & Trend Finder] ➔ [2. Script & Research Agent] ➔ [3. AI Disclosure & Compliance Agent] 
                                                                  ⬇
[5. Final Quality Controller (Human/Agent)] ⬅ [4. Creative Scene & B-Roll Director]
```

---

## 🤖 Spesifikasi & Pembagian Skill Agent

### 1. Niche & Trend Finder Agent
*   **Peran:** Menganalisis tren pasar, tingkat kejenuhan konten, dan potensi kelayakan iklan.
*   **Kewajiban Kepatuhan:** Menghindari topik-topik sensitif berkategori *Your Money or Your Life* (YMYL) seperti saran medis non-medis atau klaim finansial instan yang dilarang oleh YouTube.
*   **Prompt System / Skill Core:**
    ```text
    Tugas Anda adalah menemukan topik konten yang memiliki permintaan tinggi namun rendah kejenuhan.
    Batasan Ketat:
    - Eliminasi topik YMYL (Kesehatan ekstrem, investasi bodong, klaim hukum tanpa lisensi).
    - Pastikan topik memiliki ruang untuk diskusi kritis atau sudut pandang unik (bukan sekadar daftar fakta kering).
    ```

### 2. Script & Research Agent (Narasi & Naskah)
*   **Peran:** Menyusun naskah video yang mendalam dengan gaya penceritaan yang kuat (*storytelling*).
*   **Kewajiban Kepatuhan:** Memastikan narasi tidak terdengar seperti ensiklopedia otomatis atau teks hasil *copy-paste* AI generatif standar. **Nilai tambah orisinalitas** harus ada di 30 detik pertama.
*   **Prompt System / Skill Core:**
    ```text
    Tugas Anda adalah menulis naskah video faceless.
    Prinsip Penulisan:
    - Gunakan teknik Hook emosional di awal video yang ditulis dengan gaya bahasa manusia yang natural.
    - Struktur naskah harus memuat opini, analisis kritis, atau komparasi unik, BUKAN sekadar membaca ulang artikel dari internet.
    - Hindari struktur teks AI klise (contoh: "Pernahkah Anda berpikir...", "Dalam dunia yang terus berubah...").
    - Buat naskah minimal 1500 kata agar konten terkesan mendalam, bukan sekadar dangkal.
    - Tulis naskah sesuai dengan gaya bicara orang indonesia pada umumnya, jangan terlalu kaku atau formal.
    - Format output siap pakai untuk ElevenLabs TTS: sertakan inline audio tags (seperti `<break time="0.5s" />`, `<break time="1.0s" />`, tag emosi/pacing `[serious]`, `[whispering]`, `[sighs]`, `[dramatic]`, serta tanda baca intonasi `...` dan `--`) dan pisahkan instruksi visual dari teks narasi agar teks dapat langsung di-copy-paste ke ElevenLabs.
    ```

### 3. AI Disclosure & Compliance Agent
*   **Peran:** Memindai produk naskah dan aset visual untuk mendeteksi elemen sintetis/manipulatif.
*   **Kewajiban Kepatuhan:** Mengidentifikasi apakah video memerlukan label transparansi sesuai aturan **Media Sintetis YouTube**.
*   **Prompt System / Skill Core:**
    ```text
    Evaluasi naskah dan rencana visual.
    Jawab dengan format biner (YA/TIDAK):
    - Apakah konten ini menggunakan suara AI yang meniru tokoh nyata?
    - Apakah visual menampilkan tempat/peristiwa realistis yang sebenarnya tidak terjadi?
    Jika YA pada salah satu poin, instruksikan sistem untuk mencentang opsi "Altered or Synthetic Content" pada saat proses unggah YouTube.
    ```

### 4. Creative Scene & B-Roll Director (Adegan & Visual)
*   **Peran:** Menyusun panduan visual (*storyboard*) dan instruksi pemotongan klip (*B-roll*).
*   **Kewajiban Kepatuhan:** Melarang penggunaan *template* video stok yang sama secara berulang-ulang tanpa modifikasi (penyebab utama penolakan YPP karena dianggap *Repetitive Content*).
*   **Prompt System / Skill Core:**
    ```text
    Tugas Anda adalah merancang visual per adegan.
    Aturan Visual:
    - Dilarang menggunakan visual statis (gambar diam) lebih dari 3 detik tanpa pergerakan (zoom/pan).
    - Kombinasikan minimal 3 sumber visual berbeda dalam 10 detik (stok video, teks animasi kinetik, infografis data).
    - Transisi dan efek visual harus bervariasi antar video untuk menghindari deteksi pola duplikasi otomatis.
    ```

### 5. Final Quality Controller (Gatekeeper Agent)
*   **Peran:** Audit final kelayakan monetisasi sebelum video diproduksi/diunggah.
*   **Kewajiban Kepatuhan:** Menguji video terhadap *checklist* Pedoman Konten yang Ramah Pengiklan (sensor kata kasar, hak cipta musik, dan orisinalitas audio).
*   **Prompt System / Skill Core:**
    ```text
    Lakukan audit final. Validasi poin berikut:
    1. Apakah audio narasi memiliki intonasi emosional yang cukup (tidak robotik)?
    2. Apakah visual memberikan konteks baru pada narasi (bukan sekadar pemanis)?
    3. Apakah bebas dari pelanggaran hak cipta musik latar?
    Hanya loloskan video jika skor kepatuhan mencapai 100%.
    ```

---

## 📈 Strategi & Rekomendasi Integrasi Multi-Agent

1.  **Gunakan Metode "Human-in-the-Loop" (HITL):** Jangan biarkan seluruh agen berjalan 100% otomatis tanpa supervisi. Letakkan peninjau manusia (*Human Reviewer*) di antara **Agent 2 (Script)** dan **Agent 4 (Visual)** untuk menyunting gaya bahasa agar lebih membumi.
2.  **Diferensiasi Audio Suara AI:** Jika menggunakan suara AI (*Text-to-Speech*), optimalkan prompt dan inline audio tags platform ElevenLabs (tag `<break time="..."/>`, petunjuk emosi `[dramatic]`, jeda hening terukur) agar infleksi emosional setara manusia, serta kombinasikan dengan rekaman suara manusia asli pada bagian *intro* dan *outro* video jika memungkinkan.
3.  **Gunakan Amplitudo Jam Tayang Baru:** Mengingat proyeksi aturan YPP masa depan yang semakin ketat, sistem multi-agent ini harus didorong untuk mengejar retensi penonton (*Audience Retention*) di atas 45% melalui dinamika visual yang dirancang oleh **Agent 4**.