econ_price_keywords = [
    "harga","kenaikan harga","penurunan harga",
    "inflasi","deflasi","daya beli",
    "harga pasar","harga bahan","harga pokok",
    "stabilitas harga","lonjakan harga"
]

econ_business_keywords = [
    "umkm","usaha","pelaku usaha","wirausaha",
    "pengusaha","industri","industri kecil",
    "industri rumah tangga","produksi",
    "distribusi","rantai pasok","logistik",
    "modal usaha","perdagangan"
]

econ_food_keywords = [
    "pangan","beras","gabah","jagung",
    "cabai","bawang","minyak goreng",
    "gula","telur","daging","ikan",
    "hasil panen","komoditas"
]

econ_labor_keywords = [
    "tenaga kerja","lapangan kerja","pekerjaan",
    "upah","gaji","ump","umk",
    "buruh","pekerja","nelayan",
    "petani","pengangguran","pendapatan"
]

econ_policy_keywords = [
    "subsidi","bantuan","bansos",
    "pajak","retribusi","insentif",
    "anggaran","belanja daerah",
    "pendapatan daerah","ekonomi daerah"
]

econ_trade_keywords = [
    "perdagangan","ekspor","impor",
    "pasar tradisional","pasar rakyat",
    "pasokan","stok","distribusi barang"
]

econ_keywords = (
    econ_price_keywords +
    econ_business_keywords +
    econ_food_keywords +
    econ_labor_keywords +
    econ_policy_keywords +
    econ_trade_keywords
)

def get_all():
    return econ_keywords

def ekonomi_score(text):
    return sum(1 for k in econ_keywords if k in text)