# SCTG Course Factory V1.3 — NUM09 + NUM10 Golden Benchmark & Visual Atelier

**Status:** Paket kerja fungsional untuk produksi dan pengujian, **bukan** course baru atau sertifikat mutu otomatis. Dirancang untuk proyek SCTG V4.3. Tidak ada deployment atau perubahan repositori GitHub pengguna.

## Tujuan

Memaksa proses produksi e-course ChatGPT melakukan **build → browser QA → visual review → perbaikan internal → full QA → Final Candidate**, bukan menyerahkan prototipe 5,5/10 lalu meminta persetujuan revisi. NUM09 dan NUM10 Claude adalah **dua** contoh independen mutu desain dan mekanik, bukan kode yang harus disalin. File `standards/SCTG_V4.3.md` adalah aturan utama, dan dokumen `AGENTS.md` adalah kontrak operasi agen ChatGPT/Codex.

## Struktur penting

| Folder/file | Kegunaan |
|---|---|
| `AGENTS.md` | Aturan implementasi khusus ChatGPT (dibaca pertama kali). |
| `standards/SCTG_V4.3.md` | Dokumen resmi lengkap, single source of truth. |
| `benchmarks/NUM09_Claude_readonly.html` & `benchmarks/NUM10_Misi_Gambut_Claude_readonly.html` | Dua referensi Claude **baca saja**, kode NUM09 dan NUM10 terpisah. `MANIFEST.json` menyimpan hash keutuhan keduanya. |
| `benchmarks/evidence/` | Bukti referensi NUM09, serta cover, game HP/IFP, Ruang Baca, Final Boss NUM10. Capture NUM10 memakai state pratinjau lokal; BUKAN sertifikasi alur siswa. |
| `engine/sctg-core.js` | Fondasi SessionStore, SilentGate, StageMode, CanvasLoop, StepNavigation. |
| `engine/sctg-cinematic.js` | Orkestrasi sinematik 4–6 beat; seni adegan wajib dibuat spesifik course. |
| `engine/sctg-visual.js`, `engine/sctg-visual.css` | **Mesin visual nyata**, otomatis disatukan oleh `build`. Pseudo-3D: kedalaman isometrik, gradient lighting, soft shadows, parallax, fog, highlights, dan interaksi Canvas; tema tetap wajib dibuat khas course. |
| `demos/VISUAL_ATELIER_SHOWCASE.html` | Pratinjau offline mandiri tiga dunia visual, bukan course. PNG pendamping ada di `demos/atelier_*.png`. |
| `cli/visual_gate.py` | Pemeriksaan lima gerbang **Ya/Tidak** berbasis bukti; tidak ada persentase atau skor AI. |
| `cli/check_benchmarks.py` | Pastikan kedua benchmark Claude tetap utuh. |
| `docs/VISUAL_BLUEPRINT_TEMPLATE.md` | Rancangan estetika wajib sebelum produksi course. |
| `engine/sctg-layout.css` | Rel tiga pita, target sentuh, width-fit, reduced motion, silent unlock. |
| `cli/factory.py` | Perintah buat folder course, paket single HTML, release gate. |
| `cli/qa.py` | Pengujian Playwright sesuai profil course, matriks 13 ukuran, laporan, bukti screenshot, status FAIL/BLOCKED/PASS. |
| `profiles/` | Skema profil QA dan kontrol regresi untuk GPT/Claude. |
| `starter/` | Starter (sengaja **belum** jadi course, tidak bisa lolos QA). |
| `demos/Misi_Gambut_GPT_REJECTED.html` | Contoh nyata produk yang harus ditolak penguji. |
| `reports/regression_gpt/` | Hasil deteksi kesalahan GPT yang benar-benar dijalankan. |
| `tests/` | Test unit fondasi teknis. |

## Cara pakai dalam ChatGPT

1. Simpan dan unggah ZIP ini di chat pengembangan course, atau masukkan isinya ke repo kerja yang diakses ChatGPT melalui Codex/Work. **Jangan hanya mengunggah HTML Misi Gambut lama**; itu kontrol gagal.
2. Minta ChatGPT membaca `AGENTS.md`, `standards/SCTG_V4.3.md`, benchmark NUM09 + NUM10, dan `docs/PROTOKOL_QA.md`. Saat mode diskusi, tetapkan TP dan 10 langkah sesuai SCTG.
3. Setelah keputusan disepakati, perintah **"Gas Kode: bangun dan uji sampai semua gate lolos, lalu kirim Final Candidate atau laporan blocker yang terverifikasi"**.
4. ChatGPT wajib menggunakan CLI QA, melengkapi profil interaksi per course, memeriksa screenshot, dan melakukan perbaikan sendiri sebelum penyerahan.
5. Pengujian teknis **tidak otomatis membuktikan kelulusan visual tanpa review nyata**. Toto Gutomo tetap memberi rating subjektif setelah semua lima gerbang Ya.

## Cara jalankan di komputer lokal

Perlu Python 3.10+, paket `playwright`, dan Chromium. Instal dependensi:

```bash
python -m pip install playwright
python -m playwright install chromium
```

Buat scaffold untuk course yang **belum dirancang** (contoh):

```bash
python cli/factory.py init LIT10 --title "Judul Perjalanan Belajar" --series LIT
```

Setelah mengisi `DESIGN_BRIEF.md`, `course.js`, `course.css`, `course.html` dan skenario `qa-profile.json`, hasilkan single HTML:

```bash
python cli/factory.py build --src courses/LIT10 --out courses/LIT10/dist/index.html
```

Saat iterasi, jalankan QA singkat:

```bash
python cli/qa.py --html courses/LIT10/dist/index.html --profile courses/LIT10/qa-profile.json --out reports/LIT10 --fast
```

Sebelum final **wajib ulang tanpa `--fast`**:

```bash
python cli/qa.py --html courses/LIT10/dist/index.html --profile courses/LIT10/qa-profile.json --out reports/LIT10
python cli/visual_gate.py init --html courses/LIT10/dist/index.html --review reports/LIT10/visual-review.json
# Isi Ya/Tidak beserta bukti PNG dan catatan review nyata, kemudian:
python cli/visual_gate.py check --html courses/LIT10/dist/index.html --review reports/LIT10/visual-review.json
python cli/factory.py release --html courses/LIT10/dist/index.html --report reports/LIT10/qa-result.json --visual-review reports/LIT10/visual-review.json --out courses/LIT10/FINAL_CANDIDATE
```

Release akan **ditolak** bila ada FAIL/BLOCKED, transport sandbox, profil belum lengkap, hash HTML berubah, file benchmark berubah, atau salah satu dari lima gerbang belum **Ya** dengan bukti nyata. Satu ❌ = tidak layak rilis. **Hanya pengguna yang berhak memberi rating subjektif**, setelah kelimanya lolos.

## Mode QA ketika jaringan localhost diblokir

Lingkungan tertentu, termasuk lingkungan pengujian paket ini, melarang browser membuka alamat localhost maupun file://. Untuk **triase saja**, jalankan:

```bash
python cli/qa.py --html demos/Misi_Gambut_GPT_REJECTED.html --profile profiles/Misi_Gambut_GPT_known_fail.json --out reports/regression_gpt --fast --transport sandbox
```

Transport sandbox menggunakan DOM offline dan localStorage **tiruan**, sehingga laporan selalu `NOT_RELEASE_READY`; tidak boleh dipakai sebagai bukti telah lulus tes persistensi asli, unduhan file Android, ataupun publikasi.

## Rujukan lanjutan

- `docs/PROTOKOL_QA.md` — pengukuran dan ambang penolakan
- `docs/PROFIL_QA.md` — bahasa langkah uji yang dapat dieksekusi
- `docs/PROMPT_CHATGPT.md` — instruksi siap pakai saat mode diskusi/Gas Kode
- `docs/TEMUAN_REGRESI.md` — bukti kontrol terhadap produk GPT yang ditolak

**Penting:** Factory ini adalah fondasi QA + runtime, bukan generator keindahan otomatis. ChatGPT tetap harus membuat arah artistik dan mekanik permainan orisinal untuk setiap course. Tanpa waktu untuk inspeksi visual dan bermain langsung, hasil tidak boleh disebut Final Candidate.


## Riwayat V1.2
Factory sebelumnya mengenalkan tiga tingkat performa manual. **Pengaturan manual tersebut sudah dinonaktifkan dan tidak berlaku pada V1.3**.


## V1.3 — Adaptive Otomatis

Mesin Canvas menyesuaikan kualitas secara otomatis, tanpa pilihan Hemat/Standar/Ultra di UI murid. Lihat `docs/ADAPTIVE_PERFORMANCE_V1_3.md` dan jalankan tes.

Salah satu contoh implementasi course lengkap disimpan di `examples/LIT10_CANDIDATE_v1_3.html`. Contoh ini belum dinyatakan lolos lima Quality Gate secara penuh sampai diperiksa pada perangkat siswa.

Mesin Canvas menyesuaikan kualitas secara otomatis, tanpa pilihan Hemat/Standar/Ultra di UI murid. Lihat `docs/ADAPTIVE_PERFORMANCE_V1_3.md` dan jalankan tes.


## V1.4 — Gameplay & Cinematic Quality Loop

- `engine/sctg-steering.js` menambah kontrol gerak pemain dengan sentuh/geser arah, tombol arah hold dan keyboard, state dunia, target, benturan, win/retry. **Tidak** drag-and-drop objek.
- `engine/sctg-cinematic-typography.css` menambah teks sinematik tengah layar, berukuran besar, animasi halus; kursus harus menyediakan adegan bergerak dan makna.
- `demos/STEERING_CINEMATIC_V1_4.html` adalah demonstrasi kontrol dan tipografi, **bukan course siap rilis**.
- `cli/visual_gate.py` sekarang memakai schema `SCTG-5-GATES-1.2` dan mewajibkan `gameplay_proof` serta `cinematic_proof` berdasarkan observasi. Form lama perlu dibuat ulang saat QA course baru.
- Kritik dari LIT10 V1.3 dan contoh gambar dari SEJX06/SEJXI08 tercatat di `feedback/2026-10-18/`; tidak ada modifikasi course lama.

- `cli/feedback_loop.py` mencatat penilaian pengguna menjadi audit trail tanpa mengarang angka atau mengubah source; `feedback/PROCESS.md` menjelaskan langkah lintas-course.
