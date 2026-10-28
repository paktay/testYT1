---
name: isometric-claymation-prompts
description: Menghasilkan image prompt AI bergaya Isometric 3D Claymation dari naskah narasi bertimestamp, berformat nomor urut dengan jarak 1 baris kosong, siap pakai untuk Midjourney, Flux, atau Ideogram.
---

# Isometric 3D Claymation Image Prompts Skill

Skill ini digunakan untuk mengonversi naskah narasi video faceless atau transkrip bertimestamp (misalnya per detik/menit) menjadi serangkaian **image prompt AI** bergaya **Isometric 3D Claymation** (diorama tanah liat plastisin miniatur 3D).

## Kapan Menggunakan Skill Ini
- Pengguna meminta pembuatan prompt gambar AI bergaya claymation, isometric 3D, diorama plastisin, atau stop-motion clay.
- Perintah seperti: *"buatkan image prompt bergaya Isometric 3D Claymation dari file/baris timestamp"*, *"buat storyboard visual claymation dari naskah"*, *"generate midjourney prompt claymation per adegan"*.
- Mengotomasi pembuatan prompt gambar berseri dengan format bernomor dan berjarak 1 baris kosong untuk memudahkan copy-paste ke batch generator atau Midjourney automator.

## Formula Gaya Visual (Isometric 3D Claymation)

Setiap prompt wajib menyusun formula visual berikut:

1. **Camera Angle & Composition**:
   - `Isometric 3D cutaway diorama`, `Isometric 3D miniature scene`, `Tilt-shift depth of field`, `Low-angle isometric perspective`.
2. **Subject & Visual Storytelling**:
   - Menerjemahkan makna narasi (bukan hanya teks mentah) ke dalam elemen visual metaforis atau adegan teatrikal miniatur yang kuat (karakter tanah liat ekspresif, properti retro, grafik 3D, miniatur gedung/diorama).
3. **Texture & Clay Finish**:
   - `Handcrafted claymation aesthetic`, `textured plasticine clay finish`, `subtle fingerprint details`, `soft matte texture`, `chunky stylized clay figurines`.
4. **Lighting & Atmosphere**:
   - `Soft studio lighting`, `volumetric rim lighting`, `warm cinematic key light`, `clean diorama stage`.
5. **Technical Parameters (Midjourney / Flux standard)**:
   - `--ar 16:9 --v 6.1` (atau rasio yang diminta pengguna).

## Aturan Format Output

1. **Penomoran Urut**: Setiap prompt diawali nomor urut sesuai urutan baris/timestamp (`1. ...`, `2. ...`).
2. **Jarak Antar-Prompt**: Wajib memberikan **1 baris kosong** di antara setiap nomor prompt untuk kemudahan pembacaan dan parsing script:
   ```text
   1. Isometric 3D cutaway diorama of [adegan 1]... --ar 16:9 --v 6.1

   2. Isometric 3D clay diorama of [adegan 2]... --ar 16:9 --v 6.1
   ```
3. **Bahasa Prompt**: Selalu gunakan bahasa Inggris deskriptif berkualitas tinggi untuk memaksimalkan kepatuhan model AI (Google Flow / Imagen, Midjourney, Flux, Ideogram).
4. **Integritas Konteks Narasi**: Visual harus merefleksikan alur waktu, ekspresi emosional tokoh (misal: tegang, skeptis, takjub, bangkrut), serta elemen simbolik (seperti tumpukan uang, grafik saham turun, jam berdetik).

## Aturan Kepatuhan Kebijakan Konten (Google Flow & Imagen Safety Filter)

Agar prompt tidak memicu blokir otomatis (*safety violation / content policy trigger*) pada Google Flow / Imagen:

1. **Hindari Deskripsi Fisik Tubuh yang Diskriminatif / Negatif (*Body-Shaming*)**:
   - ❌ **Dilarang**: `rotund`, `obese`, `fat`, `ugly`, `deformed`, `grotesque`.
   - ✅ **Gunakan**: `towering`, `prominent`, `commanding figure`, `stylized clay figurine`, `oversized coat/chair`.
2. **Hindari Frasa Mockery / Bullying / Harassment**:
   - ❌ **Dilarang**: `being laughed at`, `mocked`, `ridiculed`, `cynical sneer`, `malicious laugh`.
   - ✅ **Gunakan**: `skeptical and amused expressions`, `whimsical business satire`, `patronizing smirk`, `poised posture`.
3. **Hindari Kata Terkait Kekerasan / Kerusakan Fisik (*Violence/Damage Triggers*)**:
   - ❌ **Dilarang**: `battered`, `beaten up`, `bruised`, `blood`, `mutilated`.
   - ✅ **Gunakan**: `vintage`, `weathered`, `fragile`, `modest`, `worn paper`, `cracked clay surface`.
4. **Hindari Pelanggaran Merek Dagang & Nama Brand (*Trademarks / IP*)**:
   - ❌ **Dilarang**: Menyebut nama brand langsung seperti `Blockbuster`, `Netflix`, `Disney`, dll.
   - ✅ **Gunakan**: Deskripsi visual tematik seperti `retro 1990s video rental store with blue-and-yellow accents`, `pioneering digital streaming startup`, `iconic movie rental shop`.
5. **Hindari Figur Publik, Selebriti & Standee Karakter (*Likeness Policy*)**:
   - ❌ **Dilarang**: Kata seperti `cardboard standees`, `movie posters of actors`, `celebrity cutouts` (memicu deteksi wajah tokoh/hak cipta pada Google Flow).
   - ✅ **Gunakan**: Objek interior toko generik seperti `display shelves`, `popcorn buckets`, `colorful tape boxes`.
6. **Hindari Potensi Pemicu Kebijakan Perlindungan Anak (*Child Safety Filter*)**:
   - ❌ **Dilarang**: Menyebut anak-anak atau kelompok keluarga minor rentan seperti `family of four`, `children`, `kids`, serta kata aksi fisik ambigu seperti `piling into`.
   - ✅ **Gunakan**: Subjek dewasa netral seperti `stylish miniature clay figures`, `suburban patrons`, `neighborhood characters`, `boarding a vehicle`.
7. **Hindari Kiasan Ruang Bawah Tanah / Penyembunyian Rahasia (*Captivity / Dark Tropes*)**:
   - ❌ **Dilarang**: Frasa seperti `subterranean basement beneath floorboards`, `concealing dark secret`, `eerie dungeon` (sangat rentan memicu filter CSAM / kejahatan / bahaya Google).
   - ✅ **Gunakan**: Kontras ruang kerja profesional seperti `back-office administration room`, `archival storage area`, `dual-room cutaway`.
8. **Hindari Istilah Hukuman & Pelecehan Hukum (*Punitive / Negligence Terms*)**:
   - ❌ **Dilarang**: `punitive clauses`, `sneaky`, `punish negligent customers` (memicu filter sengketa/tuduhan negatif).
   - ✅ **Gunakan**: Istilah netral seperti `corporate policy document`, `fine print terms next to an hourglass`.
9. **Hindari Penggambaran Kemarahan Ekstrem & Protes Pelanggan (*Anger & Agitation Filters*)**:
   - ❌ **Dilarang**: `angry customers`, `stomping feet in disgust`, `muttering complaints`, `forced icy plastic smile` (memicu filter agresi / pelecehan).
   - ✅ **Gunakan**: Nuansa naratif tenang seperti `disappointed, pensive postures`, `holding long receipts`, `astonished customer`.
10. **Gunakan Infografis Netral Tanpa Kata Kritik Sensitif**:
   - ❌ **Dilarang**: Frasa kritik metaforis seperti `financial irony`, `predatory late-fee slice`.
   - ✅ **Gunakan**: Elemen diagram murni seperti `glowing orange 3D pie-chart wedge labeled '16%'`, `solid green clay block labeled 'Net Profit'`.
11. **Simbolisme Aman untuk Krisis & Ancaman**:
   - Gunakan pendekatan kartun/diorama abstrak, misal: `cartoon ticking clock mechanism`, `collapsing clay blocks`, `warning red graph line` (bukan penggambaran bencana realistis yang mengerikan).
12. **Portabilitas Parameter**:
   - Jika pengguna memakai Google Flow atau Imagen berbasis web, pisahkan atau buat parameter teknis seperti `--ar 16:9 --v 6.1` opsional agar tidak memicu error parsing teks pada engine Google.

## Workflow Eksekusi

1. **Baca Input File/Teks**: Baca baris timestamp (misal: `1. (0:00) Narasi...`).
2. **Analisis Narasi per Adegan**: Tentukan representasi visual terbaik (apakah karakter, suasana ruang, simbol metafora, atau infografis clay 3D).
3. **Rakit Prompt Sesuai Formula**: Gabungkan komposisi isometric, material clay/plasticine, pencahayaan, dan parameter rasio.
4. **Tulis & Simpan ke File**: Tulis hasil dengan penomoran urut dan 1 baris kosong pemisah.
