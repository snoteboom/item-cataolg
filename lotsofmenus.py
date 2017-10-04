from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# create a user
User1 = User(name="Sydney", email="sydney.noteboom@yahoo.com")

# Menu for UrbanBurger
restaurant1 = Restaurant(name="Urban Burger")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="French Fries",
                     description="with garlic and parmesan",
                     price="$2.99",
                     course="Appetizer",
                     restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chicken Sandwich",
                     description="Juicy grilled chicken patty " +
                                 "with tomato mayo and lettuce",
                     price="$5.50",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chocolate Cake",
                     description="fresh baked and served with ice cream",
                     price="$3.99",
                     course="Dessert",
                     restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Pizza",
                     description="Made with 5 different cheeses",
                     price="$7.99",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name="Root Beer",
                     description="16oz of refreshing goodness",
                     price="$1.99",
                     course="Beverage",
                     restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(name="Iced Tea",
                     description="unsweetened with Lemon",
                     price="$.99",
                     course="Beverage",
                     restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(name="Grilled Cheese Sandwich",
                     description="On sourdough toast with American Cheese",
                     price="$3.49",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(name="Veggie Burger",
                     description="Made with freshest of ingredients",
                     price="$5.99",
                     course="Entree",
                     restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chicken Stir Fry",
                     description="with your choice of noodles " +
                                 "vegetables and sauces",
                     price="$7.99",
                     course="Entree",
                     restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Duck Stir Fry",
                     description="with your choice of noodles ",
                     price="$25",
                     course="Entree",
                     restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spicy Tuna Roll",
                     description="Tuna Roll",
                     price="$9.99",
                     course="Appetizer",
                     restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Beef Noodle Soup",
                     description="Beef Noodle soup",
                     price="$7.99",
                     course="Appetizer",
                     restaurant=restaurant2)

session.add(menuItem4)
session.commit()


# Menu for Panda Garden
restaurant3 = Restaurant(name="Cheese Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name="Nachos",
                     description="chips and melted cheese",
                     price="$5.99",
                     course="Appetizer",
                     restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cheese Pizza",
                     description="5 amazing cheese " +
                                 "on 1 great pizza.",
                     price="$7.99",
                     course="Entree",
                     restaurant=restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Cheese plate",
                     description="Assorted cheese plate ",
                     price="$12",
                     course="Entree",
                     restaurant=restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Cheap Wine",
                     description="Some delicous cheap wine ",
                     price="$4.99",
                     course="Beverage",
                     restaurant=restaurant3)
session.add(menuItem4)
session.commit()


# Menu for Tony's Bistro
restaurant5 = Restaurant(name="Tony\'s Bistro ")

session.add(restaurant5)
session.commit()


menuItem1 = MenuItem(name="Cheese Stick Tower",
                     description="Fried Mozzarella.",
                     price="$7.99",
                     course="Entree",
                     restaurant=restaurant5)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Fried Ravioli",
                     description="Deep fried Raviolis ",
                     price="$10.99",
                     course="Entree",
                     restaurant=restaurant5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Mom's Spaghetti",
                     description="A spaghetti with mild sauce.",
                     price="$8.99",
                     course="Entree",
                     restaurant=restaurant5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Chocolate Ice cream",
                     description="A chocolate Icec ream.",
                     price="$6.99",
                     course="Dessert",
                     restaurant=restaurant5)

session.add(menuItem4)
session.commit()


print "added menu items!"
