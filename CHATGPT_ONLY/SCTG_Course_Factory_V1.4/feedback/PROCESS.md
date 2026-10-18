# Feedback Loop — siklus per course yang dinyatakan final oleh pengguna

1. **Catat fakta pengguna.** Skor visual dan keseluruhan, status teknis, dan catatan asli; jangan buat skor sendiri. CLI `python cli/feedback_loop.py --course LIT10 --version v1_3 --technical lulus --visual 8 --rating 8.2 --notes "..."` hanya membuat laporan, tidak mengubah HTML.
2. **Pisahkan keterbatasan course dari masalah Factory.** Hanya perubahan lintas-course masuk modul engine/kontrak/QA; perbaikan course lama tetap perlu izin.
3. **Ubah catatan menjadi aturan yang dapat ditinjau dan diuji:** gameplay yang benar-benar dimainkan, storyboard sinematik, bukti galeri, regresi HP dan layar panggung.
4. **Uji benchmark dan build, kemudian beri nomor versi Factory.** Jangan mengklaim rating baru sampai pengguna menilai course berikutnya.
5. **Target efisiensi:** 1x build mendekati Final Candidate, 1x revisi menuju final, tetapi QA tidak boleh dilewati demi target.

SCTG V4.3 tetap sumber aturan utama. Review pengguna menjadi input peningkatan Factory, bukan mengganti standar tanpa persetujuan.
