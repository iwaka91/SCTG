# SCTG QA — NUM09 Claude reference — read-only benchmark, not factory-certified

**Status:** NOT_RELEASE_READY
**Date:** 2026-10-16T15:23:10.008058+00:00

## Auto gate

| Gate | PASS | FAIL | BLOCKED |
|---|---:|---:|---:|
| static | 2 | 0 | 0 |
| cover | 9 | 0 | 0 |
| reading | 0 | 0 | 1 |
| game | 0 | 0 | 1 |
| typing | 0 | 0 | 1 |
| silent | 0 | 0 | 1 |
| boss | 0 | 0 | 1 |
| certificate | 0 | 0 | 1 |
| cinematic | 0 | 0 | 1 |
| flow | 0 | 0 | 5 |
| manual | 0 | 0 | 5 |
| matrix | 0 | 0 | 1 |
| origin | 0 | 0 | 1 |

## Kegagalan dan hal yang belum teruji

- **BLOCKED** reading/coverage: Required scene missing from QA profile
- **BLOCKED** game/coverage: Required scene missing from QA profile
- **BLOCKED** typing/coverage: Required scene missing from QA profile
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
