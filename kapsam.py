"""
Değişken Kapsamı (Scope) ve LEGB Kuralları Raporu

1. Yerel Değişken Kapsamı:
   - Tahmin: Fonksiyon içindeki değişkene fonksiyon dışından erişilemez.
   - Gerçek Sonuç: NameError hatası fırlatır çünkü yerel (local) kapsamdadır.

2. Kapsayan (Enclosing) Kapsam ve Closure:
   - Tahmin: İçteki fonksiyon, dıştaki fonksiyonun değişkenini okuyabilir.
   - Gerçek Sonuç: Dıştaki değişkenin değeri başarıyla okunur.

3. UnboundLocalError Hatası:
   - Tahmin: UnboundLocalError hatası alınır.
   - Gerçek Sonuç: 'local variable referenced before assignment' hatası çıkar.
   - Neden: Python fonksiyonda atama yapıldığını görünce o değişkeni yerel kabul eder, fakat değer atanmadan okunmaya çalışıldığı için hata verir.
"""