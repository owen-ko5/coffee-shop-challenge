from customer import Customer
from coffee import Coffee
from order import Order

def start():
    print("=== Coffee Shop Demo - Rewritten Version ===")

    owen = Customer("Owen")
    mitchell = Customer("Mitchell")
    kennedy = Customer("Kennedy")
    print(f"Created users: {owen.name}, {mitchell.name}, {kennedy.name}")

    boba = Coffee("Boba")
    black = Coffee("Black")
    print(f"Created drinks: {boba.name}, {black.name}")

    order1 = owen.create_order(black, 5.0)
    order2 = mitchell.create_order(boba, 4.0)
    order3 = kennedy.create_order(boba, 6.0)

    print(f"Order 1: {order1.customer.name} bought {order1.coffee.name} for ${order1.price}")
    print(f"Order 2: {order2.customer.name} bought {order2.coffee.name} for ${order2.price}")
    print(f"Order 3: {order3.customer.name} bought {order3.coffee.name} for ${order3.price}")

    print(f"\nOwen's orders: {len(owen.orders())}")
    print(f"Owen likes: {[c.name for c in owen.coffees()]}")
    print(f"Customers who bought Boba: {[c.name for c in boba.customers()]}")
    print(f"Boba total sales: {boba.num_orders()}")

    print(f"\nBoba average price: ${boba.average_price():.2f}")
    print(f"Black total sales: {black.num_orders()}")

    aficionado = Customer.most_aficionado(boba)
    print(f"\nTop fan of Boba: {aficionado.name if aficionado else 'None'}")

    americano = Coffee("Americano")
    empty_fan = Customer.most_aficionado(americano)
    print(f"Top fan of Americano: {empty_fan if empty_fan else 'None'}")


if __name__ == "__main__":
    start()