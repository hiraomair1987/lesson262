class Pakistan():
    def capital(self):
        print("Islamabad is th ecapital  of Pakistan")

    def language(self):
        print("Urdu is the most widely spoken language in Pakistan")

    def type(self):
        print("Pakistan is a developing country")


class USA():
    def capital(self):
        print("Washingtan, D.C. is the capital of USA")

    def language(self):
        print("English is the primary language of USA")

    def type(self):
        print("USA is a developed country")



obj_Pak = Pakistan()
obj_USA = USA()


for country in(obj_Pak, obj_USA):
    country.capital()
    country.language()
    country.type()