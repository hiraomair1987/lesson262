class BMW():
    def fuel_type(self):
        print("Premium gasoline + electricity (plug-in hybrid)")

    def max_speed(self):
        print("a BMW can go 305 kmh")



class Ferrari():
    def fuel_type(self):
        print("Premium gasoline + electricity (plug-in hybrid)")

    def max_speed(self):
        print("a Ferrari can go 340 km/h")




obj_BMW = BMW()
obj_Ferrari = Ferrari()


for car  in(obj_BMW, obj_Ferrari):
    car.fuel_type()
    car.max_speed()
    