class Coders:
    def __init__(self, PIN: int, balans: float):
        self.PIN = PIN
        self.balans = balans
    
    def medaxil(self, mebleq: float):
        self.balans += mebleq
        print(f"Balansa {mebleq} əlavə olundu. Yeni balans: {self.balans}")
    
    def mexaric(self, mebleq: float):
        if mebleq > self.balans:
            print("Balansda kifayət qədər məbləğ yoxdur.")
        else:
            self.balans -= mebleq
            print(f"Balansdan {mebleq} məbləği çıxarıldı. Yeni balans: {self.balans}")
    
    def balans_goster(self):
        print(f"Balans: {self.balans}")


class Kredit(Coders):
    def __init__(self, PIN: int, balans: float, kreditmiq: float):
        super().__init__(PIN, balans)
        self.kreditmiq = kreditmiq
    
    def kredit_ver(self):
        self.balans += self.kreditmiq
        print(f"Kreditiniz {self.kreditmiq} məbləğində verildi. Yeni balans: {self.balans}")
    
    def kredit_odenisi(self):
        ayliq_odenis = self.kreditmiq / 12
        self.balans -= ayliq_odenis
        print(f"Kreditinizin aylıq ödənişi {ayliq_odenis} məbləğindədir. Yeni balans: {self.balans}")

Account = Coders(2004, 1455)
Account.balans_goster()
Account.medaxil(804030205050)
Account.mexaric(3300)

Creditaccount = Kredit(2004, 1000000, 223400)
Creditaccount.balans_goster()
Creditaccount.kredit_ver()
Creditaccount.kredit_odenisi()
