def gorev_kaydi(
    baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str
) -> str:
    """Görev başlığını, adımlarını ve ek bilgileri biçimlendirilmiş metin olarak döndürür."""
    satirlar = [f"[{oncelik}] {baslik}"]

    for i, adim in enumerate(adimlar, 1):
        satirlar.append(f"{i}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f"{anahtar}: {deger}")

    return "\n".join(satirlar)  