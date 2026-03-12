# Wordcloud Berita Cilacap

Proyek ini digunakan untuk mengambil berita dari Google News RSS, membersihkan teks bahasa Indonesia, melakukan stemming, lalu membuat visualisasi wordcloud untuk topik tertentu.

Topik yang sudah disiapkan:

- Ekonomi
- Kuliner

## Fitur Utama

- Scraping berita harian dari Google News RSS berdasarkan query dan rentang tanggal.
- Pembersihan teks judul dan deskripsi berita.
- Stemming bahasa Indonesia menggunakan Sastrawi.
- Filtering berbasis keyword dan blacklist (pada script ekonomi dan kuliner).
- Pembuatan file output teks:
  - `titles.txt`
  - `descriptions.txt`
  - `clean.txt`
- Pembuatan gambar wordcloud PNG.

## Struktur File Penting

- `main.py`: pipeline dasar wordcloud (tanpa filter keyword khusus).
- `ekonomi_main.py`: pipeline wordcloud topik ekonomi dengan scoring keyword dan blacklist.
- `kuliner_main.py`: pipeline wordcloud topik kuliner dengan scoring keyword dan blacklist.
- `ekonomi_keyword.py`: daftar keyword ekonomi.
- `kuliner_keywords.py`: daftar keyword kuliner.
- `blacklist.py`: daftar kata blacklist untuk mengurangi berita tidak relevan.

## Kebutuhan

Pastikan Python 3.9+ sudah terpasang.

Library yang dibutuhkan:

- feedparser
- pandas
- matplotlib
- beautifulsoup4
- wordcloud
- scikit-learn
- Sastrawi

Install dependensi:

```bash
pip install feedparser pandas matplotlib beautifulsoup4 wordcloud scikit-learn Sastrawi
```

atau

```bash
pip install -r requirements.txt
```

## Cara Menjalankan

1. Buka folder proyek ini di terminal.
2. Jalankan salah satu script berikut:

```bash
python ekonomi_main.py
```

atau

```bash
python kuliner_main.py
```

atau pipeline dasar:

```bash
python main.py
```

## Output

Setelah script selesai, file output akan dihasilkan di folder proyek:

- Teks hasil scraping dan cleaning:
  - `titles.txt` berisi judul berita yang berhasil discraping
  - `descriptions.txt` berisi deskripsi singkat dari berita yang berhasil discraping
  - `clean.txt` berisi berita bersih yang telah difilter (untuk file `ekonomi_main` dan `kuliner_main`) berdasarkan keyword
- Gambar wordcloud, contoh:
  - `wordcloud_ekonomi_cilacap_YYYYMMDD.png`
  - `wordcloud_kuliner_cilacap_YYYYMMDD.png`

## Konfigurasi yang Bisa Diubah

Di masing-masing script utama (`main.py`, `ekonomi_main.py`, `kuliner_main.py`) Anda bisa mengubah:

- `query`
- `start`
- `end`
- daftar `stop_words`

Contoh:

```python
query = 'ekonomi AND cilacap'
start = datetime(2026, 2, 1)
end = datetime(2026, 3, 10)
```

Anda juga dapat menambahkan keyword pada file `ekonomi_keyword` dan `kuliner_keyword` untuk lebih meluaskan pencarian.
Selain itu anda juga dapat menambahkan daftar kata yang akan tidak disertakan ke wordcloud dengan menambahkannya di file `blacklist.py`

## Catatan

- Jika hasil berita sedikit atau kosong, periksa kembali query dan rentang tanggal.
- Pada Windows, tampilan wordcloud bisa dipengaruhi font default. Jika ingin hasil lebih baik, Anda bisa menambahkan parameter `font_path` pada `WordCloud(...)`.
