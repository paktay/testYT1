---
name: format-timestamps
description: Merapikan naskah atau transkrip bertimestamp menjadi 1 baris per timestamp (dengan opsi penomoran urut) tanpa menghilangkan waktu atau teks narasi.
---

# Format Timestamps Skill

Skill ini digunakan untuk merapikan teks, naskah narasi, atau transkrip video yang memiliki penanda waktu (*timestamp*) di dalam baris/paragraf menjadi struktur rapi **1 baris 1 timestamp**, dengan opsi penomoran urut per baris, tetap menjaga akurasi waktu dan teks narasi 100% utuh.

## Kapan Menggunakan Skill Ini
- Pengguna meminta merapikan file atau teks bertimestamp (misal: `(0:00)`, `(1:23)`, `[02:15]`, dsb.).
- Perintah seperti: *"rapikan barisan menjadi 1 baris 1 timestamp"*, *"format timestamp"*, *"beri penomoran 1 nomor 1 baris"*, *"pisahkan tiap timestamp ke baris baru"*.
- Persiapan transkrip untuk subtitle, storyboard video faceless, checklist editing adegan, atau segmen voiceover/TTS.

## Pola Timestamp yang Didukung
- Kurung biasa: `(m:ss)`, `(mm:ss)`, `(h:mm:ss)`, `(hh:mm:ss)` — contoh: `(0:00)`, `(01:23)`, `(1:05:30)`
- Kurung siku: `[m:ss]`, `[mm:ss]`, `[h:mm:ss]`, `[hh:mm:ss]` — contoh: `[0:00]`, `[01:23]`

## Aturan Pemformatan
1. **Satu Baris Satu Timestamp:** Setiap kemunculan timestamp dipindahkan ke awal baris baru (`\n`).
2. **Penomoran (Opsional / Sesuai Permintaan):** Jika pengguna meminta penomoran ("beri nomor", "1 nomor 1 baris"), tambahkan nomor urut di awal setiap baris (contoh: `1. (0:00) Teks...`). Jika baris sudah memiliki nomor lama, perbarui nomor urutnya dari 1 secara berurutan.
3. **Integritas Data:** Jangan menghapus atau mengubah nilai timestamp maupun teks narasi yang mengikutinya.
4. **Pembersihan Whitespace:** Pastikan format spasi konsisten `(timestamp) Teks narasi...` tanpa spasi berlebih di awal/akhir baris.
5. **Akhir File:** Pastikan file memiliki baris baru (*newline*) di akhir.

## Panduan Eksekusi (Python / Regex)

### Logika Pemformatan (Dengan Opsi Penomoran)
```python
import re

def format_timestamps(text: str, add_numbering: bool = False) -> str:
    # Pola timestamp kurung biasa atau kurung siku
    pattern = r'(?<!^)\s*(\([0-9]+:[0-9]+(?::[0-9]+)?\)|\b\[[0-9]+:[0-9]+(?::[0-9]+)?\])'
    formatted = re.sub(pattern, r'\n\1', text.strip())
    
    # Rapikan spasi dan bersihkan nomor lama jika ada
    lines = []
    for line in formatted.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Hapus nomor baris lama jika ada (contoh: "1. ") sebelum re-format
        cleaned = re.sub(r'^\d+\.\s*', '', line)
        cleaned = re.sub(r'(\([0-9]+:[0-9]+(?::[0-9]+)?\)|\b\[[0-9]+:[0-9]+(?::[0-9]+)?\])\s+', r'\1 ', cleaned)
        lines.append(cleaned)
    
    if add_numbering:
        lines = [f"{i+1}. {l}" for i, l in enumerate(lines)]
        
    return '\n'.join(lines) + '\n'
```

### Eksekusi Cepat pada File

**Tanpa penomoran:**
```bash
python -c "import re; p=r'(?<!^)\s*(\([0-9]+:[0-9]+(?::[0-9]+)?\)|\b\[[0-9]+:[0-9]+(?::[0-9]+)?\])'; f='TARGET_FILE.txt'; t=open(f, encoding='utf-8').read(); open(f, 'w', encoding='utf-8').write(re.sub(p, r'\n\1', t.strip()) + '\n')"
```

**Dengan penomoran urut (1 nomor 1 baris):**
```bash
python -c "import re; f='TARGET_FILE.txt'; lines=[re.sub(r'^\d+\.\s*', '', l.strip()) for l in open(f, encoding='utf-8') if l.strip()]; open(f, 'w', encoding='utf-8').write('\n'.join(f'{i+1}. {l}' for i, l in enumerate(lines)) + '\n')"
```
