class BankaHesabiGetSet:
    def __init__(self, hesab_sahibi, sifre):
        self.hesab_sahibi = hesab_sahibi
        self._sifre = sifre

    def get_sifre(self):
        return self._sifre
    def set_sifre(self, yeni_sifre):
        if len(yeni_sifre) < 8:
            print(f"Şifre En Az 8 karakterden fazla olmadılır")
        else:
            self._sifre = yeni_sifre
class BankaHesabiDogrudan:
    def __init__(self, hesab_sahibi, sifre):
        self.hesab_sahibi = hesab_sahibi
        self.sifre = sifre


# Kullanım ÖRneği
print("GET-SET Örneği Kullanımı")
hesap1 = BankaHesabiGetSet("Ramazan",'orjinal123')
print(f"Mevcut Şifre: {hesap1.get_sifre}")
hesap1.set_sifre('yeniSifre123456')
print("Güncellenen Şifre: ", hesap1.get_sifre())

print("Doğrudan Attribute Kullanımı")
hesap2 = BankaHesabiDogrudan('Özkan',"orjinal123")
print(f"Mevcut Şifre: {hesap2.sifre}")
hesap2.sifre = "yenisifre123"
print(f"GÜncellenen Şifre: {hesap2.sifre}")