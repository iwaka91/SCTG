# Cara menulis `qa-profile.json`

Ini adalah **skenario navigasi nyata untuk course yang spesifik**. Ketika menghasilkan course baru, ChatGPT harus membuat selector sesuai DOM HTML-nya. Jangan sekadar mengganti judul pada profil contoh lama.

## Struktur

```json
{
  "title": "NUM10 — Judul",
  "cinematics": true,
  "scenes": {
    "cover": {"target": "#loginName", "touch_targets": ["#loginButton"]},
    "game": {
      "target": "#mainGameCanvas", "canvas": "#mainGameCanvas", "no_page_scroll": true,
      "actions": [
        {"action": "fill", "selector": "#loginName", "value": "Tester"},
        {"action": "click", "selector": "#loginButton"},
        {"action": "click", "selector": "#openTeacher"},
        {"action": "fill", "selector": "#teacherPassword", "value": "123456a"},
        {"action": "click", "selector": "#activateFacil"},
        {"action": "click", "selector": "#navGame"}
      ],
      "interaction": {"selector": "#mainGameCanvas", "x": 0.4, "y": 0.5, "watch": "#gameStatus", "must_change": true}
    },
    "typing": {"target": "#myProductTextarea", "actions": [], "typing": {"selector": "#myProductTextarea"}},
    "reading": {"target": "#readingRoom", "actions": [], "no_page_scroll": true},
    "silent": {"target": "#readingContinue", "actions": [], "silent": {"button": "#readingContinue", "observe_seconds": 2.5}},
    "boss": {"target": "#bossCanvas", "actions": [], "interaction": {"selector": "#attackButton", "watch": "#bossHPLabel"}},
    "certificate": {"target": "#downloadPDF", "actions": [], "download": {"selector": "#downloadPDF"}},
    "cinematic": {"target": "#cinematicCanvas", "actions": []}
  },
  "flows": {
    "normal": {"actions": [], "assert": []},
    "ez": {"actions": [], "assert": []},
    "fasil": {"actions": [], "assert": []},
    "reset": {"actions": [], "assert": []},
    "resume": {"actions": [], "assert": []}
  },
  "manual_review": {
    "pedagogy": {"status": "pending", "evidence": ""},
    "visual": {"status": "pending", "evidence": ""},
    "game_feel": {"status": "pending", "evidence": ""},
    "cinematic": {"status": "pending", "evidence": ""},
    "accessibility": {"status": "pending", "evidence": ""}
  }
}
```

**Penting:** contoh ini **sengaja belum lengkap**, sehingga harus gagal release. `actions` untuk `reading`,`typing`,`boss`, dll harus benar-benar membawa pengguna ke layar sasaran. Untuk Fasil/EZ, isi langkah navigasi sesuai akses aplikasi. Beri aksi yang menguji jawaban salah dan benar, bukan hanya klik bebas.

## Aksi yang didukung

- `{"action":"click","selector":"#btn"}`
- `{"action":"fill","selector":"#input","value":"teks"}`
- `{"action":"select","selector":"#select","value":"B"}`
- `{"action":"check","selector":"#check"}`
- `{"action":"press","selector":"#element","key":"Enter"}`
- `{"action":"tap","selector":"#canvas","x":0.45,"y":0.6}` (rasio 0–1)
- `{"action":"wait","ms":500}`
- `{"action":"visible","selector":"#game"}`
- `{"action":"text","selector":"#status","contains":"Berhasil"}`

`interaction` melakukan klik langsung lalu mewajibkan perubahan teks pada elemen `watch`. Pastikan watcher merepresentasikan **state game**, bukan jam animasi yang bergerak sendiri. `typing` mensimulasikan keyboard dengan mengurangi tinggi viewport setelah elemen fokus, lalu memeriksa bahwa fokus dan teks bertahan. `silent` mengamati suara, `scrollTo`, `focusin`, dan status tombol saat timer berakhir. `download` memeriksa awal/akhir PDF dan nama berkas.

**Batas:** Profil QA tidak boleh memanipulasi state internal agar permainan *terlihat* lulus. Fasil/EZ hanya untuk perjalanan khusus yang memang disediakan standar; jalur murid normal tetap harus diuji.
