import itertools

from restaurant import restaurant

_id = itertools.count(1)
class Restaurant:
    def __init__(self,name):
        self.res_id = next(_id)
        self.name = name
        self.menu = set()
        self.rating_sum = 0
        self.rating_count = 0


    def avg_rating(self, ):
        return self.rating_sum/self.rating_count if self.rating_count else 0

    def avg_item_rating(self, rid):
        pass

class FoodOrderSystem:
    def __init__(self):
        self.foods = {}
        self.orders = {}
        self.restaurants = {}

    def add_item(self, name):
        fid = next(_id)
        self.foods[fid] = name
        return fid

    def add_restaurant(self, name):
        rid = Restaurant(name)
        self.restaurants[rid.res_id] = rid
        return rid.res_id

    def add_to_menu(self, res, food):
        self.restaurants[res].menu.update(food)

    def create_order(self, user_id, res_id, items):
        oid = next(_id)
        self.orders[oid] = {
            "user_id": user_id,
            "restaurant_id": res_id,
            "items": items
        }
        return oid

if __name__ == '__main__':
    fo = FoodOrderSystem()
    burger = fo.add_item('burger')
    pasta = fo.add_item('pasta')

    res1 = fo.add_restaurant('res1')
    res2 = fo.add_restaurant('res2')

    print(fo.add_to_menu(res1,[burger, pasta]))

    oid = fo.create_order()



