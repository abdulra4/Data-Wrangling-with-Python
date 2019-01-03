

class ShoppingCart():

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.total += (quantity * price)
        self.items = {item_name : quantity}

    def remove_item(self, item_name, quantity, price):
        self.total -= (quantity * price)
        if quantity > self.items[item_name]:
            del self.items[item_name]
            self.items[item_name] -= quantity

    def checkout(self, cash_paid):
        balance = 0
        if int(cash_paid) < self.total:
            return "Cash paid not enough"
        balance = int(cash_paid) - self.total
        return balance

import sys, time

def babyShop():
    welcome = '''

    Welcome to Lab Adonis.
    Home of designer babies... 

    We provide a wide selection of genetic permutations to offer you the bespoke child you've always dreamed of 👶🏾👶🏾👶🏾.

    Would you like to buy a genetically modified baby?'''

    for i in welcome:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
    
    shop = input()
    baby_models = {'Nubian Prince': 800, 'Norse Goddess': 875, 'Spawn of Zues': 650, 'Amunet Reborn': 999}
    cart = ShoppingCart()
    while True:
        try:
            if shop in ['yes', 'yeah', 'Yes', 'y', 'YES']:
                print('Please choose your base model?')
                for i,j in baby_models.items():
                    print('£ {} for {}'.format(j, i))

                baby_choice = input()
                if baby_choice in baby_models.keys():
                    cart.add_item(baby_choice, 1, baby_models[baby_choice])
                    print('You have')
                    for item in cart.items:
                        print(item)
                    print('in your basket')
                    print('You total comes to $' + str(cart.total))

                    remove_baby = input('To remove this item please type yes, otherwise enter no to proceed to checkout')
                    if remove_baby in ['yes', 'yeah', 'Yes', 'y', 'YES']:
                        cart.remove_item(baby_choice, 1, baby_models[baby_choice])
                        print('You have', cart.items, 'in your basket')
                        print('You total comes to $' + str(cart.total))
                    else:
                        checkout = input ('Do you want to checkout?')
                        if checkout in ['yes', 'yeah', 'Yes', 'y', 'YES']:
                            cash = input ('Please enter the amount you wish to pay')
                            print(cart.checkout(cash))
                            print('Congratulations!!! Your genetically perfected specimen will be with you soon 😉.')
                            break 
                        else:
                            print('Please feel free to keep perusing our store.')
                else:
                    break
        except:
            print('Sorry we could not help you in this instance. We hope your search goes well 😊.')
            break

while input('Are you here to shop?') in ['yes', 'yeah', 'Yes', 'y', 'YES']:
    babyShop()
    
# Sincerest apologies for the dysfunctional spaghetti code.