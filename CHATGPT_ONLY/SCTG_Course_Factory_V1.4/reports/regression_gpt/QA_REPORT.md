# SCTG QA — Misi Gambut GPT — regression control / expected to fail

**Status:** NOT_RELEASE_READY
**Date:** 2026-10-16T15:22:03.525832+00:00

## Auto gate

| Gate | PASS | FAIL | BLOCKED |
|---|---:|---:|---:|
| static | 2 | 0 | 0 |
| cover | 9 | 0 | 0 |
| game | 8 | 7 | 1 |
| typing | 5 | 3 | 0 |
| reading | 0 | 0 | 1 |
| silent | 0 | 0 | 1 |
| boss | 0 | 0 | 1 |
| certificate | 0 | 0 | 1 |
| cinematic | 0 | 0 | 1 |
| flow | 0 | 0 | 5 |
| manual | 0 | 0 | 5 |
| matrix | 0 | 0 | 1 |
| origin | 0 | 0 | 1 |

## Kegagalan dan hal yang belum teruji

- **FAIL** game/Genggam_390x700: Horizontal overflow = 214px — `{'width': 390, 'height': 700, 'scrollWidth': 604, 'bodyScrollWidth': 604, 'scrollHeight': 1052, 'overflowX': 214, 'overflowY': 352, 'oversizeElements': [{'tag': 'DIV', 'id': '', 'cls': 'head-right', 'left': 380, 'right': 604}, {'tag': 'BUTTON', 'id': 'soundBtn', 'cls': 'icon-btn', 'left': 380, 'right': 420}, {'tag': 'BUTTON', 'id': 'speakBtn', 'cls': 'icon-btn', 'left': 426, 'right': 466}, {'tag':`
- **FAIL** game/Genggam_390x700: Vertical page scrolling in game/reading = 352px — `{'width': 390, 'height': 700, 'scrollWidth': 604, 'bodyScrollWidth': 604, 'scrollHeight': 1052, 'overflowX': 214, 'overflowY': 352, 'oversizeElements': [{'tag': 'DIV', 'id': '', 'cls': 'head-right', 'left': 380, 'right': 604}, {'tag': 'BUTTON', 'id': 'soundBtn', 'cls': 'icon-btn', 'left': 380, 'right': 420}, {'tag': 'BUTTON', 'id': 'speakBtn', 'cls': 'icon-btn', 'left': 426, 'right': 466}, {'tag':`
- **FAIL** game/Genggam_390x700: Canvas blank/invalid — `{'ok': False, 'error': 'canvas too small', 'width': 0, 'height': 0}`
- **FAIL** game/Panggung_1280x650: Vertical page scrolling in game/reading = 168px — `{'width': 1280, 'height': 650, 'scrollWidth': 1280, 'bodyScrollWidth': 1280, 'scrollHeight': 818, 'overflowX': 0, 'overflowY': 168, 'oversizeElements': [{'tag': 'DIV', 'id': '', 'cls': 'menu-head', 'left': -307, 'right': 52}, {'tag': 'DIV', 'id': '', 'cls': '', 'left': -291, 'right': -173}, {'tag': 'STRONG', 'id': '', 'cls': '', 'left': -291, 'right': -176}, {'tag': 'DIV', 'id': '', 'cls': 'tiny m`
- **FAIL** game/Panggung_1280x650: Canvas blank/invalid — `{'ok': False, 'error': 'canvas too small', 'width': 0, 'height': 0}`
- **FAIL** game/Batas_900x500: Vertical page scrolling in game/reading = 411px — `{'width': 900, 'height': 500, 'scrollWidth': 900, 'bodyScrollWidth': 900, 'scrollHeight': 911, 'overflowX': 0, 'overflowY': 411, 'oversizeElements': [{'tag': 'DIV', 'id': '', 'cls': 'menu-head', 'left': -324, 'right': 35}, {'tag': 'DIV', 'id': '', 'cls': '', 'left': -308, 'right': -190}, {'tag': 'STRONG', 'id': '', 'cls': '', 'left': -308, 'right': -193}, {'tag': 'DIV', 'id': '', 'cls': 'tiny mute`
- **FAIL** game/Batas_900x500: Canvas blank/invalid — `{'ok': False, 'error': 'canvas too small', 'width': 0, 'height': 0}`
- **FAIL** typing/Genggam_390x700: Horizontal overflow = 186px — `{'width': 390, 'height': 700, 'scrollWidth': 576, 'bodyScrollWidth': 576, 'scrollHeight': 1421, 'overflowX': 186, 'overflowY': 721, 'oversizeElements': [{'tag': 'DIV', 'id': '', 'cls': 'head-right', 'left': 352, 'right': 576}, {'tag': 'BUTTON', 'id': 'soundBtn', 'cls': 'icon-btn', 'left': 352, 'right': 392}, {'tag': 'BUTTON', 'id': 'speakBtn', 'cls': 'icon-btn', 'left': 398, 'right': 438}, {'tag':`
- **FAIL** typing/Genggam_390x700: Keyboard resize retains input focus and unsubmitted value — `{'before': 'Tes keyboard tetap aktif ABC123', 'after': '', 'focusRetained': False}`
- **FAIL** typing/Panggung_1280x650: Keyboard resize retains input focus and unsubmitted value — `{'before': 'Tes keyboard tetap aktif ABC123', 'after': '', 'focusRetained': False}`
- **BLOCKED** reading/coverage: Required scene missing from QA profile
- **BLOCKED** game/coverage: Required behavioral probe missing: interaction
- **BLOCKED** silent/coverage: Required scene missing from QA profile
- **BLOCKED** boss/coverage: Required scene missing from QA profile
- **BLOCKED** certificate/coverage: Required scene missing from QA profile
- **BLOCKED** cinematic/coverage: Cinematic scene must be checked unless explicitly not used in design
- **BLOCKED** flow/normal: Required end-to-end flow/assertions missing from QA profile
- **BLOCKED** flow/ez: Required end-to-end flow/assertions missing from QA profile
- **BLOCKED** flow/fasil: Required end-to-end flow/assertions missing from QA profile
- **BLOCKED** flow/reset: Required end-to-end flow/assertions missing from QA profile
- **BLOCKED** flow/resume: Required end-to-end flow/assertions missing from QA profile
- **BLOCKED** manual/pedagogy: Human/AI visual or pedagogy review absent
- **BLOCKED** manual/visual: Human/AI visual or pedagogy review absent
- **BLOCKED** manual/game_feel: Human/AI visual or pedagogy review absent
- **BLOCKED** manual/cinematic: Human/AI visual or pedagogy review absent
- **BLOCKED** manual/accessibility: Human/AI visual or pedagogy review absent
- **BLOCKED** matrix: Fast subset is not full SCTG matrix
- **BLOCKED** origin: Sandbox uses simulated localStorage; native persistence and downloads not certified

## Batas verifikasi

- Browser headless bukan pengganti uji Android fisik / IFP fisik.
- Canvas berwarna tidak membuktikan game playable; skenario game harus membuktikan respons input.
- Skor estetika 9,8/10 tidak dapat dihasilkan otomatis secara jujur.
- Pemeriksaan PDF harus melalui skenario unduh + pemeriksaan berkas valid; tanpa skenario status tetap BLOCKED.
- Screenshot Tahap A wajib dinilai secara visual, bukan hanya dibuat.
