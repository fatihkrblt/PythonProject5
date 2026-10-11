import pytest
from uzay_oyunu.araclar import (
    ucustaki_gezegenleri_filtrele,
    yakit_carpan_olustur,
)
from uzay_oyunu.galaksi import galaksi_kur, galaksi_yukle
from uzay_oyunu.kayit import gorev_kaydi
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


# --- GÖREV 1 TESTLERİ ---
def test_envanter_metni_dolu():
    assert (
        envanter_metni(True, False, True)
        == "Sende: bol kredi, yetenekli bir pilot"
    )


def test_envanter_metni_bos():
    assert envanter_metni(False, False, False) == ""


def test_hedef_menusu():
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen


# --- GÖREV 2 TESTİ ---
def test_gorev_kaydi():
    sonuc = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="YÜKSEK",
        sorumlu="Ayşe",
    )
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        "1. Kredi kazan\n"
        "2. Pilot bul\n"
        "3. Hiperdrive al\n"
        "sorumlu: Ayşe"
    )
    assert sonuc == beklenen


# --- GÖREV 3 TESTLERİ ---
def test_galaksi_kur_basarili():
    veri = {
        "gezegenler": ["dünya", "mars"],
        "baglantilar": {"dünya": ["mars"], "mars": []},
        "baslangic": "dünya",
        "yakit": 100,
    }
    g = galaksi_kur(**veri)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100


def test_galaksi_kur_varsayilan_yakit():
    g = galaksi_kur(
        gezegenler=["mars"], baglantilar={"mars": []}, baslangic="mars"
    )
    assert g["yakit"] == 50


def test_galaksi_kur_gecersiz_baslangic():
    with pytest.raises(ValueError):
        galaksi_kur(
            gezegenler=["dünya"], baglantilar={"dünya": []}, baslangic="jüpiter"
        )


def test_galaksi_yukle():
    g = galaksi_yukle()
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100
    assert "centauri" in g["baglantilar"]["dünya"]


# --- GÖREV 5 TESTLERİ ---
def test_yakit_carpan_olustur_closure():
    standart_ucus = yakit_carpan_olustur(2)
    guvenli_ucus = yakit_carpan_olustur(3)

    assert standart_ucus(10) == 20
    assert guvenli_ucus(10) == 30


def test_ucustaki_gezegenleri_filtrele_lambda():
    gezegenler = ["dünya", "centauri", "mars", "sirius"]
    sonuc = ucustaki_gezegenleri_filtrele(gezegenler, "m")
    assert sonuc == ["mars"]