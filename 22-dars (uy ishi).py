class Car:
    def __init__(self,name,year,color,model):
        self.name = name
        self.year = year
        self.color = color
        self.model = model
car1 = Car('Nexia',2019,'Grey','Shevrolet')
print(f"{car1.name} - {car1.year} yil, Rangi: {car1.color}, Marka: {car1.model}")
class Car:
    def nation(self,nation):
        self.nation = nation
car1 = Car('Nexia',2019,'Grey','Shevrolet','Uzb')
print(f"{car1.name} - {car1.year} yil, Rangi: {car1.color}, Marka: {car1.model}, {car1.nation}")
