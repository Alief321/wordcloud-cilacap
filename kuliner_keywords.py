kuliner_keywords = [
    "kuliner","makanan","minuman","hidangan","masakan",
    "sajian","menu","jajanan","camilan","olahan", "makan", 
    "minum", "resep","pangan","konsumsi", "takjil"
]

place_keywords = [
    "warung","restoran","rumah makan","kedai",
    "kafe","cafe","coffee shop","kopi",
    "angkringan","foodcourt","pujasera",
    "lapak","gerai","booth","tenda",
    "kantin","lesehan"
]

actor_keywords = [
    "pedagang","penjual","pengusaha","pemilik",
    "umkm","usaha","pelaku usaha","wirausaha",
    "produsen","industri rumahan",
    "usaha kecil","usaha mikro"
]

food_item_keywords = [
    "ikan","seafood","ayam","daging","telur",
    "beras","nasi","mie","tepung",
    "cabai","gula","minyak","garam",
    "kopi","teh","susu","sambal",
    "ikan asin","udang","cumi"
]

product_keywords = [
    "bakso","soto","mie ayam","nasi goreng",
    "pecel","gado gado","lontong","ketupat",
    "gorengan","kue","roti","jajanan pasar",
    "es","minuman tradisional"
]

event_keywords = [
    "festival kuliner","wisata kuliner",
    "pasar kuliner","bazaar","bazar",
    "pameran","stand makanan",
    "promo","diskon","launching menu"
]

def get_all():
    return (
        kuliner_keywords +
        place_keywords +
        actor_keywords +
        food_item_keywords +
        product_keywords +
        event_keywords
    )

kuliner_all = get_all()


def kuliner_score(text):
    return sum(1 for k in kuliner_all if k in text)