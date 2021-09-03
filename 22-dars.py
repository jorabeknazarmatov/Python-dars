class Shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.ism} {self.familiya}."
        info += f"Passport: {self.passport}, {self.tyil} - yilda tug'ilgan."
        return info

    def get_age(self,yil):
        return yil - self.tyil

inson = Shaxs('To`rabek','Nazarmatov',"AA0072123",1996)
print(f"{inson.get_info()} {inson.get_age(2021)}yoshda")
