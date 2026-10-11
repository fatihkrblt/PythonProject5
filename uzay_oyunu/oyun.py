def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Mevcut eşyalara göre envanter durum metnini oluşturur."""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""
    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandırarak menü metni olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for idx, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{idx}] {hedef}")
    return "\n".join(satirlar)