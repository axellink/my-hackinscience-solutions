class Dish(object):
    def __init__(self, name, preparation_time, dish_type):
        if not dish_type in ["starter", "dish", "dessert"]:
            raise ValueError()
        
        self.name = name
        self.preparation_time = preparation_time
        self.dish_type = dish_type

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Dish):
            raise NotImplementedError()
        
        return self.preparation_time == __value.preparation_time
    
    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Dish):
            raise NotImplementedError()
        
        return self.preparation_time < __value.preparation_time
    
    def __le__(self, __value: object) -> bool:
        return self < __value or self == __value
    
    def __ge__(self, __value: object) -> bool:
        return not self < __value
    
    def __gt__(self, __value: object) -> bool:
        return not self < __value and self != __value
    
    def __str__(self) -> str:
        return self.name


class Menu(object):
    def __init__(self, name) -> None:
        self.name = name
        self.dishes = {
            "starter": [],
            "dish": [],
            "dessert": []
        }
    
    def add_dish(self, dish: Dish) -> None:
        self.dishes[dish.dish_type] += [dish]

    def get_starters(self) -> list:
        return self.dishes["starter"]
    
    def get_dishes(self) -> list:
        return self.dishes["dish"]
    
    def get_desserts(self) -> list:
        return self.dishes["dessert"]
    
    def get_minimum_preparation_time(self) -> int:
        return (min(self.dishes["starter"], default=Dish("",0,"starter")).preparation_time +
                min(self.dishes["dish"], default=Dish("",0,"dish")).preparation_time +
                min(self.dishes["dessert"], default=Dish("",0,"dessert")).preparation_time)

    def get_maximum_preparation_time(self) -> int:
        return (max(self.dishes["starter"], default=Dish("",0,"starter")).preparation_time +
                max(self.dishes["dish"], default=Dish("",0,"dish")).preparation_time +
                max(self.dishes["dessert"], default=Dish("",0,"dessert")).preparation_time)

    def __add__(self, __value):
        res = Menu(f"{self.name} & {__value.name}")
        res.dishes = {
            "starter" : self.get_starters() + __value.get_starters(),
            "dish" : self.get_dishes() + __value.get_dishes(),
            "dessert" : self.get_desserts() + __value.get_desserts()
        }
        return res
    
    def __str__(self) -> str:
        res = []
        for key, value in self.dishes.items():
            res += [key.upper()]
            for i in value:
                res += [str(i)]
            res += [""]
        return "\n".join(res[:-1])

    

if __name__ == "__main__":
    d1 = Dish("Yolo", 5, "dessert")
    d2 = Dish("Toto", 5, "dessert")
    d3 = Dish("Prout", 2, "dessert")

    print(d1)

    assert(d1 == d2)
    assert(d1 >= d2)
    assert(d1 <= d2)
    assert(d2 > d3)
    assert(d2 >= d3)
    assert(d3 < d2)
    assert(d3 <= d2)

    m = Menu("FullDessert")
    m.add_dish(d1)
    m.add_dish(d2)
    m.add_dish(d3)
    print(m.get_maximum_preparation_time())
    print(m.get_minimum_preparation_time())

    m2 = m + m
    print(m2)