from sortedcontainers import SortedList
class restaurant:
    def __init__(self):

        self.res_menu = {}
        # which res have the same item, reverse map
        self.item_to_res = {}
        # restaurant item reviews:
        self.res_stars = {}


    def add_to_menu(self, res_id, items_price):
        if res_id not in self.res_menu:
            self.res_menu[res_id] = set()
        self.res_menu[res_id].update(items_price)

        for item, price in items_price:
            if item not in self.item_to_res:
                self.item_to_res[item] = set()
            self.item_to_res[item].add((res_id, price))

        print(self.res_menu)
        print("item_to_res",self.item_to_res)

    def order_item(self, item_name):
        return self.item_to_res[item_name]

    def rate_item(self, item, res_id, rating):
        if item not in self.res_stars:
            self.res_stars[item] = SortedList(key=lambda x: -x[1])
        self.res_stars[item].add((res_id, rating))
        print(self.res_stars)


if __name__ == '__main__':
    rs = restaurant()
    rs.add_to_menu("res1", [('vegburger', '10'), ('noodles', 20)])
    rs.add_to_menu("res2", [('vegburger', '15'), ('pasta', 25)])

    print(rs.order_item('vegburger'))
    rs.rate_item('vegburger', 'res1', '5')






