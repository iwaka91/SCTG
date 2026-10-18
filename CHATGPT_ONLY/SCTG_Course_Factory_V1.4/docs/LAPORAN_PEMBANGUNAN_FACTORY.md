# Status pembangunan SCTG Course Factory — 16 Oktober 2026

Paket dibangun untuk ChatGPT. **Bukan aplikasi GUI**, melainkan workspace yang berisi aturan, engine, script build, script QA, benchmark, dan kontrol kegagalan.

## Apa yang benar-benar diuji sekarang

- `engine/sctg-core.js` dan `engine/sctg-cinematic.js` diperiksa sintaks Node.
- 3 tes Python Playwright runtime **lolos**: Canvas+input+auto-fit breakpoint; timer tersembunyi dijeda; timer selesai mengaktifkan tombol tanpa kehilangan input/fokus.
- `cli/factory.py init` berhasil membuat scaffold course internal `DEMOQA`.
- `cli/factory.py build` berhasil menghasilkan **single HTML 15.351 byte** untuk scaffold (belum menjadi course lengkap).
- Regression runner mendeteksi kegagalan Misi Gambut GPT di viewport HP dan Panggung. Contoh laporan dalam `reports/regression_gpt/`.
- Perintah `release` **menolak** Misi Gambut karena status `NOT_RELEASE_READY`.

## Yang belum dibuktikan

- Belum ada course baru yang dihasilkan memakai factory dan lolos full QA.
- Belum diuji pada HP Android fisik atau IFP fisik.
- Transport uji di lingkungan ini harus `sandbox` (mock penyimpanan), sehingga uji localStorage asli tetap **belum terverifikasi**.
- Penilaian visual 9,8/10 dan perbandingan mutu artistik per course **belum dapat diautomasi**.

## Penggunaan yang benar

Paket ini sudah dapat dipakai untuk produksi course berikutnya dan memaksa laporan FAIL/BLOCKED yang jujur. Label `Final Candidate` hanya diperbolehkan **setelah** course spesifik dibuat, diuji pada transport HTTP dalam lingkungan yang mendukung, dan lolos semua gerbang. Jangan menyebut scaffold `DEMOQA` sebagai course selesai.

**Perubahan 17 Oktober 2026:** catatan ini merekam V1 historis. Untuk status terbaru lihat `docs/LAPORAN_INTEGRASI_NUM10_V1.1.md`. Tidak lagi menggunakan bobot/angka visual; kini lima Ya/Tidak lalu penilaian subjektif Toto Gutomo.
