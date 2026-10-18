# SCTG Factory V1.4 — Lima Gerbang Ya / Tidak (REVISI RESMI)

**Tidak ada lagi skor berbobot dan tidak ada persentase.** Semua gerbang harus `Ya`; satu `Tidak/Belum` = **BLOCKED**. Setelah kelimanya `Ya`, **Toto Gutomo** memberikan rating kualitas subjektif. Tidak ada jaminan 9,9/10 dari kode, model, atau otomatisasi.

**Dasar mutu minimal:** dua course berbeda, NUM09 Claude dan NUM10 Misi Gambut Claude, masing-masing referensi read-only. Jangan meniru ilustrasi atau memakai satu tema untuk seluruh course.

| Gate | Jawaban yang diizinkan | Bukti minimum nyata | Penolakan contoh |
|---|---|---|---|
| **1. Visual premium, identitas artistik, efek 3D/pseudo-3D memanjakan mata** | Ya / Tidak | Cover, game HP + Panggung, dan sinematik; catatan lighting, material volume, layering, parallax, identitas visual tematik | Gradien datar/tombol grid; objek Canvas polos; tak ada kedalaman; layar HP kacau |
| **2. Gameplay dan mekanik interaktif playable** | Ya / Tidak | Tangkapan/replay *aksi pemain dalam dunia* (gerak, kemudi, scan, target, rute, perubahan state) → konsekuensi → menang / ulang | Kuis terselubung; jawaban PG diberi animasi saja; tidak ada kendali ruang/objek/state |
| **3. Pedagogi SCTG V4.3** | Ya / Tidak | TP sah, 3 kolom mengajar–melatih–menguji; 10 langkah; produk dan asesmen valid; aturan gerbang baca/kunci | TP hanya ditagih bukan diajar; HOTS dengan bentuk uji salah; langkah tidak lengkap |
| **4. Sinematik dan pengalaman pengguna** | Ya / Tidak | Adegan 4–6 beat, teks besar **berpusat**, transisi halus, pergerakan kamera/properti tematik, CTA jelas | Slideshow teks datar, tulisan kecil di pojok, CTA salah, visual statis |
| **5. Stabilitas teknis dan aksesibilitas** | Ya / Tidak | Browser QA matriks 13, HP+Panggung, keyboard, no scroll horizontal, fokus tetap, suara, unduhan, resume | Crash, scroll overflow, kehilangan input, PDF rusak, fitur tidak bisa diakses |

## Aturan bukti (wajib)

- `python cli/visual_gate.py init --html <course.html> --review <reports/visual-review.json>` membuat 5 status `belum`.
- Peninjau **benar-benar** melihat screenshot dan memainkan jalur interaksi. Baru mengganti verdict dengan `ya`, menulis temuan spesifik ≥35 karakter, dan mencantumkan berkas bukti yang ada. `cli/visual_gate.py check` hanya memvalidasi *kelengkapan bukti dan kesesuaian SHA*; **tidak dapat memastikan keindahan**.
- Jangan memberi semua Ya demi lolos rilis. `factory.py release` menolak tanpa QA penuh sekaligus laporan lima gate valid.
- Rating pengguna tetap kosong (`user_rating: null`) sampai pengguna secara eksplisit menilai.

## Lima pertanyaan reviewer visual

1. Apa identitas hero scene baru yang tidak ada pada NUM09 atau NUM10?
2. Apakah layering, volume, cahaya, bayangan kontak, kilau, atmosfer dan kamera menghasilkan kedalaman, bukan kartu DOM?
3. Apakah game dapat dimenangkan/dicoba lagi lewat aksi pemain? Apakah feedback terasa dan bisa dibaca?
4. Apakah sinematik menunjukkan peristiwa visual nyata dengan adegan, bukan teks pindah otomatis?
5. Apakah HP 390×700 dan IFP 1280×650 menampilkan semua unsur esensial tanpa bertabrakan?

**Semua Ya → siap penilaian subjektif pengguna.**

## Peningkatan kualitas setelah LIT10 V1.3 (18 Oktober 2026)

Pemilik course menilai **visual 8/10**, teknis **lulus**, dan mutu akhir subjektif **8,2/10**. Ini **bukan skor Factory**, dan tidak memberi izin menaikkan nilai course lama secara otomatis. Penilaian lapangan menyoroti bahwa sesi investigasi kurang terasa seperti permainan; pertarungan Boss masih dominan kuis berkostum. Sinematik teks perlu lebih besar, berada di tengah, dan lebih halus. Contoh pembanding: kendali Susur Sungai dan Roda Nasib SEJX06 serta tipografi sinematik SEJXI08 (lihat lampiran `feedback/2026-10-18/`).

**Syarat Game Gate V1.4:** harus ada bukti tindakan pemain memengaruhi dunia dan keadaan game secara berulang (*world state*), tidak cukup mengklik jawaban PG; minimal satu aktivitas interaktif lain menurut SCTG V4.3. Kendali menggeser arah/menahan kemudi diperbolehkan, tetapi **drag-and-drop objek tetap dilarang**. Mekanik harus sesuai struktur TP. Timer/refleks memicu Jeda Paham standar SCTG, tidak boleh menghilangkan fase belajar.

**Syarat Cinematic Gate V1.4:** tipografi layar utama besar di area tengah, 4–6 beat yang melibatkan visual/kamera/properti bergerak, peralihan mulus, CTA muncul/aktif sesuai alur. Warna/teks harus tetap kontras. Visual yang hanya menampilkan teks berubah otomatis di depan gradien **bukan** keberhasilan gate ini.

CLI V1.4 meminta deskripsi observasi konkret untuk `gameplay_proof` dan `cinematic_proof` sebelum status lima gate bisa valid. CLI memverifikasi kelengkapan, **bukan menilai gameplay/keindahan secara otomatis**. Bukti nyata harus ditinjau manusia.
