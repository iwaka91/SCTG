# SCTG Visual Atelier V1.1 — mesin visual yang benar-benar tertanam

## Yang baru secara fungsional

- `engine/sctg-visual.js` dimasukkan oleh CLI `build` ke setiap HTML course; API global `SCTGVisual.mount(canvas, ...)`.
- `engine/sctg-visual.css` disatukan dengan stylesheet course.
- Renderer Canvas 2D orisinal ini menawarkan langit bergradasi, cahaya radial, *layered parallax*, kabut, bayangan kontak, material dengan sisi terang/gelap, depth panggung isometrik, objek bergaya volumetrik, animasi natural dan interaksi pointer.
- Contoh offline **bisa dibuka**: `demos/VISUAL_ATELIER_SHOWCASE.html`, tiga dunia berbeda. **Ini contoh teknologi, bukan course jadi**. Untuk course nyata wajib arah artistik orisinal berdasarkan materi/TP.
- `benchmarks/NUM09_Claude_readonly.html` dan `benchmarks/NUM10_Misi_Gambut_Claude_readonly.html` adalah dua referensi mutu independen.
- `cli/check_benchmarks.py` menjamin hash file asli belum diubah.
- `cli/visual_gate.py` adalah **5 cek Ya/Tidak tanpa persentase**, menyimpan bukti dan catatan manual; satu saja Tidak/Belum = blokir, rating Toto Gutomo baru datang setelah kelima Ya. `factory release` kini mensyaratkan bukti ini.

## API sederhana

```js
const view=SCTGVisual.mount(document.querySelector('#sceneCanvas'), {
  world:'literasi', // 'literasi' | 'numerasi' | 'sejarah'
  onActivate:({x,y,world})=>{ /* perbarui state game nyata milik course */ }
});
view.setWorld('sejarah');
view.setActive(false); // jeda bila modal/timer harus berhenti
view.destroy(); // saat berganti langkah
```

**Jangan menjadikan `SCTGVisual` sebagai game otomatis.** Fungsi `onActivate` hanyalah contoh interaksi. Gameplay sebenarnya wajib memakai aturan misi, state, feedback dan kondisi kemenangan yang didefinisikan oleh pengembang course.

## Cara review visual satu course

1. Susun `VISUAL_BLUEPRINT.md` dengan mencocokkan aspek artistik dari kedua benchmark.
2. Render screenshot cover, game, Ruang Baca, Final Boss, sinematik pada HP dan Panggung (QA penuh) lalu inspeksi hasilnya. Jangan menyatakan kualitas estetika hanya dari angka pixel.
3. Buat formulir yang masih berstatus `belum` dengan `python cli/visual_gate.py init --html <HTML> --review <QA_DIR>/visual-review.json`.
4. Isi kelima gerbang dengan `verdict: "ya"` atau `"tidak"`, alasan spesifik minimal 35 karakter serta `evidence: ["nama-file.png"]` yang ada dalam folder QA tersebut. Skrip memeriksa semua, termasuk hash HTML.
5. `python cli/visual_gate.py check --html <HTML> --review <QA_DIR>/visual-review.json`. Jika ada ❌, rilis ditolak. Rating 9,9/10 **tidak** diklaim oleh Factory.

## Batas yang jujur

Mesin ini menjadikan kedalaman gambar dan bahasa visual *tersedia secara teknis* untuk dipakai di course baru serta memastikan pemeriksaan visual tidak bisa dilewati. Ia **tidak otomatis menjamin visual memukau**: artistik spesifik, gameplay, sinematik bermakna, dan penilaian visual memerlukan rancangan serta pengujian yang sebenarnya. Benchmark tidak bisa digantikan oleh contoh showroom.
