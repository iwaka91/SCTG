# PERINTAH WAJIB UNTUK CHATGPT / CODEX — SCTG Course Factory

Dokumen ini ditujukan sebagai instruksi agen otomatis di akar proyek. **Sumber kebenaran tentang course adalah `standards/SCTG_V4.3.md`**, bukan ringkasan ini. Simpan file itu utuh; jika versi baru diberikan Toto Gutomo, ikuti instruksi terbaru dan perbarui standarnya. Untuk TKA tetap SCTG V.2.

## Kontrak kerja
1. **MODE DISKUSI** sampai Toto Gutomo secara eksplisit memerintahkan *Gas Kode / Bangun Kode / Update Kode*. Di mode diskusi: Uji Kelayakan TP, tawarkan Pola Penawaran (Final Boss, Gerbang Baca, sinematik ✅/❌, kontrol game, durasi, 10 langkah).
2. Saat sudah *Gas Kode*, itu adalah izin menyelesaikan **seluruh siklus produksi dalam permintaan yang sama**, tidak perlu persetujuan tambahan untuk QA, refactoring, polishing, dan pengujian lokal. Jangan meminta pengguna memilih "audit dulu" versus "V2". Tidak boleh mengubah/deploy course produksi lain tanpa izin.
3. Target internal mutu visual 9,9 dan target penerimaan 5 gerbang Ya/Tidak bukan angka yang dapat dicetak otomatis. Tolak klaim skor tanpa bukti. **Dua benchmark minimum persepsi mutu adalah `benchmarks/NUM09_Claude_readonly.html` dan `benchmarks/NUM10_Misi_Gambut_Claude_readonly.html`**; jangan menyalin tema/ilustrasinya atau menganggap satu referensi berlaku untuk semua materi.
4. Gunakan **desain artistik spesifik topik**, storyboard sinematik 4–6 beat + kejutan dan suara, serta **game nyata** dengan state, aksi pemain, konsekuensi, kemenangan/kondisi ulang. Quiz biasa berkulit Canvas bukan game nyata.
5. Implementasi wajib **single HTML offline**, bisa dibuka tanpa CDN atau backend, siap Netlify. Gunakan `engine/` sebagai modul teknis opsional dan rancang visual/aktivitas baru per course. Header harus sama persis ketentuan SCTG V4.3. Ikuti prioritas aturan pada dokumen sumber.
6. **Dilarang mengganti DOM input yang sedang difokuskan** akibat `resize`, `visualViewport.resize`, keyboard virtual, timer berakhir, atau perubahan tema. Simpan tulisan murid tanpa kehilangan fokus. Scroll horizontal = kegagalan.
7. **Kunci Senyap**: waktu habis hanya tombol awal yang menjadi aktif, status timer jadi ✅. Tidak ada bunyi, toast, glow, pulsasi, scroll/fokus, overlay yang memaksa siswa melanjutkan. Siswa boleh tetap membaca.
8. Game tiga pita **Soal–Arena–Jawaban/Kontrol** dalam satu layar (Genggam & Panggung), Canvas 2D berisi dunia visual pseudo-3D, sentuh langsung; jangan mengandalkan kontrol virtual saja. Mode Panggung aktif tepat untuk landscape w≥900 dan h≥500. Mode Genggam width-fit.
9. Gunakan **QA serta `cli/visual_gate.py` (lima keputusan Ya/Tidak) sebagai gerbang fail-closed**, bukan formalitas. Kerjakan pengujian nyata untuk murid normal, EZ, Fasil, ketik keyboard, game sukses/gagal, Gerbang Baca, Jeda Paham, Kunci Senyap, Final Boss loop, unduhan PDF, WA/cadangan, reset/resume. Isi `qa-profile.json` berbasis selector dan interaksi nyata. Semua viewport SCTG; jangan isi `approved` tanpa bukti.
10. Jalankan `python cli/qa.py --html ... --profile ... --out ...` dengan **transport `http`** pada mesin yang mendukung localhost. `--transport sandbox` hanya triase pada lingkungan browser terbatas; tidak bisa mensertifikasi penyimpanan asli atau final release. Gunakan `--fast` hanya selama iterasi, **selalu full matrix sebelum release**.
11. Lakukan *visual review* 4–6 screenshot Tahap A dan bandingkan **dengan mutu kedua benchmark NUM09 dan NUM10** untuk komposisi, depth, karakter, tekstur, dramaturgi sinematik, kemampuan bermain. Screenshot yang dihasilkan tidak membuktikan desain bagus; tulis catatan evaluasi dan revisi. Penilaian rasa di perangkat akhir tetap oleh Toto Gutomo.
12. **Release hanya jika seluruh pengujian wajib `PASS`, lima gerbang `Ya` dengan bukti nyata, dan semua pemeriksaan manual terdokumentasi**. Nilai subjektif diberikan Toto Gutomo setelah kelimanya Ya, bukan perhitungan otomatis. Bila ada bug, `FAIL` atau `BLOCKED`, ulangi perbaikan dan pengujian selama masih dapat dilakukan; jangan kirim prototipe sambil meminta konfirmasi tahapan. Jika lingkungan membatasi pengujian, sebutkan kegagalan dan serahkan hasil sebagai **belum layak final**, bukan Final Candidate.

## Rangkaian tindakan standar satu kali Gas Kode
- Baca standar dan DESIGN_BRIEF; pelajari implementasi benchmark (read-only); tulis rancangan artistik & mekanik konkret.
- Implementasi HTML single-file; perhatikan seluruh navigasi, aksesibilitas, konten, asesmen, dan luaran.
- Jalankan `node --check engine/*.js` satu per satu, `python -m unittest discover -s tests -v`, dan `python cli/qa.py`.
- Iterasi build–test–fix secara internal. Pastikan pengujian mencakup semua jalur dan ada hasil screenshot.
- Komit artefak: `index.html`, `QA_REPORT.md`, 4–6 bukti visual, `CHANGELOG.md`. **Jangan mengklaim lulus jika laporan berisi FAIL/BLOCKED**.
- Jangan unggah ke GitHub atau Netlify kecuali diminta; penyerahan ZIP/HTML bukan deploy.

## Kegagalan sejarah yang harus dicegah
- NUM Misi Gambut GPT (demos/Misi_Gambut_GPT_REJECTED.html): skor lapangan **3/10, tidak layak publikasi**. Visual 5,5/10, teknis 6/10, game 1/10, sinematik 1/10. Keyboard menutup/isi input hilang saat resize, overflow horizontal, game Canvas tidak dimainkan, kunci senyap meleset. Laporan pembuktian ada di `reports/regression_gpt/`.
- NUM09 Claude digunakan sebagai **batas bawah benchmark estetika/pengalaman**, bukan klaim bahwa seluruh aspek dari referensi telah lolos SCTG V4.3 (kode referensi mungkin dibuat sebelum pasal baru tertentu).

## Aturan baru V1.1 (keputusan 17 Oktober 2026)
- **Dua referensi berbeda**: NUM09 Claude dan NUM10 Misi Gambut Claude; keduanya read-only dan harus lolos `python cli/check_benchmarks.py` sebelum build.
- Setiap course punya `VISUAL_BLUEPRINT.md`: objek hero, bahan, tekstur, cahaya, jarak kamera, komposisi, transisi sinematik, dan komparasi terhadap kedua benchmark.
- Mesin `SCTGVisual` pada `engine/sctg-visual.js` ditanam otomatis ke single HTML oleh builder; gunakan bila sesuai, lalu **buat lukisan dunia baru** dan game nyata dengan state yang orisinal. Jangan mengirim showroom sebagai course.
- Lima **Ya/Tidak**: kualitas visual/3D/memanjakan mata, gameplay playable, pedagogi V4.3, sinematik/UX, stabilitas/aksesibilitas. Satu `Tidak/Belum` menghentikan rilis. **Tidak ada bobot atau persentase.** Setelah semua Ya, Toto Gutomo memberi rating subjektif.
- Screenshot preview benchmark (jika memakai pratinjau state fasilitator) tidak boleh dijadikan bukti flow siswa normal.


## Adaptive performance V1.2 (WAJIB)
Gunakan engine/sctg-performance.js, uji hemat/standar/ultra; jangan memakai glyph unicode pada Canvas sebagai ikon; cache bagian statis, batasi DPR/FPS; mode hemat tak boleh menghapus isi TP dan interaksi. Uji Canvas setelah renderStep/mengganti node, bukan hanya saat loading.


Aturan Factory V1.3: jangan tampilkan pemilih kualitas/performa kepada murid. Adaptive berjalan otomatis, berdasarkan kelancaran rendering yang diukur. Jangan ubah timing/penilaian pembelajaran karena perangkat lambat.


## Aturan pasca-evaluasi LIT10 (Factory V1.4, 18 Oktober 2026)
- **Input review pengguna:** teknis LIT10 V1.3 lulus; visual 8/10; skor subjektif final 8,2/10. Tetap simpan skor pengguna, jangan menyimpulkan 9,9/10. Course final tidak dirombak otomatis hanya karena Factory diperbarui.
- **Setiap course yang dinyatakan layak publikasi menjadi bahan belajar Factory:** tambahkan ke `feedback/` ringkasan rating dan temuan, perbaiki kontrak/engine/test yang lintas-course, verifikasi regresi, jangan mengganti SCTG V4.3 tanpa persetujuan.
- Sebelum membangun game pilih dari **sekurang-kurangnya 3 alternatif mekanik** yang relevan dengan TP (permainan kejar target, kendali perjalanan, klasifikasi conveyor, radar, dll). Pilih satu yang kuat; **tidak wajib tiga game per course**. Aktivitas utama harus punya aksi fisik interaktif yang mengubah state dunia, konsekuensi, progres, dan kondisi hasil; quiz berkostum saja tidak lolos.
- Untuk kendali sentuh: **menggeser jari untuk mengemudikan pemain, menekan/menahan kontrol arah, joystick virtual, atau menyentuh target bergerak boleh**. Larangan drag-and-drop SCTG V4.3 tetap berlaku pada memindahkan kartu/objek jawaban antar-kolom.
- Sinematik gunakan teks besar di **tengah layar** dengan transisi mulus, dukung komposisi panggung, visual/objek/kamera berubah per beat. Target sekitar 15–25 detik sesuai SCTG, 4–6 beat; hindari film teks statis. `engine/sctg-cinematic-typography.css` dan `SCTGCinematic.CinematicDirector` menyediakan pola dasar, course harus memberi adegan orisinal.
- `engine/sctg-steering.js` adalah **mekanik navigasi reusable**, bukan mekanik wajib untuk semua TP; gunakan bila logis, tambah Jeda Paham pada permainan yang bertekanan waktu/refleks, dan jangan mengubah TP demi game.
- `cli/visual_gate.py` schema 1.2 meminta **gameplay_proof** dan **cinematic_proof** dengan catatan observasi nyata. Tidak cukup mengisi Ya pada lima gate. Tidak boleh memalsukan bukti.
- Sasaran proses: *satu pembangunan serius menghasilkan Final Candidate*, lalu maksimal satu siklus revisi umpan balik menuju Final **bila semua pemeriksaan lolos**. Ini sasaran efisiensi, bukan alasan meloloskan bug atau melewati pengujian.
