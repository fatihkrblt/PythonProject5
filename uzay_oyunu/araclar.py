from typing import Callable, List


def yakit_carpan_olustur(carpan: int) -> Callable[[int], int]:
    """Verilen çarpan ile harcanacak yakıtı hesaplayan bir closure (kapanış) döndürür."""

    def hesapla(mesafe: int) -> int:
        return mesafe * carpan

    return hesapla


def ucustaki_gezegenleri_filtrele(
    gezegenler: List[str], harf: str
) -> List[str]:
    """İsmi belirli bir harfle başlayan gezegenleri lambda kullanarak filtreler."""
    return list(filter(lambda g: g.startswith(harf), gezegenler))