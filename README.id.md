<div align="center">

# ⚒️ SKILL FORGE ULTRA

### Berhenti nulis prompt. Mulai tempa skill.

**Skill Claude yang membuat Skill Claude.**<br>
Tempel ide, alur kerja, atau prompt 3 halaman → dapat `SKILL.md` yang ramping, gampang terpicu, sudah divalidasi, dan siap dipasang dalam hitungan detik.

![License: MIT](https://img.shields.io/badge/license-MIT-black)
![Claude Skill](https://img.shields.io/badge/Claude-Skill-D97757)
![Mode](https://img.shields.io/badge/mode-7-blueviolet)

[🇬🇧 English](README.md)

</div>

---

## 😩 Masalahnya

Kamu sudah bikin prompt sakti. *"Kamu adalah ahli kelas dunia…"* Panjangnya tiga halaman. Kadang berhasil, kadang tidak.

Lalu prompt itu dijadikan skill, dan ini yang terjadi:

- 🔇 **Skill tidak pernah aktif.** Tidak ada `description` yang jelas, jadi Claude tidak tahu kapan harus memakainya.
- 🫠 **Hasilnya generik.** "Harus profesional" bukan standar yang bisa diukur.
- 🐘 **Isinya gendut.** Aturan yang sama diulang empat kali, ditambah kalimat hype dan basa-basi.
- 🎲 **Sering ngarang.** Tidak ada aturan yang memisahkan fakta dari tebakan.
- 💥 **Rusak.** Merujuk ke file yang tidak ada.

## 🔥 Solusinya

**Skill Forge Ultra** adalah arsitek skill kelas elite yang dikemas dalam satu skill siap pasang. Ia tidak sekadar menulis ulang prompt kamu. Ia **merancang sistem kerja untuk satu kelas masalah**, lalu **memvalidasi dan mengemasnya**.

## ✨ Kenapa ULTRA

- 🎯 **Fokus pada pemicu.** Description ditulis dengan frasa yang benar-benar diketik pengguna, termasuk "bikin skill", "cek kode ini", dan "bikinin caption".
- 🧭 **7 mode otomatis.** CREATE, IMPROVE, DEBUG, OPTIMIZE, MERGE, AUDIT, dan EXTEND. Kamu tidak perlu memilih modenya.
- 📏 **Kata sifat diubah jadi standar terukur.** "Viral" dan "profesional" diterjemahkan menjadi cek yang bisa diamati.
- 🛡️ **Anti-halusinasi.** Fakta, asumsi, dan rekomendasi selalu dipisahkan. Tidak ada sitasi atau hasil palsu.
- 🧱 **5 template arketipe dan 10 paket quality gate domain.**
- 🪶 **Progressive disclosure.** Inti skill tetap kecil, sedangkan pengetahuan tambahan baru dimuat saat dibutuhkan.
- 🔬 **Validator dan packager.** Keduanya tanpa dependensi, sudah diuji, dan dijalankan otomatis lewat CI.

## ⚡ Pasang dalam 60 detik

1. Unduh [`dist/skill-forge-ultra.skill`](dist/skill-forge-ultra.skill).
2. Pasang sesuai tempat kamu memakai Claude:
   - **Claude.ai/app:** unggah file `.skill` di pengaturan Skills, atau buka dari chat lalu klik **Save skill**.
   - **Claude Code:** jalankan `cp -r skill-forge-ultra ~/.claude/skills/`.
3. Langsung pakai dengan bahasa sehari-hari:

```text
Jadikan prompt ini skill: <tempel prompt>
Bikin skill buat nulis caption TikTok untuk toko kopi aku
Audit SKILL.md ini: <tempel>
Skill aku nggak pernah aktif, tolong debug: <tempel>
```

## 🧭 7 Mode

| Mode | Contoh ucapan | Hasil |
|---|---|---|
| CREATE | "bikin skill buat ubah notulen rapat jadi tiket Jira" | Skill baru, sudah divalidasi dan dikemas |
| IMPROVE | "bikin skill ini jauh lebih sakti" | Versi upgrade dengan nama tetap, plus changelog |
| DEBUG | "skill aku nggak aktif waktu minta invoice" | Penyebab, perbaikan, cara cek, dan file yang sudah ditambal |
| OPTIMIZE | "skill ini kepanjangan" | Versi lebih ramping tanpa fitur yang hilang |
| MERGE | "gabungkan dua skill ini" | Satu skill yang koheren |
| AUDIT | "review SKILL.md ini" | Vonis dan daftar cacat beserta perbaikannya |
| EXTEND | "tambah ekspor CSV ke skill laporanku" | Kemampuan baru tanpa merusak yang lama |

## 🔬 Validator

```bash
python skill-forge-ultra/scripts/validate_skill.py folder-skill
python skill-forge-ultra/scripts/package_skill.py folder-skill dist/
```

Validator mengecek frontmatter, kualitas pemicu, ukuran dan estimasi token, file yang hilang atau tidak terpakai, aturan duplikat, serta placeholder yang lupa diisi. Packager akan menolak mengemas skill yang tidak valid.

## 📚 Contoh

Lihat [`examples/`](examples/), termasuk [`caption-umkm-id`](examples/caption-umkm-id/SKILL.md), skill penulis caption untuk UMKM yang ditulis full Bahasa Indonesia.

---

<div align="center">

⭐ **Kalau repo ini menghemat waktumu, kasih bintang ya!**

MIT © verycoolapps

</div>
