class Onlineshop:
  def __init__(self, name ,url):
    self.name = name
    self.url = url
    self.products = {}

  def addingItemsToCart(self, customer, product, quantity):
    if product in customer.cart:
      customer.cart[product] += quantity
    else:
      customer.cart[product] = quantity

  # def checkout(self, customer):
    # total = sum(product.price * quantity for product, quantity in customer.cart.items())
    # order = {order_id, items}
    # customer.past_orders.append(customer.cart.copy())

  def checkout(self, customer):
    if not customer.cart:
      return "Empty"

    order_id = len(customer.past_orders) + 1
    total = sum(product.price * quantity for product, quantity in customer.cart.items())
    order = {
      "order_id": order_id,
      "items": customer.cart.copy(),
      "total": total
      }
    
    customer.past_orders[order_id] = order
    customer.cart.clear()
    return f"Order #{order_id} placed success!"
  def orderTracking(self, customer, order_id):
        """
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                return order
        return "Order not found."
        """
        return customer.past_orders.get(order_id, "Order not found.")
class Product:
  def __init__(self, name, description, price, online_shop):
    self.name = name
    self.description = description
    self.price = float(price)
    self.online_shop = online_shop

class Customer:
  def __init__(self, name, email, address):
    self.name = name
    self.email = email
    self.address = address
    self.cart = {}
    self.past_orders = {}

my_store = Onlineshop("Gadget World", "www.gadgetworld.com")
my_product1 = Product("Laptop", "noob", "49", "dildo")
my_product2 = Product("Mouse", "noobs", "496", "dildo6")
my_product3 = Product("Mouse", "noobs", "496", "dildo6")
john = Customer("john", "jojo@ghjiotdh", "135897056")

my_store.addingItemsToCart(john,my_product2,1)
print(my_store.checkout(john))
print(my_store.orderTracking(john,1))