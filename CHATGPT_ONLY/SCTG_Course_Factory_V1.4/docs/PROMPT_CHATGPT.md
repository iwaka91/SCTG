# Instruksi siap pakai — ChatGPT untuk course baru

## Saat diskusi

> Kita memakai paket SCTG Course Factory ini. Baca `AGENTS.md` dan dokumen induk `standards/SCTG_V4.3.md`, lalu tentukan Uji Kelayakan TP serta Pola Penawaran untuk course baru. Jangan menulis kode sebelum saya mengucapkan Gas Kode. Jadikan **NUM09 dan NUM10 Claude** sebagai dua benchmark mutu artistik/teknis, bukan desain yang disalin. Setelah pilihan disepakati, buat blueprint yang konkret.

## Saat produksi (setelah keputusan disepakati)

> **Gas Kode.** Produksi sampai Final Candidate dalam satu mandat ini tanpa meminta konfirmasi tambahan untuk revisi internal. Jalankan semua tahap dalam `AGENTS.md`: implementasi orisinal, mekanik game nyata, sinematik, seluruh fitur SCTG V4.3, QA end-to-end, matriks 13 viewport, screenshot Tahap A, evaluasi terhadap mutu NUM09 + NUM10, bugfix, dan full QA ulang. Jangan menyederhanakan fitur atau menghentikan pekerjaan pada MVP untuk menghemat token. Jika browser/tools menghalangi tes, jangan klaim lolos; serahkan bukti dan laporan blocker. Output wajib HTML single-file, QA_REPORT.md, dan 4–6 screenshot + visual-review.json lima gerbang Ya/Tidak. Jangan deploy otomatis.

## Saat evaluasi

> Bandingkan course yang dibangun dengan benchmark NUM09 + NUM10 dan SCTG V4.3. Temukan kegagalan secara empiris, bukan berdasarkan rasa percaya diri model. Bedakan hasil yang diuji, terukur, disampel, dan belum bisa diverifikasi. Perbaiki tanpa mengubah persyaratan pedagogis.

## Untuk satu chat baru

> Gunakan file paket factory ZIP ini sebagai konteks proyek. Jangan mengandalkan memori ringkas. Baca aturan utama dan profil QA sebelum implementasi. Laporkan keterbatasan pengujian dengan jujur.
