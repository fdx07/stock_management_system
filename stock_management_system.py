from prettytable import PrettyTable

def add_product(stock_file):
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))

    with open(stock_file, "r") as file:
        lines = file.readlines()

    found = False
    with open(stock_file, "w") as file:
        for line in lines:
            name, stock_quantity = line.strip().split(",")
            if name == product_name:
                stock_quantity = int(stock_quantity)
                new_quantity = stock_quantity + quantity
                file.write(f"{name},{new_quantity}\n")
                found = True
            else:
                file.write(line)

    if not found:
        with open(stock_file, "a") as file:
            file.write(f"{product_name},{quantity}\n")

    print("Product added/updated successfully!")


def update_product(stock_file):
    product_name = input("Enter the product name: ")
    new_quantity = int(input("Enter the new quantity: "))

    with open(stock_file, "r") as file:
        lines = file.readlines()

    found = False
    with open(stock_file, "w") as file:
        for line in lines:
            name, quantity = line.strip().split(",")
            if name == product_name:
                file.write(f"{name},{new_quantity}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("Product updated successfully!")
    else:
        with open(stock_file, "a") as file:
            file.write(f"{product_name},{new_quantity}\n")
        print("Product not found in the stock. But added succesfully!")


def view_stock(stock_file):
    table = PrettyTable()
    table.field_names = ["Product", "Quantity"]
    table.border = True
    table.header = True
    table.align = "l"

    with open(stock_file, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    name, quantity = line.split(",")
                    table.add_row([name, quantity])
                    table.add_row(["-" * len(name), "-" * len(quantity)])  # Separator
                except ValueError:
                    print(f"Invalid data in stock file: {line}")

    # Remove the separator after the last row
    table.del_row(-1)

    print(table)


def sell_product(stock_file):
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity to sell: "))

    with open(stock_file, "r") as file:
        lines = file.readlines()

    found = False
    with open(stock_file, "w") as file:
        for line in lines:
            name, stock_quantity = line.strip().split(",")
            if name == product_name:
                stock_quantity = int(stock_quantity)
                if quantity <= stock_quantity:
                    new_quantity = stock_quantity - quantity
                    file.write(f"{name},{new_quantity}\n")
                    found = True
                    print("Product sold successfully!")
                else:
                    print("Insufficient stock for the sale.")
            else:
                file.write(line)

    if not found:
        print("Product not found in the stock.")


def delete_product(stock_file):
    product_name = input("Enter the product name: ")

    with open(stock_file, "r") as file:
        lines = file.readlines()

    found = False
    with open(stock_file, "w") as file:
        for line in lines:
            name, quantity = line.strip().split(",")
            if name == product_name:
                found = True
                continue  # Skip writing the line for the product to be deleted
            else:
                file.write(line)

    if found:
        print("Product deleted successfully!")
    else:
        print("Product not found in the stock.")


def main():
    stock_file = "stocks.txt"
    file = open(stock_file, 'a')
    file.close()
    
    while True:
        print("1. Add a product")
        print("2. Update a product")
        print("3. View stock data")
        print("4. Sell a product")
        print("5. Delete a product")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(stock_file)
        elif choice == "2":
            update_product(stock_file)
        elif choice == "3":
            view_stock(stock_file)
        elif choice == "4":
            sell_product(stock_file)
        elif choice == "5":
            delete_product(stock_file)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Stock system closed.")


if __name__ == "__main__":
    main()

else:
    print('This Basic Stock Management System Is Written By Faisal Durbaa\n')
    main()

