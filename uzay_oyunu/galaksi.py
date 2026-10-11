import json
from typing import Any


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Galaksi haritasını kurar ve oyun durum sözlüğünü döndürür."""
    if baslangic not in gezegenler:
        raise ValueError(
            f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde yok!"
        )

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def galaksi_yukle(dosya_yolu: str = "uzay_oyunu/galaksi.json") -> dict[str, Any]:
    """JSON dosyasını okur ve galaksi_kur fonksiyonunu çalıştırır."""
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)
    return galaksi_kur(**veri)