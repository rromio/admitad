import json

bid_list = []
optimum_price_list = [[6850183, 52300000], [6850184, 52170000]]

def get_optimum_price(id):
    for item in optimum_price_list:
        if item[0] == id:
            return item[1]

g = get_optimum_price(6850185)

print(g)