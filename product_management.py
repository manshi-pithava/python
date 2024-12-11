
products = []
customers = []

def product_manager():
    while True:

        print("\nProduct Manager")
        print("1. Product")
        print("2. Customer")
        print("3. view")
        print("4. Exit")
       
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            # Option for adding a product
            product_name = input("Enter the product name: ")
            products.append(product_name)
            print("Product added successfully!  \n  your product is -->",product_name)

        elif choice == "2":
           
            customer_name = input("Enter the customer name: ")
            customers.append(customer_name)
            print("Customer added successfully!" ,customer_name)

        elif choice == "3":
           
            print("Exiting Product or customer")
            print(products)
            print("----------------------")
            print(customers)
        
        elif choice == "4":
           
            print("Exiting Product Manager. Goodbye!")
            break


        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


product_manager()
