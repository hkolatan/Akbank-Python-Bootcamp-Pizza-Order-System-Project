# Kütüphaneleri içe aktarıyoruz.
import csv
import datetime

# Menü dosyasının yazdırılması.
with open("Menu.txt", "w") as menu:
    menu.write("Global Pizzaya Hoş Geldiniz! \n")
    menu.write("* Lütfen Bir Pizza Tabanı Seçiniz: \n")
    menu.write("1: Klasik \n")
    menu.write("2: Margarita \n")
    menu.write("3: Türk Pizza \n")
    menu.write("4: Sade Pizza \n")
    menu.write("* ve seçeceğiniz sos: \n")
    menu.write("11: Zeytin \n")
    menu.write("12: Mantar \n")
    menu.write("13: Keçi Peyniri \n")
    menu.write("14: Et \n")
    menu.write("15: Soğan \n")
    menu.write("16: Mısır \n")
    menu.write("* Teşekkür ederiz!")
    
# Pizza üst sınıfını oluşturalım. init metodu ile parametreleri tanımlıyoruz. Kapsülleme için get_description() 
# ve get_cost() yöntemlerini tanımlıyoruz.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

# Pizza alt sınıfını oluşturuyoruz.
class KlasikPizza(Pizza): 
    def __init__(self):
        super().__init__("Klasik Pizza", 30.00)

class MargaritaPizza(Pizza): 
    def __init__(self):
        super().__init__("Margarita Pizza", 28.50)
        
class TurkPizza(Pizza): 
    def __init__(self):
        super().__init__("Türk Pizza", 50.00)

class SadePizza(Pizza): 
    def __init__(self):
        super().__init__("Sade Pizza", 20.00)

# Decorator süper sınıfını oluşturuyoruz.
class Decorator(Pizza):
  def __init__(self, component, description, cost):
    self.component = component
    self.description  = description
    self.cost = cost

  def get_description(self):
    return self.component.get_description() + " " + Pizza.get_description(self)

  def get_cost(self):
    return self.component.get_cost() + Pizza.get_cost(self)

# Decoratorların alt sınıfını oluşturuyoruz.
class Zeytin(Decorator):
  def __init__(self, component):
    super().__init__(component, "Zeytin", 4.00)

class Mantar(Decorator):
  def __init__(self, component):
    super().__init__(component, "Mantar", 10.00)

class KeciPeyniri(Decorator):
  def __init__(self, component):
    super().__init__(component, "Keçi Peyniri", 12.00)

class Et(Decorator):
  def __init__(self, component):
    super().__init__(component, "Et", 15.00)

class Sogan(Decorator):
  def __init__(self, component):
    super().__init__(component, "Soğan", 5.00) 

class Misir(Decorator):
  def __init__(self, component):
    super().__init__(component, "Mısır", 6.00) 

# Main fonksiyonu oluşturuyoruz ve while not döngüsü ve if/elif/else statementlarını kullanarak önce pizza seçimi sonrasında da sos seçimini gerçekleştiriyoruz.
def main():
    with open("Menu.txt", "r") as menu:
        print(menu.read())
        
# Pizza türü ve sos seçimlerinin seçilmesi
    pizza = None
    while not pizza:
        pizza_choice = input("Bir pizza türü seçiniz (1-4): ")
        if pizza_choice == "1":
            pizza = KlasikPizza()
        elif pizza_choice == "2":
            pizza = MargaritaPizza()
        elif pizza_choice == "3":
            pizza = TurkPizza()
        elif pizza_choice == "4":
            pizza = SadePizza()
        else:
             print("Lütfen geçerli bir seçim yapınız.")

    sauce = None
    while not sauce:
        sauce_choice = input("Bir sos seçiniz (11-16): ")
        if sauce_choice == "11":
            sauce = Zeytin(pizza)
        elif sauce_choice == "12":
            sauce = Mantar(pizza)
        elif sauce_choice == "13":
            sauce = KeciPeyniri(pizza)
        elif sauce_choice == "14":
            sauce = Et(pizza)
        elif sauce_choice == "15":
            sauce = Sogan(pizza)
        elif sauce_choice == "16":
            sauce = Misir(pizza)
        else:
         print("Lütfen geçerli bir seçim yapınız.")

    toplam_tutar = sauce.get_cost()

    # Kullanıcı bilgilerinin alınması   
    isim = input("İsim: ")
    tc = input("TC Kimlik Numarası: ")
    kart_no = input("Kredi Kartı Numaranız: ")  
    kart_sifre = input("Kredi Kartı Şifreniz: ")
    
    # Sipariş bilgilerini veritabanına ekleyelim
    # Dosya daha önce varsa "a" (append) modunda açılır, böylece mevcut veriler korunur ve yeni satır eklenir. 
    with open ("Orders_Database.csv", "a", newline='') as database:
               rows = ["İsmi", "TC" , "Kart Numarası", "Pizza Adı", "Toplam Tutar", "Sipariş Tarihi", "Kart Şifresi"]
               writer = csv.writer(database)
               writer.writerow(rows)
               writer.writerow([isim, tc, kart_no, sauce.get_description(), toplam_tutar , datetime.datetime.now(), kart_sifre])

    # Sipariş bilgilerinin ekrana yazdırılan çıktıları
    print("---------------------------------------------------------------")
    print("Sipariş Detayları:")
    print("Ad:", isim)
    print("TC Kimlik Numarası:", tc)
    print("Kredi Kartı Numarası:", kart_no)
    print("Toplam Fiyat:", toplam_tutar)
    print("Siparişiniz alınmıştır. Toplam tutar: " + str(toplam_tutar) + " TL. Bizi tercih ettiğiniz için teşekkür ederiz!")
main()