
class Phone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def __str__(self):
        return f"{self.brand} {self.model} - Price: ${self.price}, Storage: {self.storage}GB"

    def update_brand(self, brand):
        self.brand = brand

    def update_model(self, model):
        self.model = model

    def update_price(self, price):
        self.price = price

    def update_storage(self, storage):
        self.storage = storage

    def delete_brand(self):
        del self.brand

    def delete_model(self):
        del self.model

    def delete_price(self):
        del self.price

    def delete_storage(self):
        del self.storage


def main_menu():
    print("Phone Management System")
    print("1. Create Phone")
    print("2. Modify Phone")
    print("3. Delete Phone")
    print("4. List Phones")
    print("5. Exit")


def create_phone():
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = float(input("Enter phone price: "))
    storage = int(input("Enter phone storage in GB: "))
    return Phone(brand, model, price, storage)


def modify_phone(phone):
    print("1. Update Brand")
    print("2. Update Model")
    print("3. Update Price")
    print("4. Update Storage")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        phone.update_brand(input("Enter new brand: "))
    elif choice == 2:
        phone.update_model(input("Enter new model: "))
    elif choice == 3:
        phone.update_price(float(input("Enter new price: ")))
    elif choice == 4:
        phone.update_storage(int(input("Enter new storage in GB: ")))


def delete_phone(phone):
    print("1. Delete Brand")
    print("2. Delete Model")
    print("3. Delete Price")
    print("4. Delete Storage")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        phone.delete_brand()
    elif choice == 2:
        phone.delete_model()
    elif choice == 3:
        phone.delete_price()
    elif choice == 4:
        phone.delete_storage()


def list_phones(phones):
    for phone in phones:
        print(phone)


def main():
    phones = []
    while True:
        main_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            phones.append(create_phone())
        elif choice == 2:
            if phones:
                print("Select a phone to modify:")
                phone_list = []
                for i in range(len(phones)):
                    phone_list.append(f"{i+1}. {phones[i]}")
                for phone in phone_list:
                    print(phone)
                choice = int(input("Enter your choice: "))
                modify_phone(phones[choice-1])
            else:
                print("No phones to modify.")
        elif choice == 3:
            if phones:
                print("Select a phone to delete:")
                phone_list = []
                for i in range(len(phones)):
                    phone_list.append(f"{i+1}. {phones[i]}")
                for phone in phone_list:
                    print(phone)
                choice = int(input("Enter your choice: "))
                del phones[choice-1]
            else:
                print("No phones to delete.")
        elif choice == 4:
            list_phones(phones)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()