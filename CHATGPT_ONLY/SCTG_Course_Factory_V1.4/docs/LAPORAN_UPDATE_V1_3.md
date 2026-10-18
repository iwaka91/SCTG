# Laporan pembaruan — SCTG Factory V1.3 dan LIT10 V1.3
Tanggal: 18 Oktober 2026

## Keputusan pengguna yang diterapkan
- Tidak ada antarmuka pengaturan Hemat/Standar/Ultra untuk siswa.
- **Adaptive berjalan otomatis**, dimulai pada render konservatif lalu menilai waktu render Canvas dan jeda requestAnimationFrame.
- Mesin dapat menurunkan beban bila tertinggal dan menaikkan kualitas jika lancar stabil dalam periode panjang, dengan hysteresis agar kualitas tidak berfluktuasi.
- Prioritaskan keterbacaan, kendali sentuh, timer pedagogis, progres, dan akurasi jawaban; hanya beban gambar yang berubah.
- Mode manual versi sebelumnya yang tersimpan dalam localStorage diabaikan. Tidak menggunakan CDN atau telemetri.

## File
- Factory: `SCTG_Course_Factory_V1_3_Adaptive_Otomatis.zip`.
- Course: `LIT10_Misteri_Dokumen_Palsu_SCTG43_v1_3_Otomatis.html`.
- Di ZIP, salinan identik LIT10 terdapat di `examples/LIT10_CANDIDATE_v1_3.html`. NUM09/NUM10 Claude tidak diubah.

## Perubahan di Factory
- `engine/sctg-performance.js` diganti dengan pengatur performa mandiri V1.3; menghapus API publik `setMode`.
- `engine/sctg-visual.js` dan `engine/sctg-core.js` memberi sampel durasi render aktif; Canvas dapat di-resize saat kualitas berubah tanpa membangun ulang DOM pelajaran.
- Aturan AGENTS, README, dan dokumen kinerja diperbarui. QA tetap lima gate biner Ya/Tidak; tidak ada rating otomatis.

## Perubahan pada LIT10
- Pemilih performa di cover dihapus.
- Engine adaptif yang sama dengan Factory tertanam satu file dalam HTML LIT10.
- Loop requestAnimationFrame lama dicegah hidup kembali ketika kualitas otomatis berubah, untuk menghindari loop ganda dan penumpukan beban CPU.
- Sistem gambar dokumen berbasis vektor, perbaikan Canvas agar tetap hidup setelah aksi, serta soal di dekat opsi tetap dipertahankan dari V1.2.

## Pengujian aktual
- Unit test Factory: **10/10 LULUS** (termasuk integritas dua benchmark, builder, adaptif tanpa kontrol pengguna, Canvas, QA).
- Browser Chromium `page.set_content`: ukuran **360×560, 390×700, 900×500, 1280×650** lulus pengujian awal. Pemilih tidak ada; peralihan kualitas otomatis yang disimulasikan tidak membuat arena game atau Boss menjadi kosong. Tidak terlihat permintaan jaringan eksternal dan tidak ada JavaScript page errors dalam uji tersebut.
- Uji interaksi pada 390×700: arsip A dihubungkan → Canvas tetap tergambar; serangan Boss pertama → Boss tetap tergambar; tidak ada JS error.
- Builder Factory menghasilkan Single HTML demo dan memuat engine V1.3; ZIP + SHA256SUMS diverifikasi.

## Batas / status
- **Belum** divalidasi pada Xiaomi 13T atau HP siswa sesungguhnya; FPS nyata, suhu, baterai, serta dukungan untuk 90% HP siswa **belum dapat diklaim**.
- Simulasi browser menggunakan mode tanpa GPU hardware; pengujian perangkat fisik tetap dibutuhkan.
- Belum full-path QA terlengkap lintas 13 ukuran pada V1.3, belum tes seluruh skenario materi/asesmen V1.3. Belum semua lima gerbang layak diberi status Ya.
- Penilaian visual 8/10 adalah umpan balik pengguna terhadap versi sebelumnya, tidak diubah menjadi rating V1.3.
- Tidak ada perubahan pada GitHub ataupun situs produksi.
