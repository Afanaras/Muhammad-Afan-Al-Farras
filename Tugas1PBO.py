#Tugas 1
print('Soal 1')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} restaurant has {self.cuisine_type} cuisine types.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is open.")
    
rest1 = Restaurant('restaurant', 'Fast Food')
print(f"{rest1.restaurant_name}")
print(f"Type of Cuisine is {rest1.cuisine_type}")
rest1.describe_restaurant()
rest1.open_restaurant()
print()

#Tugas 2
print('Soal 2')

ampera_minang = Restaurant('Ampera Minang', 'Fast Food')
pondok_barangin = Restaurant('Pondok Barangin', 'Ethnic')
uda_sayang = Restaurant('Uda Sayang', 'Casual Dinning')

ampera_minang.describe_restaurant()
pondok_barangin.describe_restaurant()
uda_sayang.describe_restaurant()
print()

#Tugas 3
print('Soal 3')

class User:
    def __init__(self, first_name, last_name, address, age, job, status):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.job = job 
        self.status = status 
    def describe_user(self):
        print(
            f"First Name : {self.first_name}\n"
            f"Last Name : {self.last_name}\n"
            f"Address : {self.address}\n"
            f"Job : {self.job}\n"
            f"Status : {self.status}"
        )
    def greet_user(self):
        print(f"Welcome {self.first_name}, Nice to meet you")
    
naruto = User('Naruto', 'Uzumaki', 'Palembang', 25, 'Influencer', 'Married')
naruto.describe_user()
naruto.greet_user()
print()

ferry = User('Ferry', 'Irwandi', 'Jambi', 33, 'Content Creator', 'Married')
ferry.describe_user()
ferry.greet_user()
print()

mutia = User('Mutia', 'Savira', 'Bengkulu', 21, 'Reporter', 'Single')
mutia.describe_user()
mutia.greet_user()

        