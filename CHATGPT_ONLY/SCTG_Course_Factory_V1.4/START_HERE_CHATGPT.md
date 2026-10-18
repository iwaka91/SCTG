# Mulai dari sini — SCTG Course Factory untuk ChatGPT

**Anda tidak harus memahami Python untuk memakainya.** Unggah ZIP factory ini di sesi ChatGPT yang mampu mengolah file dan menjalankan kode (atau letakkan di workspace Codex/Work). Sampaikan:

> Baca `AGENTS.md` dan `standards/SCTG_V4.3.md` sebagai ketentuan wajib. Jadikan `benchmarks/NUM09 + NUM10_Claude_readonly.html` benchmark mutu pengalaman, bukan template yang disalin. Kita akan mendiskusikan TP dan rancangan sampai disetujui. Setelah perintah Gas Kode, kerjakan implementasi, QA, perbaikan, dan penyerahan HTML sekali jalan, serta jangan menyatakan Final Candidate bila ada FAIL/BLOCKED.

Setelah rancangan disetujui, cukup katakan: **Gas Kode**. Jika ChatGPT tidak mempunyai akses browser lokal, pembuatan file atau pengujian Playwright, ia wajib mengatakannya; hasil tidak boleh dinyatakan sudah lulus QA.

**Sumber file:** `AGENTS.md` (kontrak), `docs/PROMPT_CHATGPT.md` (prompt), `README.md` (cara teknis), `docs/LAPORAN_PEMBANGUNAN_FACTORY.md` (status pembangunan dan batas pengujian). Tidak ada deploy otomatis.

## Upgrade 17 Oktober 2026 — Visual Atelier V1.1
Buka `demos/VISUAL_ATELIER_SHOWCASE.html`; baca `docs/VISUAL_ENGINE_GUIDE.md`, `docs/RUBRIK_VISUAL_GAME.md` dan `benchmarks/MANIFEST.json`. Integrasi engine visual bersifat fungsional dan masuk builder; tidak otomatis memberi skor visual. Lima gate wajib Ya, lalu Toto Gutomo yang menilai subjektif.


V1.3: gunakan Adaptive Performance tanpa pengaturan dari murid; perubahan visual hanya pada beban renderer.


V1.4 (18 Oktober 2026): baca `feedback/2026-10-18/LIT10_POST_RELEASE_REVIEW.md`, `docs/RUBRIK_VISUAL_GAME.md`, dan `docs/VISUAL_BLUEPRINT_TEMPLATE.md`. Bukti game harus berupa kendali dan perubahan dunia, bukan kuis berkostum. Sinematik mendorong headline besar di tengah dengan transisi halus. Mesin kendali arah tersedia di `engine/sctg-steering.js`. LIT10 V1.3 tetap arsip final hasil review; tidak otomatis berubah.
