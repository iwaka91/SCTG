# Adaptive Performance V1.3 — Otomatis dan tak terlihat oleh murid

- Tidak ada pemilih Hemat/Standar/Ultra pada antarmuka. Tidak ada `setMode` publik atau penyimpanan preferensi manual. Preferensi lokal versi lama diabaikan.
- Engine memulai pada pengaturan konservatif berdasarkan petunjuk perangkat bila tersedia. `navigator.deviceMemory` dan `hardwareConcurrency` bukan persyaratan dan bukan dasar tunggal.
- Pada setiap render aktif, waktu menggambar serta interval `requestAnimationFrame` diukur lokal. Jika render lambat, kualitas grafis internal diturunkan. Jika lancar stabil cukup lama, resolusi/efek dapat meningkat secara hati-hati; ada hysteresis untuk mencegah bolak-balik.
- Batas internal: tier hemat 16 FPS/240k piksel; standar 24 FPS/520k piksel; ultra 30 FPS/900k piksel. Ini batas maksimum target, bukan janji FPS perangkat.
- `prefers-reduced-motion` mempertahankan kualitas gerak minimal. Saat tab tersembunyi pengukuran dijeda/reset.
- Semua perubahan hanya untuk **Canvas visual**, tidak mengubah jawaban, gerbang baca, aksi sentuh, progres, maupun asesmen SCTG V4.3.
- Pengembang harus tetap menyediakan layout yang bekerja pada 13 ukuran layar serta memeriksa perangkat fisik kelas rendah. Target cakupan 90% HP adalah target uji, bukan klaim kelulusan.
- Saat menggunakan `SCTGPerformance` gunakan `size(width,height)`, `shouldDraw(ts,lastPaint)`, dan `observeFrame(drawMs,rafGapMs)`; renderer harus menangani event `sctg-performance-change` dengan resize dan mencegah RAF loop lama berjalan ganda.
