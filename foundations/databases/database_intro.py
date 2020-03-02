### Challenge: How many drinks do you need to buy to throw a great party?
# you will have a list of your friends, and their favorite drink.
# you will also know how many drinks of a certain type are drunk per hour


#list of your friends and their favorite drink
favorite_drinks = {'Adam' : 'Gin and Tonic'
                    , 'Angela' : 'Mate Vodka'
                    , 'Sven' : 'Whiskey'
                    , 'Alexandra' : 'Whiskey'
                    , 'Michael' : 'White Wine'
                    , 'Ariana' : 'Gin and Tonic'
                    , 'Thomas' : 'beer'
                    , 'Eduardo' : 'White Wine'
                    , 'Leanne' : 'Red Wine'
                    , 'Karla' : 'Whiskey'
                    , 'Taylor' : 'Mate Vodka'
                    , 'Jonathan' : 'Water'
                    , 'Paulina' : 'white wine'
                    , 'Severin' : 'long island ice tea'
                    , 'Roman' : 'moscow mule'}


#types of drinks people drink, with lists of examples
cocktails = ['gin and tonic', 'mate vodka', 'rum and coke', 'long island ice tea', 'moscow mule']

wines = ['red wine', 'white wine']

liquors = ['whiskey', 'gin', 'vokda']

nonalcoholic = ['tea', 'water', 'orange juice']

# number of drinks per hour people drink, depeneding on the type.
number_of_drinks_per_hour_per_type = {'cocktails':1, 'beers':3,'wines':2,'liquors':2,'nonalcoholic':3}


shopping_list = {
    'gin and tonic' : 0
    , 'long island ice tea' : 0
    , 'moscow mule' : 0
    , 'mate vodka' : 0
    , 'whiskey' : 0
    , 'rum and coke' : 0
    , 'red wine' : 0
    , 'white wine' : 0
    , 'whiskey' : 0
    , 'gin' : 0
    , 'vodka' : 0
    , 'tea' : 0
    , 'water' : 0
    , 'orange juice' : 0
    , 'beer' : 0
}

duration_of_party = 6

for name, drink in favorite_drinks.items():
    drink = drink.lower()
    if drink in cocktails:
        shopping_list[drink] += (1 * duration_of_party)
    elif drink in wines:
        shopping_list[drink] += (2 * duration_of_party)
    elif drink in liquors:
        shopping_list[drink] += (2 * duration_of_party)
    elif drink in nonalcoholic:
        shopping_list[drink] += (3 * duration_of_party)
    elif drink == 'beer':
        shopping_list[drink] += (3 * duration_of_party)

print(shopping_list)
