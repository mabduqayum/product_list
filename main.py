import sys
from product_list import ProductList

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <filename> <action>")
        print("Actions: add, update, delete, total")
        sys.exit(1)

    filename = sys.argv[1]
    action = sys.argv[2]

    product_list = ProductList(filename)

    match action:
        case "add":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            product_list.add_product(name, price)
        case "update":
            name = input("Enter product name to update: ")
            price = float(input("Enter new price: "))
            product_list.update_product(name, price)
        case "delete":
            name = input("Enter product name to delete: ")
            product_list.delete_product(name)
        case "total":
            product_list.print_total()

        # added this for debugging purposes
        case "list":
            product_list.list_products()
        case _:
            print("Invalid action")
            sys.exit(1)

if __name__ == "__main__":
    main()
