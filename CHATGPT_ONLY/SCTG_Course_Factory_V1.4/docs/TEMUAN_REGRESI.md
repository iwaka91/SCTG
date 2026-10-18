# Regression control — kegagalan nyata Misi Gambut GPT

Status lapangan dari Toto Gutomo: **3/10 — tidak layak publikasi**. Subskor: visual 5,5; teknis 6; game 1; sinematik 1. Ini adalah temuan pengguna, bukan nilai yang dihitung mesin.

Uji browser otomatis di lingkungan sandbox (localStorage tiruan karena akses localhost/file:// diblokir) berhasil mereproduksi: 

- **HP 390×700:** halaman game `scrollWidth` **604px**, overflow horizontal **214px**. Tinggi konten **1052px** (scroll vertikal game **352px**).
- **Panggung 1280×650:** konten game **818px** tinggi (scroll vertikal **168px**).
- **Canvas:** ukuran bitmap 0×0 pada jalur yang diuji; game tidak berjalan benar.
- **Input:** saat simulasi keyboard dengan tinggi viewport berkurang, teks yang belum tersimpan **hilang** dan fokus input **tidak bertahan**.

Bukti mesin ada di `reports/regression_gpt/qa-result.json`, `reports/regression_gpt/QA_REPORT.md`, dan tangkapan layar regresi. Jalur lain tetap `BLOCKED` karena profil contoh belum memodelkan seluruh end-to-end dan transport simulator tidak membuktikan localStorage asli. Ini **disengaja**, bukan dianggap lulus.

Arsitektur `SilentGate`, `StageMode`, `CanvasLoop` dan kasus unit test mengurangi penyebab kelas kesalahan tersebut. Namun tiap implementasi baru tetap harus diuji dengan profil course sendiri.

**Benchmark NUM09** bukan tolok mutlak kepatuhan V4.3. Bandingkan capaian desain/game-nya, audit aturan per versi secara terpisah.
