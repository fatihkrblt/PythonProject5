import pytest


def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Depo None ise yeni bir liste oluşturur."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_bagimsiz_depolar():
    depo1 = yakit_ekle(10)
    assert depo1 == [10]

    depo2 = yakit_ekle(20)
    assert depo2 == [20]