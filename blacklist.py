blacklist_crime = [
    "polisi","kriminal","narkoba","curanmor",
    "pencurian","penangkapan","tersangka",
    "pengadilan","sidang","vonis",
    "kasus","penjara","hukuman"
]

blacklist_disaster = [
    "banjir","longsor","cuaca","hujan",
    "gempa","angin","bmkg","bencana",
    "cuaca ekstrem"
]

blacklist_politics = [
    "pemilu","pilkada","kampanye","partai",
    "dprd","bupati","gubernur","menteri",
    "presiden","wakil presiden"
]

blacklist_industry = [
    "bbm","kilang","pertamina","energi",
    "industri berat","pabrik besar",
    "rfcc","petrokimia","migaS"
]

blacklist_economy = blacklist_crime + blacklist_disaster + blacklist_politics

blacklist_all = blacklist_economy + blacklist_industry

def get_all():
    return blacklist_all

def get_blacklist_economy():
    return blacklist_economy


