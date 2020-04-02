class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 2

    def describe_restaurant(self):
        print(self.restaurant_name + ' ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is opening now")

    def set_number_served(self, number):
        self.number_served = number

    def incremet_login_attempts(self,increcing_number):
        self.number_served += increcing_number


my_restaurant = Restaurant('ji', 'chicken')
print(str(my_restaurant.number_served) + "people" + ".")
my_restaurant.incremet_login_attempts(2)
my_restaurant.incremet_login_attempts(3)
print(my_restaurant.number_served)