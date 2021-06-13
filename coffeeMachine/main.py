from menu import MENU, resources


def print_line():
    print("----------------------------------------------------------------")


def sufficient(type_c):
    """"Checks if supplies are sufficient to make the coffee"""
    avail_milk = resources["milk"]
    avail_water = resources["water"]
    avail_coffee = resources["coffee"]

    req_water = MENU[type_c]["ingredients"]["water"]
    req_coffee = MENU[type_c]["ingredients"]["coffee"]
    # espresso doesn't need milk
    if "milk" not in MENU[type_c]["ingredients"]:
        req_milk = 0
    else:
        req_milk = MENU[type_c]["ingredients"]["milk"]

    # checking availability to satisfy the need
    if req_milk <= avail_milk:
        if req_water <= avail_water:
            if req_coffee <= avail_coffee:
                # only if we have all the resources, we return true,
                # otherwise we print respective message and return
                # False
                return True
            else:
                print("Sorry, there's not enough coffee for your order :( ")
                return False
        else:
            print("Sorry, there's not enough water for your order :( ")
            return False
    else:
        print("Sorry, there's not enough milk for your order :( ")
        return False


def payment(type_c):
    price = MENU[type_c]["cost"]
    # prompt price to user
    print(f"You must pay ${round(price,2)} for your {type_c}")
    quarters = int(input("Enter number of quarters : "))
    dimes = int(input("Enter number of dimes : "))
    nickels = int(input("Enter number of nickels : "))
    pennies = int(input("Enter number of pennies : "))
    paid = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    print(f"You have paid ${round(paid,2)}")
    # check if enough, return True indicates successful payment
    if paid == price:
        print("Payment Success 😄")
        return True
    elif paid > price:
        # give change to customer
        c = paid - price
        change = round(c, 2)
        print(f"Here is ${change} in return.")
        return True
    elif paid < price:
        return False


def make_coffee(type_c):
    req_water = MENU[type_c]["ingredients"]["water"]
    if "milk" not in MENU[type_c]["ingredients"]:
        req_milk = 0
    else:
        req_milk = MENU[type_c]["ingredients"]["milk"]
    req_coffee = MENU[type_c]["ingredients"]["coffee"]
    # deduct values from resources
    resources["water"] -= req_water
    resources["milk"] -= req_milk
    resources["coffee"] -= req_coffee
    resources["money"] += MENU[type_c]["cost"]


def prompt(type_c):
    if sufficient(type_c):
        if payment(type_c):
            make_coffee(type_c)
            print(f"Here's your {type_c} ☕ !")
            return
        else:
            print("You haven't inserted enough coins, transaction failed :(")
    else:
        print("Sorry for the inconvenience")


def print_report():
    print("********  REPORT  ********")
    milk = resources["milk"]
    water = resources["water"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Milk : {milk} ml\nWater : {water} ml\nCoffee : {coffee} g\nMoney : ${money}")


# main entry point
while True:
    print_line()
    print("Hello Customer ! 😄")
    op = input("What kind of coffee would you like?\n☕ latte\n☕ espresso\n☕ cappuccino\nEnter 'report' for checking "
               "ingredients\nEnter 'off' to switch off the machine : ").lower()
    if op == "off":
        break
    elif op == "report":
        print_report()
    else:
        prompt(op)
print("Shutting Down ! GoodBye 📴")
