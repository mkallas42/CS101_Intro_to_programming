"""
You work at Len’s Slice, a new pizza joint in the neighborhood.

You are going to use your knowledge of Python lists to organize some of your sales data.
"""

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
# print(num_two_dollar_slices)

num_pizzas = len(toppings)
# print(num_pizzas)

# print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"],
                    [7, "anchovies"], [2, "mushrooms"]]
# print(pizza_and_prices)

cheapest_pizza = sorted(pizza_and_prices)[0]
# print(cheapest_pizza)

priciest_pizza = sorted(pizza_and_prices)[-1]
# print(priciest_pizza)

pizza_and_prices.pop(-2)
# print(pizza_and_prices)

pizza_and_prices.append([2.5, "peppers"])
# print(sorted(pizza_and_prices))

three_cheapest = sorted(pizza_and_prices)[:3]
print(three_cheapest)