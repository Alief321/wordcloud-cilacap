import feedparser
import pandas as pd
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from datetime import datetime, timedelta


# ==============================
# 1. SCRAPE BERITA
# ==============================

# url = "https://news.google.com/rss/search?q=cilacap&hl=id&gl=ID&ceid=ID:id"

import feedparser


from urllib.parse import quote_plus

query = 'ekonomi AND cilacap'
query = query.replace(" ", "%20")  # encode spasi menjadi %20

start = datetime(2026,2,1)
end   = datetime(2026,3,10)

delta = timedelta(days=1)

all_news_title = []
all_news_desc = []

while start < end:

    next_day = start + delta

    url = f"https://news.google.com/rss/search?q={query}+after:{start.date()}+before:{next_day.date()}&hl=id&gl=ID&ceid=ID:id"

    print(f"Scraping berita dari {start.date()}...")
    print (f"URL: {url}")
    feed = feedparser.parse(url)

    for entry in feed.entries:
        # parse HTML description
        soup = BeautifulSoup(entry.description, "html.parser")
        desc_text = soup.get_text(" ")
        all_news_title.append(entry.title)
        all_news_desc.append(desc_text)

    start = next_day




# save to .txt
with open("titles.txt", "w", encoding="utf-8") as f:
    for title in all_news_title:
        f.write(title + "\n")

with open("descriptions.txt", "w", encoding="utf-8") as f:
    for description in all_news_desc:
        f.write(description + "\n")

df = pd.DataFrame({
    "title": all_news_title,
    "description": all_news_desc
})




# ==============================
# 2. CLEANING TEXT
# ==============================

def clean_text(text):

    text = text.lower()

    # ambil sebelum "-"
    text = text.split(" - ")[0]

    # ambil sebelum nbsp
    text = text.split("\xa0")[0]

    # hapus karakter selain huruf
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # rapikan spasi
    text = re.sub(r'\s+', ' ', text).strip()

    return text

df["clean"] = df["title"].apply(clean_text) + " " + df["description"].apply(clean_text)



from blacklist import get_all as  get_blacklist_economy
from ekonomi_keyword import get_all, ekonomi_score


df["econ_score"] = df["clean"].apply(ekonomi_score)

def final_score(text):
    score = 0
    score += sum(1 for k in get_all() if k in text)
    score -= sum(1 for b in get_blacklist_economy() if b in text)
    return score

df["final_score"] = df["clean"].apply(final_score)
df = df[df["final_score"] >= 1]

print (df[["title", "final_score"]].sort_values(by="final_score", ascending=False))

# masukan ke clean text untuk title dan description yang final score >= 1
df["clean"] = df.apply(lambda row: row["clean"] if row["final_score"] >= 2 else "", axis=1)
with open("clean.txt", "w", encoding="utf-8") as f:
    for text in df["clean"]:
        f.write(text + "\n")


# ==============================
# 3. STEMMING BAHASA INDONESIA
# ==============================

factory = StemmerFactory()
stemmer = factory.create_stemmer()

df["stem"] = df["clean"].apply(stemmer.stem)


# ==============================
# 4. VECTORIZE TEXT
# ==============================
stop_words=[
        "yang","dan","di","ke","dari","untuk","pada","dengan",
        "ini","itu","karena","ada","jadi","akan","lebih",
        "dalam","atau","oleh","para","juga","cilacap","kabupaten", "hari", "pemkab", "harga", "rp", "ribu", "juta", 
        "banyumas", "tengah", "purbalingga", "jawa", "makanan", "wisata", "kuliner", "minuman", "jateng", "ekonomi", "harga"
]
vectorizer = CountVectorizer(
    stop_words=stop_words
)

X = vectorizer.fit_transform(df["stem"])


# ==============================
# 5. TOPIC MODELING (LDA)
# ==============================

# n_topics = 4

# lda = LatentDirichletAllocation(
#     n_components=n_topics,
#     random_state=42
# )

# lda.fit(X)

# words = vectorizer.get_feature_names_out()


# # tampilkan kata penting tiap topik
# print("\n=== TOPIC KEYWORDS ===")

# for i, topic in enumerate(lda.components_):
#     print(f"\nTopik {i}")
#     print([words[j] for j in topic.argsort()[-10:]])


# # ==============================
# # 6. WORDCLOUD PER TOPIK
# # ==============================

# topic_results = lda.transform(X)

# df["topic"] = topic_results.argmax(axis=1)

# for t in range(n_topics):

#     text = " ".join(df[df["topic"] == t]["stem"])

#     if len(text) < 10:
#         continue

#     wc = WordCloud(
#         width=1000,
#         height=500,
#         background_color="white",
#         stopwords=stop_words,
#     ).generate(text)

#     plt.figure(figsize=(10,5))
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.title(f"Wordcloud Cilacap - Topik {t}")
#     plt.show()


# Wordcloud keseluruhan
all_text = " ".join(df["stem"])
wc_all = WordCloud(
    width=1000,
    height=500,
    background_color="white",
    stopwords=stop_words,
).generate(all_text)

plt.figure(figsize=(10,5))
plt.imshow(wc_all, interpolation="bilinear")
plt.axis("off")
plt.title("Wordcloud Ekonomi Cilacap")

from datetime import datetime

filename = f"wordcloud_ekonomi_cilacap_{datetime.now().strftime('%Y%m%d')}.png"

plt.savefig(filename, dpi=300, bbox_inches="tight")
plt.show()



# ==============================
# 7. DISTRIBUSI TOPIK
# ==============================

# topic_count = df["topic"].value_counts().sort_index()

# plt.figure(figsize=(8,4))
# topic_count.plot(kind="bar")
# plt.title("Distribusi Topik Berita Cilacap")
# plt.xlabel("Topik")
# plt.ylabel("Jumlah Berita")
# plt.show()