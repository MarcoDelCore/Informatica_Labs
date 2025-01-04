def main():
    sales = []
    customers = []
    sale = int(input("Insert the sale: "))
    while sale != 0:
        sales.append(sale)
        customer = input("Insert the customer name: ")
        customers.append(customer)
        sale = int(input("Insert the sale or 0 to exit: "))
    nameofbestcustomer(sales, customers)


def nameofbestcustomer(sales, customers):
    max_sale = max(sales)
    winner = sales.index(max_sale)
    customer = customers[winner]
    print("The winner is ", customer)


main()
