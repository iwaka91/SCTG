# Factory V1.2 — pembaruan performa

- Basis: Factory V1.1 dengan benchmark Claude NUM09 + NUM10 yang tetap read-only.
- Mesin `engine/sctg-performance.js` (Hemat/Standar/Ultra) otomatis masuk Single HTML.
- Render `engine/sctg-visual.js` menghormati budget DPR dan target FPS, berhenti saat layar tersembunyi, membersihkan listener saat destroy.
- Peraturan QA untuk artefak glyph Unicode dan pergantian canvas node.
- 9 unit tests lulus termasuk integrasi builder.
- LIT10 V1.2 terpisah: ikon dokumen vektor, cache dua latar, mode performa, animasi Hemat, renderer tanpa desynchronized.
- Limitasi: belum ada benchmark FPS perangkat rendah, pengujian lintas gawai fisik, dan uji jalur 10 langkah terbaru.
