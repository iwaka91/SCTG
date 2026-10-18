# SCTG Factory V1.1 — Hasil Integrasi NUM10 Claude

**Tanggal:** 17 Oktober 2026 · **Status:** paket Factory yang dapat dipakai, belum sertifikasi course akhir.

## Yang sudah diperbaiki secara konkret

1. **Dua baseline berbeda.** NUM09 Claude asli tetap dipertahankan. NUM10 Misi Gambut Claude dimasukkan ke `benchmarks/NUM10_Misi_Gambut_Claude_readonly.html` dengan SHA256 dan identitas NUM10 di manifest. File sumber **tidak** dimodifikasi.
2. **Rujukan visual NUM10 nyata.** Hasil tangkapan layar cover 390×700 + 1280×650; game Jeep 390×700 + 1280×650; Final Boss dan Ruang Baca 1280×650 ada di `benchmarks/evidence`. Tangkapan selain cover memakai state Fasil pratinjau dalam memori browser untuk akses cepat ke layar; **bukan bukti kelulusan jalur murid atau keamanan kode guru**.
3. **Canvas Visual Atelier.** `engine/sctg-visual.js` + `engine/sctg-visual.css`: depth panggung isometrik, parallax, atmosfer dan kabut, pencahayaan berlapis, highlight, warna tematik, animasi responsif, interaksi klik/sentuh, dan penanganan reduced-motion. Keduanya **selalu** tertanam saat `factory build`, tidak memerlukan CDN.
4. **Starter course visual.** Cover starter baru otomatis memakai mesin Canvas dengan identitas dunia awal berdasarkan series LIT/NUM/SEJ. Ini menghilangkan masalah halaman starter polos. Pengembang **wajib mengganti adegan khas course** untuk lolos review visual.
5. **Tiga dunia demo benar-benar jalan.** `demos/VISUAL_ATELIER_SHOWCASE.html` dapat dibuka sebagai satu HTML; Literasi (buku/pilar), Numerasi (kristal/orbit), Sejarah (portal waktu). Contoh ini bukan course dan tidak dihitung lulus gameplay/pedagogi.
6. **QA lima Ya/Tidak, bukan bobot %.** `cli/visual_gate.py` menolak status kosong/Tidak, bukti tidak nyata, catatan kurang spesifik, perubahan SHA course, serta benchmark yang tidak lengkap. `factory release` perlu sertifikasi QA teknis dan file bukti lima gate; rating Toto Gutomo tidak boleh dibuat otomatis.
7. **Kontrak agen + blueprint.** Perintah visual dalam `AGENTS.md`, `docs/VISUAL_BLUEPRINT_TEMPLATE.md`, `docs/VISUAL_ENGINE_GUIDE.md`, rubrik biner dan contoh instruksi diperbarui.

## Yang sudah diuji di lingkungan ini

- SHA256 kedua benchmark dan ZIP NUM09 diverifikasi utuh.
- `python -m unittest discover -s tests -v`: unit test engine awal dan visual atelier baru (termasuk browser Chromium) **lulus**.
- Browser rendering demo di **390×700 dan 1280×650**, penggantian dunia, reaksi sentuh, tidak ada horizontal overflow, tidak ada JS exception.
- Build demo-scaffold melalui `python cli/factory.py build`: engine visual dan CSS masuk dalam satu HTML.
- Uji negatif: formulir lima gate kosong dan bukti palsu ditolak.

## Batas dan risiko

- **Belum ada course baru SCTG 10 langkah yang dinyatakan 9,9/10.** Perlu membangun satu course nyata dari Factory dan memainkan semua jalur sebelum mengklaim peningkatan kualitas produk.
- Visual Atelier adalah renderer fondasi; ia **tidak menciptakan desain 3D tematik dan dramaturgi final otomatis**. Membuat dunia/karakter/grafis yang memukau tetap pekerjaan pengembangan course dan review.
- Akses localhost/file:// dibatasi dalam browser pengujian ini. Tes bisa dilakukan melalui `page.set_content`, tetapi QA *full native origin* 13 viewport, download Android, dan IFP fisik **belum disertifikasi**.
- Lima gate adalah keputusan berdasar observasi/bukti, tidak boleh otomatis diisi Ya oleh model. Rating 9,9/10 tetap semata penilaian subjektif Toto Gutomo.
- Tidak ada perubahan pada repositori GitHub atau situs produksi.
