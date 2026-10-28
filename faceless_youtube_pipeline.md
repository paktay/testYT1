# Visual Pipeline Produksi Konten YouTube Faceless & Kepatuhan Monetisasi

Dokumen ini memetakan arsitektur pipeline produksi multi-agent berdasarkan standar [`skill.md`](file:///d:/projects/YT-Faceless-Automation/.agents/skills/youtube-monetization/skill.md) untuk memastikan konten 100% aman dari dismonetisasi (*reused/repetitive content* dan pedoman pengiklan).

---

## 🗺️ Visual Architecture Pipeline

```mermaid
flowchart TD
    Start([Ide Awal / Niche Domain]) --> Agent1["1. Niche & Trend Finder Sub-Agent"]
    
    subgraph S1["Tahap 1: Validasi Pasar & Kepatuhan Awal"]
        Agent1 --> FilterYMYL{"Filter YMYL & Kejenuhan"}
        FilterYMYL -- Gagal --> Reject1[Batalkan / Reorientasi Topik]
        FilterYMYL -- Lolos --> Brief[Creative & Topic Brief]
    end

    subgraph S2["Tahap 2: Riset & Storytelling Asinkron"]
        Brief --> Agent2["2. Script & Research Sub-Agent"]
        Agent2 --> AsyncResearch["Asynchronous Case Study Research"]
        AsyncResearch --> DraftScript[Draft Naskah Lengkap]
        DraftScript --> HITL1["👤 Human-in-the-Loop Review (Gaya Bahasa & Jiwa)"]
    end

    subgraph S3["Tahap 3: Audit Kepatuhan AI & Regulasi"]
        HITL1 --> Agent3["3. AI Disclosure & Compliance Sub-Agent"]
        Agent3 --> SynthCheck{"Deteksi Suara/Visual Sintetis?"}
        SynthCheck -- Ya --> FlagSynth["Beri Flag: Altered/Synthetic Content"]
        SynthCheck -- Tidak --> CleanLabel["Beri Flag: Standard Clean"]
    end

    subgraph S4["Tahap 4: Pengarahan Adegan & Dinamika Visual"]
        FlagSynth --> Agent4["4. Creative Scene & B-Roll Director"]
        CleanLabel --> Agent4
        Agent4 --> Storyboard["Storyboard & Multi-Source B-Roll Plan"]
        Storyboard --> AntiRepetitive{"Check Aturan Anti-Repetitive (>3s Rule)"}
        AntiRepetitive -- Lolos --> RenderPackage[Visual Production Pack]
    end

    subgraph S5["Tahap 5: Gatekeeper Final & Validasi YPP"]
        RenderPackage --> Agent5["5. Final Quality Controller Sub-Agent"]
        Agent5 --> YPPAudit{"Audit 100% YPP & Advertiser Friendly"}
        YPPAudit -- Skor < 100% --> ReviseLoop[Perbaikan Terarah]
        ReviseLoop -. Revisi Naskah/Visual .-> Agent2
        YPPAudit -- Skor 100% --> FinalExport([✅ Siap Publish & Monetisasi])
    end

    style Agent1 fill:#2563eb,stroke:#1d4ed8,stroke-width:2px,color:#fff
    style Agent2 fill:#0d9488,stroke:#0f766e,stroke-width:2px,color:#fff
    style Agent3 fill:#d97706,stroke:#b45309,stroke-width:2px,color:#fff
    style Agent4 fill:#7c3aed,stroke:#6d28d9,stroke-width:2px,color:#fff
    style Agent5 fill:#059669,stroke:#047857,stroke-width:2px,color:#fff
    style FinalExport fill:#16a34a,stroke:#15803d,stroke-width:3px,color:#fff
```

---

## 🤖 Spesifikasi 5 Sub-Agent

### 1. Niche & Trend Finder Agent
- **Tanggung Jawab:** Validasi topik dengan rasio demand tinggi dan saturasi rendah.
- **Guardrail Kepatuhan:** Memblokir topik YMYL berbahaya (klaim finansial cepat kaya, saran medis berbahaya).
- **Format Output:** Topic Brief (Target Audience, Unsold Angle, Resiko Regulasi).

### 2. Script & Research Agent
- **Tanggung Jawab:** Menyusun narasi berbasis *hook* emosional, perbandingan kritis, dan penyusunan cerita dramatis.
- **Guardrail Kepatuhan:** Mengeliminasi frasa AI klise (*"Pernahkah Anda berpikir..."*, *"Dalam era modern..."*), menyuntikkan orisinalitas di 30 detik pertama.
- **Format Output:** Script Lengkap dengan penanda segmen waktu & emosi audio.

### 3. AI Disclosure & Compliance Agent
- **Tanggung Jawab:** Memindai risiko *synthetic media* sesuai aturan transparansi YouTube.
- **Guardrail Kepatuhan:** Menentukan apakah video memerlukan penandaan biner *"Altered or Synthetic Content"* pada YouTube Creator Studio.
- **Format Output:** Compliance Ledger & Disclosure Checklist.

### 4. Creative Scene & B-Roll Director
- **Tanggung Jawab:** Mengonversi narasi menjadi panduan *storyboard* dinamis dengan minimal 3 lapisan visual per 10 detik.
- **Guardrail Kepatuhan:** Tidak boleh ada gambar statis >3 detik tanpa *motion* (*pan/zoom*), rotasi sumber aset (stok klip, grafik data, tipografi kinetik) untuk mematahkan deteksi *repetitive content*.
- **Format Output:** JSON/Markdown Scene Manifest (Waktu, Visual Cue, Motion Directive, Sound FX).

### 5. Final Quality Controller (Gatekeeper Agent)
- **Tanggung Jawab:** Evaluasi ambang 100% kelayakan monetisasi.
- **Guardrail Kepatuhan:** Melarang kata sensitif, memeriksa hak cipta musik, orisinalitas nada suara, serta sinkronisasi nilai tambah.
- **Format Output:** QC Scorecard & Final Release Approval.
