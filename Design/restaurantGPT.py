from collections import defaultdict
import itertools

_id = itertools.count(1)

class Restaurant:
    def __init__(self, name):
        self.id = next(_id)
        self.name = name
        self.menu = set()                  # food_ids
        self.rating_sum = 0
        self.rating_count = 0
        self.item_ratings = defaultdict(lambda: [0, 0])   # food_id -> [sum, count]

    def avg_rating(self):
        return self.rating_sum / self.rating_count if self.rating_count else 0

    def avg_item_rating(self, fid):
        s, c = self.item_ratings[fid]
        return s/c if c else 0


class FoodOrderingSystem:
    def __init__(self):
        self.foods = {}                   # food_id -> name
        self.restaurants = {}             # rest_id -> Restaurant
        self.orders = {}                  # order_id -> (rest_id, [food_ids])

    # --- Basic creation ---
    def add_food(self, name):
        fid = next(_id)
        self.foods[fid] = name
        return fid

    def add_restaurant(self, name):
        r = Restaurant(name)
        self.restaurants[r.id] = r
        return r.id

    def add_menu_item(self, rest_id, food_id):
        self.restaurants[rest_id].menu.add(food_id)

    # --- Orders ---
    def create_order(self, user_id, rest_id, items):
        oid = next(_id)
        self.orders[oid] = (rest_id, items)
        return oid

    # --- Ratings ---
    def rate_order(self, order_id, restaurant_rating, item_ratings=None):
        rest_id, items = self.orders[order_id]
        r = self.restaurants[rest_id]

        # restaurant rating
        r.rating_sum += restaurant_rating
        r.rating_count += 1

        # per-item rating
        item_ratings = item_ratings or {}
        for fid, rating in item_ratings.items():
            s, c = r.item_ratings[fid]
            r.item_ratings[fid] = [s + rating, c + 1]

    # --- Queries ---
    def top_restaurants(self, k=5):
        res = list(self.restaurants.values())
        res.sort(key=lambda r: r.avg_rating(), reverse=True)
        return [(r.name, r.avg_rating()) for r in res[:k]]

    def top_restaurants_for_food(self, food_id, k=5):
        res = []
        for r in self.restaurants.values():
            if food_id in r.menu:
                res.append((r, r.avg_item_rating(food_id)))
        res.sort(key=lambda x: x[1], reverse=True)
        return [(r.name, score) for r, score in res[:k]]


#========================
sys = FoodOrderingSystem()

# Foods
burger = sys.add_food("Veg Burger")
roll = sys.add_food("Spring Roll")

print(burger,roll)
print(sys.foods)

# Restaurants
r1 = sys.add_restaurant("Burger King")
r2 = sys.add_restaurant("McDonalds")

sys.add_menu_item(r1, burger)
sys.add_menu_item(r2, burger)
sys.add_menu_item(r1, roll)

# Orders
o1 = sys.create_order(101, r1, [burger, roll])
o2 = sys.create_order(102, r2, [burger])

# Ratings
sys.rate_order(o1, restaurant_rating=5, item_ratings={burger:5, roll:4})
sys.rate_order(o2, restaurant_rating=4, item_ratings={burger:4})

print(sys.top_restaurants())
print(sys.top_restaurants_for_food(burger))
