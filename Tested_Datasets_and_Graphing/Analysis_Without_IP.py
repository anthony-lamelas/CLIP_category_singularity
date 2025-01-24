# %%
# !pip install pandas
# !pip install matplotlib

# %%
import pandas as pd
import numpy as np
import analysistopy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# %%
def dict_size(dict):
    total_count = sum(len(values) for values in dict.values())
    print(total_count)

# %% [markdown]
# # Accuracy Functions

# %%
def CDcheck_accuracy(csv_path, dictionary):

    normalized_dict = {key.lower(): [value.lower() for value in values] for key, values in dictionary.items()}

    # Create a reverse lookup dictionary
    reverse_dict = {}
    for key, values in normalized_dict.items():
        for value in values:
            reverse_dict[value] = key  # Map all variations to the primary key

    data = pd.read_csv(csv_path, header=None, names=['file_path', 'label'])

    data['label'] = data['label'].str.strip().str.lower()

    count = 0
    total = 0

    for index, row in data.iterrows():

        path_parts = row['file_path'].split('/')
        if len(path_parts) > 2:
            if any(char.isupper() for char in path_parts[-1]):
                name = 'cat'
            else:
                name = 'dog'

            # Find the primary key for the label using the reverse lookup dictionary
            primary_key = reverse_dict.get(row['label'], None)

            if primary_key and name in normalized_dict[primary_key]:
                count += 1
        total += 1

    accuracy = count / total if total > 0 else 0
    return round(accuracy * 100, 2)

# %%
def aObase_accuracy(csv_path):

    data = pd.read_csv(csv_path, header=None, names=['file_path', 'label'])

    # Strip and convert labels to lowercase
    data['label'] = data['label'].str.strip().str.lower()

    count = 0
    total = 0

    for index, row in data.iterrows():

        path_parts = row['file_path'].split('/')
        if len(path_parts) > 2:
            vehicle_name = path_parts[-2].strip().lower()  

            # Check if the label and vehicle name match in the dictionary
            if row['label'] == vehicle_name:
                count += 1
        total += 1

    accuracy = count / total if total > 0 else 0
    return round(accuracy * 100, 2)

# %%
def card_accuracy(csv_path, acc_dict):
    data = pd.read_csv(csv_path, header=None, names=['file_path', 'label'])

    # Normalize labels
    data['label'] = data['label'].str.strip().str.lower()

    # Normalize the dictionary keys and values
    normalized_dict = {key.lower(): [v.lower() for v in values] for key, values in acc_dict.items()}

    count = 0
    total = 0

    for index, row in data.iterrows():
        path_parts = row['file_path'].split('/')

        if len(path_parts) > 2:
            vehicle_key = path_parts[-2].strip().lower()  # Extract key from [-2]
            label = row['label']

            # Find a matching key in the dictionary
            matched_key = next((key for key in normalized_dict if key in vehicle_key), None)

            if matched_key:
                # Check if the label matches any of the values for the matched key
                if any(value in label for value in normalized_dict[matched_key]):
                    count += 1
        total += 1

    accuracy = count / total if total > 0 else 0
    return round(accuracy * 100, 2)


# %%
def aOcheck_accuracy(csv_path, dictionary):

    normalized_dict = {key.lower(): [value.lower() for value in values] for key, values in dictionary.items()}

    # Create a reverse lookup dictionary
    reverse_dict = {}
    for key, values in normalized_dict.items():
        for value in values:
            reverse_dict[value] = key  # Map all variations to the primary key

    data = pd.read_csv(csv_path, header=None, names=['file_path', 'label'])

    data['label'] = data['label'].str.strip().str.lower()

    count = 0
    total = 0

    for index, row in data.iterrows():

        path_parts = row['file_path'].split('/')
        if len(path_parts) > 2:
            name = path_parts[-2].strip().lower()  # Normalize name

            # Find the primary key for the label using the reverse lookup dictionary
            primary_key = reverse_dict.get(row['label'], None)

            if primary_key and name in normalized_dict[primary_key]:
                count += 1
        total += 1

    accuracy = count / total if total > 0 else 0

    print(round(accuracy * 100, 2))
    return round(accuracy * 100, 2)

# %%
def flowers_accuracy(csv_path, flowers_dict):
    # Reverse the dictionary to have flower names as keys
    reversed_dict = {}
    for key, values in flowers_dict.items():
        for value in values:
            reversed_dict[value.strip().lower()] = key  # Ensure the key is normalized

    # Read the CSV file (pandas is used for ease of handling CSV data)
    data = pd.read_csv(csv_path, header=None, names=['file_path', 'label'])

    # Clean the labels to be lowercase and strip any whitespace
    data['label'] = data['label'].str.strip().str.lower()

    count = 0
    total = 0

    # Loop through each row in the data
    for index, row in data.iterrows():
        # Extract the flower name from the file path
        path_parts = row['file_path'].split('/')
        if len(path_parts) > 2:
            name = path_parts[-1][:-10].strip().lower()  # Normalize name


            # Find the primary key for the label using the reverse lookup dictionary
            primary_key = reversed_dict.get(row['label'], None)

            if primary_key and name == primary_key:  # Check if the normalized names match
                count += 1
            
        total += 1

    accuracy = count / total if total > 0 else 0

    print(round(accuracy * 100, 2))
    return round(accuracy * 100, 2)


# %% [markdown]
# # Dictionaries

# %% [markdown]
# ## Animal 80

# %%
a80 = {
    "Bear": ["Bear"],
    "Brown Bear": ["Brown Bear"],
    "Bull": ["Bull"],
    "Butterfly": ["Butterfly"],
    "Camel": ["Camel"],
    "Canary": ["Canary"],
    "Caterpillar": ["Caterpillar"],
    "Cattle": ["Cattle"],
    "Centipede": ["Centipede"],
    "Cheetah": ["Cheetah"],
    "Chicken": ["Chicken"],
    "Crab": ["Crab"],
    "Crocodile": ["Crocodile"],
    "Deer": ["Deer"],
    "Duck": ["Duck"],
    "Eagle": ["Eagle"],
    "Elephant": ["Elephant"],
    "Fish": ["Fish"],
    "Fox": ["Fox"],
    "Frog": ["Frog"],
    "Giraffe": ["Giraffe"],
    "Goat": ["Goat"],
    "Goldfish": ["Goldfish"],
    "Goose": ["Goose"],
    "Hamster": ["Hamster"],
    "Harbor Seal": ["Harbor Seal"],
    "Hedgehog": ["Hedgehog"],
    "Hippopotamus": ["Hippopotamus"],
    "Horse": ["Horse"],
    "Jaguar": ["Jaguar"],
    "Jellyfish": ["Jellyfish"],
    "Kangaroo": ["Kangaroo"],
    "Koala": ["Koala"],
    "Ladybug": ["Ladybug"],
    "Leopard": ["Leopard"],
    "Lion": ["Lion"],
    "Lizard": ["Lizard"],
    "Lynx": ["Lynx"],
    "Magpie": ["Magpie"],
    "Monkey": ["Monkey"],
    "Moths and butterflies": ["Moths and butterflies"],
    "Mouse": ["Mouse"],
    "Mule": ["Mule"],
    "Ostrich": ["Ostrich"],
    "Otter": ["Otter"],
    "Owl": ["Owl"],
    "Panda": ["Panda"],
    "Parrot": ["Parrot"],
    "Penguin": ["Penguin"],
    "Pig": ["Pig"],
    "Polar Bear": ["Polar Bear"],
    "Rabbit": ["Rabbit"],
    "Raccoon": ["Raccoon"],
    "Raven": ["Raven"],
    "Red panda": ["Red panda"],
    "Rhinoceros": ["Rhinoceros"],
    "Scorpion": ["Scorpion"],
    "Seahorse": ["Seahorse"],
    "Sea Lion": ["Sea Lion"],
    "Sea Turtle": ["Sea Turtle"],
    "Shark": ["Shark"],
    "Sheep": ["Sheep"],
    "Shrimp": ["Shrimp"],
    "Snail": ["Snail"],
    "Snake": ["Snake"],
    "Sparrow": ["Sparrow"],
    "Spider": ["Spider"],
    "Squid": ["Squid"],
    "Squirrel": ["Squirrel"],
    "Starfish": ["Starfish"],
    "Swan": ["Swan"],
    "Tick": ["Tick"],
    "Tiger": ["Tiger"],
    "Tortoise": ["Tortoise"],
    "Turkey": ["Turkey"],
    "Turtle": ["Turtle"],
    "Whale": ["Whale"],
    "Woodpecker": ["Woodpecker"],
    "Worm": ["Worm"],
    "Zebra": ["Zebra"]
}


# Bear, Brown Bear, Bull, Butterfly, Camel, Canary, Caterpillar, Cattle, Centipede, Cheetah, Chicken, Crab, Crocodile, Deer, Duck, Eagle, Elephant, Fish, Fox, Frog, Giraffe, Goat, Goldfish, Goose, Hamster, Harbor Seal, Hedgehog, Hippopotamus, Horse, Jaguar, Jellyfish, Kangaroo, Koala, Ladybug, Leopard, Lion, Lizard, Lynx, Magpie, Monkey, Moths and butterflies, Mouse, Mule, Ostrich, Otter, Owl, Panda, Parrot, Penguin, Pig, Polar Bear, Rabbit, Raccoon, Raven, Red panda, Rhinoceros, Scorpion, Seahorse, Sea Lion, Sea Turtle, Shark, Sheep, Shrimp, Snail, Snake, Sparrow, Spider, Squid, Squirrel, Starfish, Swan, Tick, Tiger, Tortoise, Turkey, Turtle, Whale, Woodpecker, Worm, Zebra



# dict_size(a80)
print(aOcheck_accuracy('animal80/a80.csv', a80))

# %%
a160 = {
    "Bear": ["Bear", "Bears"],
    "Brown Bear": ["Brown Bear", "Brown Bears"],
    "Bull": ["Bull", "Bulls"],
    "Butterfly": ["Butterfly", "Butterflies"],
    "Camel": ["Camel", "Camels"],
    "Canary": ["Canary", "Canaries"],
    "Caterpillar": ["Caterpillar", "Caterpillars"],
    "Cattle": ["Cattle", "Cattle"],
    "Centipede": ["Centipede", "Centipedes"],
    "Cheetah": ["Cheetah", "Cheetahs"],
    "Chicken": ["Chicken", "Chickens"],
    "Crab": ["Crab", "Crabs"],
    "Crocodile": ["Crocodile", "Crocodiles"],
    "Deer": ["Deer", "Deer"],
    "Duck": ["Duck", "Ducks"],
    "Eagle": ["Eagle", "Eagles"],
    "Elephant": ["Elephant", "Elephants"],
    "Fish": ["Fish", "Fish"],
    "Fox": ["Fox", "Foxes"],
    "Frog": ["Frog", "Frogs"],
    "Giraffe": ["Giraffe", "Giraffes"],
    "Goat": ["Goat", "Goats"],
    "Goldfish": ["Goldfish", "Goldfish"],
    "Goose": ["Goose", "Geese"],
    "Hamster": ["Hamster", "Hamsters"],
    "Harbor Seal": ["Harbor Seal", "Harbor Seals"],
    "Hedgehog": ["Hedgehog", "Hedgehogs"],
    "Hippopotamus": ["Hippopotamus", "Hippopotamuses"],
    "Horse": ["Horse", "Horses"],
    "Jaguar": ["Jaguar", "Jaguars"],
    "Jellyfish": ["Jellyfish", "Jellyfish"],
    "Kangaroo": ["Kangaroo", "Kangaroos"],
    "Koala": ["Koala", "Koalas"],
    "Ladybug": ["Ladybug", "Ladybugs"],
    "Leopard": ["Leopard", "Leopards"],
    "Lion": ["Lion", "Lions"],
    "Lizard": ["Lizard", "Lizards"],
    "Lynx": ["Lynx", "Lynxes"],
    "Magpie": ["Magpie", "Magpies"],
    "Monkey": ["Monkey", "Monkeys"],
    "Moths and butterflies": ["Moths and butterflies", "Moths and butterflies"],
    "Mouse": ["Mouse", "Mice"],
    "Mule": ["Mule", "Mules"],
    "Ostrich": ["Ostrich", "Ostriches"],
    "Otter": ["Otter", "Otters"],
    "Owl": ["Owl", "Owls"],
    "Panda": ["Panda", "Pandas"],
    "Parrot": ["Parrot", "Parrots"],
    "Penguin": ["Penguin", "Penguins"],
    "Pig": ["Pig", "Pigs"],
    "Polar Bear": ["Polar Bear", "Polar Bears"],
    "Rabbit": ["Rabbit", "Rabbits"],
    "Raccoon": ["Raccoon", "Raccoons"],
    "Raven": ["Raven", "Ravens"],
    "Red panda": ["Red panda", "Red pandas"],
    "Rhinoceros": ["Rhinoceros", "Rhinoceroses"],
    "Scorpion": ["Scorpion", "Scorpions"],
    "Seahorse": ["Seahorse", "Seahorses"],
    "Sea Lion": ["Sea Lion", "Sea Lions"],
    "Sea Turtle": ["Sea Turtle", "Sea Turtles"],
    "Shark": ["Shark", "Sharks"],
    "Sheep": ["Sheep", "Sheep"],
    "Shrimp": ["Shrimp", "Shrimp"],
    "Snail": ["Snail", "Snails"],
    "Snake": ["Snake", "Snakes"],
    "Sparrow": ["Sparrow", "Sparrows"],
    "Spider": ["Spider", "Spiders"],
    "Squid": ["Squid", "Squids"],
    "Squirrel": ["Squirrel", "Squirrels"],
    "Starfish": ["Starfish", "Starfish"],
    "Swan": ["Swan", "Swans"],
    "Tick": ["Tick", "Ticks"],
    "Tiger": ["Tiger", "Tigers"],
    "Tortoise": ["Tortoise", "Tortoises"],
    "Turkey": ["Turkey", "Turkeys"],
    "Turtle": ["Turtle", "Turtles"],
    "Whale": ["Whale", "Whales"],
    "Woodpecker": ["Woodpecker", "Woodpeckers"],
    "Worm": ["Worm", "Worms"],
    "Zebra": ["Zebra", "Zebras"]
}

# Bear, Bears, Brown Bear, Brown Bears, Bull, Bulls, Butterfly, Butterflies, Camel, Camels, Canary, Canaries, Caterpillar, Caterpillars, Cattle, Cattle, Centipede, Centipedes, Cheetah, Cheetahs, Chicken, Chickens, Crab, Crabs, Crocodile, Crocodiles, Deer, Deer, Duck, Ducks, Eagle, Eagles, Elephant, Elephants, Fish, Fish, Fox, Foxes, Frog, Frogs, Giraffe, Giraffes, Goat, Goats, Goldfish, Goldfish, Goose, Geese, Hamster, Hamsters, Harbor Seal, Harbor Seals, Hedgehog, Hedgehogs, Hippopotamus, Hippopotamuses, Horse, Horses, Jaguar, Jaguars, Jellyfish, Jellyfish, Kangaroo, Kangaroos, Koala, Koalas, Ladybug, Ladybugs, Leopard, Leopards, Lion, Lions, Lizard, Lizards, Lynx, Lynxes, Magpie, Magpies, Monkey, Monkeys, Moths and butterflies, Moths and butterflies, Mouse, Mice, Mule, Mules, Ostrich, Ostriches, Otter, Otters, Owl, Owls, Panda, Pandas, Parrot, Parrots, Penguin, Penguins, Pig, Pigs, Polar Bear, Polar Bears, Rabbit, Rabbits, Raccoon, Raccoons, Raven, Ravens, Red panda, Red pandas, Rhinoceros, Rhinoceroses, Scorpion, Scorpions, Seahorse, Seahorses, Sea Lion, Sea Lions, Sea Turtle, Sea Turtles, Shark, Sharks, Sheep, Sheep, Shrimp, Shrimp, Snail, Snails, Snake, Snakes, Sparrow, Sparrows, Spider, Spiders, Squid, Squids, Squirrel, Squirrels, Starfish, Starfish, Swan, Swans, Tick, Ticks, Tiger, Tigers, Tortoise, Tortoises, Turkey, Turkeys, Turtle, Turtles, Whale, Whales, Woodpecker, Woodpeckers, Worm, Worms, Zebra, Zebras

# dict_size(a160)
print(aOcheck_accuracy('animal80/a160.csv', a160))

# %%
a240 = {
    "Bear": ["Bear", "Bears", "Large Bear"],
    "Brown Bear": ["Brown Bear", "Brown Bears", "Large Brown Bear"],
    "Bull": ["Bull", "Bulls", "Large Bull"],
    "Butterfly": ["Butterfly", "Butterflies", "Large Butterfly"],
    "Camel": ["Camel", "Camels", "Large Camel"],
    "Canary": ["Canary", "Canaries", "Large Canary"],
    "Caterpillar": ["Caterpillar", "Caterpillars", "Large Caterpillar"],
    "Cattle": ["Cattle", "Cattle", "Large Cattle"],
    "Centipede": ["Centipede", "Centipedes", "Large Centipede"],
    "Cheetah": ["Cheetah", "Cheetahs", "Large Cheetah"],
    "Chicken": ["Chicken", "Chickens", "Large Chicken"],
    "Crab": ["Crab", "Crabs", "Large Crab"],
    "Crocodile": ["Crocodile", "Crocodiles", "Large Crocodile"],
    "Deer": ["Deer", "Deer", "Large Deer"],
    "Duck": ["Duck", "Ducks", "Large Duck"],
    "Eagle": ["Eagle", "Eagles", "Large Eagle"],
    "Elephant": ["Elephant", "Elephants", "Large Elephant"],
    "Fish": ["Fish", "Fish", "Large Fish"],
    "Fox": ["Fox", "Foxes", "Large Fox"],
    "Frog": ["Frog", "Frogs", "Large Frog"],
    "Giraffe": ["Giraffe", "Giraffes", "Large Giraffe"],
    "Goat": ["Goat", "Goats", "Large Goat"],
    "Goldfish": ["Goldfish", "Goldfish", "Large Goldfish"],
    "Goose": ["Goose", "Geese", "Large Goose"],
    "Hamster": ["Hamster", "Hamsters", "Large Hamster"],
    "Harbor Seal": ["Harbor Seal", "Harbor Seals", "Large Harbor Seal"],
    "Hedgehog": ["Hedgehog", "Hedgehogs", "Large Hedgehog"],
    "Hippopotamus": ["Hippopotamus", "Hippopotamuses", "Large Hippopotamus"],
    "Horse": ["Horse", "Horses", "Large Horse"],
    "Jaguar": ["Jaguar", "Jaguars", "Large Jaguar"],
    "Jellyfish": ["Jellyfish", "Jellyfish", "Large Jellyfish"],
    "Kangaroo": ["Kangaroo", "Kangaroos", "Large Kangaroo"],
    "Koala": ["Koala", "Koalas", "Large Koala"],
    "Ladybug": ["Ladybug", "Ladybugs", "Large Ladybug"],
    "Leopard": ["Leopard", "Leopards", "Large Leopard"],
    "Lion": ["Lion", "Lions", "Large Lion"],
    "Lizard": ["Lizard", "Lizards", "Large Lizard"],
    "Lynx": ["Lynx", "Lynxes", "Large Lynx"],
    "Magpie": ["Magpie", "Magpies", "Large Magpie"],
    "Monkey": ["Monkey", "Monkeys", "Large Monkey"],
    "Moths and butterflies": ["Moths and butterflies", "Moths and butterflies", "Large Moths and butterflies"],
    "Mouse": ["Mouse", "Mice", "Large Mouse"],
    "Mule": ["Mule", "Mules", "Large Mule"],
    "Ostrich": ["Ostrich", "Ostriches", "Large Ostrich"],
    "Otter": ["Otter", "Otters", "Large Otter"],
    "Owl": ["Owl", "Owls", "Large Owl"],
    "Panda": ["Panda", "Pandas", "Large Panda"],
    "Parrot": ["Parrot", "Parrots", "Large Parrot"],
    "Penguin": ["Penguin", "Penguins", "Large Penguin"],
    "Pig": ["Pig", "Pigs", "Large Pig"],
    "Polar Bear": ["Polar Bear", "Polar Bears", "Large Polar Bear"],
    "Rabbit": ["Rabbit", "Rabbits", "Large Rabbit"],
    "Raccoon": ["Raccoon", "Raccoons", "Large Raccoon"],
    "Raven": ["Raven", "Ravens", "Large Raven"],
    "Red panda": ["Red panda", "Red pandas", "Large Red panda"],
    "Rhinoceros": ["Rhinoceros", "Rhinoceroses", "Large Rhinoceros"],
    "Scorpion": ["Scorpion", "Scorpions", "Large Scorpion"],
    "Seahorse": ["Seahorse", "Seahorses", "Large Seahorse"],
    "Sea Lion": ["Sea Lion", "Sea Lions", "Large Sea Lion"],
    "Sea Turtle": ["Sea Turtle", "Sea Turtles", "Large Sea Turtle"],
    "Shark": ["Shark", "Sharks", "Large Shark"],
    "Sheep": ["Sheep", "Sheep", "Large Sheep"],
    "Shrimp": ["Shrimp", "Shrimp", "Large Shrimp"],
    "Snail": ["Snail", "Snails", "Large Snail"],
    "Snake": ["Snake", "Snakes", "Large Snake"],
    "Sparrow": ["Sparrow", "Sparrows", "Large Sparrow"],
    "Spider": ["Spider", "Spiders", "Large Spider"],
    "Squid": ["Squid", "Squids", "Large Squid"],
    "Squirrel": ["Squirrel", "Squirrels", "Large Squirrel"],
    "Starfish": ["Starfish", "Starfish", "Large Starfish"],
    "Swan": ["Swan", "Swans", "Large Swan"],
    "Tick": ["Tick", "Ticks", "Large Tick"],
    "Tiger": ["Tiger", "Tigers", "Large Tiger"],
    "Tortoise": ["Tortoise", "Tortoises", "Large Tortoise"],
    "Turkey": ["Turkey", "Turkeys", "Large Turkey"],
    "Turtle": ["Turtle", "Turtles", "Large Turtle"],
    "Whale": ["Whale", "Whales", "Large Whale"],
    "Woodpecker": ["Woodpecker", "Woodpeckers", "Large Woodpecker"],
    "Worm": ["Worm", "Worms", "Large Worm"],
    "Zebra": ["Zebra", "Zebras", "Large Zebra"]
}

# Bear, Bears, Large Bear, Brown Bear, Brown Bears, Large Brown Bear, Bull, Bulls, Large Bull, Butterfly, Butterflies, Large Butterfly, Camel, Camels, Large Camel, Canary, Canaries, Large Canary, Caterpillar, Caterpillars, Large Caterpillar, Cattle, Cattle, Large Cattle, Centipede, Centipedes, Large Centipede, Cheetah, Cheetahs, Large Cheetah, Chicken, Chickens, Large Chicken, Crab, Crabs, Large Crab, Crocodile, Crocodiles, Large Crocodile, Deer, Deer, Large Deer, Duck, Ducks, Large Duck, Eagle, Eagles, Large Eagle, Elephant, Elephants, Large Elephant, Fish, Fish, Large Fish, Fox, Foxes, Large Fox, Frog, Frogs, Large Frog, Giraffe, Giraffes, Large Giraffe, Goat, Goats, Large Goat, Goldfish, Goldfish, Large Goldfish, Goose, Geese, Large Goose, Hamster, Hamsters, Large Hamster, Harbor Seal, Harbor Seals, Large Harbor Seal, Hedgehog, Hedgehogs, Large Hedgehog, Hippopotamus, Hippopotamuses, Large Hippopotamus, Horse, Horses, Large Horse, Jaguar, Jaguars, Large Jaguar, Jellyfish, Jellyfish, Large Jellyfish, Kangaroo, Kangaroos, Large Kangaroo, Koala, Koalas, Large Koala, Ladybug, Ladybugs, Large Ladybug, Leopard, Leopards, Large Leopard, Lion, Lions, Large Lion, Lizard, Lizards, Large Lizard, Lynx, Lynxes, Large Lynx, Magpie, Magpies, Large Magpie, Monkey, Monkeys, Large Monkey, Moths and butterflies, Moths and butterflies, Large Moths and butterflies, Mouse, Mice, Large Mouse, Mule, Mules, Large Mule, Ostrich, Ostriches, Large Ostrich, Otter, Otters, Large Otter, Owl, Owls, Large Owl, Panda, Pandas, Large Panda, Parrot, Parrots, Large Parrot, Penguin, Penguins, Large Penguin, Pig, Pigs, Large Pig, Polar Bear, Polar Bears, Large Polar Bear, Rabbit, Rabbits, Large Rabbit, Raccoon, Raccoons, Large Raccoon, Raven, Ravens, Large Raven, Red panda, Red pandas, Large Red panda, Rhinoceros, Rhinoceroses, Large Rhinoceros, Scorpion, Scorpions, Large Scorpion, Seahorse, Seahorses, Large Seahorse, Sea Lion, Sea Lions, Large Sea Lion, Sea Turtle, Sea Turtles, Large Sea Turtle, Shark, Sharks, Large Shark, Sheep, Sheep, Large Sheep, Shrimp, Shrimp, Large Shrimp, Snail, Snails, Large Snail, Snake, Snakes, Large Snake, Sparrow, Sparrows, Large Sparrow, Spider, Spiders, Large Spider, Squid, Squids, Large Squid, Squirrel, Squirrels, Large Squirrel, Starfish, Starfish, Large Starfish, Swan, Swans, Large Swan, Tick, Ticks, Large Tick, Tiger, Tigers, Large Tiger, Tortoise, Tortoises, Large Tortoise, Turkey, Turkeys, Large Turkey, Turtle, Turtles, Large Turtle, Whale, Whales, Large Whale, Woodpecker, Woodpeckers, Large Woodpecker, Worm, Worms, Large Worm, Zebra, Zebras, Large Zebra

dict_size(a240)
print(aOcheck_accuracy('animal80/a240.csv', a240))


# %%
a320 = {
    "Bear": ["Bear", "Bears", "Large Bear", "Small Bear"],
    "Brown Bear": ["Brown Bear", "Brown Bears", "Large Brown Bear", "Small Brown Bear"],
    "Bull": ["Bull", "Bulls", "Large Bull", "Small Bull"],
    "Butterfly": ["Butterfly", "Butterflies", "Large Butterfly", "Small Butterfly"],
    "Camel": ["Camel", "Camels", "Large Camel", "Small Camel"],
    "Canary": ["Canary", "Canaries", "Large Canary", "Small Canary"],
    "Caterpillar": ["Caterpillar", "Caterpillars", "Large Caterpillar", "Small Caterpillar"],
    "Cattle": ["Cattle", "Cattle", "Large Cattle", "Small Cattle"],
    "Centipede": ["Centipede", "Centipedes", "Large Centipede", "Small Centipede"],
    "Cheetah": ["Cheetah", "Cheetahs", "Large Cheetah", "Small Cheetah"],
    "Chicken": ["Chicken", "Chickens", "Large Chicken", "Small Chicken"],
    "Crab": ["Crab", "Crabs", "Large Crab", "Small Crab"],
    "Crocodile": ["Crocodile", "Crocodiles", "Large Crocodile", "Small Crocodile"],
    "Deer": ["Deer", "Deer", "Large Deer", "Small Deer"],
    "Duck": ["Duck", "Ducks", "Large Duck", "Small Duck"],
    "Eagle": ["Eagle", "Eagles", "Large Eagle", "Small Eagle"],
    "Elephant": ["Elephant", "Elephants", "Large Elephant", "Small Elephant"],
    "Fish": ["Fish", "Fish", "Large Fish", "Small Fish"],
    "Fox": ["Fox", "Foxes", "Large Fox", "Small Fox"],
    "Frog": ["Frog", "Frogs", "Large Frog", "Small Frog"],
    "Giraffe": ["Giraffe", "Giraffes", "Large Giraffe", "Small Giraffe"],
    "Goat": ["Goat", "Goats", "Large Goat", "Small Goat"],
    "Goldfish": ["Goldfish", "Goldfish", "Large Goldfish", "Small Goldfish"],
    "Goose": ["Goose", "Geese", "Large Goose", "Small Goose"],
    "Hamster": ["Hamster", "Hamsters", "Large Hamster", "Small Hamster"],
    "Harbor Seal": ["Harbor Seal", "Harbor Seals", "Large Harbor Seal", "Small Harbor Seal"],
    "Hedgehog": ["Hedgehog", "Hedgehogs", "Large Hedgehog", "Small Hedgehog"],
    "Hippopotamus": ["Hippopotamus", "Hippopotamuses", "Large Hippopotamus", "Small Hippopotamus"],
    "Horse": ["Horse", "Horses", "Large Horse", "Small Horse"],
    "Jaguar": ["Jaguar", "Jaguars", "Large Jaguar", "Small Jaguar"],
    "Jellyfish": ["Jellyfish", "Jellyfish", "Large Jellyfish", "Small Jellyfish"],
    "Kangaroo": ["Kangaroo", "Kangaroos", "Large Kangaroo", "Small Kangaroo"],
    "Koala": ["Koala", "Koalas", "Large Koala", "Small Koala"],
    "Ladybug": ["Ladybug", "Ladybugs", "Large Ladybug", "Small Ladybug"],
    "Leopard": ["Leopard", "Leopards", "Large Leopard", "Small Leopard"],
    "Lion": ["Lion", "Lions", "Large Lion", "Small Lion"],
    "Lizard": ["Lizard", "Lizards", "Large Lizard", "Small Lizard"],
    "Lynx": ["Lynx", "Lynxes", "Large Lynx", "Small Lynx"],
    "Magpie": ["Magpie", "Magpies", "Large Magpie", "Small Magpie"],
    "Monkey": ["Monkey", "Monkeys", "Large Monkey", "Small Monkey"],
    "Moths and butterflies": ["Moths and butterflies", "Moths and butterflies", "Large Moths and butterflies", "Small Moths and butterflies"],
    "Mouse": ["Mouse", "Mice", "Large Mouse", "Small Mouse"],
    "Mule": ["Mule", "Mules", "Large Mule", "Small Mule"],
    "Ostrich": ["Ostrich", "Ostriches", "Large Ostrich", "Small Ostrich"],
    "Otter": ["Otter", "Otters", "Large Otter", "Small Otter"],
    "Owl": ["Owl", "Owls", "Large Owl", "Small Owl"],
    "Panda": ["Panda", "Pandas", "Large Panda", "Small Panda"],
    "Parrot": ["Parrot", "Parrots", "Large Parrot", "Small Parrot"],
    "Penguin": ["Penguin", "Penguins", "Large Penguin", "Small Penguin"],
    "Pig": ["Pig", "Pigs", "Large Pig", "Small Pig"],
    "Polar Bear": ["Polar Bear", "Polar Bears", "Large Polar Bear", "Small Polar Bear"],
    "Rabbit": ["Rabbit", "Rabbits", "Large Rabbit", "Small Rabbit"],
    "Raccoon": ["Raccoon", "Raccoons", "Large Raccoon", "Small Raccoon"],
    "Raven": ["Raven", "Ravens", "Large Raven", "Small Raven"],
    "Red panda": ["Red panda", "Red pandas", "Large Red panda", "Small Red panda"],
    "Rhinoceros": ["Rhinoceros", "Rhinoceroses", "Large Rhinoceros", "Small Rhinoceros"],
    "Scorpion": ["Scorpion", "Scorpions", "Large Scorpion", "Small Scorpion"],
    "Seahorse": ["Seahorse", "Seahorses", "Large Seahorse", "Small Seahorse"],
    "Sea Lion": ["Sea Lion", "Sea Lions", "Large Sea Lion", "Small Sea Lion"],
    "Sea Turtle": ["Sea Turtle", "Sea Turtles", "Large Sea Turtle", "Small Sea Turtle"],
    "Shark": ["Shark", "Sharks", "Large Shark", "Small Shark"],
    "Sheep": ["Sheep", "Sheep", "Large Sheep", "Small Sheep"],
    "Shrimp": ["Shrimp", "Shrimp", "Large Shrimp", "Small Shrimp"],
    "Snail": ["Snail", "Snails", "Large Snail", "Small Snail"],
    "Snake": ["Snake", "Snakes", "Large Snake", "Small Snake"],
    "Sparrow": ["Sparrow", "Sparrows", "Large Sparrow", "Small Sparrow"],
    "Spider": ["Spider", "Spiders", "Large Spider", "Small Spider"],
    "Squid": ["Squid", "Squids", "Large Squid", "Small Squid"],
    "Squirrel": ["Squirrel", "Squirrels", "Large Squirrel", "Small Squirrel"],
    "Starfish": ["Starfish", "Starfish", "Large Starfish", "Small Starfish"],
    "Swan": ["Swan", "Swans", "Large Swan", "Small Swan"],
    "Tick": ["Tick", "Ticks", "Large Tick", "Small Tick"],
    "Tiger": ["Tiger", "Tigers", "Large Tiger", "Small Tiger"],
    "Tortoise": ["Tortoise", "Tortoises", "Large Tortoise", "Small Tortoise"],
    "Turkey": ["Turkey", "Turkeys", "Large Turkey", "Small Turkey"],
    "Turtle": ["Turtle", "Turtles", "Large Turtle", "Small Turtle"],
    "Whale": ["Whale", "Whales", "Large Whale", "Small Whale"],
    "Woodpecker": ["Woodpecker", "Woodpeckers", "Large Woodpecker", "Small Woodpecker"],
    "Worm": ["Worm", "Worms", "Large Worm", "Small Worm"],
    "Zebra": ["Zebra", "Zebras", "Large Zebra", "Small Zebra"]
}

# Bear, Bears, Large Bear, Small Bear, Brown Bear, Brown Bears, Large Brown Bear, Small Brown Bear, Bull, Bulls, Large Bull, Small Bull, Butterfly, Butterflies, Large Butterfly, Small Butterfly, Camel, Camels, Large Camel, Small Camel, Canary, Canaries, Large Canary, Small Canary, Caterpillar, Caterpillars, Large Caterpillar, Small Caterpillar, Cattle, Cattle, Large Cattle, Small Cattle, Centipede, Centipedes, Large Centipede, Small Centipede, Cheetah, Cheetahs, Large Cheetah, Small Cheetah, Chicken, Chickens, Large Chicken, Small Chicken, Crab, Crabs, Large Crab, Small Crab, Crocodile, Crocodiles, Large Crocodile, Small Crocodile, Deer, Deer, Large Deer, Small Deer, Duck, Ducks, Large Duck, Small Duck, Eagle, Eagles, Large Eagle, Small Eagle, Elephant, Elephants, Large Elephant, Small Elephant, Fish, Fish, Large Fish, Small Fish, Fox, Foxes, Large Fox, Small Fox, Frog, Frogs, Large Frog, Small Frog, Giraffe, Giraffes, Large Giraffe, Small Giraffe, Goat, Goats, Large Goat, Small Goat, Goldfish, Goldfish, Large Goldfish, Small Goldfish, Goose, Geese, Large Goose, Small Goose, Hamster, Hamsters, Large Hamster, Small Hamster, Harbor Seal, Harbor Seals, Large Harbor Seal, Small Harbor Seal, Hedgehog, Hedgehogs, Large Hedgehog, Small Hedgehog, Hippopotamus, Hippopotamuses, Large Hippopotamus, Small Hippopotamus, Horse, Horses, Large Horse, Small Horse, Jaguar, Jaguars, Large Jaguar, Small Jaguar, Jellyfish, Jellyfish, Large Jellyfish, Small Jellyfish, Kangaroo, Kangaroos, Large Kangaroo, Small Kangaroo, Koala, Koalas, Large Koala, Small Koala, Ladybug, Ladybugs, Large Ladybug, Small Ladybug, Leopard, Leopards, Large Leopard, Small Leopard, Lion, Lions, Large Lion, Small Lion, Lizard, Lizards, Large Lizard, Small Lizard, Lynx, Lynxes, Large Lynx, Small Lynx, Magpie, Magpies, Large Magpie, Small Magpie, Monkey, Monkeys, Large Monkey, Small Monkey, Moths and butterflies, Moths and butterflies, Large Moths and butterflies, Small Moths and butterflies, Mouse, Mice, Large Mouse, Small Mouse, Mule, Mules, Large Mule, Small Mule, Ostrich, Ostriches, Large Ostrich, Small Ostrich, Otter, Otters, Large Otter, Small Otter, Owl, Owls, Large Owl, Small Owl, Panda, Pandas, Large Panda, Small Panda, Parrot, Parrots, Large Parrot, Small Parrot, Penguin, Penguins, Large Penguin, Small Penguin, Pig, Pigs, Large Pig, Small Pig, Polar Bear, Polar Bears, Large Polar Bear, Small Polar Bear, Rabbit, Rabbits, Large Rabbit, Small Rabbit, Raccoon, Raccoons, Large Raccoon, Small Raccoon, Raven, Ravens, Large Raven, Small Raven, Red panda, Red pandas, Large Red panda, Small Red panda, Rhinoceros, Rhinoceroses, Large Rhinoceros, Small Rhinoceros, Scorpion, Scorpions, Large Scorpion, Small Scorpion, Seahorse, Seahorses, Large Seahorse, Small Seahorse, Sea Lion, Sea Lions, Large Sea Lion, Small Sea Lion, Sea Turtle, Sea Turtles, Large Sea Turtle, Small Sea Turtle, Shark, Sharks, Large Shark, Small Shark, Sheep, Sheep, Large Sheep, Small Sheep, Shrimp, Shrimp, Large Shrimp, Small Shrimp, Snail, Snails, Large Snail, Small Snail, Snake, Snakes, Large Snake, Small Snake, Sparrow, Sparrows, Large Sparrow, Small Sparrow, Spider, Spiders, Large Spider, Small Spider, Squid, Squids, Large Squid, Small Squid, Squirrel, Squirrels, Large Squirrel, Small Squirrel, Starfish, Starfish, Large Starfish, Small Starfish, Swan, Swans, Large Swan, Small Swan, Tick, Ticks, Large Tick, Small Tick, Tiger, Tigers, Large Tiger, Small Tiger, Tortoise, Tortoises, Large Tortoise, Small Tortoise, Turkey, Turkeys, Large Turkey, Small Turkey, Turtle, Turtles, Large Turtle, Small Turtle, Whale, Whales, Large Whale, Small Whale, Woodpecker, Woodpeckers, Large Woodpecker, Small Woodpecker, Worm, Worms, Large Worm, Small Worm, Zebra, Zebras, Large Zebra, Small Zebra

dict_size(a320)
print(aOcheck_accuracy('animal80/a320.csv', a320))


# %%
a400 = {
    "Bear": ["Bear", "Bears", "Large Bear", "Small Bear", "Wild Bear"],
    "Brown Bear": ["Brown Bear", "Brown Bears", "Large Brown Bear", "Small Brown Bear", "Wild Brown Bear"],
    "Bull": ["Bull", "Bulls", "Large Bull", "Small Bull", "Wild Bull"],
    "Butterfly": ["Butterfly", "Butterflies", "Large Butterfly", "Small Butterfly", "Wild Butterfly"],
    "Camel": ["Camel", "Camels", "Large Camel", "Small Camel", "Wild Camel"],
    "Canary": ["Canary", "Canaries", "Large Canary", "Small Canary", "Wild Canary"],
    "Caterpillar": ["Caterpillar", "Caterpillars", "Large Caterpillar", "Small Caterpillar", "Wild Caterpillar"],
    "Cattle": ["Cattle", "Cattle", "Large Cattle", "Small Cattle", "Wild Cattle"],
    "Centipede": ["Centipede", "Centipedes", "Large Centipede", "Small Centipede", "Wild Centipede"],
    "Cheetah": ["Cheetah", "Cheetahs", "Large Cheetah", "Small Cheetah", "Wild Cheetah"],
    "Chicken": ["Chicken", "Chickens", "Large Chicken", "Small Chicken", "Wild Chicken"],
    "Crab": ["Crab", "Crabs", "Large Crab", "Small Crab", "Wild Crab"],
    "Crocodile": ["Crocodile", "Crocodiles", "Large Crocodile", "Small Crocodile", "Wild Crocodile"],
    "Deer": ["Deer", "Deer", "Large Deer", "Small Deer", "Wild Deer"],
    "Duck": ["Duck", "Ducks", "Large Duck", "Small Duck", "Wild Duck"],
    "Eagle": ["Eagle", "Eagles", "Large Eagle", "Small Eagle", "Wild Eagle"],
    "Elephant": ["Elephant", "Elephants", "Large Elephant", "Small Elephant", "Wild Elephant"],
    "Fish": ["Fish", "Fish", "Large Fish", "Small Fish", "Wild Fish"],
    "Fox": ["Fox", "Foxes", "Large Fox", "Small Fox", "Wild Fox"],
    "Frog": ["Frog", "Frogs", "Large Frog", "Small Frog", "Wild Frog"],
    "Giraffe": ["Giraffe", "Giraffes", "Large Giraffe", "Small Giraffe", "Wild Giraffe"],
    "Goat": ["Goat", "Goats", "Large Goat", "Small Goat", "Wild Goat"],
    "Goldfish": ["Goldfish", "Goldfish", "Large Goldfish", "Small Goldfish", "Wild Goldfish"],
    "Goose": ["Goose", "Geese", "Large Goose", "Small Goose", "Wild Goose"],
    "Hamster": ["Hamster", "Hamsters", "Large Hamster", "Small Hamster", "Wild Hamster"],
    "Harbor Seal": ["Harbor Seal", "Harbor Seals", "Large Harbor Seal", "Small Harbor Seal", "Wild Harbor Seal"],
    "Hedgehog": ["Hedgehog", "Hedgehogs", "Large Hedgehog", "Small Hedgehog", "Wild Hedgehog"],
    "Hippopotamus": ["Hippopotamus", "Hippopotamuses", "Large Hippopotamus", "Small Hippopotamus", "Wild Hippopotamus"],
    "Horse": ["Horse", "Horses", "Large Horse", "Small Horse", "Wild Horse"],
    "Jaguar": ["Jaguar", "Jaguars", "Large Jaguar", "Small Jaguar", "Wild Jaguar"],
    "Jellyfish": ["Jellyfish", "Jellyfish", "Large Jellyfish", "Small Jellyfish", "Wild Jellyfish"],
    "Kangaroo": ["Kangaroo", "Kangaroos", "Large Kangaroo", "Small Kangaroo", "Wild Kangaroo"],
    "Koala": ["Koala", "Koalas", "Large Koala", "Small Koala", "Wild Koala"],
    "Ladybug": ["Ladybug", "Ladybugs", "Large Ladybug", "Small Ladybug", "Wild Ladybug"],
    "Leopard": ["Leopard", "Leopards", "Large Leopard", "Small Leopard", "Wild Leopard"],
    "Lion": ["Lion", "Lions", "Large Lion", "Small Lion", "Wild Lion"],
    "Lizard": ["Lizard", "Lizards", "Large Lizard", "Small Lizard", "Wild Lizard"],
    "Lynx": ["Lynx", "Lynxes", "Large Lynx", "Small Lynx", "Wild Lynx"],
    "Magpie": ["Magpie", "Magpies", "Large Magpie", "Small Magpie", "Wild Magpie"],
    "Monkey": ["Monkey", "Monkeys", "Large Monkey", "Small Monkey", "Wild Monkey"],
    "Moths and butterflies": ["Moths and butterflies", "Moths and butterflies", "Large Moths and butterflies", "Small Moths and butterflies", "Wild Moths and butterflies"],
    "Mouse": ["Mouse", "Mice", "Large Mouse", "Small Mouse", "Wild Mouse"],
    "Mule": ["Mule", "Mules", "Large Mule", "Small Mule", "Wild Mule"],
    "Ostrich": ["Ostrich", "Ostriches", "Large Ostrich", "Small Ostrich", "Wild Ostrich"],
    "Otter": ["Otter", "Otters", "Large Otter", "Small Otter", "Wild Otter"],
    "Owl": ["Owl", "Owls", "Large Owl", "Small Owl", "Wild Owl"],
    "Panda": ["Panda", "Pandas", "Large Panda", "Small Panda", "Wild Panda"],
    "Parrot": ["Parrot", "Parrots", "Large Parrot", "Small Parrot", "Wild Parrot"],
    "Penguin": ["Penguin", "Penguins", "Large Penguin", "Small Penguin", "Wild Penguin"],
    "Pig": ["Pig", "Pigs", "Large Pig", "Small Pig", "Wild Pig"],
    "Polar Bear": ["Polar Bear", "Polar Bears", "Large Polar Bear", "Small Polar Bear", "Wild Polar Bear"],
    "Rabbit": ["Rabbit", "Rabbits", "Large Rabbit", "Small Rabbit", "Wild Rabbit"],
    "Raccoon": ["Raccoon", "Raccoons", "Large Raccoon", "Small Raccoon", "Wild Raccoon"],
    "Raven": ["Raven", "Ravens", "Large Raven", "Small Raven", "Wild Raven"],
    "Red panda": ["Red panda", "Red pandas", "Large Red panda", "Small Red panda", "Wild Red panda"],
    "Rhinoceros": ["Rhinoceros", "Rhinoceroses", "Large Rhinoceros", "Small Rhinoceros", "Wild Rhinoceros"],
    "Scorpion": ["Scorpion", "Scorpions", "Large Scorpion", "Small Scorpion", "Wild Scorpion"],
    "Seahorse": ["Seahorse", "Seahorses", "Large Seahorse", "Small Seahorse", "Wild Seahorse"],
    "Sea Lion": ["Sea Lion", "Sea Lions", "Large Sea Lion", "Small Sea Lion", "Wild Sea Lion"],
    "Sea Turtle": ["Sea Turtle", "Sea Turtles", "Large Sea Turtle", "Small Sea Turtle", "Wild Sea Turtle"],
    "Shark": ["Shark", "Sharks", "Large Shark", "Small Shark", "Wild Shark"],
    "Sheep": ["Sheep", "Sheep", "Large Sheep", "Small Sheep", "Wild Sheep"],
    "Shrimp": ["Shrimp", "Shrimp", "Large Shrimp", "Small Shrimp", "Wild Shrimp"],
    "Snail": ["Snail", "Snails", "Large Snail", "Small Snail", "Wild Snail"],
    "Snake": ["Snake", "Snakes", "Large Snake", "Small Snake", "Wild Snake"],
    "Sparrow": ["Sparrow", "Sparrows", "Large Sparrow", "Small Sparrow", "Wild Sparrow"],
    "Spider": ["Spider", "Spiders", "Large Spider", "Small Spider", "Wild Spider"],
    "Squid": ["Squid", "Squids", "Large Squid", "Small Squid", "Wild Squid"],
    "Squirrel": ["Squirrel", "Squirrels", "Large Squirrel", "Small Squirrel", "Wild Squirrel"],
    "Starfish": ["Starfish", "Starfish", "Large Starfish", "Small Starfish", "Wild Starfish"],
    "Swan": ["Swan", "Swans", "Large Swan", "Small Swan", "Wild Swan"],
    "Tick": ["Tick", "Ticks", "Large Tick", "Small Tick", "Wild Tick"],
    "Tiger": ["Tiger", "Tigers", "Large Tiger", "Small Tiger", "Wild Tiger"],
    "Tortoise": ["Tortoise", "Tortoises", "Large Tortoise", "Small Tortoise", "Wild Tortoise"],
    "Turkey": ["Turkey", "Turkeys", "Large Turkey", "Small Turkey", "Wild Turkey"],
    "Turtle": ["Turtle", "Turtles", "Large Turtle", "Small Turtle", "Wild Turtle"],
    "Whale": ["Whale", "Whales", "Large Whale", "Small Whale", "Wild Whale"],
    "Woodpecker": ["Woodpecker", "Woodpeckers", "Large Woodpecker", "Small Woodpecker", "Wild Woodpecker"],
    "Worm": ["Worm", "Worms", "Large Worm", "Small Worm", "Wild Worm"],
    "Zebra": ["Zebra", "Zebras", "Large Zebra", "Small Zebra", "Wild Zebra"]
}

# Bear, Bears, Large Bear, Small Bear, Wild Bear, Brown Bear, Brown Bears, Large Brown Bear, Small Brown Bear, Wild Brown Bear, Bull, Bulls, Large Bull, Small Bull, Wild Bull, Butterfly, Butterflies, Large Butterfly, Small Butterfly, Wild Butterfly, Camel, Camels, Large Camel, Small Camel, Wild Camel, Canary, Canaries, Large Canary, Small Canary, Wild Canary, Caterpillar, Caterpillars, Large Caterpillar, Small Caterpillar, Wild Caterpillar, Cattle, Cattle, Large Cattle, Small Cattle, Wild Cattle, Centipede, Centipedes, Large Centipede, Small Centipede, Wild Centipede, Cheetah, Cheetahs, Large Cheetah, Small Cheetah, Wild Cheetah, Chicken, Chickens, Large Chicken, Small Chicken, Wild Chicken, Crab, Crabs, Large Crab, Small Crab, Wild Crab, Crocodile, Crocodiles, Large Crocodile, Small Crocodile, Wild Crocodile, Deer, Deer, Large Deer, Small Deer, Wild Deer, Duck, Ducks, Large Duck, Small Duck, Wild Duck, Eagle, Eagles, Large Eagle, Small Eagle, Wild Eagle, Elephant, Elephants, Large Elephant, Small Elephant, Wild Elephant, Fish, Fish, Large Fish, Small Fish, Wild Fish, Fox, Foxes, Large Fox, Small Fox, Wild Fox, Frog, Frogs, Large Frog, Small Frog, Wild Frog, Giraffe, Giraffes, Large Giraffe, Small Giraffe, Wild Giraffe, Goat, Goats, Large Goat, Small Goat, Wild Goat, Goldfish, Goldfish, Large Goldfish, Small Goldfish, Wild Goldfish, Goose, Geese, Large Goose, Small Goose, Wild Goose, Hamster, Hamsters, Large Hamster, Small Hamster, Wild Hamster, Harbor Seal, Harbor Seals, Large Harbor Seal, Small Harbor Seal, Wild Harbor Seal, Hedgehog, Hedgehogs, Large Hedgehog, Small Hedgehog, Wild Hedgehog, Hippopotamus, Hippopotamuses, Large Hippopotamus, Small Hippopotamus, Wild Hippopotamus, Horse, Horses, Large Horse, Small Horse, Wild Horse, Jaguar, Jaguars, Large Jaguar, Small Jaguar, Wild Jaguar, Jellyfish, Jellyfish, Large Jellyfish, Small Jellyfish, Wild Jellyfish, Kangaroo, Kangaroos, Large Kangaroo, Small Kangaroo, Wild Kangaroo, Koala, Koalas, Large Koala, Small Koala, Wild Koala, Ladybug, Ladybugs, Large Ladybug, Small Ladybug, Wild Ladybug, Leopard, Leopards, Large Leopard, Small Leopard, Wild Leopard, Lion, Lions, Large Lion, Small Lion, Wild Lion, Lizard, Lizards, Large Lizard, Small Lizard, Wild Lizard, Lynx, Lynxes, Large Lynx, Small Lynx, Wild Lynx, Magpie, Magpies, Large Magpie, Small Magpie, Wild Magpie, Monkey, Monkeys, Large Monkey, Small Monkey, Wild Monkey, Moths and butterflies, Moths and butterflies, Large Moths and butterflies, Small Moths and butterflies, Wild Moths and butterflies, Mouse, Mice, Large Mouse, Small Mouse, Wild Mouse, Mule, Mules, Large Mule, Small Mule, Wild Mule, Ostrich, Ostriches, Large Ostrich, Small Ostrich, Wild Ostrich, Otter, Otters, Large Otter, Small Otter, Wild Otter, Owl, Owls, Large Owl, Small Owl, Wild Owl, Panda, Pandas, Large Panda, Small Panda, Wild Panda, Parrot, Parrots, Large Parrot, Small Parrot, Wild Parrot, Penguin, Penguins, Large Penguin, Small Penguin, Wild Penguin, Pig, Pigs, Large Pig, Small Pig, Wild Pig, Polar Bear, Polar Bears, Large Polar Bear, Small Polar Bear, Wild Polar Bear, Rabbit, Rabbits, Large Rabbit, Small Rabbit, Wild Rabbit, Raccoon, Raccoons, Large Raccoon, Small Raccoon, Wild Raccoon, Raven, Ravens, Large Raven, Small Raven, Wild Raven, Red panda, Red pandas, Large Red panda, Small Red panda, Wild Red panda, Rhinoceros, Rhinoceroses, Large Rhinoceros, Small Rhinoceros, Wild Rhinoceros, Scorpion, Scorpions, Large Scorpion, Small Scorpion, Wild Scorpion, Seahorse, Seahorses, Large Seahorse, Small Seahorse, Wild Seahorse, Sea Lion, Sea Lions, Large Sea Lion, Small Sea Lion, Wild Sea Lion, Sea Turtle, Sea Turtles, Large Sea Turtle, Small Sea Turtle, Wild Sea Turtle, Shark, Sharks, Large Shark, Small Shark, Wild Shark, Sheep, Sheep, Large Sheep, Small Sheep, Wild Sheep, Shrimp, Shrimp, Large Shrimp, Small Shrimp, Wild Shrimp, Snail, Snails, Large Snail, Small Snail, Wild Snail, Snake, Snakes, Large Snake, Small Snake, Wild Snake, Sparrow, Sparrows, Large Sparrow, Small Sparrow, Wild Sparrow, Spider, Spiders, Large Spider, Small Spider, Wild Spider, Squid, Squids, Large Squid, Small Squid, Wild Squid, Squirrel, Squirrels, Large Squirrel, Small Squirrel, Wild Squirrel, Starfish, Starfish, Large Starfish, Small Starfish, Wild Starfish, Swan, Swans, Large Swan, Small Swan, Wild Swan, Tick, Ticks, Large Tick, Small Tick, Wild Tick, Tiger, Tigers, Large Tiger, Small Tiger, Wild Tiger, Tortoise, Tortoises, Large Tortoise, Small Tortoise, Wild Tortoise, Turkey, Turkeys, Large Turkey, Small Turkey, Wild Turkey, Turtle, Turtles, Large Turtle, Small Turtle, Wild Turtle, Whale, Whales, Large Whale, Small Whale, Wild Whale, Woodpecker, Woodpeckers, Large Woodpecker, Small Woodpecker, Wild Woodpecker, Worm, Worms, Large Worm, Small Worm, Wild Worm, Zebra, Zebras, Large Zebra, Small Zebra, Wild Zebra

dict_size(a400)
print(aOcheck_accuracy('animal80/a400.csv', a400))


# %%
a480 = {
    "Bear": ["Bear", "Bears", "Large Bear", "Small Bear", "Wild Bear", "Animal Bear"],
    "Brown Bear": ["Brown Bear", "Brown Bears", "Large Brown Bear", "Small Brown Bear", "Wild Brown Bear", "Animal Brown Bear"],
    "Bull": ["Bull", "Bulls", "Large Bull", "Small Bull", "Wild Bull", "Animal Bull"],
    "Butterfly": ["Butterfly", "Butterflies", "Large Butterfly", "Small Butterfly", "Wild Butterfly", "Animal Butterfly"],
    "Camel": ["Camel", "Camels", "Large Camel", "Small Camel", "Wild Camel", "Animal Camel"],
    "Canary": ["Canary", "Canaries", "Large Canary", "Small Canary", "Wild Canary", "Animal Canary"],
    "Caterpillar": ["Caterpillar", "Caterpillars", "Large Caterpillar", "Small Caterpillar", "Wild Caterpillar", "Animal Caterpillar"],
    "Cattle": ["Cattle", "Cattle", "Large Cattle", "Small Cattle", "Wild Cattle", "Animal Cattle"],
    "Centipede": ["Centipede", "Centipedes", "Large Centipede", "Small Centipede", "Wild Centipede", "Animal Centipede"],
    "Cheetah": ["Cheetah", "Cheetahs", "Large Cheetah", "Small Cheetah", "Wild Cheetah", "Animal Cheetah"],
    "Chicken": ["Chicken", "Chickens", "Large Chicken", "Small Chicken", "Wild Chicken", "Animal Chicken"],
    "Crab": ["Crab", "Crabs", "Large Crab", "Small Crab", "Wild Crab", "Animal Crab"],
    "Crocodile": ["Crocodile", "Crocodiles", "Large Crocodile", "Small Crocodile", "Wild Crocodile", "Animal Crocodile"],
    "Deer": ["Deer", "Deer", "Large Deer", "Small Deer", "Wild Deer", "Animal Deer"],
    "Duck": ["Duck", "Ducks", "Large Duck", "Small Duck", "Wild Duck", "Animal Duck"],
    "Eagle": ["Eagle", "Eagles", "Large Eagle", "Small Eagle", "Wild Eagle", "Animal Eagle"],
    "Elephant": ["Elephant", "Elephants", "Large Elephant", "Small Elephant", "Wild Elephant", "Animal Elephant"],
    "Fish": ["Fish", "Fish", "Large Fish", "Small Fish", "Wild Fish", "Animal Fish"],
    "Fox": ["Fox", "Foxes", "Large Fox", "Small Fox", "Wild Fox", "Animal Fox"],
    "Frog": ["Frog", "Frogs", "Large Frog", "Small Frog", "Wild Frog", "Animal Frog"],
    "Giraffe": ["Giraffe", "Giraffes", "Large Giraffe", "Small Giraffe", "Wild Giraffe", "Animal Giraffe"],
    "Goat": ["Goat", "Goats", "Large Goat", "Small Goat", "Wild Goat", "Animal Goat"],
    "Goldfish": ["Goldfish", "Goldfish", "Large Goldfish", "Small Goldfish", "Wild Goldfish", "Animal Goldfish"],
    "Goose": ["Goose", "Geese", "Large Goose", "Small Goose", "Wild Goose", "Animal Goose"],
    "Hamster": ["Hamster", "Hamsters", "Large Hamster", "Small Hamster", "Wild Hamster", "Animal Hamster"],
    "Harbor Seal": ["Harbor Seal", "Harbor Seals", "Large Harbor Seal", "Small Harbor Seal", "Wild Harbor Seal", "Animal Harbor Seal"],
    "Hedgehog": ["Hedgehog", "Hedgehogs", "Large Hedgehog", "Small Hedgehog", "Wild Hedgehog", "Animal Hedgehog"],
    "Hippopotamus": ["Hippopotamus", "Hippopotamuses", "Large Hippopotamus", "Small Hippopotamus", "Wild Hippopotamus", "Animal Hippopotamus"],
    "Horse": ["Horse", "Horses", "Large Horse", "Small Horse", "Wild Horse", "Animal Horse"],
    "Jaguar": ["Jaguar", "Jaguars", "Large Jaguar", "Small Jaguar", "Wild Jaguar", "Animal Jaguar"],
    "Jellyfish": ["Jellyfish", "Jellyfish", "Large Jellyfish", "Small Jellyfish", "Wild Jellyfish", "Animal Jellyfish"],
    "Kangaroo": ["Kangaroo", "Kangaroos", "Large Kangaroo", "Small Kangaroo", "Wild Kangaroo", "Animal Kangaroo"],
    "Koala": ["Koala", "Koalas", "Large Koala", "Small Koala", "Wild Koala", "Animal Koala"],
    "Ladybug": ["Ladybug", "Ladybugs", "Large Ladybug", "Small Ladybug", "Wild Ladybug", "Animal Ladybug"],
    "Leopard": ["Leopard", "Leopards", "Large Leopard", "Small Leopard", "Wild Leopard", "Animal Leopard"],
    "Lion": ["Lion", "Lions", "Large Lion", "Small Lion", "Wild Lion", "Animal Lion"],
    "Lizard": ["Lizard", "Lizards", "Large Lizard", "Small Lizard", "Wild Lizard", "Animal Lizard"],
    "Lynx": ["Lynx", "Lynxes", "Large Lynx", "Small Lynx", "Wild Lynx", "Animal Lynx"],
    "Magpie": ["Magpie", "Magpies", "Large Magpie", "Small Magpie", "Wild Magpie", "Animal Magpie"],
    "Monkey": ["Monkey", "Monkeys", "Large Monkey", "Small Monkey", "Wild Monkey", "Animal Monkey"],
    "Moths and butterflies": ["Moths and butterflies", "Moths and butterflies", "Large Moths and butterflies", "Small Moths and butterflies", "Wild Moths and butterflies", "Animal Moths and butterflies"],
    "Mouse": ["Mouse", "Mice", "Large Mouse", "Small Mouse", "Wild Mouse", "Animal Mouse"],
    "Mule": ["Mule", "Mules", "Large Mule", "Small Mule", "Wild Mule", "Animal Mule"],
    "Ostrich": ["Ostrich", "Ostriches", "Large Ostrich", "Small Ostrich", "Wild Ostrich", "Animal Ostrich"],
    "Otter": ["Otter", "Otters", "Large Otter", "Small Otter", "Wild Otter", "Animal Otter"],
    "Owl": ["Owl", "Owls", "Large Owl", "Small Owl", "Wild Owl", "Animal Owl"],
    "Panda": ["Panda", "Pandas", "Large Panda", "Small Panda", "Wild Panda", "Animal Panda"],
    "Parrot": ["Parrot", "Parrots", "Large Parrot", "Small Parrot", "Wild Parrot", "Animal Parrot"],
    "Penguin": ["Penguin", "Penguins", "Large Penguin", "Small Penguin", "Wild Penguin", "Animal Penguin"],
    "Pig": ["Pig", "Pigs", "Large Pig", "Small Pig", "Wild Pig", "Animal Pig"],
    "Polar Bear": ["Polar Bear", "Polar Bears", "Large Polar Bear", "Small Polar Bear", "Wild Polar Bear", "Animal Polar Bear"],
    "Rabbit": ["Rabbit", "Rabbits", "Large Rabbit", "Small Rabbit", "Wild Rabbit", "Animal Rabbit"],
    "Raccoon": ["Raccoon", "Raccoons", "Large Raccoon", "Small Raccoon", "Wild Raccoon", "Animal Raccoon"],
    "Raven": ["Raven", "Ravens", "Large Raven", "Small Raven", "Wild Raven", "Animal Raven"],
    "Red panda": ["Red panda", "Red pandas", "Large Red panda", "Small Red panda", "Wild Red panda", "Animal Red panda"],
    "Rhinoceros": ["Rhinoceros", "Rhinoceroses", "Large Rhinoceros", "Small Rhinoceros", "Wild Rhinoceros", "Animal Rhinoceros"],
    "Scorpion": ["Scorpion", "Scorpions", "Large Scorpion", "Small Scorpion", "Wild Scorpion", "Animal Scorpion"],
    "Seahorse": ["Seahorse", "Seahorses", "Large Seahorse", "Small Seahorse", "Wild Seahorse", "Animal Seahorse"],
    "Sea Lion": ["Sea Lion", "Sea Lions", "Large Sea Lion", "Small Sea Lion", "Wild Sea Lion", "Animal Sea Lion"],
    "Sea Turtle": ["Sea Turtle", "Sea Turtles", "Large Sea Turtle", "Small Sea Turtle", "Wild Sea Turtle", "Animal Sea Turtle"],
    "Shark": ["Shark", "Sharks", "Large Shark", "Small Shark", "Wild Shark", "Animal Shark"],
    "Sheep": ["Sheep", "Sheep", "Large Sheep", "Small Sheep", "Wild Sheep", "Animal Sheep"],
    "Shrimp": ["Shrimp", "Shrimp", "Large Shrimp", "Small Shrimp", "Wild Shrimp", "Animal Shrimp"],
    "Snail": ["Snail", "Snails", "Large Snail", "Small Snail", "Wild Snail", "Animal Snail"],
    "Snake": ["Snake", "Snakes", "Large Snake", "Small Snake", "Wild Snake", "Animal Snake"],
    "Sparrow": ["Sparrow", "Sparrows", "Large Sparrow", "Small Sparrow", "Wild Sparrow", "Animal Sparrow"],
    "Spider": ["Spider", "Spiders", "Large Spider", "Small Spider", "Wild Spider", "Animal Spider"],
    "Squid": ["Squid", "Squids", "Large Squid", "Small Squid", "Wild Squid", "Animal Squid"],
    "Squirrel": ["Squirrel", "Squirrels", "Large Squirrel", "Small Squirrel", "Wild Squirrel", "Animal Squirrel"],
    "Starfish": ["Starfish", "Starfish", "Large Starfish", "Small Starfish", "Wild Starfish", "Animal Starfish"],
    "Swan": ["Swan", "Swans", "Large Swan", "Small Swan", "Wild Swan", "Animal Swan"],
    "Tick": ["Tick", "Ticks", "Large Tick", "Small Tick", "Wild Tick", "Animal Tick"],
    "Tiger": ["Tiger", "Tigers", "Large Tiger", "Small Tiger", "Wild Tiger", "Animal Tiger"],
    "Tortoise": ["Tortoise", "Tortoises", "Large Tortoise", "Small Tortoise", "Wild Tortoise", "Animal Tortoise"],
    "Turkey": ["Turkey", "Turkeys", "Large Turkey", "Small Turkey", "Wild Turkey", "Animal Turkey"],
    "Turtle": ["Turtle", "Turtles", "Large Turtle", "Small Turtle", "Wild Turtle", "Animal Turtle"],
    "Whale": ["Whale", "Whales", "Large Whale", "Small Whale", "Wild Whale", "Animal Whale"],
    "Woodpecker": ["Woodpecker", "Woodpeckers", "Large Woodpecker", "Small Woodpecker", "Wild Woodpecker", "Animal Woodpecker"],
    "Worm": ["Worm", "Worms", "Large Worm", "Small Worm", "Wild Worm", "Animal Worm"],
    "Zebra": ["Zebra", "Zebras", "Large Zebra", "Small Zebra", "Wild Zebra", "Animal Zebra"]
}

# Bear, Bears, Large Bear, Small Bear, Wild Bear, Animal Bear, Brown Bear, Brown Bears, Large Brown Bear, Small Brown Bear, Wild Brown Bear, Animal Brown Bear, Bull, Bulls, Large Bull, Small Bull, Wild Bull, Animal Bull, Butterfly, Butterflies, Large Butterfly, Small Butterfly, Wild Butterfly, Animal Butterfly, Camel, Camels, Large Camel, Small Camel, Wild Camel, Animal Camel, Canary, Canaries, Large Canary, Small Canary, Wild Canary, Animal Canary, Caterpillar, Caterpillars, Large Caterpillar, Small Caterpillar, Wild Caterpillar, Animal Caterpillar, Cattle, Cattle, Large Cattle, Small Cattle, Wild Cattle, Animal Cattle, Centipede, Centipedes, Large Centipede, Small Centipede, Wild Centipede, Animal Centipede, Cheetah, Cheetahs, Large Cheetah, Small Cheetah, Wild Cheetah, Animal Cheetah, Chicken, Chickens, Large Chicken, Small Chicken, Wild Chicken, Animal Chicken, Crab, Crabs, Large Crab, Small Crab, Wild Crab, Animal Crab, Crocodile, Crocodiles, Large Crocodile, Small Crocodile, Wild Crocodile, Animal Crocodile, Deer, Deer, Large Deer, Small Deer, Wild Deer, Animal Deer, Duck, Ducks, Large Duck, Small Duck, Wild Duck, Animal Duck, Eagle, Eagles, Large Eagle, Small Eagle, Wild Eagle, Animal Eagle, Elephant, Elephants, Large Elephant, Small Elephant, Wild Elephant, Animal Elephant, Fish, Fish, Large Fish, Small Fish, Wild Fish, Animal Fish, Fox, Foxes, Large Fox, Small Fox, Wild Fox, Animal Fox, Frog, Frogs, Large Frog, Small Frog, Wild Frog, Animal Frog, Giraffe, Giraffes, Large Giraffe, Small Giraffe, Wild Giraffe, Animal Giraffe, Goat, Goats, Large Goat, Small Goat, Wild Goat, Animal Goat, Goldfish, Goldfish, Large Goldfish, Small Goldfish, Wild Goldfish, Animal Goldfish, Goose, Geese, Large Goose, Small Goose, Wild Goose, Animal Goose, Hamster, Hamsters, Large Hamster, Small Hamster, Wild Hamster, Animal Hamster, Harbor Seal, Harbor Seals, Large Harbor Seal, Small Harbor Seal, Wild Harbor Seal, Animal Harbor Seal, Hedgehog, Hedgehogs, Large Hedgehog, Small Hedgehog, Wild Hedgehog, Animal Hedgehog, Hippopotamus, Hippopotamuses, Large Hippopotamus, Small Hippopotamus, Wild Hippopotamus, Animal Hippopotamus, Horse, Horses, Large Horse, Small Horse, Wild Horse, Animal Horse, Jaguar, Jaguars, Large Jaguar, Small Jaguar, Wild Jaguar, Animal Jaguar, Jellyfish, Jellyfish, Large Jellyfish, Small Jellyfish, Wild Jellyfish, Animal Jellyfish, Kangaroo, Kangaroos, Large Kangaroo, Small Kangaroo, Wild Kangaroo, Animal Kangaroo, Koala, Koalas, Large Koala, Small Koala, Wild Koala, Animal Koala, Ladybug, Ladybugs, Large Ladybug, Small Ladybug, Wild Ladybug, Animal Ladybug, Leopard, Leopards, Large Leopard, Small Leopard, Wild Leopard, Animal Leopard, Lion, Lions, Large Lion, Small Lion, Wild Lion, Animal Lion, Lizard, Lizards, Large Lizard, Small Lizard, Wild Lizard, Animal Lizard, Lynx, Lynxes, Large Lynx, Small Lynx, Wild Lynx, Animal Lynx, Magpie, Magpies, Large Magpie, Small Magpie, Wild Magpie, Animal Magpie, Monkey, Monkeys, Large Monkey, Small Monkey, Wild Monkey, Animal Monkey, Moths and butterflies, Moths and butterflies, Large Moths and butterflies, Small Moths and butterflies, Wild Moths and butterflies, Animal Moths and butterflies, Mouse, Mice, Large Mouse, Small Mouse, Wild Mouse, Animal Mouse, Mule, Mules, Large Mule, Small Mule, Wild Mule, Animal Mule, Ostrich, Ostriches, Large Ostrich, Small Ostrich, Wild Ostrich, Animal Ostrich, Otter, Otters, Large Otter, Small Otter, Wild Otter, Animal Otter, Owl, Owls, Large Owl, Small Owl, Wild Owl, Animal Owl, Panda, Pandas, Large Panda, Small Panda, Wild Panda, Animal Panda, Parrot, Parrots, Large Parrot, Small Parrot, Wild Parrot, Animal Parrot, Penguin, Penguins, Large Penguin, Small Penguin, Wild Penguin, Animal Penguin, Pig, Pigs, Large Pig, Small Pig, Wild Pig, Animal Pig, Polar Bear, Polar Bears, Large Polar Bear, Small Polar Bear, Wild Polar Bear, Animal Polar Bear, Rabbit, Rabbits, Large Rabbit, Small Rabbit, Wild Rabbit, Animal Rabbit, Raccoon, Raccoons, Large Raccoon, Small Raccoon, Wild Raccoon, Animal Raccoon, Raven, Ravens, Large Raven, Small Raven, Wild Raven, Animal Raven, Red panda, Red pandas, Large Red panda, Small Red panda, Wild Red panda, Animal Red panda, Rhinoceros, Rhinoceroses, Large Rhinoceros, Small Rhinoceros, Wild Rhinoceros, Animal Rhinoceros, Scorpion, Scorpions, Large Scorpion, Small Scorpion, Wild Scorpion, Animal Scorpion, Seahorse, Seahorses, Large Seahorse, Small Seahorse, Wild Seahorse, Animal Seahorse, Sea Lion, Sea Lions, Large Sea Lion, Small Sea Lion, Wild Sea Lion, Animal Sea Lion, Sea Turtle, Sea Turtles, Large Sea Turtle, Small Sea Turtle, Wild Sea Turtle, Animal Sea Turtle, Shark, Sharks, Large Shark, Small Shark, Wild Shark, Animal Shark, Sheep, Sheep, Large Sheep, Small Sheep, Wild Sheep, Animal Sheep, Shrimp, Shrimp, Large Shrimp, Small Shrimp, Wild Shrimp, Animal Shrimp, Snail, Snails, Large Snail, Small Snail, Wild Snail, Animal Snail, Snake, Snakes, Large Snake, Small Snake, Wild Snake, Animal Snake, Sparrow, Sparrows, Large Sparrow, Small Sparrow, Wild Sparrow, Animal Sparrow, Spider, Spiders, Large Spider, Small Spider, Wild Spider, Animal Spider, Squid, Squids, Large Squid, Small Squid, Wild Squid, Animal Squid, Squirrel, Squirrels, Large Squirrel, Small Squirrel, Wild Squirrel, Animal Squirrel, Starfish, Starfish, Large Starfish, Small Starfish, Wild Starfish, Animal Starfish, Swan, Swans, Large Swan, Small Swan, Wild Swan, Animal Swan, Tick, Ticks, Large Tick, Small Tick, Wild Tick, Animal Tick, Tiger, Tigers, Large Tiger, Small Tiger, Wild Tiger, Animal Tiger, Tortoise, Tortoises, Large Tortoise, Small Tortoise, Wild Tortoise, Animal Tortoise, Turkey, Turkeys, Large Turkey, Small Turkey, Wild Turkey, Animal Turkey, Turtle, Turtles, Large Turtle, Small Turtle, Wild Turtle, Animal Turtle, Whale, Whales, Large Whale, Small Whale, Wild Whale, Animal Whale, Woodpecker, Woodpeckers, Large Woodpecker, Small Woodpecker, Wild Woodpecker, Animal Woodpecker, Worm, Worms, Large Worm, Small Worm, Wild Worm, Animal Worm, Zebra, Zebras, Large Zebra, Small Zebra, Wild Zebra, Animal Zebra

dict_size(a480)
print(aOcheck_accuracy("animal80/a480.csv", a480))


# %%
a560 = {
    "Bear": ["Bear", "Bears", "Large Bear", "Small Bear", "Wild Bear", "Animal Bear", "Animal Bears"],
    "Brown Bear": ["Brown Bear", "Brown Bears", "Large Brown Bear", "Small Brown Bear", "Wild Brown Bear", "Animal Brown Bear", "Animal Brown Bears"],
    "Bull": ["Bull", "Bulls", "Large Bull", "Small Bull", "Wild Bull", "Animal Bull", "Animal Bulls"],
    "Butterfly": ["Butterfly", "Butterflies", "Large Butterfly", "Small Butterfly", "Wild Butterfly", "Animal Butterfly", "Animal Butterflies"],
    "Camel": ["Camel", "Camels", "Large Camel", "Small Camel", "Wild Camel", "Animal Camel", "Animal Camels"],
    "Canary": ["Canary", "Canaries", "Large Canary", "Small Canary", "Wild Canary", "Animal Canary", "Animal Canaries"],
    "Caterpillar": ["Caterpillar", "Caterpillars", "Large Caterpillar", "Small Caterpillar", "Wild Caterpillar", "Animal Caterpillar", "Animal Caterpillars"],
    "Cattle": ["Cattle", "Cattle", "Large Cattle", "Small Cattle", "Wild Cattle", "Animal Cattle", "Animal Cattle"],
    "Centipede": ["Centipede", "Centipedes", "Large Centipede", "Small Centipede", "Wild Centipede", "Animal Centipede", "Animal Centipedes"],
    "Cheetah": ["Cheetah", "Cheetahs", "Large Cheetah", "Small Cheetah", "Wild Cheetah", "Animal Cheetah", "Animal Cheetahs"],
    "Chicken": ["Chicken", "Chickens", "Large Chicken", "Small Chicken", "Wild Chicken", "Animal Chicken", "Animal Chickens"],
    "Crab": ["Crab", "Crabs", "Large Crab", "Small Crab", "Wild Crab", "Animal Crab", "Animal Crabs"],
    "Crocodile": ["Crocodile", "Crocodiles", "Large Crocodile", "Small Crocodile", "Wild Crocodile", "Animal Crocodile", "Animal Crocodiles"],
    "Deer": ["Deer", "Deer", "Large Deer", "Small Deer", "Wild Deer", "Animal Deer", "Animal Deer"],
    "Duck": ["Duck", "Ducks", "Large Duck", "Small Duck", "Wild Duck", "Animal Duck", "Animal Ducks"],
    "Eagle": ["Eagle", "Eagles", "Large Eagle", "Small Eagle", "Wild Eagle", "Animal Eagle", "Animal Eagles"],
    "Elephant": ["Elephant", "Elephants", "Large Elephant", "Small Elephant", "Wild Elephant", "Animal Elephant", "Animal Elephants"],
    "Fish": ["Fish", "Fish", "Large Fish", "Small Fish", "Wild Fish", "Animal Fish", "Animal Fish"],
    "Fox": ["Fox", "Foxes", "Large Fox", "Small Fox", "Wild Fox", "Animal Fox", "Animal Foxes"],
    "Frog": ["Frog", "Frogs", "Large Frog", "Small Frog", "Wild Frog", "Animal Frog", "Animal Frogs"],
    "Giraffe": ["Giraffe", "Giraffes", "Large Giraffe", "Small Giraffe", "Wild Giraffe", "Animal Giraffe", "Animal Giraffes"],
    "Goat": ["Goat", "Goats", "Large Goat", "Small Goat", "Wild Goat", "Animal Goat", "Animal Goats"],
    "Goldfish": ["Goldfish", "Goldfish", "Large Goldfish", "Small Goldfish", "Wild Goldfish", "Animal Goldfish", "Animal Goldfish"],
    "Goose": ["Goose", "Geese", "Large Goose", "Small Goose", "Wild Goose", "Animal Goose", "Animal Geese"],
    "Hamster": ["Hamster", "Hamsters", "Large Hamster", "Small Hamster", "Wild Hamster", "Animal Hamster", "Animal Hamsters"],
    "Harbor Seal": ["Harbor Seal", "Harbor Seals", "Large Harbor Seal", "Small Harbor Seal", "Wild Harbor Seal", "Animal Harbor Seal", "Animal Harbor Seals"],
    "Hedgehog": ["Hedgehog", "Hedgehogs", "Large Hedgehog", "Small Hedgehog", "Wild Hedgehog", "Animal Hedgehog", "Animal Hedgehogs"],
    "Hippopotamus": ["Hippopotamus", "Hippopotamuses", "Large Hippopotamus", "Small Hippopotamus", "Wild Hippopotamus", "Animal Hippopotamus", "Animal Hippopotamuses"],
    "Horse": ["Horse", "Horses", "Large Horse", "Small Horse", "Wild Horse", "Animal Horse", "Animal Horses"],
    "Jaguar": ["Jaguar", "Jaguars", "Large Jaguar", "Small Jaguar", "Wild Jaguar", "Animal Jaguar", "Animal Jaguars"],
    "Jellyfish": ["Jellyfish", "Jellyfish", "Large Jellyfish", "Small Jellyfish", "Wild Jellyfish", "Animal Jellyfish", "Animal Jellyfish"],
    "Kangaroo": ["Kangaroo", "Kangaroos", "Large Kangaroo", "Small Kangaroo", "Wild Kangaroo", "Animal Kangaroo", "Animal Kangaroos"],
    "Koala": ["Koala", "Koalas", "Large Koala", "Small Koala", "Wild Koala", "Animal Koala", "Animal Koalas"],
    "Ladybug": ["Ladybug", "Ladybugs", "Large Ladybug", "Small Ladybug", "Wild Ladybug", "Animal Ladybug", "Animal Ladybugs"],
    "Leopard": ["Leopard", "Leopards", "Large Leopard", "Small Leopard", "Wild Leopard", "Animal Leopard", "Animal Leopards"],
    "Lion": ["Lion", "Lions", "Large Lion", "Small Lion", "Wild Lion", "Animal Lion", "Animal Lions"],
    "Lizard": ["Lizard", "Lizards", "Large Lizard", "Small Lizard", "Wild Lizard", "Animal Lizard", "Animal Lizards"],
    "Lynx": ["Lynx", "Lynxes", "Large Lynx", "Small Lynx", "Wild Lynx", "Animal Lynx", "Animal Lynxes"],
    "Magpie": ["Magpie", "Magpies", "Large Magpie", "Small Magpie", "Wild Magpie", "Animal Magpie", "Animal Magpies"],
    "Monkey": ["Monkey", "Monkeys", "Large Monkey", "Small Monkey", "Wild Monkey", "Animal Monkey", "Animal Monkeys"],
    "Moths and butterflies": ["Moths and butterflies", "Moths and butterflies", "Large Moths and butterflies", "Small Moths and butterflies", "Wild Moths and butterflies", "Animal Moths and butterflies", "Animal Moths and butterflies"],
    "Mouse": ["Mouse", "Mice", "Large Mouse", "Small Mouse", "Wild Mouse", "Animal Mouse", "Animal Mice"],
    "Mule": ["Mule", "Mules", "Large Mule", "Small Mule", "Wild Mule", "Animal Mule", "Animal Mules"],
    "Ostrich": ["Ostrich", "Ostriches", "Large Ostrich", "Small Ostrich", "Wild Ostrich", "Animal Ostrich", "Animal Ostriches"],
    "Otter": ["Otter", "Otters", "Large Otter", "Small Otter", "Wild Otter", "Animal Otter", "Animal Otters"],
    "Owl": ["Owl", "Owls", "Large Owl", "Small Owl", "Wild Owl", "Animal Owl", "Animal Owls"],
    "Panda": ["Panda", "Pandas", "Large Panda", "Small Panda", "Wild Panda", "Animal Panda", "Animal Pandas"],
    "Parrot": ["Parrot", "Parrots", "Large Parrot", "Small Parrot", "Wild Parrot", "Animal Parrot", "Animal Parrots"],
    "Penguin": ["Penguin", "Penguins", "Large Penguin", "Small Penguin", "Wild Penguin", "Animal Penguin", "Animal Penguins"],
    "Pig": ["Pig", "Pigs", "Large Pig", "Small Pig", "Wild Pig", "Animal Pig", "Animal Pigs"],
    "Polar Bear": ["Polar Bear", "Polar Bears", "Large Polar Bear", "Small Polar Bear", "Wild Polar Bear", "Animal Polar Bear", "Animal Polar Bears"],
    "Rabbit": ["Rabbit", "Rabbits", "Large Rabbit", "Small Rabbit", "Wild Rabbit", "Animal Rabbit", "Animal Rabbits"],
    "Raccoon": ["Raccoon", "Raccoons", "Large Raccoon", "Small Raccoon", "Wild Raccoon", "Animal Raccoon", "Animal Raccoons"],
    "Raven": ["Raven", "Ravens", "Large Raven", "Small Raven", "Wild Raven", "Animal Raven", "Animal Ravens"],
    "Red panda": ["Red panda", "Red pandas", "Large Red panda", "Small Red panda", "Wild Red panda", "Animal Red panda", "Animal Red pandas"],
    "Rhinoceros": ["Rhinoceros", "Rhinoceroses", "Large Rhinoceros", "Small Rhinoceros", "Wild Rhinoceros", "Animal Rhinoceros", "Animal Rhinoceroses"],
    "Scorpion": ["Scorpion", "Scorpions", "Large Scorpion", "Small Scorpion", "Wild Scorpion", "Animal Scorpion", "Animal Scorpions"],
    "Seahorse": ["Seahorse", "Seahorses", "Large Seahorse", "Small Seahorse", "Wild Seahorse", "Animal Seahorse", "Animal Seahorses"],
    "Sea Lion": ["Sea Lion", "Sea Lions", "Large Sea Lion", "Small Sea Lion", "Wild Sea Lion", "Animal Sea Lion", "Animal Sea Lions"],
    "Sea Turtle": ["Sea Turtle", "Sea Turtles", "Large Sea Turtle", "Small Sea Turtle", "Wild Sea Turtle", "Animal Sea Turtle", "Animal Sea Turtles"],
    "Shark": ["Shark", "Sharks", "Large Shark", "Small Shark", "Wild Shark", "Animal Shark", "Animal Sharks"],
    "Sheep": ["Sheep", "Sheep", "Large Sheep", "Small Sheep", "Wild Sheep", "Animal Sheep", "Animal Sheep"],
    "Shrimp": ["Shrimp", "Shrimp", "Large Shrimp", "Small Shrimp", "Wild Shrimp", "Animal Shrimp", "Animal Shrimp"],
    "Snail": ["Snail", "Snails", "Large Snail", "Small Snail", "Wild Snail", "Animal Snail", "Animal Snails"],
    "Snake": ["Snake", "Snakes", "Large Snake", "Small Snake", "Wild Snake", "Animal Snake", "Animal Snakes"],
    "Sparrow": ["Sparrow", "Sparrows", "Large Sparrow", "Small Sparrow", "Wild Sparrow", "Animal Sparrow", "Animal Sparrows"],
    "Spider": ["Spider", "Spiders", "Large Spider", "Small Spider", "Wild Spider", "Animal Spider", "Animal Spiders"],
    "Squid": ["Squid", "Squids", "Large Squid", "Small Squid", "Wild Squid", "Animal Squid", "Animal Squids"],
    "Squirrel": ["Squirrel", "Squirrels", "Large Squirrel", "Small Squirrel", "Wild Squirrel", "Animal Squirrel", "Animal Squirrels"],
    "Starfish": ["Starfish", "Starfish", "Large Starfish", "Small Starfish", "Wild Starfish", "Animal Starfish", "Animal Starfish"],
    "Swan": ["Swan", "Swans", "Large Swan", "Small Swan", "Wild Swan", "Animal Swan", "Animal Swans"],
    "Tick": ["Tick", "Ticks", "Large Tick", "Small Tick", "Wild Tick", "Animal Tick", "Animal Ticks"],
    "Tiger": ["Tiger", "Tigers", "Large Tiger", "Small Tiger", "Wild Tiger", "Animal Tiger", "Animal Tigers"],
    "Tortoise": ["Tortoise", "Tortoises", "Large Tortoise", "Small Tortoise", "Wild Tortoise", "Animal Tortoise", "Animal Tortoises"],
    "Turkey": ["Turkey", "Turkeys", "Large Turkey", "Small Turkey", "Wild Turkey", "Animal Turkey", "Animal Turkeys"],
    "Turtle": ["Turtle", "Turtles", "Large Turtle", "Small Turtle", "Wild Turtle", "Animal Turtle", "Animal Turtles"],
    "Whale": ["Whale", "Whales", "Large Whale", "Small Whale", "Wild Whale", "Animal Whale", "Animal Whales"],
    "Woodpecker": ["Woodpecker", "Woodpeckers", "Large Woodpecker", "Small Woodpecker", "Wild Woodpecker", "Animal Woodpecker", "Animal Woodpeckers"],
    "Worm": ["Worm", "Worms", "Large Worm", "Small Worm", "Wild Worm", "Animal Worm", "Animal Worms"],
    "Zebra": ["Zebra", "Zebras", "Large Zebra", "Small Zebra", "Wild Zebra", "Animal Zebra", "Animal Zebras"]
}

# Bear, Bears, Large Bear, Small Bear, Wild Bear, Animal Bear, Animal Bears, Brown Bear, Brown Bears, Large Brown Bear, Small Brown Bear, Wild Brown Bear, Animal Brown Bear, Animal Brown Bears, Bull, Bulls, Large Bull, Small Bull, Wild Bull, Animal Bull, Animal Bulls, Butterfly, Butterflies, Large Butterfly, Small Butterfly, Wild Butterfly, Animal Butterfly, Animal Butterflies, Camel, Camels, Large Camel, Small Camel, Wild Camel, Animal Camel, Animal Camels, Canary, Canaries, Large Canary, Small Canary, Wild Canary, Animal Canary, Animal Canaries, Caterpillar, Caterpillars, Large Caterpillar, Small Caterpillar, Wild Caterpillar, Animal Caterpillar, Animal Caterpillars, Cattle, Cattle, Large Cattle, Small Cattle, Wild Cattle, Animal Cattle, Animal Cattle, Centipede, Centipedes, Large Centipede, Small Centipede, Wild Centipede, Animal Centipede, Animal Centipedes, Cheetah, Cheetahs, Large Cheetah, Small Cheetah, Wild Cheetah, Animal Cheetah, Animal Cheetahs, Chicken, Chickens, Large Chicken, Small Chicken, Wild Chicken, Animal Chicken, Animal Chickens, Crab, Crabs, Large Crab, Small Crab, Wild Crab, Animal Crab, Animal Crabs, Crocodile, Crocodiles, Large Crocodile, Small Crocodile, Wild Crocodile, Animal Crocodile, Animal Crocodiles, Deer, Deer, Large Deer, Small Deer, Wild Deer, Animal Deer, Animal Deer, Duck, Ducks, Large Duck, Small Duck, Wild Duck, Animal Duck, Animal Ducks, Eagle, Eagles, Large Eagle, Small Eagle, Wild Eagle, Animal Eagle, Animal Eagles, Elephant, Elephants, Large Elephant, Small Elephant, Wild Elephant, Animal Elephant, Animal Elephants, Fish, Fish, Large Fish, Small Fish, Wild Fish, Animal Fish, Animal Fish, Fox, Foxes, Large Fox, Small Fox, Wild Fox, Animal Fox, Animal Foxes, Frog, Frogs, Large Frog, Small Frog, Wild Frog, Animal Frog, Animal Frogs, Giraffe, Giraffes, Large Giraffe, Small Giraffe, Wild Giraffe, Animal Giraffe, Animal Giraffes, Goat, Goats, Large Goat, Small Goat, Wild Goat, Animal Goat, Animal Goats, Goldfish, Goldfish, Large Goldfish, Small Goldfish, Wild Goldfish, Animal Goldfish, Animal Goldfish, Goose, Geese, Large Goose, Small Goose, Wild Goose, Animal Goose, Animal Geese, Hamster, Hamsters, Large Hamster, Small Hamster, Wild Hamster, Animal Hamster, Animal Hamsters, Harbor Seal, Harbor Seals, Large Harbor Seal, Small Harbor Seal, Wild Harbor Seal, Animal Harbor Seal, Animal Harbor Seals, Hedgehog, Hedgehogs, Large Hedgehog, Small Hedgehog, Wild Hedgehog, Animal Hedgehog, Animal Hedgehogs, Hippopotamus, Hippopotamuses, Large Hippopotamus, Small Hippopotamus, Wild Hippopotamus, Animal Hippopotamus, Animal Hippopotamuses, Horse, Horses, Large Horse, Small Horse, Wild Horse, Animal Horse, Animal Horses, Jaguar, Jaguars, Large Jaguar, Small Jaguar, Wild Jaguar, Animal Jaguar, Animal Jaguars, Jellyfish, Jellyfish, Large Jellyfish, Small Jellyfish, Wild Jellyfish, Animal Jellyfish, Animal Jellyfish, Kangaroo, Kangaroos, Large Kangaroo, Small Kangaroo, Wild Kangaroo, Animal Kangaroo, Animal Kangaroos, Koala, Koalas, Large Koala, Small Koala, Wild Koala, Animal Koala, Animal Koalas, Ladybug, Ladybugs, Large Ladybug, Small Ladybug, Wild Ladybug, Animal Ladybug, Animal Ladybugs, Leopard, Leopards, Large Leopard, Small Leopard, Wild Leopard, Animal Leopard, Animal Leopards, Lion, Lions, Large Lion, Small Lion, Wild Lion, Animal Lion, Animal Lions, Lizard, Lizards, Large Lizard, Small Lizard, Wild Lizard, Animal Lizard, Animal Lizards, Lynx, Lynxes, Large Lynx, Small Lynx, Wild Lynx, Animal Lynx, Animal Lynxes, Magpie, Magpies, Large Magpie, Small Magpie, Wild Magpie, Animal Magpie, Animal Magpies, Monkey, Monkeys, Large Monkey, Small Monkey, Wild Monkey, Animal Monkey, Animal Monkeys, Moths and butterflies, Moths and butterflies, Large Moths and butterflies, Small Moths and butterflies, Wild Moths and butterflies, Animal Moths and butterflies, Animal Moths and butterflies, Mouse, Mice, Large Mouse, Small Mouse, Wild Mouse, Animal Mouse, Animal Mice, Mule, Mules, Large Mule, Small Mule, Wild Mule, Animal Mule, Animal Mules, Ostrich, Ostriches, Large Ostrich, Small Ostrich, Wild Ostrich, Animal Ostrich, Animal Ostriches, Otter, Otters, Large Otter, Small Otter, Wild Otter, Animal Otter, Animal Otters, Owl, Owls, Large Owl, Small Owl, Wild Owl, Animal Owl, Animal Owls, Panda, Pandas, Large Panda, Small Panda, Wild Panda, Animal Panda, Animal Pandas, Parrot, Parrots, Large Parrot, Small Parrot, Wild Parrot, Animal Parrot, Animal Parrots, Penguin, Penguins, Large Penguin, Small Penguin, Wild Penguin, Animal Penguin, Animal Penguins, Pig, Pigs, Large Pig, Small Pig, Wild Pig, Animal Pig, Animal Pigs, Polar Bear, Polar Bears, Large Polar Bear, Small Polar Bear, Wild Polar Bear, Animal Polar Bear, Animal Polar Bears, Rabbit, Rabbits, Large Rabbit, Small Rabbit, Wild Rabbit, Animal Rabbit, Animal Rabbits, Raccoon, Raccoons, Large Raccoon, Small Raccoon, Wild Raccoon, Animal Raccoon, Animal Raccoons, Raven, Ravens, Large Raven, Small Raven, Wild Raven, Animal Raven, Animal Ravens, Red panda, Red pandas, Large Red panda, Small Red panda, Wild Red panda, Animal Red panda, Animal Red pandas, Rhinoceros, Rhinoceroses, Large Rhinoceros, Small Rhinoceros, Wild Rhinoceros, Animal Rhinoceros, Animal Rhinoceroses, Scorpion, Scorpions, Large Scorpion, Small Scorpion, Wild Scorpion, Animal Scorpion, Animal Scorpions, Seahorse, Seahorses, Large Seahorse, Small Seahorse, Wild Seahorse, Animal Seahorse, Animal Seahorses, Sea Lion, Sea Lions, Large Sea Lion, Small Sea Lion, Wild Sea Lion, Animal Sea Lion, Animal Sea Lions, Sea Turtle, Sea Turtles, Large Sea Turtle, Small Sea Turtle, Wild Sea Turtle, Animal Sea Turtle, Animal Sea Turtles, Shark, Sharks, Large Shark, Small Shark, Wild Shark, Animal Shark, Animal Sharks, Sheep, Sheep, Large Sheep, Small Sheep, Wild Sheep, Animal Sheep, Animal Sheep, Shrimp, Shrimp, Large Shrimp, Small Shrimp, Wild Shrimp, Animal Shrimp, Animal Shrimp, Snail, Snails, Large Snail, Small Snail, Wild Snail, Animal Snail, Animal Snails, Snake, Snakes, Large Snake, Small Snake, Wild Snake, Animal Snake, Animal Snakes, Sparrow, Sparrows, Large Sparrow, Small Sparrow, Wild Sparrow, Animal Sparrow, Animal Sparrows, Spider, Spiders, Large Spider, Small Spider, Wild Spider, Animal Spider, Animal Spiders, Squid, Squids, Large Squid, Small Squid, Wild Squid, Animal Squid, Animal Squids, Squirrel, Squirrels, Large Squirrel, Small Squirrel, Wild Squirrel, Animal Squirrel, Animal Squirrels, Starfish, Starfish, Large Starfish, Small Starfish, Wild Starfish, Animal Starfish, Animal Starfish, Swan, Swans, Large Swan, Small Swan, Wild Swan, Animal Swan, Animal Swans, Tick, Ticks, Large Tick, Small Tick, Wild Tick, Animal Tick, Animal Ticks, Tiger, Tigers, Large Tiger, Small Tiger, Wild Tiger, Animal Tiger, Animal Tigers, Tortoise, Tortoises, Large Tortoise, Small Tortoise, Wild Tortoise, Animal Tortoise, Animal Tortoises, Turkey, Turkeys, Large Turkey, Small Turkey, Wild Turkey, Animal Turkey, Animal Turkeys, Turtle, Turtles, Large Turtle, Small Turtle, Wild Turtle, Animal Turtle, Animal Turtles, Whale, Whales, Large Whale, Small Whale, Wild Whale, Animal Whale, Animal Whales, Woodpecker, Woodpeckers, Large Woodpecker, Small Woodpecker, Wild Woodpecker, Animal Woodpecker, Animal Woodpeckers, Worm, Worms, Large Worm, Small Worm, Wild Worm, Animal Worm, Animal Worms, Zebra, Zebras, Large Zebra, Small Zebra, Wild Zebra, Animal Zebra, Animal Zebras
dict_size(a560)
print(aOcheck_accuracy("animal80/a560.csv", a560))


# %% [markdown]
# ## Animal 4

# %%
dict_8 = {
    "Buffalo": ["Buffalo", "Buffaloes"],
    "Elephant": ["Elephant", "Elephants"],
    "Rhino": ["Rhino", "Rhinoceros"],
    "Zebra": ["Zebra", "Zebras"],
}

#Buffalo,Buffaloes,Elephant,Elephants,Rhino,Rhinoceros,Zebra,Zebras

# dict_size(dict_8)
# print(aOcheck_accuracy("animal4/AO8.csv", dict_8))

# %%
dict_12 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Elephant, Elephants, Picture of Elephant, Rhino, Rhinoceros, Picture of Rhino, Zebra, Zebras, Picture of Zebra

# dict_size(dict_12)
# print(aOcheck_accuracy("animal4/AO12.csv", dict_12))


# %%
dict_16 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Elephant, Elephants, Picture of Elephant, Image of Elephant, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Zebra, Zebras, Picture of Zebra, Image of Zebra

# dict_size(dict_16)
# print(aOcheck_accuracy("animal4/AO16.csv", dict_16))


# %%
dict_20 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra

# dict_size(dict_20)
# print(aOcheck_accuracy("animal4/AO20.csv", dict_20))


# %%
dict_24 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd

# dict_size(dict_24)
# print(aOcheck_accuracy("animal4/AO24.csv", dict_24))


# %%
dict_32 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd", "African Buffalo", "Buffalo in the Wild"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd", "African Elephant", "Elephant in the Wild"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd", "African Rhino", "Rhino in the Wild"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd", "African Zebra", "Zebra in the Wild"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild

# dict_size(dict_32)
# print(aOcheck_accuracy("animal4/AO32.csv", dict_32))


# %%
dict_36 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd", "African Buffalo", "Buffalo in the Wild", "Large Buffalo"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd", "African Elephant", "Elephant in the Wild", "Large Elephant"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd", "African Rhino", "Rhino in the Wild", "Large Rhino"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd", "African Zebra", "Zebra in the Wild", "Large Zebra"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Large Buffalo, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Large Elephant, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Large Rhino, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild, Large Zebra

# dict_size(dict_36)
# print(aOcheck_accuracy("animal4/AO36.csv", dict_36))


# %%
dict_40 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd", "African Buffalo", "Buffalo in the Wild", "Large Buffalo", "Buffalo Plains"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd", "African Elephant", "Elephant in the Wild", "Large Elephant", "Elephant Plains"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd", "African Rhino", "Rhino in the Wild", "Large Rhino", "Rhino Plains"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd", "African Zebra", "Zebra in the Wild", "Large Zebra", "Zebra Plains"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Large Buffalo, Buffalo Plains, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Large Elephant, Elephant Plains, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Large Rhino, Rhino Plains, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild, Large Zebra, Zebra Plains

# dict_size(dict_40)
# print(aOcheck_accuracy("animal4/AO40.csv", dict_40))


# %%
dict_44 = {#problem
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd", "African Buffalo", "Buffalo in the Wild", "Large Buffalo", "Buffalo Plains", "Moving Buffalo"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd", "African Elephant", "Elephant in the Wild", "Large Elephant", "Elephant Plains", "Moving Elephant"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd", "African Rhino", "Rhino in the Wild", "Large Rhino", "Rhino Plains", "Moving Rhino"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd", "African Zebra", "Zebra in the Wild", "Large Zebra", "Zebra Plains", "Moving Zebra"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Large Buffalo, Buffalo Plains, Moving Buffalo, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Large Elephant, Elephant Plains, Moving Elephant, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Large Rhino, Rhino Plains, Moving Rhino, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild, Large Zebra, Zebra Plains, Moving Zebra

# dict_size(dict_44)
# print(aOcheck_accuracy("animal4/AO44.csv", dict_44))


# %%
dict_48 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd", "African Buffalo", "Buffalo in the Wild", "Large Buffalo", "Buffalo Plains", "Moving Buffalo", "American Buffalo"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd", "African Elephant", "Elephant in the Wild", "Large Elephant", "Elephant Plains", "Moving Elephant", "Asian Elephant"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd", "African Rhino", "Rhino in the Wild", "Large Rhino", "Rhino Plains", "Moving Rhino", "Black Rhino"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd", "African Zebra", "Zebra in the Wild", "Large Zebra", "Zebra Plains", "Moving Zebra", "Wild Plains Zebra"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Large Buffalo, Buffalo Plains, Moving Buffalo, American Buffalo, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Large Elephant, Elephant Plains, Moving Elephant, Asian Elephant, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Large Rhino, Rhino Plains, Moving Rhino, Black Rhino, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild, Large Zebra, Zebra Plains, Moving Zebra, Wild Plains Zebra

# dict_size(dict_48)
# print(aOcheck_accuracy("animal4/AO48.csv", dict_48))


# %%
dict_52 = {
    "Buffalo": ["Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd", "African Buffalo", "Buffalo in the Wild", "Large Buffalo", "Buffalo Plains", "Moving Buffalo", "American Buffalo", "Buffalo in Herds"],
    "Elephant": ["Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd", "African Elephant", "Elephant in the Wild", "Large Elephant", "Elephant Plains", "Moving Elephant", "Asian Elephant", "Elephant in Herds"],
    "Rhino": ["Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd", "African Rhino", "Rhino in the Wild", "Large Rhino", "Rhino Plains", "Moving Rhino", "Black Rhino", "Rhino in Herds"],
    "Zebra": ["Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd", "African Zebra", "Zebra in the Wild", "Large Zebra", "Zebra Plains", "Moving Zebra", "Wild Plains Zebra", "Zebra in Herds"],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Large Buffalo, Buffalo Plains, Moving Buffalo, American Buffalo, Buffalo in Herds, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Large Elephant, Elephant Plains, Moving Elephant, Asian Elephant, Elephant in Herds, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Large Rhino, Rhino Plains, Moving Rhino, Black Rhino, Rhino in Herds, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild, Large Zebra, Zebra Plains, Moving Zebra, Wild Plains Zebra, Zebra in Herds

# dict_size(dict_52)
# print(aOcheck_accuracy("animal4/AO52.csv", dict_52))


# %%
dict_56 = {
    "Buffalo": [
        "Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd",
        "African Buffalo", "Buffalo in the Wild", "Large Buffalo", "Buffalo Plains", "Moving Buffalo",
        "American Buffalo", "Buffalo in Herds", "Savannah Buffalo"
    ],
    "Elephant": [
        "Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd",
        "African Elephant", "Elephant in the Wild", "Large Elephant", "Elephant Plains", "Moving Elephant",
        "Asian Elephant", "Elephant in Herds", "Savannah Elephant"
    ],
    "Rhino": [
        "Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd",
        "African Rhino", "Rhino in the Wild", "Large Rhino", "Rhino Plains", "Moving Rhino",
        "Black Rhino", "Rhino in Herds", "Savannah Rhino"
    ],
    "Zebra": [
        "Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd",
        "African Zebra", "Zebra in the Wild", "Large Zebra", "Zebra Plains", "Moving Zebra",
        "Wild Plains Zebra", "Zebra in Herds", "Savannah Zebra"
    ],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Large Buffalo, Buffalo Plains, Moving Buffalo, American Buffalo, Buffalo in Herds, Savannah Buffalo, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Large Elephant, Elephant Plains, Moving Elephant, Asian Elephant, Elephant in Herds, Savannah Elephant, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Large Rhino, Rhino Plains, Moving Rhino, Black Rhino, Rhino in Herds, Savannah Rhino, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild, Large Zebra, Zebra Plains, Moving Zebra, Wild Plains Zebra, Zebra in Herds, Savannah Zebra

# dict_size(dict_56)
# print(aOcheck_accuracy("animal4/AO56.csv", dict_56))


# %%
dict_60 = {
    "Buffalo": [
        "Buffalo", "Buffaloes", "Picture of Buffalo", "Image of Buffalo", "Wild Buffalo", "Buffalo Herd",
        "African Buffalo", "Buffalo in the Wild", "Large Buffalo", "Buffalo Plains", "Moving Buffalo",
        "American Buffalo", "Buffalo in Herds", "Savannah Buffalo", "Horned Buffalo"
    ],
    "Elephant": [
        "Elephant", "Elephants", "Picture of Elephant", "Image of Elephant", "Wild Elephant", "Elephant Herd",
        "African Elephant", "Elephant in the Wild", "Large Elephant", "Elephant Plains", "Moving Elephant",
        "Asian Elephant", "Elephant in Herds", "Savannah Elephant", "Tusker Elephant"
    ],
    "Rhino": [
        "Rhino", "Rhinoceros", "Picture of Rhino", "Image of Rhino", "Wild Rhino", "Rhino Herd",
        "African Rhino", "Rhino in the Wild", "Large Rhino", "Rhino Plains", "Moving Rhino",
        "Black Rhino", "Rhino in Herds", "Savannah Rhino", "Horned Rhino"
    ],
    "Zebra": [
        "Zebra", "Zebras", "Picture of Zebra", "Image of Zebra", "Wild Zebra", "Zebra Herd",
        "African Zebra", "Zebra in the Wild", "Large Zebra", "Zebra Plains", "Moving Zebra",
        "Wild Plains Zebra", "Zebra in Herds", "Savannah Zebra", "Mountain Zebra"
    ],
}

# Buffalo, Buffaloes, Picture of Buffalo, Image of Buffalo, Wild Buffalo, Buffalo Herd, African Buffalo, Buffalo in the Wild, Large Buffalo, Buffalo Plains, Moving Buffalo, American Buffalo, Buffalo in Herds, Savannah Buffalo, Horned Buffalo, Elephant, Elephants, Picture of Elephant, Image of Elephant, Wild Elephant, Elephant Herd, African Elephant, Elephant in the Wild, Large Elephant, Elephant Plains, Moving Elephant, Asian Elephant, Elephant in Herds, Savannah Elephant, Tusker Elephant, Rhino, Rhinoceros, Picture of Rhino, Image of Rhino, Wild Rhino, Rhino Herd, African Rhino, Rhino in the Wild, Large Rhino, Rhino Plains, Moving Rhino, Black Rhino, Rhino in Herds, Savannah Rhino, Horned Rhino, Zebra, Zebras, Picture of Zebra, Image of Zebra, Wild Zebra, Zebra Herd, African Zebra, Zebra in the Wild, Large Zebra, Zebra Plains, Moving Zebra, Wild Plains Zebra, Zebra in Herds, Savannah Zebra, Mountain Zebra

# dict_size(dict_60)
# print(aOcheck_accuracy("animal4/AO60.csv", dict_60))


# %% [markdown]
# ## CatDog

# %%
CDdict2 = {
        'cat': ['cat'],
        'dog': ['dog']
    }


# %%
CDdict4 = { 
    'cat': ['cat', 'picture of cat'],
    'dog': ['dog', 'picture of dog']
}

# %%
CDdict6 = { 
    'cat': ['cat', 'picture of cat', 'cats'],
    'dog': ['dog', 'picture of dog', 'dogs']
}


# %%
CDdict8 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs']
}


# %%
CDdict10 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog']
}

# %%
CDdict12 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture']
}

# %%
CDdict14 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image']
}


# %%
CDdict16 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image', 'cool cat'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image', 'cool dog']
}


# %%
CDdict18 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image', 'cool cat', 'sitting cat'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image', 'cool dog', 'sitting dog']
}


# %%
CDdict20 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image', 'cool cat', 'sitting cat', 'nice cat'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image', 'cool dog', 'sitting dog', 'nice dog']
}

# %%
CDdict22 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image', 'cool cat', 'sitting cat', 'nice cat', 'image of nice cat'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image', 'cool dog', 'sitting dog', 'nice dog', 'image of nice dog']
}

# %%
CDdict24 = { 
    'cat': ['cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image', 'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat'],
    'dog': ['dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image', 'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog']
}


# %%
CDdict26 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog'
    ]
}

# %%
CDdict28 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat', 'picture of cats'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog', 'picture of dogs'
    ]
}

# %%
CDdict30 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog'
    ]
}


# %%
CDdict32 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog'
    ]
}


# %%
CDdict36 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog'
    ]
}

# %%
CDdict38 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog'
    ]
}

# %%
CDdict42 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat',
        'cute cat', 'cute image of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog',
        'cute dog', 'cute image of dog'
    ]
}


# %%
CDdict44 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat',
        'cute cat', 'cute image of cat', 'cute picture of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog',
        'cute dog', 'cute image of dog', 'cute picture of dog'
    ]
}

# %%
CDdict48 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat',
        'cute cat', 'cute image of cat', 'cute picture of cat',
        'amazing cat', 'amazing image of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog',
        'cute dog', 'cute image of dog', 'cute picture of dog',
        'amazing dog', 'amazing image of dog'
    ]
}

# %%
CDdict50 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat',
        'cute cat', 'cute image of cat', 'cute picture of cat',
        'amazing cat', 'amazing image of cat', 'amazing picture of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog',
        'cute dog', 'cute image of dog', 'cute picture of dog',
        'amazing dog', 'amazing image of dog', 'amazing picture of dog'
    ]
}

# %%
CDdict52 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat',
        'cute cat', 'cute image of cat', 'cute picture of cat',
        'amazing cat', 'amazing image of cat', 'amazing picture of cat',
        'adorable cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog',
        'cute dog', 'cute image of dog', 'cute picture of dog',
        'amazing dog', 'amazing image of dog', 'amazing picture of dog',
        'adorable dog'
    ]
}

# %%
CDdict54 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat',
        'cute cat', 'cute image of cat', 'cute picture of cat',
        'amazing cat', 'amazing image of cat', 'amazing picture of cat',
        'adorable cat', 'adorable image of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog',
        'cute dog', 'cute image of dog', 'cute picture of dog',
        'amazing dog', 'amazing image of dog', 'amazing picture of dog',
        'adorable dog', 'adorable image of dog'
    ]
}


# %%
CDdict56 = { 
    'cat': [
        'cat', 'picture of cat', 'cats', 'image of cats', 'moving cat', 'cat picture', 'cat image',
        'cool cat', 'sitting cat', 'nice cat', 'image of nice cat', 'image of cool cat', 'image of cat',
        'picture of cats', 'moving picture of cat', 'cool picture of cat',
        'funny cat', 'funny image of cat', 'funny picture of cat',
        'cute cat', 'cute image of cat', 'cute picture of cat',
        'amazing cat', 'amazing image of cat', 'amazing picture of cat',
        'adorable cat', 'adorable image of cat', 'adorable picture of cat'
    ],
    'dog': [
        'dog', 'picture of dog', 'dogs', 'image of dogs', 'moving dog', 'dog picture', 'dog image',
        'cool dog', 'sitting dog', 'nice dog', 'image of nice dog', 'image of cool dog', 'image of dog',
        'picture of dogs', 'moving picture of dog', 'cool picture of dog',
        'funny dog', 'funny image of dog', 'funny picture of dog',
        'cute dog', 'cute image of dog', 'cute picture of dog',
        'amazing dog', 'amazing image of dog', 'amazing picture of dog',
        'adorable dog', 'adorable image of dog', 'adorable picture of dog'
    ]
}

# %% [markdown]
# 

# %% [markdown]
# ## Vegetables

# %%
# veg15 = {"Bean" : ["Bean"],
#          "Bitter Gourd" : ["Bitter Gourd"],
#          "Bottle Gourd" : ["Bottle Gourd"],
#          "Brinjal" : ["Brinjal"],
#          "Cabbage" : ["Cabbage"],
#          "Broccoli" : ["Broccoli"],
#          "Capsicum" : ["Capsicum"],
#          "Carrot" : ["Carrot"],
#          "Cauliflower" : ["Cauliflower"],
#          "Cucumber" : ["Cucumber"],
#          "Papaya" : ["Papaya"],
#          "Potato" : ["Potato"],
#          "Pumpkin" : ["Pumpkin"],
#          "Radish" : ["Radish"],
#          "Tomato" : ["Tomato"]}

# # Bean, Bitter Gourd, Bottle Gourd, Brinjal, Cabbage, Broccoli, Capsicum, Carrot, Cauliflower, Cucumber, Papaya, Potato, Pumpkin, Radish, Tomato

# # dict_size(veg15)
# print(aOcheck_accuracy("WithoutIP/Vegetable15/veg15.csv", veg15))

# %%
# veg30 = {
#     "Bean": ["Bean", "Beans"],
#     "Bitter Gourd": ["Bitter Gourd", "Bitter Gourds"],
#     "Bottle Gourd": ["Bottle Gourd", "Bottle Gourds"],
#     "Brinjal": ["Brinjal", "Brinjals"],
#     "Cabbage": ["Cabbage", "Cabbages"],
#     "Broccoli": ["Broccoli", "Broccolis"],
#     "Capsicum": ["Capsicum", "Capsicums"],
#     "Carrot": ["Carrot", "Carrots"],
#     "Cauliflower": ["Cauliflower", "Cauliflowers"],
#     "Cucumber": ["Cucumber", "Cucumbers"],
#     "Papaya": ["Papaya", "Papayas"],
#     "Potato": ["Potato", "Potatoes"],
#     "Pumpkin": ["Pumpkin", "Pumpkins"],
#     "Radish": ["Radish", "Radishes"],
#     "Tomato": ["Tomato", "Tomatoes"]
# }

# # Bean, Beans, Bitter Gourd, Bitter Gourds, Bottle Gourd, Bottle Gourds, Brinjal, Brinjals, Cabbage, Cabbages, Broccoli, Broccolis, Capsicum, Capsicums, Carrot, Carrots, Cauliflower, Cauliflowers, Cucumber, Cucumbers, Papaya, Papayas, Potato, Potatoes, Pumpkin, Pumpkins, Radish, Radishes, Tomato, Tomatoes

# # dict_size(veg30)
# print(aOcheck_accuracy("WithoutIP/Vegetable15/veg30.csv", veg30))

# %%
# veg45 = {
#     "Bean": ["Bean", "Beans", "Large Bean"],
#     "Bitter Gourd": ["Bitter Gourd", "Bitter Gourds", "Large Bitter Gourd"],
#     "Bottle Gourd": ["Bottle Gourd", "Bottle Gourds", "Large Bottle Gourd"],
#     "Brinjal": ["Brinjal", "Brinjals", "Large Brinjal"],
#     "Cabbage": ["Cabbage", "Cabbages", "Large Cabbage"],
#     "Broccoli": ["Broccoli", "Broccolis", "Large Broccoli"],
#     "Capsicum": ["Capsicum", "Capsicums", "Large Capsicum"],
#     "Carrot": ["Carrot", "Carrots", "Large Carrot"],
#     "Cauliflower": ["Cauliflower", "Cauliflowers", "Large Cauliflower"],
#     "Cucumber": ["Cucumber", "Cucumbers", "Large Cucumber"],
#     "Papaya": ["Papaya", "Papayas", "Large Papaya"],
#     "Potato": ["Potato", "Potatoes", "Large Potato"],
#     "Pumpkin": ["Pumpkin", "Pumpkins", "Large Pumpkin"],
#     "Radish": ["Radish", "Radishes", "Large Radish"],
#     "Tomato": ["Tomato", "Tomatoes", "Large Tomato"]
# }

# # Bean, Beans, Large Bean, Bitter Gourd, Bitter Gourds, Large Bitter Gourd, Bottle Gourd, Bottle Gourds, Large Bottle Gourd, Brinjal, Brinjals, Large Brinjal, Cabbage, Cabbages, Large Cabbage, Broccoli, Broccolis, Large Broccoli, Capsicum, Capsicums, Large Capsicum, Carrot, Carrots, Large Carrot, Cauliflower, Cauliflowers, Large Cauliflower, Cucumber, Cucumbers, Large Cucumber, Papaya, Papayas, Large Papaya, Potato, Potatoes, Large Potato, Pumpkin, Pumpkins, Large Pumpkin, Radish, Radishes, Large Radish, Tomato, Tomatoes, Large Tomato

# # dict_size(veg45)
# print(aOcheck_accuracy("WithoutIP/Vegetable15/veg45.csv", veg45))


# %%
# veg60 = {
#     "Bean": ["Bean", "Beans", "Large Bean", "Small Bean"],
#     "Bitter Gourd": ["Bitter Gourd", "Bitter Gourds", "Large Bitter Gourd", "Small Bitter Gourd"],
#     "Bottle Gourd": ["Bottle Gourd", "Bottle Gourds", "Large Bottle Gourd", "Small Bottle Gourd"],
#     "Brinjal": ["Brinjal", "Brinjals", "Large Brinjal", "Small Brinjal"],
#     "Cabbage": ["Cabbage", "Cabbages", "Large Cabbage", "Small Cabbage"],
#     "Broccoli": ["Broccoli", "Broccolis", "Large Broccoli", "Small Broccoli"],
#     "Capsicum": ["Capsicum", "Capsicums", "Large Capsicum", "Small Capsicum"],
#     "Carrot": ["Carrot", "Carrots", "Large Carrot", "Small Carrot"],
#     "Cauliflower": ["Cauliflower", "Cauliflowers", "Large Cauliflower", "Small Cauliflower"],
#     "Cucumber": ["Cucumber", "Cucumbers", "Large Cucumber", "Small Cucumber"],
#     "Papaya": ["Papaya", "Papayas", "Large Papaya", "Small Papaya"],
#     "Potato": ["Potato", "Potatoes", "Large Potato", "Small Potato"],
#     "Pumpkin": ["Pumpkin", "Pumpkins", "Large Pumpkin", "Small Pumpkin"],
#     "Radish": ["Radish", "Radishes", "Large Radish", "Small Radish"],
#     "Tomato": ["Tomato", "Tomatoes", "Large Tomato", "Small Tomato"]
# }

# # Bean, Beans, Large Bean, Small Bean, Bitter Gourd, Bitter Gourds, Large Bitter Gourd, Small Bitter Gourd, Bottle Gourd, Bottle Gourds, Large Bottle Gourd, Small Bottle Gourd, Brinjal, Brinjals, Large Brinjal, Small Brinjal, Cabbage, Cabbages, Large Cabbage, Small Cabbage, Broccoli, Broccolis, Large Broccoli, Small Broccoli, Capsicum, Capsicums, Large Capsicum, Small Capsicum, Carrot, Carrots, Large Carrot, Small Carrot, Cauliflower, Cauliflowers, Large Cauliflower, Small Cauliflower, Cucumber, Cucumbers, Large Cucumber, Small Cucumber, Papaya, Papayas, Large Papaya, Small Papaya, Potato, Potatoes, Large Potato, Small Potato, Pumpkin, Pumpkins, Large Pumpkin, Small Pumpkin, Radish, Radishes, Large Radish, Small Radish, Tomato, Tomatoes, Large Tomato, Small Tomato

# # dict_size(veg60)
# print(aOcheck_accuracy("WithoutIP/Vegetable15/veg60.csv", veg60))


# %%
# veg75 = {
#     "Bean": ["Bean", "Beans", "Large Bean", "Large Beans", "Small Bean"],
#     "Bitter Gourd": ["Bitter Gourd", "Bitter Gourds", "Large Bitter Gourd", "Large Bitter Gourds", "Small Bitter Gourd"],
#     "Bottle Gourd": ["Bottle Gourd", "Bottle Gourds", "Large Bottle Gourd", "Large Bottle Gourds", "Small Bottle Gourd"],
#     "Brinjal": ["Brinjal", "Brinjals", "Large Brinjal", "Large Brinjals", "Small Brinjal"],
#     "Cabbage": ["Cabbage", "Cabbages", "Large Cabbage", "Large Cabbages", "Small Cabbage"],
#     "Broccoli": ["Broccoli", "Broccolis", "Large Broccoli", "Large Broccolis", "Small Broccoli"],
#     "Capsicum": ["Capsicum", "Capsicums", "Large Capsicum", "Large Capsicums", "Small Capsicum"],
#     "Carrot": ["Carrot", "Carrots", "Large Carrot", "Large Carrots", "Small Carrot"],
#     "Cauliflower": ["Cauliflower", "Cauliflowers", "Large Cauliflower", "Large Cauliflowers", "Small Cauliflower"],
#     "Cucumber": ["Cucumber", "Cucumbers", "Large Cucumber", "Large Cucumbers", "Small Cucumber"],
#     "Papaya": ["Papaya", "Papayas", "Large Papaya", "Large Papayas", "Small Papaya"],
#     "Potato": ["Potato", "Potatoes", "Large Potato", "Large Potatoes", "Small Potato"],
#     "Pumpkin": ["Pumpkin", "Pumpkins", "Large Pumpkin", "Large Pumpkins", "Small Pumpkin"],
#     "Radish": ["Radish", "Radishes", "Large Radish", "Large Radishes", "Small Radish"],
#     "Tomato": ["Tomato", "Tomatoes", "Large Tomato", "Large Tomatoes", "Small Tomato"]
# }

# # Bean, Beans, Large Bean, Large Beans, Small Bean, Bitter Gourd, Bitter Gourds, Large Bitter Gourd, Large Bitter Gourds, Small Bitter Gourd, Bottle Gourd, Bottle Gourds, Large Bottle Gourd, Large Bottle Gourds, Small Bottle Gourd, Brinjal, Brinjals, Large Brinjal, Large Brinjals, Small Brinjal, Cabbage, Cabbages, Large Cabbage, Large Cabbages, Small Cabbage, Broccoli, Broccolis, Large Broccoli, Large Broccolis, Small Broccoli, Capsicum, Capsicums, Large Capsicum, Large Capsicums, Small Capsicum, Carrot, Carrots, Large Carrot, Large Carrots, Small Carrot, Cauliflower, Cauliflowers, Large Cauliflower, Large Cauliflowers, Small Cauliflower, Cucumber, Cucumbers, Large Cucumber, Large Cucumbers, Small Cucumber, Papaya, Papayas, Large Papaya, Large Papayas, Small Papaya, Potato, Potatoes, Large Potato, Large Potatoes, Small Potato, Pumpkin, Pumpkins, Large Pumpkin, Large Pumpkins, Small Pumpkin, Radish, Radishes, Large Radish, Large Radishes, Small Radish, Tomato, Tomatoes, Large Tomato, Large Tomatoes, Small Tomato

# # dict_size(veg75)
# print(aOcheck_accuracy("WithoutIP/Vegetable15/veg75.csv", veg75))


# %%
# veg90 = {
#     "Bean": ["Bean", "Beans", "Large Bean", "Large Beans", "Small Bean", "Small Beans"],
#     "Bitter Gourd": ["Bitter Gourd", "Bitter Gourds", "Large Bitter Gourd", "Large Bitter Gourds", "Small Bitter Gourd", "Small Bitter Gourds"],
#     "Bottle Gourd": ["Bottle Gourd", "Bottle Gourds", "Large Bottle Gourd", "Large Bottle Gourds", "Small Bottle Gourd", "Small Bottle Gourds"],
#     "Brinjal": ["Brinjal", "Brinjals", "Large Brinjal", "Large Brinjals", "Small Brinjal", "Small Brinjals"],
#     "Cabbage": ["Cabbage", "Cabbages", "Large Cabbage", "Large Cabbages", "Small Cabbage", "Small Cabbages"],
#     "Broccoli": ["Broccoli", "Broccolis", "Large Broccoli", "Large Broccolis", "Small Broccoli", "Small Broccolis"],
#     "Capsicum": ["Capsicum", "Capsicums", "Large Capsicum", "Large Capsicums", "Small Capsicum", "Small Capsicums"],
#     "Carrot": ["Carrot", "Carrots", "Large Carrot", "Large Carrots", "Small Carrot", "Small Carrots"],
#     "Cauliflower": ["Cauliflower", "Cauliflowers", "Large Cauliflower", "Large Cauliflowers", "Small Cauliflower", "Small Cauliflowers"],
#     "Cucumber": ["Cucumber", "Cucumbers", "Large Cucumber", "Large Cucumbers", "Small Cucumber", "Small Cucumbers"],
#     "Papaya": ["Papaya", "Papayas", "Large Papaya", "Large Papayas", "Small Papaya", "Small Papayas"],
#     "Potato": ["Potato", "Potatoes", "Large Potato", "Large Potatoes", "Small Potato", "Small Potatoes"],
#     "Pumpkin": ["Pumpkin", "Pumpkins", "Large Pumpkin", "Large Pumpkins", "Small Pumpkin", "Small Pumpkins"],
#     "Radish": ["Radish", "Radishes", "Large Radish", "Large Radishes", "Small Radish", "Small Radishes"],
#     "Tomato": ["Tomato", "Tomatoes", "Large Tomato", "Large Tomatoes", "Small Tomato", "Small Tomatoes"]
# }

# # Bean, Beans, Large Bean, Large Beans, Small Bean, Small Beans, Bitter Gourd, Bitter Gourds, Large Bitter Gourd, Large Bitter Gourds, Small Bitter Gourd, Small Bitter Gourds, Bottle Gourd, Bottle Gourds, Large Bottle Gourd, Large Bottle Gourds, Small Bottle Gourd, Small Bottle Gourds, Brinjal, Brinjals, Large Brinjal, Large Brinjals, Small Brinjal, Small Brinjals, Cabbage, Cabbages, Large Cabbage, Large Cabbages, Small Cabbage, Small Cabbages, Broccoli, Broccolis, Large Broccoli, Large Broccolis, Small Broccoli, Small Broccolis, Capsicum, Capsicums, Large Capsicum, Large Capsicums, Small Capsicum, Small Capsicums, Carrot, Carrots, Large Carrot, Large Carrots, Small Carrot, Small Carrots, Cauliflower, Cauliflowers, Large Cauliflower, Large Cauliflowers, Small Cauliflower, Small Cauliflowers, Cucumber, Cucumbers, Large Cucumber, Large Cucumbers, Small Cucumber, Small Cucumbers, Papaya, Papayas, Large Papaya, Large Papayas, Small Papaya, Small Papayas, Potato, Potatoes, Large Potato, Large Potatoes, Small Potato, Small Potatoes, Pumpkin, Pumpkins, Large Pumpkin, Large Pumpkins, Small Pumpkin, Small Pumpkins, Radish, Radishes, Large Radish, Large Radishes, Small Radish, Small Radishes, Tomato, Tomatoes, Large Tomato, Large Tomatoes, Small Tomato, Small Tomatoes

# # dict_size(veg90)
# print(aOcheck_accuracy("WithoutIP/Vegetable15/veg90.csv", veg90))


# %%
# veg105 = {
#     "Bean": ["Bean", "Beans", "Large Bean", "Small Bean", "Large Beans", "Small Beans", "Vegetable Bean"],
#     "Bitter Gourd": ["Bitter Gourd", "Bitter Gourds", "Large Bitter Gourd", "Small Bitter Gourd", "Large Bitter Gourds", "Small Bitter Gourds", "Vegetable Bitter Gourd"],
#     "Bottle Gourd": ["Bottle Gourd", "Bottle Gourds", "Large Bottle Gourd", "Small Bottle Gourd", "Large Bottle Gourds", "Small Bottle Gourds", "Vegetable Bottle Gourd"],
#     "Brinjal": ["Brinjal", "Brinjals", "Large Brinjal", "Small Brinjal", "Large Brinjals", "Small Brinjals", "Vegetable Brinjal"],
#     "Cabbage": ["Cabbage", "Cabbages", "Large Cabbage", "Small Cabbage", "Large Cabbages", "Small Cabbages", "Vegetable Cabbage"],
#     "Broccoli": ["Broccoli", "Broccolis", "Large Broccoli", "Small Broccoli", "Large Broccolis", "Small Broccolis", "Vegetable Broccoli"],
#     "Capsicum": ["Capsicum", "Capsicums", "Large Capsicum", "Small Capsicum", "Large Capsicums", "Small Capsicums", "Vegetable Capsicum"],
#     "Carrot": ["Carrot", "Carrots", "Large Carrot", "Small Carrot", "Large Carrots", "Small Carrots", "Vegetable Carrot"],
#     "Cauliflower": ["Cauliflower", "Cauliflowers", "Large Cauliflower", "Small Cauliflower", "Large Cauliflowers", "Small Cauliflowers", "Vegetable Cauliflower"],
#     "Cucumber": ["Cucumber", "Cucumbers", "Large Cucumber", "Small Cucumber", "Large Cucumbers", "Small Cucumbers", "Vegetable Cucumber"],
#     "Papaya": ["Papaya", "Papayas", "Large Papaya", "Small Papaya", "Large Papayas", "Small Papayas", "Vegetable Papaya"],
#     "Potato": ["Potato", "Potatoes", "Large Potato", "Small Potato", "Large Potatoes", "Small Potatoes", "Vegetable Potato"],
#     "Pumpkin": ["Pumpkin", "Pumpkins", "Large Pumpkin", "Small Pumpkin", "Large Pumpkins", "Small Pumpkins", "Vegetable Pumpkin"],
#     "Radish": ["Radish", "Radishes", "Large Radish", "Small Radish", "Large Radishes", "Small Radishes", "Vegetable Radish"],
#     "Tomato": ["Tomato", "Tomatoes", "Large Tomato", "Small Tomato", "Large Tomatoes", "Small Tomatoes", "Vegetable Tomato"]
# }

# # Bean, Beans, Large Bean, Small Bean, Large Beans, Small Beans, Vegetable Bean, Bitter Gourd, Bitter Gourds, Large Bitter Gourd, Small Bitter Gourd, Large Bitter Gourds, Small Bitter Gourds, Vegetable Bitter Gourd, Bottle Gourd, Bottle Gourds, Large Bottle Gourd, Small Bottle Gourd, Large Bottle Gourds, Small Bottle Gourds, Vegetable Bottle Gourd, Brinjal, Brinjals, Large Brinjal, Small Brinjal, Large Brinjals, Small Brinjals, Vegetable Brinjal, Cabbage, Cabbages, Large Cabbage, Small Cabbage, Large Cabbages, Small Cabbages, Vegetable Cabbage, Broccoli, Broccolis, Large Broccoli, Small Broccoli, Large Broccolis, Small Broccolis, Vegetable Broccoli, Capsicum, Capsicums, Large Capsicum, Small Capsicum, Large Capsicums, Small Capsicums, Vegetable Capsicum, Carrot, Carrots, Large Carrot, Small Carrot, Large Carrots, Small Carrots, Vegetable Carrot, Cauliflower, Cauliflowers, Large Cauliflower, Small Cauliflower, Large Cauliflowers, Small Cauliflowers, Vegetable Cauliflower, Cucumber, Cucumbers, Large Cucumber, Small Cucumber, Large Cucumbers, Small Cucumbers, Vegetable Cucumber, Papaya, Papayas, Large Papaya, Small Papaya, Large Papayas, Small Papayas, Vegetable Papaya, Potato, Potatoes, Large Potato, Small Potato, Large Potatoes, Small Potatoes, Vegetable Potato, Pumpkin, Pumpkins, Large Pumpkin, Small Pumpkin, Large Pumpkins, Small Pumpkins, Vegetable Pumpkin, Radish, Radishes, Large Radish, Small Radish, Large Radishes, Small Radishes, Vegetable Radish, Tomato, Tomatoes, Large Tomato, Small Tomato, Large Tomatoes, Small Tomatoes, Vegetable Tomato

# # dict_size(veg105)
# print(aOcheck_accuracy("WithoutIP/Vegetable15/veg105.csv", veg105))


# %% [markdown]
# ## Deck of Cards

# %%
cards4 = {
    "Clubs" : ["Card of Clubs"],
    "Diamonds" : ["Card of Diamonds"],
    "Hearts" : ["Card of Hearts"],
    "Spades" : ["Card of Spades"]
}

# Card of Clubs, Card of Diamonds, Card of Hearts, Card of Spades

# dict_size(cards4) 
# print(card_accuracy("Card15/cards4.csv", cards4))

# %%
cards8 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades"]
}

# # Card of Clubs, Image of Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Card of Hearts, Image of Card of Hearts, Card of Spades, Image of Card of Spades

# dict_size(cards8)
# print(card_accuracy("Card15/cards8.csv", cards8))


# %%
cards12 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades

# dict_size(cards12)
# print(card_accuracy("Card15/cards12.csv", cards12))


# %%
cards16 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades

# dict_size(cards16)
# print(card_accuracy("Card15/cards16.csv", cards16))


# %%
cards20 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades

# dict_size(cards20)
# print(card_accuracy("Card15/cards20.csv", cards20))


# %%
cards24 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs", "Vintage Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds", "Vintage Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts", "Vintage Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades", "Vintage Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Vintage Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Vintage Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Vintage Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades, Vintage Card of Spades

# dict_size(cards24)
# print(card_accuracy("Card15/cards24.csv", cards24))


# %%
cards28 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs", "Vintage Card of Clubs", "Royal Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds", "Vintage Card of Diamonds", "Royal Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts", "Vintage Card of Hearts", "Royal Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades", "Vintage Card of Spades", "Royal Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Vintage Card of Clubs, Royal Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Vintage Card of Diamonds, Royal Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Vintage Card of Hearts, Royal Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades, Vintage Card of Spades, Royal Card of Spades

# dict_size(cards28)
# print(card_accuracy("Card15/cards28.csv", cards28))


# %%
cards32 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs", "Vintage Card of Clubs", "Royal Card of Clubs", "Deluxe Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds", "Vintage Card of Diamonds", "Royal Card of Diamonds", "Deluxe Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts", "Vintage Card of Hearts", "Royal Card of Hearts", "Deluxe Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades", "Vintage Card of Spades", "Royal Card of Spades", "Deluxe Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Vintage Card of Clubs, Royal Card of Clubs, Deluxe Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Vintage Card of Diamonds, Royal Card of Diamonds, Deluxe Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Vintage Card of Hearts, Royal Card of Hearts, Deluxe Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades, Vintage Card of Spades, Royal Card of Spades, Deluxe Card of Spades

# dict_size(cards32)
# print(card_accuracy("Card15/cards32.csv", cards32))


# %%
cards36 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs", "Vintage Card of Clubs", "Royal Card of Clubs", "Deluxe Card of Clubs", "Exclusive Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds", "Vintage Card of Diamonds", "Royal Card of Diamonds", "Deluxe Card of Diamonds", "Exclusive Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts", "Vintage Card of Hearts", "Royal Card of Hearts", "Deluxe Card of Hearts", "Exclusive Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades", "Vintage Card of Spades", "Royal Card of Spades", "Deluxe Card of Spades", "Exclusive Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Vintage Card of Clubs, Royal Card of Clubs, Deluxe Card of Clubs, Exclusive Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Vintage Card of Diamonds, Royal Card of Diamonds, Deluxe Card of Diamonds, Exclusive Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Vintage Card of Hearts, Royal Card of Hearts, Deluxe Card of Hearts, Exclusive Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades, Vintage Card of Spades, Royal Card of Spades, Deluxe Card of Spades, Exclusive Card of Spades

# dict_size(cards36)
# print(card_accuracy("Card15/cards36.csv", cards36))


# %%
cards40 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs", "Vintage Card of Clubs", "Royal Card of Clubs", "Deluxe Card of Clubs", "Exclusive Card of Clubs", "Premium Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds", "Vintage Card of Diamonds", "Royal Card of Diamonds", "Deluxe Card of Diamonds", "Exclusive Card of Diamonds", "Premium Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts", "Vintage Card of Hearts", "Royal Card of Hearts", "Deluxe Card of Hearts", "Exclusive Card of Hearts", "Premium Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades", "Vintage Card of Spades", "Royal Card of Spades", "Deluxe Card of Spades", "Exclusive Card of Spades", "Premium Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Vintage Card of Clubs, Royal Card of Clubs, Deluxe Card of Clubs, Exclusive Card of Clubs, Premium Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Vintage Card of Diamonds, Royal Card of Diamonds, Deluxe Card of Diamonds, Exclusive Card of Diamonds, Premium Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Vintage Card of Hearts, Royal Card of Hearts, Deluxe Card of Hearts, Exclusive Card of Hearts, Premium Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades, Vintage Card of Spades, Royal Card of Spades, Deluxe Card of Spades, Exclusive Card of Spades, Premium Card of Spades

# dict_size(cards40)
# print(card_accuracy("Card15/cards40.csv", cards40))


# %%
cards44 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs", "Vintage Card of Clubs", "Royal Card of Clubs", "Deluxe Card of Clubs", "Exclusive Card of Clubs", "Premium Card of Clubs", "Elegant Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds", "Vintage Card of Diamonds", "Royal Card of Diamonds", "Deluxe Card of Diamonds", "Exclusive Card of Diamonds", "Premium Card of Diamonds", "Elegant Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts", "Vintage Card of Hearts", "Royal Card of Hearts", "Deluxe Card of Hearts", "Exclusive Card of Hearts", "Premium Card of Hearts", "Elegant Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades", "Vintage Card of Spades", "Royal Card of Spades", "Deluxe Card of Spades", "Exclusive Card of Spades", "Premium Card of Spades", "Elegant Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Vintage Card of Clubs, Royal Card of Clubs, Deluxe Card of Clubs, Exclusive Card of Clubs, Premium Card of Clubs, Elegant Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Vintage Card of Diamonds, Royal Card of Diamonds, Deluxe Card of Diamonds, Exclusive Card of Diamonds, Premium Card of Diamonds, Elegant Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Vintage Card of Hearts, Royal Card of Hearts, Deluxe Card of Hearts, Exclusive Card of Hearts, Premium Card of Hearts, Elegant Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades, Vintage Card of Spades, Royal Card of Spades, Deluxe Card of Spades, Exclusive Card of Spades, Premium Card of Spades, Elegant Card of Spades

# dict_size(cards44)
# print(card_accuracy("Card15/cards44.csv", cards44))


# %%
cards48 = {
    "Clubs": ["Card of Clubs", "Image of Card of Clubs", "Picture of Card of Clubs", "Poker Card of Clubs", "Classic Card of Clubs", "Vintage Card of Clubs", "Royal Card of Clubs", "Deluxe Card of Clubs", "Exclusive Card of Clubs", "Premium Card of Clubs", "Elegant Card of Clubs", "Prestige Card of Clubs"],
    "Diamonds": ["Card of Diamonds", "Image of Card of Diamonds", "Picture of Card of Diamonds", "Poker Card of Diamonds", "Classic Card of Diamonds", "Vintage Card of Diamonds", "Royal Card of Diamonds", "Deluxe Card of Diamonds", "Exclusive Card of Diamonds", "Premium Card of Diamonds", "Elegant Card of Diamonds", "Prestige Card of Diamonds"],
    "Hearts": ["Card of Hearts", "Image of Card of Hearts", "Picture of Card of Hearts", "Poker Card of Hearts", "Classic Card of Hearts", "Vintage Card of Hearts", "Royal Card of Hearts", "Deluxe Card of Hearts", "Exclusive Card of Hearts", "Premium Card of Hearts", "Elegant Card of Hearts", "Prestige Card of Hearts"],
    "Spades": ["Card of Spades", "Image of Card of Spades", "Picture of Card of Spades", "Poker Card of Spades", "Classic Card of Spades", "Vintage Card of Spades", "Royal Card of Spades", "Deluxe Card of Spades", "Exclusive Card of Spades", "Premium Card of Spades", "Elegant Card of Spades", "Prestige Card of Spades"]
}

# Card of Clubs, Image of Card of Clubs, Picture of Card of Clubs, Poker Card of Clubs, Classic Card of Clubs, Vintage Card of Clubs, Royal Card of Clubs, Deluxe Card of Clubs, Exclusive Card of Clubs, Premium Card of Clubs, Elegant Card of Clubs, Prestige Card of Clubs, Card of Diamonds, Image of Card of Diamonds, Picture of Card of Diamonds, Poker Card of Diamonds, Classic Card of Diamonds, Vintage Card of Diamonds, Royal Card of Diamonds, Deluxe Card of Diamonds, Exclusive Card of Diamonds, Premium Card of Diamonds, Elegant Card of Diamonds, Prestige Card of Diamonds, Card of Hearts, Image of Card of Hearts, Picture of Card of Hearts, Poker Card of Hearts, Classic Card of Hearts, Vintage Card of Hearts, Royal Card of Hearts, Deluxe Card of Hearts, Exclusive Card of Hearts, Premium Card of Hearts, Elegant Card of Hearts, Prestige Card of Hearts, Card of Spades, Image of Card of Spades, Picture of Card of Spades, Poker Card of Spades, Classic Card of Spades, Vintage Card of Spades, Royal Card of Spades, Deluxe Card of Spades, Exclusive Card of Spades, Premium Card of Spades, Elegant Card of Spades, Prestige Card of Spades

# dict_size(cards48)
# print(card_accuracy("Card15/cards48.csv", cards48))


# %% [markdown]
# ## Food 10

# %%
f10 = { "Baked Potato" : ["Baked Potato"],
       "Burger" : ["Burger"],
       "Crispy Chicken" : ["Crispy Chicken"],
       "Donut" : ["Donut"],
       "Fries" : ["Fries"],
       "Hot Dog" : ["Hot Dog"],
       "Pizza" : ["Pizza"],
       "Sandwich" : ["Sandwich"],
       "Taco" : ["Taco"],
       "Taquito" : ["Taquito"]}

# Baked Potato, Burger, Crispy Chicken, Donut, Fries, Hot Dog, Pizza, Sandwich, Taco, Taquito

# dict_size(f10)
print(aOcheck_accuracy("WithoutIP/food10/f10.csv", f10))

# %%
f20 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes"],
    "Burger": ["Burger", "Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens"],
    "Donut": ["Donut", "Donuts"],
    "Fries": ["Fries", "Fries"],  # Fries already plural
    "Hot Dog": ["Hot Dog", "Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches"],
    "Taco": ["Taco", "Tacos"],
    "Taquito": ["Taquito", "Taquitos"]
}

# Baked Potato, Baked Potatoes, Burger, Burgers, Crispy Chicken, Crispy Chickens, Donut, Donuts, Fries, Fries, Hot Dog, Hot Dogs, Pizza, Pizzas, Sandwich, Sandwiches, Taco, Tacos, Taquito, Taquitos

# dict_size(f20)
print(aOcheck_accuracy("WithoutIP/food10/f20.csv", f20))


# %%
f30 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato"],
    "Burger": ["Burger", "Burgers", "Large Burger"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut"],
    "Fries": ["Fries", "Fries", "Large Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Burger, Burgers, Large Burger, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Donut, Donuts, Large Donut, Fries, Fries, Large Fries, Hot Dog, Hot Dogs, Large Hot Dog, Pizza, Pizzas, Large Pizza, Sandwich, Sandwiches, Large Sandwich, Taco, Tacos, Large Taco, Taquito, Taquitos, Large Taquito

# dict_size(f30)
print(aOcheck_accuracy("WithoutIP/food10/f30.csv", f30))


# %%
f40 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Burger, Burgers, Large Burger, Large Burgers, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Fries, Fries, Large Fries, Large Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Pizza, Pizzas, Large Pizza, Large Pizzas, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos

# dict_size(f40)
print(aOcheck_accuracy("WithoutIP/food10/f40.csv", f40))


# %%
f50 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Fries, Fries, Large Fries, Large Fries, Small Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito

# dict_size(f50)
print(aOcheck_accuracy("WithoutIP/food10/f50.csv", f50))


# %%
f60 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos

# dict_size(f60)
print(aOcheck_accuracy("WithoutIP/food10/f60.csv", f60))


# %%
f70 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito

# dict_size(f70)
print(aOcheck_accuracy("WithoutIP/food10/f70.csv", f70))


# %%
f80 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries", "Medium Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Medium Burgers, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Medium Donuts, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Medium Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Medium Pizzas, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Medium Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Medium Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito, Medium Taquitos

# dict_size(f80)
print(aOcheck_accuracy("WithoutIP/food10/f80.csv", f80))


# %%
f90 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries", "Medium Fries", "Food Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Food Baked Potato, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Medium Burgers, Food Burger, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Food Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Medium Donuts, Food Donut, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Medium Fries, Food Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Food Hot Dog, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Medium Pizzas, Food Pizza, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Medium Sandwiches, Food Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Medium Tacos, Food Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito, Medium Taquitos, Food Taquito

# dict_size(f90)
print(aOcheck_accuracy("WithoutIP/food10/f90.csv", f90))


# %%
f100 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries", "Medium Fries", "Food Fries", "Food Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Medium Burgers, Food Burger, Food Burgers, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Medium Donuts, Food Donut, Food Donuts, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Medium Fries, Food Fries, Food Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Food Hot Dog, Food Hot Dogs, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Medium Pizzas, Food Pizza, Food Pizzas, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Medium Sandwiches, Food Sandwich, Food Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Medium Tacos, Food Taco, Food Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito, Medium Taquitos, Food Taquito, Food Taquitos

# dict_size(f100)
print(aOcheck_accuracy("WithoutIP/food10/f100.csv", f100))


# %%
f110 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries", "Medium Fries", "Food Fries", "Food Fries", "Edible Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Edible Baked Potato, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Medium Burgers, Food Burger, Food Burgers, Edible Burger, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Edible Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Medium Donuts, Food Donut, Food Donuts, Edible Donut, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Medium Fries, Food Fries, Food Fries, Edible Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Food Hot Dog, Food Hot Dogs, Edible Hot Dog, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Medium Pizzas, Food Pizza, Food Pizzas, Edible Pizza, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Medium Sandwiches, Food Sandwich, Food Sandwiches, Edible Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Medium Tacos, Food Taco, Food Tacos, Edible Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito, Medium Taquitos, Food Taquito, Food Taquitos, Edible Taquito

# dict_size(f110)
print(aOcheck_accuracy("WithoutIP/food10/f110.csv", f110))


# %%
f120 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato", "Edible Baked Potatoes"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger", "Edible Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken", "Edible Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut", "Edible Donuts"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries", "Medium Fries", "Food Fries", "Food Fries", "Edible Fries", "Edible Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog", "Edible Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza", "Edible Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich", "Edible Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco", "Edible Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito", "Edible Taquitos"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Edible Baked Potato, Edible Baked Potatoes, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Medium Burgers, Food Burger, Food Burgers, Edible Burger, Edible Burgers, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Edible Crispy Chicken, Edible Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Medium Donuts, Food Donut, Food Donuts, Edible Donut, Edible Donuts, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Medium Fries, Food Fries, Food Fries, Edible Fries, Edible Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Food Hot Dog, Food Hot Dogs, Edible Hot Dog, Edible Hot Dogs, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Medium Pizzas, Food Pizza, Food Pizzas, Edible Pizza, Edible Pizzas, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Medium Sandwiches, Food Sandwich, Food Sandwiches, Edible Sandwich, Edible Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Medium Tacos, Food Taco, Food Tacos, Edible Taco, Edible Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito, Medium Taquitos, Food Taquito, Food Taquitos, Edible Taquito, Edible Taquitos

# dict_size(f120)
print(aOcheck_accuracy("WithoutIP/food10/f120.csv", f120))


# %%
f130 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato", "Edible Baked Potatoes", "Tiny Baked Potato"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger", "Edible Burgers", "Tiny Burger"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken", "Edible Crispy Chickens", "Tiny Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut", "Edible Donuts", "Tiny Donut"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries", "Medium Fries", "Food Fries", "Food Fries", "Edible Fries", "Edible Fries", "Tiny Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog", "Edible Hot Dogs", "Tiny Hot Dog"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza", "Edible Pizzas", "Tiny Pizza"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich", "Edible Sandwiches", "Tiny Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco", "Edible Tacos", "Tiny Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito", "Edible Taquitos", "Tiny Taquito"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Edible Baked Potato, Edible Baked Potatoes, Tiny Baked Potato, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Medium Burgers, Food Burger, Food Burgers, Edible Burger, Edible Burgers, Tiny Burger, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Edible Crispy Chicken, Edible Crispy Chickens, Tiny Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Medium Donuts, Food Donut, Food Donuts, Edible Donut, Edible Donuts, Tiny Donut, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Medium Fries, Food Fries, Food Fries, Edible Fries, Edible Fries, Tiny Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Food Hot Dog, Food Hot Dogs, Edible Hot Dog, Edible Hot Dogs, Tiny Hot Dog, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Medium Pizzas, Food Pizza, Food Pizzas, Edible Pizza, Edible Pizzas, Tiny Pizza, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Medium Sandwiches, Food Sandwich, Food Sandwiches, Edible Sandwich, Edible Sandwiches, Tiny Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Medium Tacos, Food Taco, Food Tacos, Edible Taco, Edible Tacos, Tiny Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito, Medium Taquitos, Food Taquito, Food Taquitos, Edible Taquito, Edible Taquitos, Tiny Taquito

# dict_size(f130)
print(aOcheck_accuracy("WithoutIP/food10/f130.csv", f130))


# %%
f140 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato", "Edible Baked Potatoes", "Tiny Baked Potato", "Tiny Baked Potatoes"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger", "Edible Burgers", "Tiny Burger", "Tiny Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken", "Edible Crispy Chickens", "Tiny Crispy Chicken", "Tiny Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut", "Edible Donuts", "Tiny Donut", "Tiny Donuts"],
    "Fries": ["Fries", "Fries", "Large Fries", "Large Fries", "Small Fries", "Small Fries", "Medium Fries", "Medium Fries", "Food Fries", "Food Fries", "Edible Fries", "Edible Fries", "Tiny Fries", "Tiny Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog", "Edible Hot Dogs", "Tiny Hot Dog", "Tiny Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza", "Edible Pizzas", "Tiny Pizza", "Tiny Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich", "Edible Sandwiches", "Tiny Sandwich", "Tiny Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco", "Edible Tacos", "Tiny Taco", "Tiny Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito", "Edible Taquitos", "Tiny Taquito", "Tiny Taquitos"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Edible Baked Potato, Edible Baked Potatoes, Tiny Baked Potato, Tiny Baked Potatoes, Burger, Burgers, Large Burger, Large Burgers, Small Burger, Small Burgers, Medium Burger, Medium Burgers, Food Burger, Food Burgers, Edible Burger, Edible Burgers, Tiny Burger, Tiny Burgers, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Edible Crispy Chicken, Edible Crispy Chickens, Tiny Crispy Chicken, Tiny Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Medium Donut, Medium Donuts, Food Donut, Food Donuts, Edible Donut, Edible Donuts, Tiny Donut, Tiny Donuts, Fries, Fries, Large Fries, Large Fries, Small Fries, Small Fries, Medium Fries, Medium Fries, Food Fries, Food Fries, Edible Fries, Edible Fries, Tiny Fries, Tiny Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Food Hot Dog, Food Hot Dogs, Edible Hot Dog, Edible Hot Dogs, Tiny Hot Dog, Tiny Hot Dogs, Pizza, Pizzas, Large Pizza, Large Pizzas, Small Pizza, Small Pizzas, Medium Pizza, Medium Pizzas, Food Pizza, Food Pizzas, Edible Pizza, Edible Pizzas, Tiny Pizza, Tiny Pizzas, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Medium Sandwich, Medium Sandwiches, Food Sandwich, Food Sandwiches, Edible Sandwich, Edible Sandwiches, Tiny Sandwich, Tiny Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Medium Taco, Medium Tacos, Food Taco, Food Tacos, Edible Taco, Edible Tacos, Tiny Taco, Tiny Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Medium Taquito, Medium Taquitos, Food Taquito, Food Taquitos, Edible Taquito, Edible Taquitos, Tiny Taquito, Tiny Taquitos

# dict_size(f140)
print(aOcheck_accuracy("WithoutIP/food10/f140.csv", f140))


# %%
f150 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato", "Edible Baked Potatoes", "Tiny Baked Potato", "Tiny Baked Potatoes", "Giant Baked Potato"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger", "Edible Burgers", "Tiny Burger", "Tiny Burgers", "Giant Burger"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken", "Edible Crispy Chickens", "Tiny Crispy Chicken", "Tiny Crispy Chickens", "Giant Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut", "Edible Donuts", "Tiny Donut", "Tiny Donuts", "Giant Donut"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Medium Fries", "Medium Fry", "Food Fries", "Food Fry", "Edible Fries", "Edible Fry", "Tiny Fries", "Tiny Fry", "Giant Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog", "Edible Hot Dogs", "Tiny Hot Dog", "Tiny Hot Dogs", "Giant Hot Dog"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza", "Edible Pizzas", "Tiny Pizza", "Tiny Pizzas", "Giant Pizza"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich", "Edible Sandwiches", "Tiny Sandwich", "Tiny Sandwiches", "Giant Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco", "Edible Tacos", "Tiny Taco", "Tiny Tacos", "Giant Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito", "Edible Taquitos", "Tiny Taquito", "Tiny Taquitos", "Giant Taquito"]
}

# baked potato, baked potatoes, large baked potato, large baked potatoes, small baked potato, small baked potatoes, medium baked potato, medium baked potatoes, food baked potato, food baked potatoes, edible baked potato, edible baked potatoes, tiny baked potato, tiny baked potatoes, giant baked potato, burger, burgers, large burger, large burgers, small burger, small burgers, medium burger, medium burgers, food burger, food burgers, edible burger, edible burgers, tiny burger, tiny burgers, giant burger, crispy chicken, crispy chickens, large crispy chicken, large crispy chickens, small crispy chicken, small crispy chickens, medium crispy chicken, medium crispy chickens, food crispy chicken, food crispy chickens, edible crispy chicken, edible crispy chickens, tiny crispy chicken, tiny crispy chickens, giant crispy chicken, donut, donuts, large donut, large donuts, small donut, small donuts, medium donut, medium donuts, food donut, food donuts, edible donut, edible donuts, tiny donut, tiny donuts, giant donut, fries, fry, large fries, large fry, small fries, small fry, medium fries, medium fry, food fries, food fry, edible fries, edible fry, tiny fries, tiny fry, giant fries, hot dog, hot dogs, large hot dog, large hot dogs, small hot dog, small hot dogs, medium hot dog, medium hot dogs, food hot dog, food hot dogs, edible hot dog, edible hot dogs, tiny hot dog, tiny hot dogs, giant hot dog, pizza, pizzas, large pizza, large pizzas, small pizza, small pizzas, medium pizza, medium pizzas, food pizza, food pizzas, edible pizza, edible pizzas, tiny pizza, tiny pizzas, giant pizza, sandwich, sandwiches, large sandwich, large sandwiches, small sandwich, small sandwiches, medium sandwich, medium sandwiches, food sandwich, food sandwiches, edible sandwich, edible sandwiches, tiny sandwich, tiny sandwiches, giant sandwich, taco, tacos, large taco, large tacos, small taco, small tacos, medium taco, medium tacos, food taco, food tacos, edible taco, edible tacos, tiny taco, tiny tacos, giant taco, taquito, taquitos, large taquito, large taquitos, small taquito, small taquitos, medium taquito, medium taquitos, food taquito, food taquitos, edible taquito, edible taquitos, tiny taquito, tiny taquitos, giant taquito

# dict_size(f150)
print(aOcheck_accuracy("WithoutIP/food10/f150.csv", f150))

# %%
f160 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato", "Edible Baked Potatoes", "Tiny Baked Potato", "Tiny Baked Potatoes", "Giant Baked Potato", "Giant Baked Potatoes"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger", "Edible Burgers", "Tiny Burger", "Tiny Burgers", "Giant Burger", "Giant Burgers"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken", "Edible Crispy Chickens", "Tiny Crispy Chicken", "Tiny Crispy Chickens", "Giant Crispy Chicken", "Giant Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut", "Edible Donuts", "Tiny Donut", "Tiny Donuts", "Giant Donut", "Giant Donuts"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Medium Fries", "Medium Fry", "Food Fries", "Food Fry", "Edible Fries", "Edible Fry", "Tiny Fries", "Tiny Fry", "Giant Fries", "Giant Fry"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog", "Edible Hot Dogs", "Tiny Hot Dog", "Tiny Hot Dogs", "Giant Hot Dog", "Giant Hot Dogs"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza", "Edible Pizzas", "Tiny Pizza", "Tiny Pizzas", "Giant Pizza", "Giant Pizzas"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich", "Edible Sandwiches", "Tiny Sandwich", "Tiny Sandwiches", "Giant Sandwich", "Giant Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco", "Edible Tacos", "Tiny Taco", "Tiny Tacos", "Giant Taco", "Giant Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito", "Edible Taquitos", "Tiny Taquito", "Tiny Taquitos", "Giant Taquito", "Giant Taquitos"]
}

# baked potato, baked potatoes, large baked potato, large baked potatoes, small baked potato, small baked potatoes, medium baked potato, medium baked potatoes, food baked potato, food baked potatoes, edible baked potato, edible baked potatoes, tiny baked potato, tiny baked potatoes, giant baked potato, giant baked potatoes, burger, burgers, large burger, large burgers, small burger, small burgers, medium burger, medium burgers, food burger, food burgers, edible burger, edible burgers, tiny burger, tiny burgers, giant burger, giant burgers, crispy chicken, crispy chickens, large crispy chicken, large crispy chickens, small crispy chicken, small crispy chickens, medium crispy chicken, medium crispy chickens, food crispy chicken, food crispy chickens, edible crispy chicken, edible crispy chickens, tiny crispy chicken, tiny crispy chickens, giant crispy chicken, giant crispy chickens, donut, donuts, large donut, large donuts, small donut, small donuts, medium donut, medium donuts, food donut, food donuts, edible donut, edible donuts, tiny donut, tiny donuts, giant donut, giant donuts, fries, fry, large fries, large fry, small fries, small fry, medium fries, medium fry, food fries, food fry, edible fries, edible fry, tiny fries, tiny fry, giant fries, giant fry, hot dog, hot dogs, large hot dog, large hot dogs, small hot dog, small hot dogs, medium hot dog, medium hot dogs, food hot dog, food hot dogs, edible hot dog, edible hot dogs, tiny hot dog, tiny hot dogs, giant hot dog, giant hot dogs, pizza, pizzas, large pizza, large pizzas, small pizza, small pizzas, medium pizza, medium pizzas, food pizza, food pizzas, edible pizza, edible pizzas, tiny pizza, tiny pizzas, giant pizza, giant pizzas, sandwich, sandwiches, large sandwich, large sandwiches, small sandwich, small sandwiches, medium sandwich, medium sandwiches, food sandwich, food sandwiches, edible sandwich, edible sandwiches, tiny sandwich, tiny sandwiches, giant sandwich, giant sandwiches, taco, tacos, large taco, large tacos, small taco, small tacos, medium taco, medium tacos, food taco, food tacos, edible taco, edible tacos, tiny taco, tiny tacos, giant taco, giant tacos, taquito, taquitos, large taquito, large taquitos, small taquito, small taquitos, medium taquito, medium taquitos, food taquito, food taquitos, edible taquito, edible taquitos, tiny taquito, tiny taquitos, giant taquito, giant taquitos

# dict_size(f160)
print(aOcheck_accuracy("WithoutIP/food10/f160.csv", f160))

# %%
fx170 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato", "Edible Baked Potatoes", "Tiny Baked Potato", "Tiny Baked Potatoes", "Giant Baked Potato", "Giant Baked Potatoes", "Baked Potato Food"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger", "Edible Burgers", "Tiny Burger", "Tiny Burgers", "Giant Burger", "Giant Burgers", "Burger Food"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken", "Edible Crispy Chickens", "Tiny Crispy Chicken", "Tiny Crispy Chickens", "Giant Crispy Chicken", "Giant Crispy Chickens", "Crispy Chicken Food"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut", "Edible Donuts", "Tiny Donut", "Tiny Donuts", "Giant Donut", "Giant Donuts", "Donut Food"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Medium Fries", "Medium Fry", "Food Fries", "Food Fry", "Edible Fries", "Edible Fry", "Tiny Fries", "Tiny Fry", "Giant Fries", "Giant Fry", "Fries Food"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog", "Edible Hot Dogs", "Tiny Hot Dog", "Tiny Hot Dogs", "Giant Hot Dog", "Giant Hot Dogs", "Hot Dog Food"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza", "Edible Pizzas", "Tiny Pizza", "Tiny Pizzas", "Giant Pizza", "Giant Pizzas", "Pizza Food"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich", "Edible Sandwiches", "Tiny Sandwich", "Tiny Sandwiches", "Giant Sandwich", "Giant Sandwiches", "Sandwich Food"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco", "Edible Tacos", "Tiny Taco", "Tiny Tacos", "Giant Taco", "Giant Tacos", "Taco Food"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito", "Edible Taquitos", "Tiny Taquito", "Tiny Taquitos", "Giant Taquito", "Giant Taquitos", "Taquito Food"]
}

# baked potato, baked potatoes, large baked potato, large baked potatoes, small baked potato, small baked potatoes, medium baked potato, medium baked potatoes, food baked potato, food baked potatoes, edible baked potato, edible baked potatoes, tiny baked potato, tiny baked potatoes, giant baked potato, giant baked potatoes, baked potato food, burger, burgers, large burger, large burgers, small burger, small burgers, medium burger, medium burgers, food burger, food burgers, edible burger, edible burgers, tiny burger, tiny burgers, giant burger, giant burgers, burger food, crispy chicken, crispy chickens, large crispy chicken, large crispy chickens, small crispy chicken, small crispy chickens, medium crispy chicken, medium crispy chickens, food crispy chicken, food crispy chickens, edible crispy chicken, edible crispy chickens, tiny crispy chicken, tiny crispy chickens, giant crispy chicken, giant crispy chickens, crispy chicken food, donut, donuts, large donut, large donuts, small donut, small donuts, medium donut, medium donuts, food donut, food donuts, edible donut, edible donuts, tiny donut, tiny donuts, giant donut, giant donuts, donut food, fries, fry, large fries, large fry, small fries, small fry, medium fries, medium fry, food fries, food fry, edible fries, edible fry, tiny fries, tiny fry, giant fries, giant fry, fries food, hot dog, hot dogs, large hot dog, large hot dogs, small hot dog, small hot dogs, medium hot dog, medium hot dogs, food hot dog, food hot dogs, edible hot dog, edible hot dogs, tiny hot dog, tiny hot dogs, giant hot dog, giant hot dogs, hot dog food, pizza, pizzas, large pizza, large pizzas, small pizza, small pizzas, medium pizza, medium pizzas, food pizza, food pizzas, edible pizza, edible pizzas, tiny pizza, tiny pizzas, giant pizza, giant pizzas, pizza food, sandwich, sandwiches, large sandwich, large sandwiches, small sandwich, small sandwiches, medium sandwich, medium sandwiches, food sandwich, food sandwiches, edible sandwich, edible sandwiches, tiny sandwich, tiny sandwiches, giant sandwich, giant sandwiches, sandwich food, taco, tacos, large taco, large tacos, small taco, small tacos, medium taco, medium tacos, food taco, food tacos, edible taco, edible tacos, tiny taco, tiny tacos, giant taco, giant tacos, taco food, taquito, taquitos, large taquito, large taquitos, small taquito, small taquitos, medium taquito, medium taquitos, food taquito, food taquitos, edible taquito, edible taquitos, tiny taquito, tiny taquitos, giant taquito, giant taquitos, taquito food

# dict_size(fx170)
print(aOcheck_accuracy("WithoutIP/food10/f170.csv", fx170))


# %%
f180 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Edible Baked Potato", "Edible Baked Potatoes", "Tiny Baked Potato", "Tiny Baked Potatoes", "Giant Baked Potato", "Giant Baked Potatoes", "Baked Potato Food", "Baked Potatoes Food"],
    "Burger": ["Burger", "Burgers", "Large Burger", "Large Burgers", "Small Burger", "Small Burgers", "Medium Burger", "Medium Burgers", "Food Burger", "Food Burgers", "Edible Burger", "Edible Burgers", "Tiny Burger", "Tiny Burgers", "Giant Burger", "Giant Burgers", "Burger Food", "Burgers Food"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Edible Crispy Chicken", "Edible Crispy Chickens", "Tiny Crispy Chicken", "Tiny Crispy Chickens", "Giant Crispy Chicken", "Giant Crispy Chickens", "Crispy Chicken Food", "Crispy Chickens Food"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Medium Donut", "Medium Donuts", "Food Donut", "Food Donuts", "Edible Donut", "Edible Donuts", "Tiny Donut", "Tiny Donuts", "Giant Donut", "Giant Donuts", "Donut Food", "Donuts Food"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Medium Fries", "Medium Fry", "Food Fries", "Food Fry", "Edible Fries", "Edible Fry", "Tiny Fries", "Tiny Fry", "Giant Fries", "Giant Fry", "Fries Food", "Fry Food"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Edible Hot Dog", "Edible Hot Dogs", "Tiny Hot Dog", "Tiny Hot Dogs", "Giant Hot Dog", "Giant Hot Dogs", "Hot Dog Food", "Hot Dogs Food"],
    "Pizza": ["Pizza", "Pizzas", "Large Pizza", "Large Pizzas", "Small Pizza", "Small Pizzas", "Medium Pizza", "Medium Pizzas", "Food Pizza", "Food Pizzas", "Edible Pizza", "Edible Pizzas", "Tiny Pizza", "Tiny Pizzas", "Giant Pizza", "Giant Pizzas", "Pizza Food", "Pizzas Food"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Food Sandwich", "Food Sandwiches", "Edible Sandwich", "Edible Sandwiches", "Tiny Sandwich", "Tiny Sandwiches", "Giant Sandwich", "Giant Sandwiches", "Sandwich Food", "Sandwiches Food"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Medium Taco", "Medium Tacos", "Food Taco", "Food Tacos", "Edible Taco", "Edible Tacos", "Tiny Taco", "Tiny Tacos", "Giant Taco", "Giant Tacos", "Taco Food", "Tacos Food"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Medium Taquito", "Medium Taquitos", "Food Taquito", "Food Taquitos", "Edible Taquito", "Edible Taquitos", "Tiny Taquito", "Tiny Taquitos", "Giant Taquito", "Giant Taquitos", "Taquito Food", "Taquitos Food"]
}

# baked potato, baked potatoes, large baked potato, large baked potatoes, small baked potato, small baked potatoes, medium baked potato, medium baked potatoes, food baked potato, food baked potatoes, edible baked potato, edible baked potatoes, tiny baked potato, tiny baked potatoes, giant baked potato, giant baked potatoes, baked potato food, baked potatoes food, burger, burgers, large burger, large burgers, small burger, small burgers, medium burger, medium burgers, food burger, food burgers, edible burger, edible burgers, tiny burger, tiny burgers, giant burger, giant burgers, burger food, burgers food, crispy chicken, crispy chickens, large crispy chicken, large crispy chickens, small crispy chicken, small crispy chickens, medium crispy chicken, medium crispy chickens, food crispy chicken, food crispy chickens, edible crispy chicken, edible crispy chickens, tiny crispy chicken, tiny crispy chickens, giant crispy chicken, giant crispy chickens, crispy chicken food, crispy chickens food, donut, donuts, large donut, large donuts, small donut, small donuts, medium donut, medium donuts, food donut, food donuts, edible donut, edible donuts, tiny donut, tiny donuts, giant donut, giant donuts, donut food, donuts food, fries, fry, large fries, large fry, small fries, small fry, medium fries, medium fry, food fries, food fry, edible fries, edible fry, tiny fries, tiny fry, giant fries, giant fry, fries food, fry food, hot dog, hot dogs, large hot dog, large hot dogs, small hot dog, small hot dogs, medium hot dog, medium hot dogs, food hot dog, food hot dogs, edible hot dog, edible hot dogs, tiny hot dog, tiny hot dogs, giant hot dog, giant hot dogs, hot dog food, hot dogs food, pizza, pizzas, large pizza, large pizzas, small pizza, small pizzas, medium pizza, medium pizzas, food pizza, food pizzas, edible pizza, edible pizzas, tiny pizza, tiny pizzas, giant pizza, giant pizzas, pizza food, pizzas food, sandwich, sandwiches, large sandwich, large sandwiches, small sandwich, small sandwiches, medium sandwich, medium sandwiches, food sandwich, food sandwiches, edible sandwich, edible sandwiches, tiny sandwich, tiny sandwiches, giant sandwich, giant sandwiches, sandwich food, sandwiches food, taco, tacos, large taco, large tacos, small taco, small tacos, medium taco, medium tacos, food taco, food tacos, edible taco, edible tacos, tiny taco, tiny tacos, giant taco, giant tacos, taco food, tacos food, taquito, taquitos, large taquito, large taquitos, small taquito, small taquitos, medium taquito, medium taquitos, food taquito, food taquitos, edible taquito, edible taquitos, tiny taquito, tiny taquitos, giant taquito, giant taquitos, taquito food, taquitos food

# dict_size(f180)
print(aOcheck_accuracy("WithoutIP/food10/f180.csv", f180))

# %% [markdown]
# ## Vehicles 20

# %%
v20 = {
    "car": ["car"],
    "motorcycle": ["motorcycle"],
    "bicycle": ["bicycle"],
    "truck": ["truck"],
    "bus": ["bus"],
    "van": ["van"],
    "rickshaw": ["rickshaw"],
    "scooter": ["scooter"],
    "skateboard": ["skateboard"],
    "ambulance": ["ambulance"],
    "fire truck": ["fire truck"],
    "tractor": ["tractor"],
    "segway": ["segway"],
    "unicycle": ["unicycle"],
    "jet ski": ["jet ski"],
    "helicopter": ["helicopter"],
    "airplane": ["airplane"],
    "boat": ["boat"],
    "kayak": ["kayak"],
    "hovercraft" : ["hovercraft"]
}

# car,motorcycle, bicycle,truck,bus,van,rickshaw,scooter,skateboard,ambulance,fire truck,tractor,segway,unicycle,jet ski,helicopter,airplane,boat,kayak, hovercraft

# dict_size(v20)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v20.csv", v20))

# %%
v40 = {
    "car": ["car", "cars"],
    "motorcycle": ["motorcycle", "motorcycles"],
    "bicycle": ["bicycle", "bicycles"],
    "truck": ["truck", "trucks"],
    "bus": ["bus", "buses"],
    "van": ["van", "vans"],
    "rickshaw": ["rickshaw", "rickshaws"],
    "scooter": ["scooter", "scooters"],
    "skateboard": ["skateboard", "skateboards"],
    "ambulance": ["ambulance", "ambulances"],
    "fire truck": ["fire truck", "fire trucks"],
    "tractor": ["tractor", "tractors"],
    "segway": ["segway", "segways"],
    "unicycle": ["unicycle", "unicycles"],
    "jet ski": ["jet ski", "jet skis"],
    "helicopter": ["helicopter", "helicopters"],
    "airplane": ["airplane", "airplanes"],
    "boat": ["boat", "boats"],
    "kayak": ["kayak", "kayaks"],
    "hovercraft": ["hovercraft", "hovercrafts"]
}

# car, cars, motorcycle, motorcycles, bicycle, bicycles, truck, trucks, bus, buses, van, vans, rickshaw, rickshaws, scooter, scooters, skateboard, skateboards, ambulance, ambulances, fire truck, fire trucks, tractor, tractors, segway, segways, unicycle, unicycles, jet ski, jet skis, helicopter, helicopters, airplane, airplanes, boat, boats, kayak, kayaks, hovercraft, hovercrafts

# dict_size(v40)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v40.csv", v40))


# %%
v60 = {
    "car": ["car", "cars", "Large car"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle"],
    "truck": ["truck", "trucks", "Large truck"],
    "bus": ["bus", "buses", "Large bus"],
    "van": ["van", "vans", "Large van"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw"],
    "scooter": ["scooter", "scooters", "Large scooter"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck"],
    "tractor": ["tractor", "tractors", "Large tractor"],
    "segway": ["segway", "segways", "Large segway"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter"],
    "airplane": ["airplane", "airplanes", "Large airplane"],
    "boat": ["boat", "boats", "Large boat"],
    "kayak": ["kayak", "kayaks", "Large kayak"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft"]
}

# car, cars, Large car, motorcycle, motorcycles, Large motorcycle, bicycle, bicycles, Large bicycle, truck, trucks, Large truck, bus, buses, Large bus, van, vans, Large van, rickshaw, rickshaws, Large rickshaw, scooter, scooters, Large scooter, skateboard, skateboards, Large skateboard, ambulance, ambulances, Large ambulance, fire truck, fire trucks, Large fire truck, tractor, tractors, Large tractor, segway, segways, Large segway, unicycle, unicycles, Large unicycle, jet ski, jet skis, Large jet ski, helicopter, helicopters, Large helicopter, airplane, airplanes, Large airplane, boat, boats, Large boat, kayak, kayaks, Large kayak, hovercraft, hovercrafts, Large hovercraft

# dict_size(v60)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v60.csv", v60))


# %%
v80 = {
    "car": ["car", "cars", "Large car", "Large cars"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle", "Large motorcycles"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle", "Large bicycles"],
    "truck": ["truck", "trucks", "Large truck", "Large trucks"],
    "bus": ["bus", "buses", "Large bus", "Large buses"],
    "van": ["van", "vans", "Large van", "Large vans"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw", "Large rickshaws"],
    "scooter": ["scooter", "scooters", "Large scooter", "Large scooters"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard", "Large skateboards"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance", "Large ambulances"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck", "Large fire trucks"],
    "tractor": ["tractor", "tractors", "Large tractor", "Large tractors"],
    "segway": ["segway", "segways", "Large segway", "Large segways"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle", "Large unicycles"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski", "Large jet skis"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter", "Large helicopters"],
    "airplane": ["airplane", "airplanes", "Large airplane", "Large airplanes"],
    "boat": ["boat", "boats", "Large boat", "Large boats"],
    "kayak": ["kayak", "kayaks", "Large kayak", "Large kayaks"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft", "Large hovercrafts"]
}

# car, cars, Large car, Large cars, motorcycle, motorcycles, Large motorcycle, Large motorcycles, bicycle, bicycles, Large bicycle, Large bicycles, truck, trucks, Large truck, Large trucks, bus, buses, Large bus, Large buses, van, vans, Large van, Large vans, rickshaw, rickshaws, Large rickshaw, Large rickshaws, scooter, scooters, Large scooter, Large scooters, skateboard, skateboards, Large skateboard, Large skateboards, ambulance, ambulances, Large ambulance, Large ambulances, fire truck, fire trucks, Large fire truck, Large fire trucks, tractor, tractors, Large tractor, Large tractors, segway, segways, Large segway, Large segways, unicycle, unicycles, Large unicycle, Large unicycles, jet ski, jet skis, Large jet ski, Large jet skis, helicopter, helicopters, Large helicopter, Large helicopters, airplane, airplanes, Large airplane, Large airplanes, boat, boats, Large boat, Large boats, kayak, kayaks, Large kayak, Large kayaks, hovercraft, hovercrafts, Large hovercraft, Large hovercrafts

# dict_size(v80)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v80.csv", v80))


# %%
v100 = {
    "car": ["car", "cars", "Large car", "Large cars", "Small car"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle", "Large motorcycles", "Small motorcycle"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle", "Large bicycles", "Small bicycle"],
    "truck": ["truck", "trucks", "Large truck", "Large trucks", "Small truck"],
    "bus": ["bus", "buses", "Large bus", "Large buses", "Small bus"],
    "van": ["van", "vans", "Large van", "Large vans", "Small van"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw", "Large rickshaws", "Small rickshaw"],
    "scooter": ["scooter", "scooters", "Large scooter", "Large scooters", "Small scooter"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard", "Large skateboards", "Small skateboard"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance", "Large ambulances", "Small ambulance"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck", "Large fire trucks", "Small fire truck"],
    "tractor": ["tractor", "tractors", "Large tractor", "Large tractors", "Small tractor"],
    "segway": ["segway", "segways", "Large segway", "Large segways", "Small segway"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle", "Large unicycles", "Small unicycle"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski", "Large jet skis", "Small jet ski"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter", "Large helicopters", "Small helicopter"],
    "airplane": ["airplane", "airplanes", "Large airplane", "Large airplanes", "Small airplane"],
    "boat": ["boat", "boats", "Large boat", "Large boats", "Small boat"],
    "kayak": ["kayak", "kayaks", "Large kayak", "Large kayaks", "Small kayak"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft", "Large hovercrafts", "Small hovercraft"]
}

# car, cars, Large car, Large cars, Small car, motorcycle, motorcycles, Large motorcycle, Large motorcycles, Small motorcycle, bicycle, bicycles, Large bicycle, Large bicycles, Small bicycle, truck, trucks, Large truck, Large trucks, Small truck, bus, buses, Large bus, Large buses, Small bus, van, vans, Large van, Large vans, Small van, rickshaw, rickshaws, Large rickshaw, Large rickshaws, Small rickshaw, scooter, scooters, Large scooter, Large scooters, Small scooter, skateboard, skateboards, Large skateboard, Large skateboards, Small skateboard, ambulance, ambulances, Large ambulance, Large ambulances, Small ambulance, fire truck, fire trucks, Large fire truck, Large fire trucks, Small fire truck, tractor, tractors, Large tractor, Large tractors, Small tractor, segway, segways, Large segway, Large segways, Small segway, unicycle, unicycles, Large unicycle, Large unicycles, Small unicycle, jet ski, jet skis, Large jet ski, Large jet skis, Small jet ski, helicopter, helicopters, Large helicopter, Large helicopters, Small helicopter, airplane, airplanes, Large airplane, Large airplanes, Small airplane, boat, boats, Large boat, Large boats, Small boat, kayak, kayaks, Large kayak, Large kayaks, Small kayak, hovercraft, hovercrafts, Large hovercraft, Large hovercrafts, Small hovercraft

# dict_size(v100)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v100.csv", v100))


# %%
v120 = {
    "car": ["car", "cars", "Large car", "Large cars", "Small car", "Small cars"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle", "Large motorcycles", "Small motorcycle", "Small motorcycles"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle", "Large bicycles", "Small bicycle", "Small bicycles"],
    "truck": ["truck", "trucks", "Large truck", "Large trucks", "Small truck", "Small trucks"],
    "bus": ["bus", "buses", "Large bus", "Large buses", "Small bus", "Small buses"],
    "van": ["van", "vans", "Large van", "Large vans", "Small van", "Small vans"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw", "Large rickshaws", "Small rickshaw", "Small rickshaws"],
    "scooter": ["scooter", "scooters", "Large scooter", "Large scooters", "Small scooter", "Small scooters"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard", "Large skateboards", "Small skateboard", "Small skateboards"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance", "Large ambulances", "Small ambulance", "Small ambulances"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck", "Large fire trucks", "Small fire truck", "Small fire trucks"],
    "tractor": ["tractor", "tractors", "Large tractor", "Large tractors", "Small tractor", "Small tractors"],
    "segway": ["segway", "segways", "Large segway", "Large segways", "Small segway", "Small segways"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle", "Large unicycles", "Small unicycle", "Small unicycles"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski", "Large jet skis", "Small jet ski", "Small jet skis"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter", "Large helicopters", "Small helicopter", "Small helicopters"],
    "airplane": ["airplane", "airplanes", "Large airplane", "Large airplanes", "Small airplane", "Small airplanes"],
    "boat": ["boat", "boats", "Large boat", "Large boats", "Small boat", "Small boats"],
    "kayak": ["kayak", "kayaks", "Large kayak", "Large kayaks", "Small kayak", "Small kayaks"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft", "Large hovercrafts", "Small hovercraft", "Small hovercrafts"]
}

# car, cars, Large car, Large cars, Small car, Small cars, motorcycle, motorcycles, Large motorcycle, Large motorcycles, Small motorcycle, Small motorcycles, bicycle, bicycles, Large bicycle, Large bicycles, Small bicycle, Small bicycles, truck, trucks, Large truck, Large trucks, Small truck, Small trucks, bus, buses, Large bus, Large buses, Small bus, Small buses, van, vans, Large van, Large vans, Small van, Small vans, rickshaw, rickshaws, Large rickshaw, Large rickshaws, Small rickshaw, Small rickshaws, scooter, scooters, Large scooter, Large scooters, Small scooter, Small scooters, skateboard, skateboards, Large skateboard, Large skateboards, Small skateboard, Small skateboards, ambulance, ambulances, Large ambulance, Large ambulances, Small ambulance, Small ambulances, fire truck, fire trucks, Large fire truck, Large fire trucks, Small fire truck, Small fire trucks, tractor, tractors, Large tractor, Large tractors, Small tractor, Small tractors, segway, segways, Large segway, Large segways, Small segway, Small segways, unicycle, unicycles, Large unicycle, Large unicycles, Small unicycle, Small unicycles, jet ski, jet skis, Large jet ski, Large jet skis, Small jet ski, Small jet skis, helicopter, helicopters, Large helicopter, Large helicopters, Small helicopter, Small helicopters, airplane, airplanes, Large airplane, Large airplanes, Small airplane, Small airplanes, boat, boats, Large boat, Large boats, Small boat, Small boats, kayak, kayaks, Large kayak, Large kayaks, Small kayak, Small kayaks, hovercraft, hovercrafts, Large hovercraft, Large hovercrafts, Small hovercraft, Small hovercrafts

# dict_size(v120)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v120.csv", v120))


# %%
v140 = {
    "car": ["car", "cars", "Large car", "Large cars", "Small car", "Small cars", "Mid-Sized car"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle", "Large motorcycles", "Small motorcycle", "Small motorcycles", "Mid-Sized motorcycle"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle", "Large bicycles", "Small bicycle", "Small bicycles", "Mid-Sized bicycle"],
    "truck": ["truck", "trucks", "Large truck", "Large trucks", "Small truck", "Small trucks", "Mid-Sized truck"],
    "bus": ["bus", "buses", "Large bus", "Large buses", "Small bus", "Small buses", "Mid-Sized bus"],
    "van": ["van", "vans", "Large van", "Large vans", "Small van", "Small vans", "Mid-Sized van"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw", "Large rickshaws", "Small rickshaw", "Small rickshaws", "Mid-Sized rickshaw"],
    "scooter": ["scooter", "scooters", "Large scooter", "Large scooters", "Small scooter", "Small scooters", "Mid-Sized scooter"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard", "Large skateboards", "Small skateboard", "Small skateboards", "Mid-Sized skateboard"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance", "Large ambulances", "Small ambulance", "Small ambulances", "Mid-Sized ambulance"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck", "Large fire trucks", "Small fire truck", "Small fire trucks", "Mid-Sized fire truck"],
    "tractor": ["tractor", "tractors", "Large tractor", "Large tractors", "Small tractor", "Small tractors", "Mid-Sized tractor"],
    "segway": ["segway", "segways", "Large segway", "Large segways", "Small segway", "Small segways", "Mid-Sized segway"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle", "Large unicycles", "Small unicycle", "Small unicycles", "Mid-Sized unicycle"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski", "Large jet skis", "Small jet ski", "Small jet skis", "Mid-Sized jet ski"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter", "Large helicopters", "Small helicopter", "Small helicopters", "Mid-Sized helicopter"],
    "airplane": ["airplane", "airplanes", "Large airplane", "Large airplanes", "Small airplane", "Small airplanes", "Mid-Sized airplane"],
    "boat": ["boat", "boats", "Large boat", "Large boats", "Small boat", "Small boats", "Mid-Sized boat"],
    "kayak": ["kayak", "kayaks", "Large kayak", "Large kayaks", "Small kayak", "Small kayaks", "Mid-Sized kayak"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft", "Large hovercrafts", "Small hovercraft", "Small hovercrafts", "Mid-Sized hovercraft"]
}

# car, cars, Large car, Large cars, Small car, Small cars, Mid-Sized car, motorcycle, motorcycles, Large motorcycle, Large motorcycles, Small motorcycle, Small motorcycles, Mid-Sized motorcycle, bicycle, bicycles, Large bicycle, Large bicycles, Small bicycle, Small bicycles, Mid-Sized bicycle, truck, trucks, Large truck, Large trucks, Small truck, Small trucks, Mid-Sized truck, bus, buses, Large bus, Large buses, Small bus, Small buses, Mid-Sized bus, van, vans, Large van, Large vans, Small van, Small vans, Mid-Sized van, rickshaw, rickshaws, Large rickshaw, Large rickshaws, Small rickshaw, Small rickshaws, Mid-Sized rickshaw, scooter, scooters, Large scooter, Large scooters, Small scooter, Small scooters, Mid-Sized scooter, skateboard, skateboards, Large skateboard, Large skateboards, Small skateboard, Small skateboards, Mid-Sized skateboard, ambulance, ambulances, Large ambulance, Large ambulances, Small ambulance, Small ambulances, Mid-Sized ambulance, fire truck, fire trucks, Large fire truck, Large fire trucks, Small fire truck, Small fire trucks, Mid-Sized fire truck, tractor, tractors, Large tractor, Large tractors, Small tractor, Small tractors, Mid-Sized tractor, segway, segways, Large segway, Large segways, Small segway, Small segways, Mid-Sized segway, unicycle, unicycles, Large unicycle, Large unicycles, Small unicycle, Small unicycles, Mid-Sized unicycle, jet ski, jet skis, Large jet ski, Large jet skis, Small jet ski, Small jet skis, Mid-Sized jet ski, helicopter, helicopters, Large helicopter, Large helicopters, Small helicopter, Small helicopters, Mid-Sized helicopter, airplane, airplanes, Large airplane, Large airplanes, Small airplane, Small airplanes, Mid-Sized airplane, boat, boats, Large boat, Large boats, Small boat, Small boats, Mid-Sized boat, kayak, kayaks, Large kayak, Large kayaks, Small kayak, Small kayaks, Mid-Sized kayak, hovercraft, hovercrafts, Large hovercraft, Large hovercrafts, Small hovercraft, Small hovercrafts, Mid-Sized hovercraft

# dict_size(v140)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v140.csv", v140))


# %%
v160 = {
    "car": ["car", "cars", "Large car", "Large cars", "Small car", "Small cars", "Mid-Sized car", "Mid-Sized cars"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle", "Large motorcycles", "Small motorcycle", "Small motorcycles", "Mid-Sized motorcycle", "Mid-Sized motorcycles"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle", "Large bicycles", "Small bicycle", "Small bicycles", "Mid-Sized bicycle", "Mid-Sized bicycles"],
    "truck": ["truck", "trucks", "Large truck", "Large trucks", "Small truck", "Small trucks", "Mid-Sized truck", "Mid-Sized trucks"],
    "bus": ["bus", "buses", "Large bus", "Large buses", "Small bus", "Small buses", "Mid-Sized bus", "Mid-Sized buses"],
    "van": ["van", "vans", "Large van", "Large vans", "Small van", "Small vans", "Mid-Sized van", "Mid-Sized vans"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw", "Large rickshaws", "Small rickshaw", "Small rickshaws", "Mid-Sized rickshaw", "Mid-Sized rickshaws"],
    "scooter": ["scooter", "scooters", "Large scooter", "Large scooters", "Small scooter", "Small scooters", "Mid-Sized scooter", "Mid-Sized scooters"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard", "Large skateboards", "Small skateboard", "Small skateboards", "Mid-Sized skateboard", "Mid-Sized skateboards"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance", "Large ambulances", "Small ambulance", "Small ambulances", "Mid-Sized ambulance", "Mid-Sized ambulances"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck", "Large fire trucks", "Small fire truck", "Small fire trucks", "Mid-Sized fire truck", "Mid-Sized fire trucks"],
    "tractor": ["tractor", "tractors", "Large tractor", "Large tractors", "Small tractor", "Small tractors", "Mid-Sized tractor", "Mid-Sized tractors"],
    "segway": ["segway", "segways", "Large segway", "Large segways", "Small segway", "Small segways", "Mid-Sized segway", "Mid-Sized segways"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle", "Large unicycles", "Small unicycle", "Small unicycles", "Mid-Sized unicycle", "Mid-Sized unicycles"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski", "Large jet skis", "Small jet ski", "Small jet skis", "Mid-Sized jet ski", "Mid-Sized jet skis"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter", "Large helicopters", "Small helicopter", "Small helicopters", "Mid-Sized helicopter", "Mid-Sized helicopters"],
    "airplane": ["airplane", "airplanes", "Large airplane", "Large airplanes", "Small airplane", "Small airplanes", "Mid-Sized airplane", "Mid-Sized airplanes"],
    "boat": ["boat", "boats", "Large boat", "Large boats", "Small boat", "Small boats", "Mid-Sized boat", "Mid-Sized boats"],
    "kayak": ["kayak", "kayaks", "Large kayak", "Large kayaks", "Small kayak", "Small kayaks", "Mid-Sized kayak", "Mid-Sized kayaks"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft", "Large hovercrafts", "Small hovercraft", "Small hovercrafts", "Mid-Sized hovercraft", "Mid-Sized hovercrafts"]
}

# car, cars, Large car, Large cars, Small car, Small cars, Mid-Sized car, Mid-Sized cars, motorcycle, motorcycles, Large motorcycle, Large motorcycles, Small motorcycle, Small motorcycles, Mid-Sized motorcycle, Mid-Sized motorcycles, bicycle, bicycles, Large bicycle, Large bicycles, Small bicycle, Small bicycles, Mid-Sized bicycle, Mid-Sized bicycles, truck, trucks, Large truck, Large trucks, Small truck, Small trucks, Mid-Sized truck, Mid-Sized trucks, bus, buses, Large bus, Large buses, Small bus, Small buses, Mid-Sized bus, Mid-Sized buses, van, vans, Large van, Large vans, Small van, Small vans, Mid-Sized van, Mid-Sized vans, rickshaw, rickshaws, Large rickshaw, Large rickshaws, Small rickshaw, Small rickshaws, Mid-Sized rickshaw, Mid-Sized rickshaws, scooter, scooters, Large scooter, Large scooters, Small scooter, Small scooters, Mid-Sized scooter, Mid-Sized scooters, skateboard, skateboards, Large skateboard, Large skateboards, Small skateboard, Small skateboards, Mid-Sized skateboard, Mid-Sized skateboards, ambulance, ambulances, Large ambulance, Large ambulances, Small ambulance, Small ambulances, Mid-Sized ambulance, Mid-Sized ambulances, fire truck, fire trucks, Large fire truck, Large fire trucks, Small fire truck, Small fire trucks, Mid-Sized fire truck, Mid-Sized fire trucks, tractor, tractors, Large tractor, Large tractors, Small tractor, Small tractors, Mid-Sized tractor, Mid-Sized tractors, segway, segways, Large segway, Large segways, Small segway, Small segways, Mid-Sized segway, Mid-Sized segways, unicycle, unicycles, Large unicycle, Large unicycles, Small unicycle, Small unicycles, Mid-Sized unicycle, Mid-Sized unicycles, jet ski, jet skis, Large jet ski, Large jet skis, Small jet ski, Small jet skis, Mid-Sized jet ski, Mid-Sized jet skis, helicopter, helicopters, Large helicopter, Large helicopters, Small helicopter, Small helicopters, Mid-Sized helicopter, Mid-Sized helicopters, airplane, airplanes, Large airplane, Large airplanes, Small airplane, Small airplanes, Mid-Sized airplane, Mid-Sized airplanes, boat, boats, Large boat, Large boats, Small boat, Small boats, Mid-Sized boat, Mid-Sized boats, kayak, kayaks, Large kayak, Large kayaks, Small kayak, Small kayaks, Mid-Sized kayak, Mid-Sized kayaks, hovercraft, hovercrafts, Large hovercraft, Large hovercrafts, Small hovercraft, Small hovercrafts, Mid-Sized hovercraft, Mid-Sized hovercrafts

# dict_size(v160)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v160.csv", v160))


# %%
v180 = {
    "car": ["car", "cars", "Large car", "Large cars", "Small car", "Small cars", "Mid-Sized car", "Mid-Sized cars", "Vehicle car"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle", "Large motorcycles", "Small motorcycle", "Small motorcycles", "Mid-Sized motorcycle", "Mid-Sized motorcycles", "Vehicle motorcycle"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle", "Large bicycles", "Small bicycle", "Small bicycles", "Mid-Sized bicycle", "Mid-Sized bicycles", "Vehicle bicycle"],
    "truck": ["truck", "trucks", "Large truck", "Large trucks", "Small truck", "Small trucks", "Mid-Sized truck", "Mid-Sized trucks", "Vehicle truck"],
    "bus": ["bus", "buses", "Large bus", "Large buses", "Small bus", "Small buses", "Mid-Sized bus", "Mid-Sized buses", "Vehicle bus"],
    "van": ["van", "vans", "Large van", "Large vans", "Small van", "Small vans", "Mid-Sized van", "Mid-Sized vans", "Vehicle van"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw", "Large rickshaws", "Small rickshaw", "Small rickshaws", "Mid-Sized rickshaw", "Mid-Sized rickshaws", "Vehicle rickshaw"],
    "scooter": ["scooter", "scooters", "Large scooter", "Large scooters", "Small scooter", "Small scooters", "Mid-Sized scooter", "Mid-Sized scooters", "Vehicle scooter"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard", "Large skateboards", "Small skateboard", "Small skateboards", "Mid-Sized skateboard", "Mid-Sized skateboards", "Vehicle skateboard"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance", "Large ambulances", "Small ambulance", "Small ambulances", "Mid-Sized ambulance", "Mid-Sized ambulances", "Vehicle ambulance"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck", "Large fire trucks", "Small fire truck", "Small fire trucks", "Mid-Sized fire truck", "Mid-Sized fire trucks", "Vehicle fire truck"],
    "tractor": ["tractor", "tractors", "Large tractor", "Large tractors", "Small tractor", "Small tractors", "Mid-Sized tractor", "Mid-Sized tractors", "Vehicle tractor"],
    "segway": ["segway", "segways", "Large segway", "Large segways", "Small segway", "Small segways", "Mid-Sized segway", "Mid-Sized segways", "Vehicle segway"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle", "Large unicycles", "Small unicycle", "Small unicycles", "Mid-Sized unicycle", "Mid-Sized unicycles", "Vehicle unicycle"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski", "Large jet skis", "Small jet ski", "Small jet skis", "Mid-Sized jet ski", "Mid-Sized jet skis", "Vehicle jet ski"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter", "Large helicopters", "Small helicopter", "Small helicopters", "Mid-Sized helicopter", "Mid-Sized helicopters", "Vehicle helicopter"],
    "airplane": ["airplane", "airplanes", "Large airplane", "Large airplanes", "Small airplane", "Small airplanes", "Mid-Sized airplane", "Mid-Sized airplanes", "Vehicle airplane"],
    "boat": ["boat", "boats", "Large boat", "Large boats", "Small boat", "Small boats", "Mid-Sized boat", "Mid-Sized boats", "Vehicle boat"],
    "kayak": ["kayak", "kayaks", "Large kayak", "Large kayaks", "Small kayak", "Small kayaks", "Mid-Sized kayak", "Mid-Sized kayaks", "Vehicle kayak"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft", "Large hovercrafts", "Small hovercraft", "Small hovercrafts", "Mid-Sized hovercraft", "Mid-Sized hovercrafts", "Vehicle hovercraft"]
}

# car, cars, Large car, Large cars, Small car, Small cars, Mid-Sized car, Mid-Sized cars, Vehicle car, motorcycle, motorcycles, Large motorcycle, Large motorcycles, Small motorcycle, Small motorcycles, Mid-Sized motorcycle, Mid-Sized motorcycles, Vehicle motorcycle, bicycle, bicycles, Large bicycle, Large bicycles, Small bicycle, Small bicycles, Mid-Sized bicycle, Mid-Sized bicycles, Vehicle bicycle, truck, trucks, Large truck, Large trucks, Small truck, Small trucks, Mid-Sized truck, Mid-Sized trucks, Vehicle truck, bus, buses, Large bus, Large buses, Small bus, Small buses, Mid-Sized bus, Mid-Sized buses, Vehicle bus, van, vans, Large van, Large vans, Small van, Small vans, Mid-Sized van, Mid-Sized vans, Vehicle van, rickshaw, rickshaws, Large rickshaw, Large rickshaws, Small rickshaw, Small rickshaws, Mid-Sized rickshaw, Mid-Sized rickshaws, Vehicle rickshaw, scooter, scooters, Large scooter, Large scooters, Small scooter, Small scooters, Mid-Sized scooter, Mid-Sized scooters, Vehicle scooter, skateboard, skateboards, Large skateboard, Large skateboards, Small skateboard, Small skateboards, Mid-Sized skateboard, Mid-Sized skateboards, Vehicle skateboard, ambulance, ambulances, Large ambulance, Large ambulances, Small ambulance, Small ambulances, Mid-Sized ambulance, Mid-Sized ambulances, Vehicle ambulance, fire truck, fire trucks, Large fire truck, Large fire trucks, Small fire truck, Small fire trucks, Mid-Sized fire truck, Mid-Sized fire trucks, Vehicle fire truck, tractor, tractors, Large tractor, Large tractors, Small tractor, Small tractors, Mid-Sized tractor, Mid-Sized tractors, Vehicle tractor, segway, segways, Large segway, Large segways, Small segway, Small segways, Mid-Sized segway, Mid-Sized segways, Vehicle segway, unicycle, unicycles, Large unicycle, Large unicycles, Small unicycle, Small unicycles, Mid-Sized unicycle, Mid-Sized unicycles, Vehicle unicycle, jet ski, jet skis, Large jet ski, Large jet skis, Small jet ski, Small jet skis, Mid-Sized jet ski, Mid-Sized jet skis, Vehicle jet ski, helicopter, helicopters, Large helicopter, Large helicopters, Small helicopter, Small helicopters, Mid-Sized helicopter, Mid-Sized helicopters, Vehicle helicopter, airplane, airplanes, Large airplane, Large airplanes, Small airplane, Small airplanes, Mid-Sized airplane, Mid-Sized airplanes, Vehicle airplane, boat, boats, Large boat, Large boats, Small boat, Small boats, Mid-Sized boat, Mid-Sized boats, Vehicle boat, kayak, kayaks, Large kayak, Large kayaks, Small kayak, Small kayaks, Mid-Sized kayak, Mid-Sized kayaks, Vehicle kayak, hovercraft, hovercrafts, Large hovercraft, Large hovercrafts, Small hovercraft, Small hovercrafts, Mid-Sized hovercraft, Mid-Sized hovercrafts, Vehicle hovercraft

# dict_size(v180)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v180.csv", v180))


# %%
v200 = {
    "car": ["car", "cars", "Large car", "Large cars", "Small car", "Small cars", "Mid-Sized car", "Mid-Sized cars", "Vehicle car", "Vehicle cars"],
    "motorcycle": ["motorcycle", "motorcycles", "Large motorcycle", "Large motorcycles", "Small motorcycle", "Small motorcycles", "Mid-Sized motorcycle", "Mid-Sized motorcycles", "Vehicle motorcycle", "Vehicle motorcycles"],
    "bicycle": ["bicycle", "bicycles", "Large bicycle", "Large bicycles", "Small bicycle", "Small bicycles", "Mid-Sized bicycle", "Mid-Sized bicycles", "Vehicle bicycle", "Vehicle bicycles"],
    "truck": ["truck", "trucks", "Large truck", "Large trucks", "Small truck", "Small trucks", "Mid-Sized truck", "Mid-Sized trucks", "Vehicle truck", "Vehicle trucks"],
    "bus": ["bus", "buses", "Large bus", "Large buses", "Small bus", "Small buses", "Mid-Sized bus", "Mid-Sized buses", "Vehicle bus", "Vehicle buses"],
    "van": ["van", "vans", "Large van", "Large vans", "Small van", "Small vans", "Mid-Sized van", "Mid-Sized vans", "Vehicle van", "Vehicle vans"],
    "rickshaw": ["rickshaw", "rickshaws", "Large rickshaw", "Large rickshaws", "Small rickshaw", "Small rickshaws", "Mid-Sized rickshaw", "Mid-Sized rickshaws", "Vehicle rickshaw", "Vehicle rickshaws"],
    "scooter": ["scooter", "scooters", "Large scooter", "Large scooters", "Small scooter", "Small scooters", "Mid-Sized scooter", "Mid-Sized scooters", "Vehicle scooter", "Vehicle scooters"],
    "skateboard": ["skateboard", "skateboards", "Large skateboard", "Large skateboards", "Small skateboard", "Small skateboards", "Mid-Sized skateboard", "Mid-Sized skateboards", "Vehicle skateboard", "Vehicle skateboards"],
    "ambulance": ["ambulance", "ambulances", "Large ambulance", "Large ambulances", "Small ambulance", "Small ambulances", "Mid-Sized ambulance", "Mid-Sized ambulances", "Vehicle ambulance", "Vehicle ambulances"],
    "fire truck": ["fire truck", "fire trucks", "Large fire truck", "Large fire trucks", "Small fire truck", "Small fire trucks", "Mid-Sized fire truck", "Mid-Sized fire trucks", "Vehicle fire truck", "Vehicle fire trucks"],
    "tractor": ["tractor", "tractors", "Large tractor", "Large tractors", "Small tractor", "Small tractors", "Mid-Sized tractor", "Mid-Sized tractors", "Vehicle tractor", "Vehicle tractors"],
    "segway": ["segway", "segways", "Large segway", "Large segways", "Small segway", "Small segways", "Mid-Sized segway", "Mid-Sized segways", "Vehicle segway", "Vehicle segways"],
    "unicycle": ["unicycle", "unicycles", "Large unicycle", "Large unicycles", "Small unicycle", "Small unicycles", "Mid-Sized unicycle", "Mid-Sized unicycles", "Vehicle unicycle", "Vehicle unicycles"],
    "jet ski": ["jet ski", "jet skis", "Large jet ski", "Large jet skis", "Small jet ski", "Small jet skis", "Mid-Sized jet ski", "Mid-Sized jet skis", "Vehicle jet ski", "Vehicle jet skis"],
    "helicopter": ["helicopter", "helicopters", "Large helicopter", "Large helicopters", "Small helicopter", "Small helicopters", "Mid-Sized helicopter", "Mid-Sized helicopters", "Vehicle helicopter", "Vehicle helicopters"],
    "airplane": ["airplane", "airplanes", "Large airplane", "Large airplanes", "Small airplane", "Small airplanes", "Mid-Sized airplane", "Mid-Sized airplanes", "Vehicle airplane", "Vehicle airplanes"],
    "boat": ["boat", "boats", "Large boat", "Large boats", "Small boat", "Small boats", "Mid-Sized boat", "Mid-Sized boats", "Vehicle boat", "Vehicle boats"],
    "kayak": ["kayak", "kayaks", "Large kayak", "Large kayaks", "Small kayak", "Small kayaks", "Mid-Sized kayak", "Mid-Sized kayaks", "Vehicle kayak", "Vehicle kayaks"],
    "hovercraft": ["hovercraft", "hovercrafts", "Large hovercraft", "Large hovercrafts", "Small hovercraft", "Small hovercrafts", "Mid-Sized hovercraft", "Mid-Sized hovercrafts", "Vehicle hovercraft", "Vehicle hovercrafts"]
}

# car, cars, Large car, Large cars, Small car, Small cars, Mid-Sized car, Mid-Sized cars, Vehicle car, Vehicle cars, motorcycle, motorcycles, Large motorcycle, Large motorcycles, Small motorcycle, Small motorcycles, Mid-Sized motorcycle, Mid-Sized motorcycles, Vehicle motorcycle, Vehicle motorcycles, bicycle, bicycles, Large bicycle, Large bicycles, Small bicycle, Small bicycles, Mid-Sized bicycle, Mid-Sized bicycles, Vehicle bicycle, Vehicle bicycles, truck, trucks, Large truck, Large trucks, Small truck, Small trucks, Mid-Sized truck, Mid-Sized trucks, Vehicle truck, Vehicle trucks, bus, buses, Large bus, Large buses, Small bus, Small buses, Mid-Sized bus, Mid-Sized buses, Vehicle bus, Vehicle buses, van, vans, Large van, Large vans, Small van, Small vans, Mid-Sized van, Mid-Sized vans, Vehicle van, Vehicle vans, rickshaw, rickshaws, Large rickshaw, Large rickshaws, Small rickshaw, Small rickshaws, Mid-Sized rickshaw, Mid-Sized rickshaws, Vehicle rickshaw, Vehicle rickshaws, scooter, scooters, Large scooter, Large scooters, Small scooter, Small scooters, Mid-Sized scooter, Mid-Sized scooters, Vehicle scooter, Vehicle scooters, skateboard, skateboards, Large skateboard, Large skateboards, Small skateboard, Small skateboards, Mid-Sized skateboard, Mid-Sized skateboards, Vehicle skateboard, Vehicle skateboards, ambulance, ambulances, Large ambulance, Large ambulances, Small ambulance, Small ambulances, Mid-Sized ambulance, Mid-Sized ambulances, Vehicle ambulance, Vehicle ambulances, fire truck, fire trucks, Large fire truck, Large fire trucks, Small fire truck, Small fire trucks, Mid-Sized fire truck, Mid-Sized fire trucks, Vehicle fire truck, Vehicle fire trucks, tractor, tractors, Large tractor, Large tractors, Small tractor, Small tractors, Mid-Sized tractor, Mid-Sized tractors, Vehicle tractor, Vehicle tractors, segway, segways, Large segway, Large segways, Small segway, Small segways, Mid-Sized segway, Mid-Sized segways, Vehicle segway, Vehicle segways, unicycle, unicycles, Large unicycle, Large unicycles, Small unicycle, Small unicycles, Mid-Sized unicycle, Mid-Sized unicycles, Vehicle unicycle, Vehicle unicycles, jet ski, jet skis, Large jet ski, Large jet skis, Small jet ski, Small jet skis, Mid-Sized jet ski, Mid-Sized jet skis, Vehicle jet ski, Vehicle jet skis, helicopter, helicopters, Large helicopter, Large helicopters, Small helicopter, Small helicopters, Mid-Sized helicopter, Mid-Sized helicopters, Vehicle helicopter, Vehicle helicopters, airplane, airplanes, Large airplane, Large airplanes, Small airplane, Small airplanes, Mid-Sized airplane, Mid-Sized airplanes, Vehicle airplane, Vehicle airplanes, boat, boats, Large boat, Large boats, Small boat, Small boats, Mid-Sized boat, Mid-Sized boats, Vehicle boat, Vehicle boats, kayak, kayaks, Large kayak, Large kayaks, Small kayak, Small kayaks, Mid-Sized kayak, Mid-Sized kayaks, Vehicle kayak, Vehicle kayaks, hovercraft, hovercrafts, Large hovercraft, Large hovercrafts, Small hovercraft, Small hovercrafts, Mid-Sized hovercraft, Mid-Sized hovercrafts, Vehicle hovercraft, Vehicle hovercrafts

# dict_size(v200)
print(aOcheck_accuracy("WithoutIP/Vehicle20/v200.csv", v200))


# %% [markdown]
# ## Flowers 10

# %%
fl10 = { "bougainvillea" : ["bougainvillea"],
       "daisies" : ["daisies"],
       "garden_roses" : ["garden roses"],
       "gardenias" : ["gardenias"],
       "hibiscus" : ["hibiscus"],
         "hydrangeas" : ["hydrangeas"],
            "lilies" : ["lilies"],
            "orchids" : ["orchids"],
            "peonies" : ["peonies"],
            "tulip" : ["tulip"]
       }

# bougainvillea, daisies, garden_roses, gardenias, hibiscus, hydrangeas, lilies, orchids, peonies, tulip

dict_size(fl10)
print(flowers_accuracy("WithoutIP/flowers10/f10.csv", fl10))

# %%
fl20 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas"],
    "daisies": ["daisies", "daisy"],
    "garden_roses": ["garden roses", "garden rose"],
    "gardenias": ["gardenias", "gardenia"],
    "hibiscus": ["hibiscus", "hibiscuses"],
    "hydrangeas": ["hydrangeas", "hydrangea"],
    "lilies": ["lilies", "lily"],
    "orchids": ["orchids", "orchid"],
    "peonies": ["peonies", "peony"],
    "tulip": ["tulip", "tulips"]
}

# bougainvillea, bougainvilleas, daisies, daisy, garden_roses, garden rose, gardenias, gardenia, hibiscus, hibiscuses, hydrangeas, hydrangea, lilies, lily, orchids, orchid, peonies, peony, tulip, tulips

# dict_size(fl20)
print(flowers_accuracy("WithoutIP/flowers10/f20.csv", fl20))


# %%
fl30 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea"],
    "daisies": ["daisies", "daisy", "Large daisies"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas"],
    "lilies": ["lilies", "lily", "Large lilies"],
    "orchids": ["orchids", "orchid", "Large orchids"],
    "peonies": ["peonies", "peony", "Large peonies"],
    "tulip": ["tulip", "tulips", "Large tulip"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, daisies, daisy, Large daisies, garden_roses, garden rose, Large garden roses, gardenias, gardenia, Large gardenias, hibiscus, hibiscuses, Large hibiscus, hydrangeas, hydrangea, Large hydrangeas, lilies, lily, Large lilies, orchids, orchid, Large orchids, peonies, peony, Large peonies, tulip, tulips, Large tulip

# dict_size(fl30)
print(flowers_accuracy("WithoutIP/flowers10/f30.csv", fl30))


# %%
fl40 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, daisies, daisy, Large daisies, Large daisy, garden_roses, garden rose, Large garden roses, Large garden rose, gardenias, gardenia, Large gardenias, Large gardenia, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, lilies, lily, Large lilies, Large lily, orchids, orchid, Large orchids, Large orchid, peonies, peony, Large peonies, Large peony, tulip, tulips, Large tulip, Large tulips

# dict_size(fl40)
print(flowers_accuracy("WithoutIP/flowers10/f40.csv", fl40))


# %%
fl50 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, daisies, daisy, Large daisies, Large daisy, Small daisies, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, lilies, lily, Large lilies, Large lily, Small lilies, orchids, orchid, Large orchids, Large orchid, Small orchids, peonies, peony, Large peonies, Large peony, Small peonies, tulip, tulips, Large tulip, Large tulips, Small tulip

# dict_size(fl50)
print(flowers_accuracy("WithoutIP/flowers10/f50.csv", fl50))


# %%
fl60 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, Small bougainvilleas, daisies, daisy, Large daisies, Large daisy, Small daisies, Small daisy, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, Small garden rose, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, Small gardenia, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, Small hibiscuses, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, Small hydrangea, lilies, lily, Large lilies, Large lily, Small lilies, Small lily, orchids, orchid, Large orchids, Large orchid, Small orchids, Small orchid, peonies, peony, Large peonies, Large peony, Small peonies, Small peony, tulip, tulips, Large tulip, Large tulips, Small tulip, Small tulips

# dict_size(fl60)
print(flowers_accuracy("WithoutIP/flowers10/f60.csv", fl60))


# %%
fl70 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, Small bougainvilleas, Medium bougainvillea, daisies, daisy, Large daisies, Large daisy, Small daisies, Small daisy, Medium daisies, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, Small garden rose, Medium garden roses, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, Small gardenia, Medium gardenias, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, Small hibiscuses, Medium hibiscus, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, Small hydrangea, Medium hydrangeas, lilies, lily, Large lilies, Large lily, Small lilies, Small lily, Medium lilies, orchids, orchid, Large orchids, Large orchid, Small orchids, Small orchid, Medium orchids, peonies, peony, Large peonies, Large peony, Small peonies, Small peony, Medium peonies, tulip, tulips, Large tulip, Large tulips, Small tulip, Small tulips, Medium tulip

# dict_size(fl70)
print(flowers_accuracy("WithoutIP/flowers10/f70.csv", fl70))


# %%
fl80 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea", "Medium bougainvilleas"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies", "Medium daisy"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses", "Medium garden rose"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias", "Medium gardenia"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus", "Medium hibiscuses"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas", "Medium hydrangea"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies", "Medium lily"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids", "Medium orchid"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies", "Medium peony"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip", "Medium tulips"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, Small bougainvilleas, Medium bougainvillea, Medium bougainvilleas, daisies, daisy, Large daisies, Large daisy, Small daisies, Small daisy, Medium daisies, Medium daisy, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, Small garden rose, Medium garden roses, Medium garden rose, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, Small gardenia, Medium gardenias, Medium gardenia, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, Small hibiscuses, Medium hibiscus, Medium hibiscuses, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, Small hydrangea, Medium hydrangeas, Medium hydrangea, lilies, lily, Large lilies, Large lily, Small lilies, Small lily, Medium lilies, Medium lily, orchids, orchid, Large orchids, Large orchid, Small orchids, Small orchid, Medium orchids, Medium orchid, peonies, peony, Large peonies, Large peony, Small peonies, Small peony, Medium peonies, Medium peony, tulip, tulips, Large tulip, Large tulips, Small tulip, Small tulips, Medium tulip, Medium tulips

# dict_size(fl80)
print(flowers_accuracy("WithoutIP/flowers10/f80.csv", fl80))


# %%
fl90 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea", "Medium bougainvilleas", "Flower bougainvillea"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies", "Medium daisy", "Flower daisies"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses", "Medium garden rose", "Flower garden roses"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias", "Medium gardenia", "Flower gardenias"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus", "Medium hibiscuses", "Flower hibiscus"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas", "Medium hydrangea", "Flower hydrangeas"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies", "Medium lily", "Flower lilies"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids", "Medium orchid", "Flower orchids"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies", "Medium peony", "Flower peonies"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip", "Medium tulips", "Flower tulip"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, Small bougainvilleas, Medium bougainvillea, Medium bougainvilleas, Flower bougainvillea, daisies, daisy, Large daisies, Large daisy, Small daisies, Small daisy, Medium daisies, Medium daisy, Flower daisies, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, Small garden rose, Medium garden roses, Medium garden rose, Flower garden roses, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, Small gardenia, Medium gardenias, Medium gardenia, Flower gardenias, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, Small hibiscuses, Medium hibiscus, Medium hibiscuses, Flower hibiscus, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, Small hydrangea, Medium hydrangeas, Medium hydrangea, Flower hydrangeas, lilies, lily, Large lilies, Large lily, Small lilies, Small lily, Medium lilies, Medium lily, Flower lilies, orchids, orchid, Large orchids, Large orchid, Small orchids, Small orchid, Medium orchids, Medium orchid, Flower orchids, peonies, peony, Large peonies, Large peony, Small peonies, Small peony, Medium peonies, Medium peony, Flower peonies, tulip, tulips, Large tulip, Large tulips, Small tulip, Small tulips, Medium tulip, Medium tulips, Flower tulip

# dict_size(fl90)
print(flowers_accuracy("WithoutIP/flowers10/f90.csv", fl90))


# %%
fl100 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea", "Medium bougainvilleas", "Flower bougainvillea", "Flower bougainvilleas"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies", "Medium daisy", "Flower daisies", "Flower daisy"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses", "Medium garden rose", "Flower garden roses", "Flower garden rose"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias", "Medium gardenia", "Flower gardenias", "Flower gardenia"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus", "Medium hibiscuses", "Flower hibiscus", "Flower hibiscuses"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas", "Medium hydrangea", "Flower hydrangeas", "Flower hydrangea"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies", "Medium lily", "Flower lilies", "Flower lily"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids", "Medium orchid", "Flower orchids", "Flower orchid"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies", "Medium peony", "Flower peonies", "Flower peony"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip", "Medium tulips", "Flower tulip", "Flower tulips"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, Small bougainvilleas, Medium bougainvillea, Medium bougainvilleas, Flower bougainvillea, Flower bougainvilleas, daisies, daisy, Large daisies, Large daisy, Small daisies, Small daisy, Medium daisies, Medium daisy, Flower daisies, Flower daisy, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, Small garden rose, Medium garden roses, Medium garden rose, Flower garden roses, Flower garden rose, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, Small gardenia, Medium gardenias, Medium gardenia, Flower gardenias, Flower gardenia, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, Small hibiscuses, Medium hibiscus, Medium hibiscuses, Flower hibiscus, Flower hibiscuses, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, Small hydrangea, Medium hydrangeas, Medium hydrangea, Flower hydrangeas, Flower hydrangea, lilies, lily, Large lilies, Large lily, Small lilies, Small lily, Medium lilies, Medium lily, Flower lilies, Flower lily, orchids, orchid, Large orchids, Large orchid, Small orchids, Small orchid, Medium orchids, Medium orchid, Flower orchids, Flower orchid, peonies, peony, Large peonies, Large peony, Small peonies, Small peony, Medium peonies, Medium peony, Flower peonies, Flower peony, tulip, tulips, Large tulip, Large tulips, Small tulip, Small tulips, Medium tulip, Medium tulips, Flower tulip, Flower tulips

# dict_size(fl100)
print(flowers_accuracy("WithoutIP/flowers10/f100.csv", fl100))


# %%
fl110 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea", "Medium bougainvilleas", "Flower bougainvillea", "Flower bougainvilleas", "Wild bougainvillea"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies", "Medium daisy", "Flower daisies", "Flower daisy", "Wild daisies"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses", "Medium garden rose", "Flower garden roses", "Flower garden rose", "Wild garden roses"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias", "Medium gardenia", "Flower gardenias", "Flower gardenia", "Wild gardenias"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus", "Medium hibiscuses", "Flower hibiscus", "Flower hibiscuses", "Wild hibiscus"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas", "Medium hydrangea", "Flower hydrangeas", "Flower hydrangea", "Wild hydrangeas"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies", "Medium lily", "Flower lilies", "Flower lily", "Wild lilies"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids", "Medium orchid", "Flower orchids", "Flower orchid", "Wild orchids"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies", "Medium peony", "Flower peonies", "Flower peony", "Wild peonies"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip", "Medium tulips", "Flower tulip", "Flower tulips", "Wild tulip"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, Small bougainvilleas, Medium bougainvillea, Medium bougainvilleas, Flower bougainvillea, Flower bougainvilleas, Wild bougainvillea, daisies, daisy, Large daisies, Large daisy, Small daisies, Small daisy, Medium daisies, Medium daisy, Flower daisies, Flower daisy, Wild daisies, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, Small garden rose, Medium garden roses, Medium garden rose, Flower garden roses, Flower garden rose, Wild garden roses, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, Small gardenia, Medium gardenias, Medium gardenia, Flower gardenias, Flower gardenia, Wild gardenias, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, Small hibiscuses, Medium hibiscus, Medium hibiscuses, Flower hibiscus, Flower hibiscuses, Wild hibiscus, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, Small hydrangea, Medium hydrangeas, Medium hydrangea, Flower hydrangeas, Flower hydrangea, Wild hydrangeas, lilies, lily, Large lilies, Large lily, Small lilies, Small lily, Medium lilies, Medium lily, Flower lilies, Flower lily, Wild lilies, orchids, orchid, Large orchids, Large orchid, Small orchids, Small orchid, Medium orchids, Medium orchid, Flower orchids, Flower orchid, Wild orchids, peonies, peony, Large peonies, Large peony, Small peonies, Small peony, Medium peonies, Medium peony, Flower peonies, Flower peony, Wild peonies, tulip, tulips, Large tulip, Large tulips, Small tulip, Small tulips, Medium tulip, Medium tulips, Flower tulip, Flower tulips, Wild tulip

# dict_size(fl110)
print(flowers_accuracy("WithoutIP/flowers10/fl110.csv", fl110))


# %%
fl120 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea", "Medium bougainvilleas", "Flower bougainvillea", "Flower bougainvilleas", "Wild bougainvillea", "Wild bougainvilleas"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies", "Medium daisy", "Flower daisies", "Flower daisy", "Wild daisies", "Wild daisy"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses", "Medium garden rose", "Flower garden roses", "Flower garden rose", "Wild garden roses", "Wild garden rose"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias", "Medium gardenia", "Flower gardenias", "Flower gardenia", "Wild gardenias", "Wild gardenia"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus", "Medium hibiscuses", "Flower hibiscus", "Flower hibiscuses", "Wild hibiscus", "Wild hibiscuses"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas", "Medium hydrangea", "Flower hydrangeas", "Flower hydrangea", "Wild hydrangeas", "Wild hydrangea"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies", "Medium lily", "Flower lilies", "Flower lily", "Wild lilies", "Wild lily"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids", "Medium orchid", "Flower orchids", "Flower orchid", "Wild orchids", "Wild orchid"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies", "Medium peony", "Flower peonies", "Flower peony", "Wild peonies", "Wild peony"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip", "Medium tulips", "Flower tulip", "Flower tulips", "Wild tulip", "Wild tulips"]
}

# bougainvillea, bougainvilleas, Large bougainvillea, Large bougainvilleas, Small bougainvillea, Small bougainvilleas, Medium bougainvillea, Medium bougainvilleas, Flower bougainvillea, Flower bougainvilleas, Wild bougainvillea, Wild bougainvilleas, daisies, daisy, Large daisies, Large daisy, Small daisies, Small daisy, Medium daisies, Medium daisy, Flower daisies, Flower daisy, Wild daisies, Wild daisy, garden_roses, garden rose, Large garden roses, Large garden rose, Small garden roses, Small garden rose, Medium garden roses, Medium garden rose, Flower garden roses, Flower garden rose, Wild garden roses, Wild garden rose, gardenias, gardenia, Large gardenias, Large gardenia, Small gardenias, Small gardenia, Medium gardenias, Medium gardenia, Flower gardenias, Flower gardenia, Wild gardenias, Wild gardenia, hibiscus, hibiscuses, Large hibiscus, Large hibiscuses, Small hibiscus, Small hibiscuses, Medium hibiscus, Medium hibiscuses, Flower hibiscus, Flower hibiscuses, Wild hibiscus, Wild hibiscuses, hydrangeas, hydrangea, Large hydrangeas, Large hydrangea, Small hydrangeas, Small hydrangea, Medium hydrangeas, Medium hydrangea, Flower hydrangeas, Flower hydrangea, Wild hydrangeas, Wild hydrangea, lilies, lily, Large lilies, Large lily, Small lilies, Small lily, Medium lilies, Medium lily, Flower lilies, Flower lily, Wild lilies, Wild lily, orchids, orchid, Large orchids, Large orchid, Small orchids, Small orchid, Medium orchids, Medium orchid, Flower orchids, Flower orchid, Wild orchids, Wild orchid, peonies, peony, Large peonies, Large peony, Small peonies, Small peony, Medium peonies, Medium peony, Flower peonies, Flower peony, Wild peonies, Wild peony, tulip, tulips, Large tulip, Large tulips, Small tulip, Small tulips, Medium tulip, Medium tulips, Flower tulip, Flower tulips, Wild tulip, Wild tulips

# dict_size(fl120)
print(flowers_accuracy("WithoutIP/flowers10/fl120.csv", fl120))


# %%
fl130 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea", "Medium bougainvilleas", "Flower bougainvillea", "Flower bougainvilleas", "Wild bougainvillea", "Wild bougainvilleas", "Tiny bougainvillea"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies", "Medium daisy", "Flower daisies", "Flower daisy", "Wild daisies", "Wild daisy", "Tiny daisies"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses", "Medium garden rose", "Flower garden roses", "Flower garden rose", "Wild garden roses", "Wild garden rose", "Tiny garden roses"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias", "Medium gardenia", "Flower gardenias", "Flower gardenia", "Wild gardenias", "Wild gardenia", "Tiny gardenias"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus", "Medium hibiscuses", "Flower hibiscus", "Flower hibiscuses", "Wild hibiscus", "Wild hibiscuses", "Tiny hibiscus"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas", "Medium hydrangea", "Flower hydrangeas", "Flower hydrangea", "Wild hydrangeas", "Wild hydrangea", "Tiny hydrangeas"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies", "Medium lily", "Flower lilies", "Flower lily", "Wild lilies", "Wild lily", "Tiny lilies"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids", "Medium orchid", "Flower orchids", "Flower orchid", "Wild orchids", "Wild orchid", "Tiny orchids"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies", "Medium peony", "Flower peonies", "Flower peony", "Wild peonies", "Wild peony", "Tiny peonies"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip", "Medium tulips", "Flower tulip", "Flower tulips", "Wild tulip", "Wild tulips", "Tiny tulip"]
}

# bougainvillea, bougainvilleas, large bougainvillea, large bougainvilleas, small bougainvillea, small bougainvilleas, medium bougainvillea, medium bougainvilleas, flower bougainvillea, flower bougainvilleas, wild bougainvillea, wild bougainvilleas, tiny bougainvillea, daisies, daisy, large daisies, large daisy, small daisies, small daisy, medium daisies, medium daisy, flower daisies, flower daisy, wild daisies, wild daisy, tiny daisies, garden_roses, garden rose, large garden roses, large garden rose, small garden roses, small garden rose, medium garden roses, medium garden rose, flower garden roses, flower garden rose, wild garden roses, wild garden rose, tiny garden roses, gardenias, gardenia, large gardenias, large gardenia, small gardenias, small gardenia, medium gardenias, medium gardenia, flower gardenias, flower gardenia, wild gardenias, wild gardenia, tiny gardenias, hibiscus, hibiscuses, large hibiscus, large hibiscuses, small hibiscus, small hibiscuses, medium hibiscus, medium hibiscuses, flower hibiscus, flower hibiscuses, wild hibiscus, wild hibiscuses, tiny hibiscus, hydrangeas, hydrangea, large hydrangeas, large hydrangea, small hydrangeas, small hydrangea, medium hydrangeas, medium hydrangea, flower hydrangeas, flower hydrangea, wild hydrangeas, wild hydrangea, tiny hydrangeas, lilies, lily, large lilies, large lily, small lilies, small lily, medium lilies, medium lily, flower lilies, flower lily, wild lilies, wild lily, tiny lilies, orchids, orchid, large orchids, large orchid, small orchids, small orchid, medium orchids, medium orchid, flower orchids, flower orchid, wild orchids, wild orchid, tiny orchids, peonies, peony, large peonies, large peony, small peonies, small peony, medium peonies, medium peony, flower peonies, flower peony, wild peonies, wild peony, tiny peonies, tulip, tulips, large tulip, large tulips, small tulip, small tulips, medium tulip, medium tulips, flower tulip, flower tulips, wild tulip, wild tulips, tiny tulip

# dict_size(fl130)
print(flowers_accuracy("WithoutIP/flowers10/fl130.csv", fl130))


# %%
fl140 = {
    "bougainvillea": ["bougainvillea", "bougainvilleas", "Large bougainvillea", "Large bougainvilleas", "Small bougainvillea", "Small bougainvilleas", "Medium bougainvillea", "Medium bougainvilleas", "Flower bougainvillea", "Flower bougainvilleas", "Wild bougainvillea", "Wild bougainvilleas", "Tiny bougainvillea", "Tiny bougainvilleas"],
    "daisies": ["daisies", "daisy", "Large daisies", "Large daisy", "Small daisies", "Small daisy", "Medium daisies", "Medium daisy", "Flower daisies", "Flower daisy", "Wild daisies", "Wild daisy", "Tiny daisies", "Tiny daisy"],
    "garden_roses": ["garden roses", "garden rose", "Large garden roses", "Large garden rose", "Small garden roses", "Small garden rose", "Medium garden roses", "Medium garden rose", "Flower garden roses", "Flower garden rose", "Wild garden roses", "Wild garden rose", "Tiny garden roses", "Tiny garden rose"],
    "gardenias": ["gardenias", "gardenia", "Large gardenias", "Large gardenia", "Small gardenias", "Small gardenia", "Medium gardenias", "Medium gardenia", "Flower gardenias", "Flower gardenia", "Wild gardenias", "Wild gardenia", "Tiny gardenias", "Tiny gardenia"],
    "hibiscus": ["hibiscus", "hibiscuses", "Large hibiscus", "Large hibiscuses", "Small hibiscus", "Small hibiscuses", "Medium hibiscus", "Medium hibiscuses", "Flower hibiscus", "Flower hibiscuses", "Wild hibiscus", "Wild hibiscuses", "Tiny hibiscus", "Tiny hibiscuses"],
    "hydrangeas": ["hydrangeas", "hydrangea", "Large hydrangeas", "Large hydrangea", "Small hydrangeas", "Small hydrangea", "Medium hydrangeas", "Medium hydrangea", "Flower hydrangeas", "Flower hydrangea", "Wild hydrangeas", "Wild hydrangea", "Tiny hydrangeas", "Tiny hydrangea"],
    "lilies": ["lilies", "lily", "Large lilies", "Large lily", "Small lilies", "Small lily", "Medium lilies", "Medium lily", "Flower lilies", "Flower lily", "Wild lilies", "Wild lily", "Tiny lilies", "Tiny lily"],
    "orchids": ["orchids", "orchid", "Large orchids", "Large orchid", "Small orchids", "Small orchid", "Medium orchids", "Medium orchid", "Flower orchids", "Flower orchid", "Wild orchids", "Wild orchid", "Tiny orchids", "Tiny orchid"],
    "peonies": ["peonies", "peony", "Large peonies", "Large peony", "Small peonies", "Small peony", "Medium peonies", "Medium peony", "Flower peonies", "Flower peony", "Wild peonies", "Wild peony", "Tiny peonies", "Tiny peony"],
    "tulip": ["tulip", "tulips", "Large tulip", "Large tulips", "Small tulip", "Small tulips", "Medium tulip", "Medium tulips", "Flower tulip", "Flower tulips", "Wild tulip", "Wild tulips", "Tiny tulip", "Tiny tulips"]
}

# bougainvillea, bougainvilleas, large bougainvillea, large bougainvilleas, small bougainvillea, small bougainvilleas, medium bougainvillea, medium bougainvilleas, flower bougainvillea, flower bougainvilleas, wild bougainvillea, wild bougainvilleas, tiny bougainvillea, tiny bougainvilleas, daisies, daisy, large daisies, large daisy, small daisies, small daisy, medium daisies, medium daisy, flower daisies, flower daisy, wild daisies, wild daisy, tiny daisies, tiny daisy, garden_roses, garden rose, large garden roses, large garden rose, small garden roses, small garden rose, medium garden roses, medium garden rose, flower garden roses, flower garden rose, wild garden roses, wild garden rose, tiny garden roses, tiny garden rose, gardenias, gardenia, large gardenias, large gardenia, small gardenias, small gardenia, medium gardenias, medium gardenia, flower gardenias, flower gardenia, wild gardenias, wild gardenia, tiny gardenias, tiny gardenia, hibiscus, hibiscuses, large hibiscus, large hibiscuses, small hibiscus, small hibiscuses, medium hibiscus, medium hibiscuses, flower hibiscus, flower hibiscuses, wild hibiscus, wild hibiscuses, tiny hibiscus, tiny hibiscuses, hydrangeas, hydrangea, large hydrangeas, large hydrangea, small hydrangeas, small hydrangea, medium hydrangeas, medium hydrangea, flower hydrangeas, flower hydrangea, wild hydrangeas, wild hydrangea, tiny hydrangeas, tiny hydrangea, lilies, lily, large lilies, large lily, small lilies, small lily, medium lilies, medium lily, flower lilies, flower lily, wild lilies, wild lily, tiny lilies, tiny lily, orchids, orchid, large orchids, large orchid, small orchids, small orchid, medium orchids, medium orchid, flower orchids, flower orchid, wild orchids, wild orchid, tiny orchids, tiny orchid, peonies, peony, large peonies, large peony, small peonies, small peony, medium peonies, medium peony, flower peonies, flower peony, wild peonies, wild peony, tiny peonies, tiny peony, tulip, tulips, large tulip, large tulips, small tulip, small tulips, medium tulip, medium tulips, flower tulip, flower tulips, wild tulip, wild tulips, tiny tulip, tiny tulips

# dict_size(fl140)
print(flowers_accuracy("WithoutIP/flowers10/fl130.csv", fl140))


# %% [markdown]
# ## Fruits 10

# %%
fr10 = {
    "Apple" : ["Apple"],
    "Orange" : ["Orange"],
    "Avocado" : ["Avocado"],
    "Kiwi" : ["Kiwi"],
    "Mango" : ["Mango"],
    "Pineapple" : ["Pineapple"],
    "strawberries" : ["strawberries"],
    "Banana" : ["Banana"],
    "Cherry" : ["Cherry"],
    "Watermelon" : ["Watermelon"]
}

# Apple, Orange, Avocado, Kiwi, Mango, Pineapple, strawberries, Banana, Cherry, Watermelon

dict_size(fr10)
print(aOcheck_accuracy("WithoutIP/fruits10/fr10.csv", fr10))

# %%
fr20 = {
    "Apple": ["Apple", "Apples"],
    "Orange": ["Orange", "Oranges"],
    "Avocado": ["Avocado", "Avocados"],
    "Kiwi": ["Kiwi", "Kiwis"],
    "Mango": ["Mango", "Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples"],
    "strawberries": ["strawberries", "strawberry"],
    "Banana": ["Banana", "Bananas"],
    "Cherry": ["Cherry", "Cherries"],
    "Watermelon": ["Watermelon", "Watermelons"]
}

# Apple, Apples, Orange, Oranges, Avocado, Avocados, Kiwi, Kiwis, Mango, Mangoes, Pineapple, Pineapples, strawberries, strawberry, Banana, Bananas, Cherry, Cherries, Watermelon, Watermelons

# dict_size(fr20)
print(aOcheck_accuracy("WithoutIP/fruits10/fr20.csv", fr20))


# %%
fr30 = {
    "Apple": ["Apple", "Apples", "Large Apple"],
    "Orange": ["Orange", "Oranges", "Large Orange"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi"],
    "Mango": ["Mango", "Mangoes", "Large Mango"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries"],
    "Banana": ["Banana", "Bananas", "Large Banana"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon"]
}

# Apple, Apples, Large Apple, Orange, Oranges, Large Orange, Avocado, Avocados, Large Avocado, Kiwi, Kiwis, Large Kiwi, Mango, Mangoes, Large Mango, Pineapple, Pineapples, Large Pineapple, strawberries, strawberry, Large strawberries, Banana, Bananas, Large Banana, Cherry, Cherries, Large Cherry, Watermelon, Watermelons, Large Watermelon

# dict_size(fr30)
print(aOcheck_accuracy("WithoutIP/fruits10/fr30.csv", fr30))


# %%
fr40 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons"]
}

# Apple, Apples, Large Apple, Large Apples, Orange, Oranges, Large Orange, Large Oranges, Avocado, Avocados, Large Avocado, Large Avocados, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Mango, Mangoes, Large Mango, Large Mangoes, Pineapple, Pineapples, Large Pineapple, Large Pineapples, strawberries, strawberry, Large strawberries, Large strawberry, Banana, Bananas, Large Banana, Large Bananas, Cherry, Cherries, Large Cherry, Large Cherries, Watermelon, Watermelons, Large Watermelon, Large Watermelons

# dict_size(fr40)
print(aOcheck_accuracy("WithoutIP/fruits10/fr40.csv", fr40))


# %%
fr50 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon

# dict_size(fr50)
print(aOcheck_accuracy("WithoutIP/fruits10/fr50.csv", fr50))


# %%
fr60 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons

# dict_size(fr60)
print(aOcheck_accuracy("WithoutIP/fruits10/fr60.csv", fr60))


# %%
fr70 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon

# dict_size(fr70)
print(aOcheck_accuracy("WithoutIP/fruits10/fr70.csv", fr70))


# %%
fr80 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons

# dict_size(fr80)
print(aOcheck_accuracy("WithoutIP/fruits10/fr80.csv", fr80))


# %%
fr90 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Fruit Apple, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Fruit Orange, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Fruit Avocado, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Fruit Kiwi, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Fruit Mango, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, Fruit Pineapple, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Fruit strawberries, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Fruit Banana, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Fruit Cherry, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons, Fruit Watermelon

# dict_size(fr90)
print(aOcheck_accuracy("WithoutIP/fruits10/fr90.csv", fr90))


# %%
fr100 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple", "Fruit Apples"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange", "Fruit Oranges"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado", "Fruit Avocados"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi", "Fruit Kiwis"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango", "Fruit Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple", "Fruit Pineapples"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries", "Fruit strawberry"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana", "Fruit Bananas"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry", "Fruit Cherries"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon", "Fruit Watermelons"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Fruit Apple, Fruit Apples, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Fruit Orange, Fruit Oranges, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Fruit Avocado, Fruit Avocados, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Fruit Kiwi, Fruit Kiwis, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Fruit Mango, Fruit Mangoes, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, Fruit Pineapple, Fruit Pineapples, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Fruit strawberries, Fruit strawberry, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Fruit Banana, Fruit Bananas, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Fruit Cherry, Fruit Cherries, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons, Fruit Watermelon, Fruit Watermelons

# dict_size(fr100)
print(aOcheck_accuracy("WithoutIP/fruits10/fr100.csv", fr100))


# %%
fr110 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple", "Fruit Apples", "Food Apple"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange", "Fruit Oranges", "Food Orange"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado", "Fruit Avocados", "Food Avocado"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi", "Fruit Kiwis", "Food Kiwi"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango", "Fruit Mangoes", "Food Mango"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple", "Fruit Pineapples", "Food Pineapple"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries", "Fruit strawberry", "Food strawberries"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana", "Fruit Bananas", "Food Banana"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry", "Fruit Cherries", "Food Cherry"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon", "Fruit Watermelons", "Food Watermelon"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Fruit Apple, Fruit Apples, Food Apple, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Fruit Orange, Fruit Oranges, Food Orange, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Fruit Avocado, Fruit Avocados, Food Avocado, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Fruit Kiwi, Fruit Kiwis, Food Kiwi, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Fruit Mango, Fruit Mangoes, Food Mango, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, Fruit Pineapple, Fruit Pineapples, Food Pineapple, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Fruit strawberries, Fruit strawberry, Food strawberries, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Fruit Banana, Fruit Bananas, Food Banana, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Fruit Cherry, Fruit Cherries, Food Cherry, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons, Fruit Watermelon, Fruit Watermelons, Food Watermelon

# dict_size(fr110)
print(aOcheck_accuracy("WithoutIP/fruits10/fr110.csv", fr110))


# %%
fr120 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple", "Fruit Apples", "Food Apple", "Food Apples"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange", "Fruit Oranges", "Food Orange", "Food Oranges"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado", "Fruit Avocados", "Food Avocado", "Food Avocados"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi", "Fruit Kiwis", "Food Kiwi", "Food Kiwis"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango", "Fruit Mangoes", "Food Mango", "Food Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple", "Fruit Pineapples", "Food Pineapple", "Food Pineapples"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries", "Fruit strawberry", "Food strawberries", "Food strawberry"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana", "Fruit Bananas", "Food Banana", "Food Bananas"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry", "Fruit Cherries", "Food Cherry", "Food Cherries"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon", "Fruit Watermelons", "Food Watermelon", "Food Watermelons"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Fruit Apple, Fruit Apples, Food Apple, Food Apples, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Fruit Orange, Fruit Oranges, Food Orange, Food Oranges, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Fruit Avocado, Fruit Avocados, Food Avocado, Food Avocados, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Fruit Kiwi, Fruit Kiwis, Food Kiwi, Food Kiwis, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Fruit Mango, Fruit Mangoes, Food Mango, Food Mangoes, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, Fruit Pineapple, Fruit Pineapples, Food Pineapple, Food Pineapples, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Fruit strawberries, Fruit strawberry, Food strawberries, Food strawberry, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Fruit Banana, Fruit Bananas, Food Banana, Food Bananas, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Fruit Cherry, Fruit Cherries, Food Cherry, Food Cherries, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons, Fruit Watermelon, Fruit Watermelons, Food Watermelon, Food Watermelons

# dict_size(fr120)
print(aOcheck_accuracy("WithoutIP/fruits10/fr120.csv", fr120))


# %%
fr130 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple", "Fruit Apples", "Food Apple", "Food Apples", "Edible Apple"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange", "Fruit Oranges", "Food Orange", "Food Oranges", "Edible Orange"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado", "Fruit Avocados", "Food Avocado", "Food Avocados", "Edible Avocado"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi", "Fruit Kiwis", "Food Kiwi", "Food Kiwis", "Edible Kiwi"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango", "Fruit Mangoes", "Food Mango", "Food Mangoes", "Edible Mango"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple", "Fruit Pineapples", "Food Pineapple", "Food Pineapples", "Edible Pineapple"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries", "Fruit strawberry", "Food strawberries", "Food strawberry", "Edible strawberries"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana", "Fruit Bananas", "Food Banana", "Food Bananas", "Edible Banana"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry", "Fruit Cherries", "Food Cherry", "Food Cherries", "Edible Cherry"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon", "Fruit Watermelons", "Food Watermelon", "Food Watermelons", "Edible Watermelon"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Fruit Apple, Fruit Apples, Food Apple, Food Apples, Edible Apple, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Fruit Orange, Fruit Oranges, Food Orange, Food Oranges, Edible Orange, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Fruit Avocado, Fruit Avocados, Food Avocado, Food Avocados, Edible Avocado, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Fruit Kiwi, Fruit Kiwis, Food Kiwi, Food Kiwis, Edible Kiwi, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Fruit Mango, Fruit Mangoes, Food Mango, Food Mangoes, Edible Mango, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, Fruit Pineapple, Fruit Pineapples, Food Pineapple, Food Pineapples, Edible Pineapple, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Fruit strawberries, Fruit strawberry, Food strawberries, Food strawberry, Edible strawberries, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Fruit Banana, Fruit Bananas, Food Banana, Food Bananas, Edible Banana, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Fruit Cherry, Fruit Cherries, Food Cherry, Food Cherries, Edible Cherry, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons, Fruit Watermelon, Fruit Watermelons, Food Watermelon, Food Watermelons, Edible Watermelon

# dict_size(fr130)
print(aOcheck_accuracy("WithoutIP/fruits10/fr130.csv", fr130))


# %%
fr140 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple", "Fruit Apples", "Food Apple", "Food Apples", "Edible Apple", "Edible Apples"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange", "Fruit Oranges", "Food Orange", "Food Oranges", "Edible Orange", "Edible Oranges"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado", "Fruit Avocados", "Food Avocado", "Food Avocados", "Edible Avocado", "Edible Avocados"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi", "Fruit Kiwis", "Food Kiwi", "Food Kiwis", "Edible Kiwi", "Edible Kiwis"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango", "Fruit Mangoes", "Food Mango", "Food Mangoes", "Edible Mango", "Edible Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple", "Fruit Pineapples", "Food Pineapple", "Food Pineapples", "Edible Pineapple", "Edible Pineapples"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries", "Fruit strawberry", "Food strawberries", "Food strawberry", "Edible strawberries", "Edible strawberry"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana", "Fruit Bananas", "Food Banana", "Food Bananas", "Edible Banana", "Edible Bananas"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry", "Fruit Cherries", "Food Cherry", "Food Cherries", "Edible Cherry", "Edible Cherries"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon", "Fruit Watermelons", "Food Watermelon", "Food Watermelons", "Edible Watermelon", "Edible Watermelons"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Fruit Apple, Fruit Apples, Food Apple, Food Apples, Edible Apple, Edible Apples, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Fruit Orange, Fruit Oranges, Food Orange, Food Oranges, Edible Orange, Edible Oranges, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Fruit Avocado, Fruit Avocados, Food Avocado, Food Avocados, Edible Avocado, Edible Avocados, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Fruit Kiwi, Fruit Kiwis, Food Kiwi, Food Kiwis, Edible Kiwi, Edible Kiwis, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Fruit Mango, Fruit Mangoes, Food Mango, Food Mangoes, Edible Mango, Edible Mangoes, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, Fruit Pineapple, Fruit Pineapples, Food Pineapple, Food Pineapples, Edible Pineapple, Edible Pineapples, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Fruit strawberries, Fruit strawberry, Food strawberries, Food strawberry, Edible strawberries, Edible strawberry, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Fruit Banana, Fruit Bananas, Food Banana, Food Bananas, Edible Banana, Edible Bananas, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Fruit Cherry, Fruit Cherries, Food Cherry, Food Cherries, Edible Cherry, Edible Cherries, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons, Fruit Watermelon, Fruit Watermelons, Food Watermelon, Food Watermelons, Edible Watermelon, Edible Watermelons

# dict_size(fr140)
print(aOcheck_accuracy("WithoutIP/fruits10/fr140.csv", fr140))

# %%
fr150 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple", "Fruit Apples", "Food Apple", "Food Apples", "Edible Apple", "Edible Apples", "Fruit Apple"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange", "Fruit Oranges", "Food Orange", "Food Oranges", "Edible Orange", "Edible Oranges", "Fruit Orange"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado", "Fruit Avocados", "Food Avocado", "Food Avocados", "Edible Avocado", "Edible Avocados", "Fruit Avocado"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi", "Fruit Kiwis", "Food Kiwi", "Food Kiwis", "Edible Kiwi", "Edible Kiwis", "Fruit Kiwi"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango", "Fruit Mangoes", "Food Mango", "Food Mangoes", "Edible Mango", "Edible Mangoes", "Fruit Mango"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple", "Fruit Pineapples", "Food Pineapple", "Food Pineapples", "Edible Pineapple", "Edible Pineapples", "Fruit Pineapple"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries", "Fruit strawberry", "Food strawberries", "Food strawberry", "Edible strawberries", "Edible strawberry", "Fruit strawberries"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana", "Fruit Bananas", "Food Banana", "Food Bananas", "Edible Banana", "Edible Bananas", "Fruit Banana"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry", "Fruit Cherries", "Food Cherry", "Food Cherries", "Edible Cherry", "Edible Cherries", "Fruit Cherry"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon", "Fruit Watermelons", "Food Watermelon", "Food Watermelons", "Edible Watermelon", "Edible Watermelons", "Fruit Watermelon"]
}

# apple, apples, large apple, large apples, small apple, small apples, medium apple, medium apples, fruit apple, fruit apples, food apple, food apples, edible apple, edible apples, fruit apple, orange, oranges, large orange, large oranges, small orange, small oranges, medium orange, medium oranges, fruit orange, fruit oranges, food orange, food oranges, edible orange, edible oranges, fruit orange, avocado, avocados, large avocado, large avocados, small avocado, small avocados, medium avocado, medium avocados, fruit avocado, fruit avocados, food avocado, food avocados, edible avocado, edible avocados, fruit avocado, kiwi, kiwis, large kiwi, large kiwis, small kiwi, small kiwis, medium kiwi, medium kiwis, fruit kiwi, fruit kiwis, food kiwi, food kiwis, edible kiwi, edible kiwis, fruit kiwi, mango, mangoes, large mango, large mangoes, small mango, small mangoes, medium mango, medium mangoes, fruit mango, fruit mangoes, food mango, food mangoes, edible mango, edible mangoes, fruit mango, pineapple, pineapples, large pineapple, large pineapples, small pineapple, small pineapples, medium pineapple, medium pineapples, fruit pineapple, fruit pineapples, food pineapple, food pineapples, edible pineapple, edible pineapples, fruit pineapple, strawberries, strawberry, large strawberries, large strawberry, small strawberries, small strawberry, medium strawberries, medium strawberry, fruit strawberries, fruit strawberry, food strawberries, food strawberry, edible strawberries, edible strawberry, fruit strawberries, banana, bananas, large banana, large bananas, small banana, small bananas, medium banana, medium bananas, fruit banana, fruit bananas, food banana, food bananas, edible banana, edible bananas, fruit banana, cherry, cherries, large cherry, large cherries, small cherry, small cherries, medium cherry, medium cherries, fruit cherry, fruit cherries, food cherry, food cherries, edible cherry, edible cherries, fruit cherry, watermelon, watermelons, large watermelon, large watermelons, small watermelon, small watermelons, medium watermelon, medium watermelons, fruit watermelon, fruit watermelons, food watermelon, food watermelons, edible watermelon, edible watermelons, fruit watermelon

# dict_size(fr150)
print(aOcheck_accuracy("WithoutIP/fruits10/fr150.csv", fr150))

# %%
fr160 = {
    "Apple": ["Apple", "Apples", "Large Apple", "Large Apples", "Small Apple", "Small Apples", "Medium Apple", "Medium Apples", "Fruit Apple", "Fruit Apples", "Food Apple", "Food Apples", "Edible Apple", "Edible Apples", "Fruit Apple", "Fruit Apples"],
    "Orange": ["Orange", "Oranges", "Large Orange", "Large Oranges", "Small Orange", "Small Oranges", "Medium Orange", "Medium Oranges", "Fruit Orange", "Fruit Oranges", "Food Orange", "Food Oranges", "Edible Orange", "Edible Oranges", "Fruit Orange", "Fruit Oranges"],
    "Avocado": ["Avocado", "Avocados", "Large Avocado", "Large Avocados", "Small Avocado", "Small Avocados", "Medium Avocado", "Medium Avocados", "Fruit Avocado", "Fruit Avocados", "Food Avocado", "Food Avocados", "Edible Avocado", "Edible Avocados", "Fruit Avocado", "Fruit Avocados"],
    "Kiwi": ["Kiwi", "Kiwis", "Large Kiwi", "Large Kiwis", "Small Kiwi", "Small Kiwis", "Medium Kiwi", "Medium Kiwis", "Fruit Kiwi", "Fruit Kiwis", "Food Kiwi", "Food Kiwis", "Edible Kiwi", "Edible Kiwis", "Fruit Kiwi", "Fruit Kiwis"],
    "Mango": ["Mango", "Mangoes", "Large Mango", "Large Mangoes", "Small Mango", "Small Mangoes", "Medium Mango", "Medium Mangoes", "Fruit Mango", "Fruit Mangoes", "Food Mango", "Food Mangoes", "Edible Mango", "Edible Mangoes", "Fruit Mango", "Fruit Mangoes"],
    "Pineapple": ["Pineapple", "Pineapples", "Large Pineapple", "Large Pineapples", "Small Pineapple", "Small Pineapples", "Medium Pineapple", "Medium Pineapples", "Fruit Pineapple", "Fruit Pineapples", "Food Pineapple", "Food Pineapples", "Edible Pineapple", "Edible Pineapples", "Fruit Pineapple", "Fruit Pineapples"],
    "strawberries": ["strawberries", "strawberry", "Large strawberries", "Large strawberry", "Small strawberries", "Small strawberry", "Medium strawberries", "Medium strawberry", "Fruit strawberries", "Fruit strawberry", "Food strawberries", "Food strawberry", "Edible strawberries", "Edible strawberry", "Fruit strawberries", "Fruit strawberry"],
    "Banana": ["Banana", "Bananas", "Large Banana", "Large Bananas", "Small Banana", "Small Bananas", "Medium Banana", "Medium Bananas", "Fruit Banana", "Fruit Bananas", "Food Banana", "Food Bananas", "Edible Banana", "Edible Bananas", "Fruit Banana", "Fruit Bananas"],
    "Cherry": ["Cherry", "Cherries", "Large Cherry", "Large Cherries", "Small Cherry", "Small Cherries", "Medium Cherry", "Medium Cherries", "Fruit Cherry", "Fruit Cherries", "Food Cherry", "Food Cherries", "Edible Cherry", "Edible Cherries", "Fruit Cherry", "Fruit Cherries"],
    "Watermelon": ["Watermelon", "Watermelons", "Large Watermelon", "Large Watermelons", "Small Watermelon", "Small Watermelons", "Medium Watermelon", "Medium Watermelons", "Fruit Watermelon", "Fruit Watermelons", "Food Watermelon", "Food Watermelons", "Edible Watermelon", "Edible Watermelons", "Fruit Watermelon", "Fruit Watermelons"]
}

# Apple, Apples, Large Apple, Large Apples, Small Apple, Small Apples, Medium Apple, Medium Apples, Fruit Apple, Fruit Apples, Food Apple, Food Apples, Edible Apple, Edible Apples, Fruit Apple, Fruit Apples, Orange, Oranges, Large Orange, Large Oranges, Small Orange, Small Oranges, Medium Orange, Medium Oranges, Fruit Orange, Fruit Oranges, Food Orange, Food Oranges, Edible Orange, Edible Oranges, Fruit Orange, Fruit Oranges, Avocado, Avocados, Large Avocado, Large Avocados, Small Avocado, Small Avocados, Medium Avocado, Medium Avocados, Fruit Avocado, Fruit Avocados, Food Avocado, Food Avocados, Edible Avocado, Edible Avocados, Fruit Avocado, Fruit Avocados, Kiwi, Kiwis, Large Kiwi, Large Kiwis, Small Kiwi, Small Kiwis, Medium Kiwi, Medium Kiwis, Fruit Kiwi, Fruit Kiwis, Food Kiwi, Food Kiwis, Edible Kiwi, Edible Kiwis, Fruit Kiwi, Fruit Kiwis, Mango, Mangoes, Large Mango, Large Mangoes, Small Mango, Small Mangoes, Medium Mango, Medium Mangoes, Fruit Mango, Fruit Mangoes, Food Mango, Food Mangoes, Edible Mango, Edible Mangoes, Fruit Mango, Fruit Mangoes, Pineapple, Pineapples, Large Pineapple, Large Pineapples, Small Pineapple, Small Pineapples, Medium Pineapple, Medium Pineapples, Fruit Pineapple, Fruit Pineapples, Food Pineapple, Food Pineapples, Edible Pineapple, Edible Pineapples, Fruit Pineapple, Fruit Pineapples, strawberries, strawberry, Large strawberries, Large strawberry, Small strawberries, Small strawberry, Medium strawberries, Medium strawberry, Fruit strawberries, Fruit strawberry, Food strawberries, Food strawberry, Edible strawberries, Edible strawberry, Fruit strawberries, Fruit strawberry, Banana, Bananas, Large Banana, Large Bananas, Small Banana, Small Bananas, Medium Banana, Medium Bananas, Fruit Banana, Fruit Bananas, Food Banana, Food Bananas, Edible Banana, Edible Bananas, Fruit Banana, Fruit Bananas, Cherry, Cherries, Large Cherry, Large Cherries, Small Cherry, Small Cherries, Medium Cherry, Medium Cherries, Fruit Cherry, Fruit Cherries, Food Cherry, Food Cherries, Edible Cherry, Edible Cherries, Fruit Cherry, Fruit Cherries, Watermelon, Watermelons, Large Watermelon, Large Watermelons, Small Watermelon, Small Watermelons, Medium Watermelon, Medium Watermelons, Fruit Watermelon, Fruit Watermelons, Food Watermelon, Food Watermelons, Edible Watermelon, Edible Watermelons, Fruit Watermelon, Fruit Watermelons

# dict_size(fr160)
print(aOcheck_accuracy("WithoutIP/fruits10/fr160.csv", fr160))

# %% [markdown]
# ## Food 34

# %%
f34 = {
    "Baked Potato": ["Baked Potato"],
    "Crispy Chicken": ["Crispy Chicken"],
    "Donut": ["Donut"],
    "Fries": ["Fries"],
    "Hot Dog": ["Hot Dog"],
    "Sandwich": ["Sandwich"],
    "Taco": ["Taco"],
    "Taquito": ["Taquito"],
    "apple_pie": ["apple_pie"],
    "burger": ["burger"],
    "butter_naan": ["butter_naan"],
    "chai": ["chai"],
    "chapati": ["chapati"],
    "cheesecake": ["cheesecake"],
    "chicken_curry": ["chicken_curry"],
    "chole_bhature": ["chole_bhature"],
    "dal_makhani": ["dal_makhani"],
    "dhokla": ["dhokla"],
    "fried_rice": ["fried_rice"],
    "ice_cream": ["ice_cream"],
    "idli": ["idli"],
    "jalebi": ["jalebi"],
    "kaathi_rolls": ["kaathi_rolls"],
    "kadai_paneer": ["kadai_paneer"],
    "kulfi": ["kulfi"],
    "masala_dosa": ["masala_dosa"],
    "momos": ["momos"],
    "omelette": ["omelette"],
    "paani_puri": ["paani_puri"],
    "pakode": ["pakode"],
    "pav_bhaji": ["pav_bhaji"],
    "pizza": ["pizza"],
    "samosa": ["samosa"],
    "sushi": ["sushi"],
}

# Baked Potato, Crispy Chicken, Donut, Fries, Hot Dog, Sandwich, Taco, Taquito, apple_pie, burger, butter_naan, chai, chapati, cheesecake, chicken_curry, chole_bhature, dal_makhani, dhokla, fried_rice, ice_cream, idli, jalebi, kaathi_rolls, kadai_paneer, kulfi, masala_dosa, momos, omelette, paani_puri, pakode, pav_bhaji, pizza, samosa, sushi

dict_size(f34)
print(aOcheck_accuracy("WithoutIP/food34/f34.csv", f34))

# %%
f68 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens"],
    "Donut": ["Donut", "Donuts"],
    "Fries": ["Fries", "Fry"],
    "Hot Dog": ["Hot Dog", "Hot Dogs"],
    "Sandwich": ["Sandwich", "Sandwiches"],
    "Taco": ["Taco", "Tacos"],
    "Taquito": ["Taquito", "Taquitos"],
    "apple_pie": ["apple_pie", "apple_pies"],
    "burger": ["burger", "burgers"],
    "butter_naan": ["butter_naan", "butter_naans"],
    "chai": ["chai", "chais"],
    "chapati": ["chapati", "chapatis"],
    "cheesecake": ["cheesecake", "cheesecakes"],
    "chicken_curry": ["chicken_curry", "chicken_curries"],
    "chole_bhature": ["chole_bhature", "chole_bhatures"],
    "dal_makhani": ["dal_makhani", "dal_makhanis"],
    "dhokla": ["dhokla", "dhoklas"],
    "fried_rice": ["fried_rice", "fried_rices"],
    "ice_cream": ["ice_cream", "ice_creams"],
    "idli": ["idli", "idlis"],
    "jalebi": ["jalebi", "jalebis"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers"],
    "kulfi": ["kulfi", "kulfis"],
    "masala_dosa": ["masala_dosa", "masala_dosas"],
    "momos": ["momos", "momo"],
    "omelette": ["omelette", "omelettes"],
    "paani_puri": ["paani_puri", "paani_puris"],
    "pakode": ["pakode", "pakodas"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis"],
    "pizza": ["pizza", "pizzas"],
    "samosa": ["samosa", "samosas"],
    "sushi": ["sushi", "sushis"]
}

# Baked Potato, Baked Potatoes, Crispy Chicken, Crispy Chickens, Donut, Donuts, Fries, Fry, Hot Dog, Hot Dogs, Sandwich, Sandwiches, Taco, Tacos, Taquito, Taquitos, apple_pie, apple_pies, burger, burgers, butter_naan, butter_naans, chai, chais, chapati, chapatis, cheesecake, cheesecakes, chicken_curry, chicken_curries, chole_bhature, chole_bhatures, dal_makhani, dal_makhanis, dhokla, dhoklas, fried_rice, fried_rices, ice_cream, ice_creams, idli, idlis, jalebi, jalebis, kaathi_rolls, kaathi_roll, kadai_paneer, kadai_paneers, kulfi, kulfis, masala_dosa, masala_dosas, momos, momo, omelette, omelettes, paani_puri, paani_puris, pakode, pakodas, pav_bhaji, pav_bhajis, pizza, pizzas, samosa, samosas, sushi, sushis

# dict_size(f68)
print(aOcheck_accuracy("WithoutIP/food34/f68.csv", f68))


# %%
f102 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut"],
    "Fries": ["Fries", "Fry", "Large Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie"],
    "burger": ["burger", "burgers", "Large burger"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan"],
    "chai": ["chai", "chais", "Large chai"],
    "chapati": ["chapati", "chapatis", "Large chapati"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream"],
    "idli": ["idli", "idlis", "Large idli"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa"],
    "momos": ["momos", "momo", "Large momos"],
    "omelette": ["omelette", "omelettes", "Large omelette"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri"],
    "pakode": ["pakode", "pakodas", "Large pakode"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji"],
    "pizza": ["pizza", "pizzas", "Large pizza"],
    "samosa": ["samosa", "samosas", "Large samosa"],
    "sushi": ["sushi", "sushis", "Large sushi"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Donut, Donuts, Large Donut, Fries, Fry, Large Fries, Hot Dog, Hot Dogs, Large Hot Dog, Sandwich, Sandwiches, Large Sandwich, Taco, Tacos, Large Taco, Taquito, Taquitos, Large Taquito, apple_pie, apple_pies, Large apple_pie, burger, burgers, Large burger, butter_naan, butter_naans, Large butter_naan, chai, chais, Large chai, chapati, chapatis, Large chapati, cheesecake, cheesecakes, Large cheesecake, chicken_curry, chicken_curries, Large chicken_curry, chole_bhature, chole_bhatures, Large chole_bhature, dal_makhani, dal_makhanis, Large dal_makhani, dhokla, dhoklas, Large dhokla, fried_rice, fried_rices, Large fried_rice, ice_cream, ice_creams, Large ice_cream, idli, idlis, Large idli, jalebi, jalebis, Large jalebi, kaathi_rolls, kaathi_roll, Large kaathi_rolls, kadai_paneer, kadai_paneers, Large kadai_paneer, kulfi, kulfis, Large kulfi, masala_dosa, masala_dosas, Large masala_dosa, momos, momo, Large momos, omelette, omelettes, Large omelette, paani_puri, paani_puris, Large paani_puri, pakode, pakodas, Large pakode, pav_bhaji, pav_bhajis, Large pav_bhaji, pizza, pizzas, Large pizza, samosa, samosas, Large samosa, sushi, sushis, Large sushi

# dict_size(f102)
print(aOcheck_accuracy("WithoutIP/food34/f102.csv", f102))


# %%
f136 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans"],
    "chai": ["chai", "chais", "Large chai", "Large chais"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas"],
    "momos": ["momos", "momo", "Large momos", "Large momo"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Fries, Fry, Large Fries, Large Fry, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, apple_pie, apple_pies, Large apple_pie, Large apple_pies, burger, burgers, Large burger, Large burgers, butter_naan, butter_naans, Large butter_naan, Large butter_naans, chai, chais, Large chai, Large chais, chapati, chapatis, Large chapati, Large chapatis, cheesecake, cheesecakes, Large cheesecake, Large cheesecakes, chicken_curry, chicken_curries, Large chicken_curry, Large chicken_curries, chole_bhature, chole_bhatures, Large chole_bhature, Large chole_bhatures, dal_makhani, dal_makhanis, Large dal_makhani, Large dal_makhanis, dhokla, dhoklas, Large dhokla, Large dhoklas, fried_rice, fried_rices, Large fried_rice, Large fried_rices, ice_cream, ice_creams, Large ice_cream, Large ice_creams, idli, idlis, Large idli, Large idlis, jalebi, jalebis, Large jalebi, Large jalebis, kaathi_rolls, kaathi_roll, Large kaathi_rolls, Large kaathi_roll, kadai_paneer, kadai_paneers, Large kadai_paneer, Large kadai_paneers, kulfi, kulfis, Large kulfi, Large kulfis, masala_dosa, masala_dosas, Large masala_dosa, Large masala_dosas, momos, momo, Large momos, Large momo, omelette, omelettes, Large omelette, Large omelettes, paani_puri, paani_puris, Large paani_puri, Large paani_puris, pakode, pakodas, Large pakode, Large pakodas, pav_bhaji, pav_bhajis, Large pav_bhaji, Large pav_bhajis, pizza, pizzas, Large pizza, Large pizzas, samosa, samosas, Large samosa, Large samosas, sushi, sushis, Large sushi, Large sushis

# dict_size(f136)
print(aOcheck_accuracy("WithoutIP/food34/f136.csv", f136))


# %%
f170 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies", "Small apple_pie"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers", "Small burger"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans", "Small butter_naan"],
    "chai": ["chai", "chais", "Large chai", "Large chais", "Small chai"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis", "Small chapati"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes", "Small cheesecake"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries", "Small chicken_curry"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures", "Small chole_bhature"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis", "Small dal_makhani"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas", "Small dhokla"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices", "Small fried_rice"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams", "Small ice_cream"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis", "Small idli"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis", "Small jalebi"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll", "Small kaathi_rolls"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers", "Small kadai_paneer"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis", "Small kulfi"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas", "Small masala_dosa"],
    "momos": ["momos", "momo", "Large momos", "Large momo", "Small momos"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes", "Small omelette"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris", "Small paani_puri"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas", "Small pakode"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis", "Small pav_bhaji"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas", "Small pizza"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas", "Small samosa"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis", "Small sushi"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Fries, Fry, Large Fries, Large Fry, Small Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, apple_pie, apple_pies, Large apple_pie, Large apple_pies, Small apple_pie, burger, burgers, Large burger, Large burgers, Small burger, butter_naan, butter_naans, Large butter_naan, Large butter_naans, Small butter_naan, chai, chais, Large chai, Large chais, Small chai, chapati, chapatis, Large chapati, Large chapatis, Small chapati, cheesecake, cheesecakes, Large cheesecake, Large cheesecakes, Small cheesecake, chicken_curry, chicken_curries, Large chicken_curry, Large chicken_curries, Small chicken_curry, chole_bhature, chole_bhatures, Large chole_bhature, Large chole_bhatures, Small chole_bhature, dal_makhani, dal_makhanis, Large dal_makhani, Large dal_makhanis, Small dal_makhani, dhokla, dhoklas, Large dhokla, Large dhoklas, Small dhokla, fried_rice, fried_rices, Large fried_rice, Large fried_rices, Small fried_rice, ice_cream, ice_creams, Large ice_cream, Large ice_creams, Small ice_cream, idli, idlis, Large idli, Large idlis, Small idli, jalebi, jalebis, Large jalebi, Large jalebis, Small jalebi, kaathi_rolls, kaathi_roll, Large kaathi_rolls, Large kaathi_roll, Small kaathi_rolls, kadai_paneer, kadai_paneers, Large kadai_paneer, Large kadai_paneers, Small kadai_paneer, kulfi, kulfis, Large kulfi, Large kulfis, Small kulfi, masala_dosa, masala_dosas, Large masala_dosa, Large masala_dosas, Small masala_dosa, momos, momo, Large momos, Large momo, Small momos, omelette, omelettes, Large omelette, Large omelettes, Small omelette, paani_puri, paani_puris, Large paani_puri, Large paani_puris, Small paani_puri, pakode, pakodas, Large pakode, Large pakodas, Small pakode, pav_bhaji, pav_bhajis, Large pav_bhaji, Large pav_bhajis, Small pav_bhaji, pizza, pizzas, Large pizza, Large pizzas, Small pizza, samosa, samosas, Large samosa, Large samosas, Small samosa, sushi, sushis, Large sushi, Large sushis, Small sushi

# dict_size(f170)
print(aOcheck_accuracy("WithoutIP/food34/f170.csv", f170))


# %%
f204 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies", "Small apple_pie", "Small apple_pies"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers", "Small burger", "Small burgers"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans", "Small butter_naan", "Small butter_naans"],
    "chai": ["chai", "chais", "Large chai", "Large chais", "Small chai", "Small chais"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis", "Small chapati", "Small chapatis"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes", "Small cheesecake", "Small cheesecakes"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries", "Small chicken_curry", "Small chicken_curries"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures", "Small chole_bhature", "Small chole_bhatures"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis", "Small dal_makhani", "Small dal_makhanis"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas", "Small dhokla", "Small dhoklas"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices", "Small fried_rice", "Small fried_rices"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams", "Small ice_cream", "Small ice_creams"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis", "Small idli", "Small idlis"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis", "Small jalebi", "Small jalebis"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll", "Small kaathi_rolls", "Small kaathi_roll"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers", "Small kadai_paneer", "Small kadai_paneers"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis", "Small kulfi", "Small kulfis"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas", "Small masala_dosa", "Small masala_dosas"],
    "momos": ["momos", "momo", "Large momos", "Large momo", "Small momos", "Small momo"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes", "Small omelette", "Small omelettes"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris", "Small paani_puri", "Small paani_puris"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas", "Small pakode", "Small pakodas"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis", "Small pav_bhaji", "Small pav_bhajis"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas", "Small pizza", "Small pizzas"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas", "Small samosa", "Small samosas"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis", "Small sushi", "Small sushis"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Fries, Fry, Large Fries, Large Fry, Small Fries, Small Fry, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, apple_pie, apple_pies, Large apple_pie, Large apple_pies, Small apple_pie, Small apple_pies, burger, burgers, Large burger, Large burgers, Small burger, Small burgers, butter_naan, butter_naans, Large butter_naan, Large butter_naans, Small butter_naan, Small butter_naans, chai, chais, Large chai, Large chais, Small chai, Small chais, chapati, chapatis, Large chapati, Large chapatis, Small chapati, Small chapatis, cheesecake, cheesecakes, Large cheesecake, Large cheesecakes, Small cheesecake, Small cheesecakes, chicken_curry, chicken_curries, Large chicken_curry, Large chicken_curries, Small chicken_curry, Small chicken_curries, chole_bhature, chole_bhatures, Large chole_bhature, Large chole_bhatures, Small chole_bhature, Small chole_bhatures, dal_makhani, dal_makhanis, Large dal_makhani, Large dal_makhanis, Small dal_makhani, Small dal_makhanis, dhokla, dhoklas, Large dhokla, Large dhoklas, Small dhokla, Small dhoklas, fried_rice, fried_rices, Large fried_rice, Large fried_rices, Small fried_rice, Small fried_rices, ice_cream, ice_creams, Large ice_cream, Large ice_creams, Small ice_cream, Small ice_creams, idli, idlis, Large idli, Large idlis, Small idli, Small idlis, jalebi, jalebis, Large jalebi, Large jalebis, Small jalebi, Small jalebis, kaathi_rolls, kaathi_roll, Large kaathi_rolls, Large kaathi_roll, Small kaathi_rolls, Small kaathi_roll, kadai_paneer, kadai_paneers, Large kadai_paneer, Large kadai_paneers, Small kadai_paneer, Small kadai_paneers, kulfi, kulfis, Large kulfi, Large kulfis, Small kulfi, Small kulfis, masala_dosa, masala_dosas, Large masala_dosa, Large masala_dosas, Small masala_dosa, Small masala_dosas, momos, momo, Large momos, Large momo, Small momos, Small momo, omelette, omelettes, Large omelette, Large omelettes, Small omelette, Small omelettes, paani_puri, paani_puris, Large paani_puri, Large paani_puris, Small paani_puri, Small paani_puris, pakode, pakodas, Large pakode, Large pakodas, Small pakode, Small pakodas, pav_bhaji, pav_bhajis, Large pav_bhaji, Large pav_bhajis, Small pav_bhaji, Small pav_bhajis, pizza, pizzas, Large pizza, Large pizzas, Small pizza, Small pizzas, samosa, samosas, Large samosa, Large samosas, Small samosa, Small samosas, sushi, sushis, Large sushi, Large sushis, Small sushi, Small sushis

# dict_size(f204)
print(aOcheck_accuracy("WithoutIP/food34/f204.csv", f204))


# %%
f238 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Food Baked Potato"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Food Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Food Donut"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Food Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Food Hot Dog"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Food Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Food Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Food Taquito"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies", "Small apple_pie", "Small apple_pies", "Food apple_pie"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers", "Small burger", "Small burgers", "Food burger"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans", "Small butter_naan", "Small butter_naans", "Food butter_naan"],
    "chai": ["chai", "chais", "Large chai", "Large chais", "Small chai", "Small chais", "Food chai"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis", "Small chapati", "Small chapatis", "Food chapati"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes", "Small cheesecake", "Small cheesecakes", "Food cheesecake"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries", "Small chicken_curry", "Small chicken_curries", "Food chicken_curry"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures", "Small chole_bhature", "Small chole_bhatures", "Food chole_bhature"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis", "Small dal_makhani", "Small dal_makhanis", "Food dal_makhani"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas", "Small dhokla", "Small dhoklas", "Food dhokla"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices", "Small fried_rice", "Small fried_rices", "Food fried_rice"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams", "Small ice_cream", "Small ice_creams", "Food ice_cream"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis", "Small idli", "Small idlis", "Food idli"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis", "Small jalebi", "Small jalebis", "Food jalebi"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll", "Small kaathi_rolls", "Small kaathi_roll", "Food kaathi_rolls"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers", "Small kadai_paneer", "Small kadai_paneers", "Food kadai_paneer"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis", "Small kulfi", "Small kulfis", "Food kulfi"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas", "Small masala_dosa", "Small masala_dosas", "Food masala_dosa"],
    "momos": ["momos", "momo", "Large momos", "Large momo", "Small momos", "Small momo", "Food momos"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes", "Small omelette", "Small omelettes", "Food omelette"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris", "Small paani_puri", "Small paani_puris", "Food paani_puri"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas", "Small pakode", "Small pakodas", "Food pakode"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis", "Small pav_bhaji", "Small pav_bhajis", "Food pav_bhaji"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas", "Small pizza", "Small pizzas", "Food pizza"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas", "Small samosa", "Small samosas", "Food samosa"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis", "Small sushi", "Small sushis", "Food sushi"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Food Baked Potato, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Food Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Food Donut, Fries, Fry, Large Fries, Large Fry, Small Fries, Small Fry, Food Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Food Hot Dog, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Food Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Food Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Food Taquito, apple_pie, apple_pies, Large apple_pie, Large apple_pies, Small apple_pie, Small apple_pies, Food apple_pie, burger, burgers, Large burger, Large burgers, Small burger, Small burgers, Food burger, butter_naan, butter_naans, Large butter_naan, Large butter_naans, Small butter_naan, Small butter_naans, Food butter_naan, chai, chais, Large chai, Large chais, Small chai, Small chais, Food chai, chapati, chapatis, Large chapati, Large chapatis, Small chapati, Small chapatis, Food chapati, cheesecake, cheesecakes, Large cheesecake, Large cheesecakes, Small cheesecake, Small cheesecakes, Food cheesecake, chicken_curry, chicken_curries, Large chicken_curry, Large chicken_curries, Small chicken_curry, Small chicken_curries, Food chicken_curry, chole_bhature, chole_bhatures, Large chole_bhature, Large chole_bhatures, Small chole_bhature, Small chole_bhatures, Food chole_bhature, dal_makhani, dal_makhanis, Large dal_makhani, Large dal_makhanis, Small dal_makhani, Small dal_makhanis, Food dal_makhani, dhokla, dhoklas, Large dhokla, Large dhoklas, Small dhokla, Small dhoklas, Food dhokla, fried_rice, fried_rices, Large fried_rice, Large fried_rices, Small fried_rice, Small fried_rices, Food fried_rice, ice_cream, ice_creams, Large ice_cream, Large ice_creams, Small ice_cream, Small ice_creams, Food ice_cream, idli, idlis, Large idli, Large idlis, Small idli, Small idlis, Food idli, jalebi, jalebis, Large jalebi, Large jalebis, Small jalebi, Small jalebis, Food jalebi, kaathi_rolls, kaathi_roll, Large kaathi_rolls, Large kaathi_roll, Small kaathi_rolls, Small kaathi_roll, Food kaathi_rolls, kadai_paneer, kadai_paneers, Large kadai_paneer, Large kadai_paneers, Small kadai_paneer, Small kadai_paneers, Food kadai_paneer, kulfi, kulfis, Large kulfi, Large kulfis, Small kulfi, Small kulfis, Food kulfi, masala_dosa, masala_dosas, Large masala_dosa, Large masala_dosas, Small masala_dosa, Small masala_dosas, Food masala_dosa, momos, momo, Large momos, Large momo, Small momos, Small momo, Food momos, omelette, omelettes, Large omelette, Large omelettes, Small omelette, Small omelettes, Food omelette, paani_puri, paani_puris, Large paani_puri, Large paani_puris, Small paani_puri, Small paani_puris, Food paani_puri, pakode, pakodas, Large pakode, Large pakodas, Small pakode, Small pakodas, Food pakode, pav_bhaji, pav_bhajis, Large pav_bhaji, Large pav_bhajis, Small pav_bhaji, Small pav_bhajis, Food pav_bhaji, pizza, pizzas, Large pizza, Large pizzas, Small pizza, Small pizzas, Food pizza, samosa, samosas, Large samosa, Large samosas, Small samosa, Small samosas, Food samosa, sushi, sushis, Large sushi, Large sushis, Small sushi, Small sushis, Food sushi

# dict_size(f238)
print(aOcheck_accuracy("WithoutIP/food34/f238.csv", f238))


# %%
f272 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Food Donut", "Food Donuts"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Food Fries", "Food Fry"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Food Hot Dog", "Food Hot Dogs"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Food Sandwich", "Food Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Food Taco", "Food Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Food Taquito", "Food Taquitos"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies", "Small apple_pie", "Small apple_pies", "Food apple_pie", "Food apple_pies"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers", "Small burger", "Small burgers", "Food burger", "Food burgers"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans", "Small butter_naan", "Small butter_naans", "Food butter_naan", "Food butter_naans"],
    "chai": ["chai", "chais", "Large chai", "Large chais", "Small chai", "Small chais", "Food chai", "Food chais"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis", "Small chapati", "Small chapatis", "Food chapati", "Food chapatis"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes", "Small cheesecake", "Small cheesecakes", "Food cheesecake", "Food cheesecakes"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries", "Small chicken_curry", "Small chicken_curries", "Food chicken_curry", "Food chicken_curries"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures", "Small chole_bhature", "Small chole_bhatures", "Food chole_bhature", "Food chole_bhatures"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis", "Small dal_makhani", "Small dal_makhanis", "Food dal_makhani", "Food dal_makhanis"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas", "Small dhokla", "Small dhoklas", "Food dhokla", "Food dhoklas"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices", "Small fried_rice", "Small fried_rices", "Food fried_rice", "Food fried_rices"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams", "Small ice_cream", "Small ice_creams", "Food ice_cream", "Food ice_creams"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis", "Small idli", "Small idlis", "Food idli", "Food idlis"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis", "Small jalebi", "Small jalebis", "Food jalebi", "Food jalebis"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll", "Small kaathi_rolls", "Small kaathi_roll", "Food kaathi_rolls", "Food kaathi_roll"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers", "Small kadai_paneer", "Small kadai_paneers", "Food kadai_paneer", "Food kadai_paneers"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis", "Small kulfi", "Small kulfis", "Food kulfi", "Food kulfis"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas", "Small masala_dosa", "Small masala_dosas", "Food masala_dosa", "Food masala_dosas"],
    "momos": ["momos", "momo", "Large momos", "Large momo", "Small momos", "Small momo", "Food momos", "Food momo"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes", "Small omelette", "Small omelettes", "Food omelette", "Food omelettes"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris", "Small paani_puri", "Small paani_puris", "Food paani_puri", "Food paani_puris"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas", "Small pakode", "Small pakodas", "Food pakode", "Food pakodas"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis", "Small pav_bhaji", "Small pav_bhajis", "Food pav_bhaji", "Food pav_bhajis"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas", "Small pizza", "Small pizzas", "Food pizza", "Food pizzas"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas", "Small samosa", "Small samosas", "Food samosa", "Food samosas"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis", "Small sushi", "Small sushis", "Food sushi", "Food sushis"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Food Donut, Food Donuts, Fries, Fry, Large Fries, Large Fry, Small Fries, Small Fry, Food Fries, Food Fry, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Food Hot Dog, Food Hot Dogs, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Food Sandwich, Food Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Food Taco, Food Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Food Taquito, Food Taquitos, apple_pie, apple_pies, Large apple_pie, Large apple_pies, Small apple_pie, Small apple_pies, Food apple_pie, Food apple_pies, burger, burgers, Large burger, Large burgers, Small burger, Small burgers, Food burger, Food burgers, butter_naan, butter_naans, Large butter_naan, Large butter_naans, Small butter_naan, Small butter_naans, Food butter_naan, Food butter_naans, chai, chais, Large chai, Large chais, Small chai, Small chais, Food chai, Food chais, chapati, chapatis, Large chapati, Large chapatis, Small chapati, Small chapatis, Food chapati, Food chapatis, cheesecake, cheesecakes, Large cheesecake, Large cheesecakes, Small cheesecake, Small cheesecakes, Food cheesecake, Food cheesecakes, chicken_curry, chicken_curries, Large chicken_curry, Large chicken_curries, Small chicken_curry, Small chicken_curries, Food chicken_curry, Food chicken_curries, chole_bhature, chole_bhatures, Large chole_bhature, Large chole_bhatures, Small chole_bhature, Small chole_bhatures, Food chole_bhature, Food chole_bhatures, dal_makhani, dal_makhanis, Large dal_makhani, Large dal_makhanis, Small dal_makhani, Small dal_makhanis, Food dal_makhani, Food dal_makhanis, dhokla, dhoklas, Large dhokla, Large dhoklas, Small dhokla, Small dhoklas, Food dhokla, Food dhoklas, fried_rice, fried_rices, Large fried_rice, Large fried_rices, Small fried_rice, Small fried_rices, Food fried_rice, Food fried_rices, ice_cream, ice_creams, Large ice_cream, Large ice_creams, Small ice_cream, Small ice_creams, Food ice_cream, Food ice_creams, idli, idlis, Large idli, Large idlis, Small idli, Small idlis, Food idli, Food idlis, jalebi, jalebis, Large jalebi, Large jalebis, Small jalebi, Small jalebis, Food jalebi, Food jalebis, kaathi_rolls, kaathi_roll, Large kaathi_rolls, Large kaathi_roll, Small kaathi_rolls, Small kaathi_roll, Food kaathi_rolls, Food kaathi_roll, kadai_paneer, kadai_paneers, Large kadai_paneer, Large kadai_paneers, Small kadai_paneer, Small kadai_paneers, Food kadai_paneer, Food kadai_paneers, kulfi, kulfis, Large kulfi, Large kulfis, Small kulfi, Small kulfis, Food kulfi, Food kulfis, masala_dosa, masala_dosas, Large masala_dosa, Large masala_dosas, Small masala_dosa, Small masala_dosas, Food masala_dosa, Food masala_dosas, momos, momo, Large momos, Large momo, Small momos, Small momo, Food momos, Food momo, omelette, omelettes, Large omelette, Large omelettes, Small omelette, Small omelettes, Food omelette, Food omelettes, paani_puri, paani_puris, Large paani_puri, Large paani_puris, Small paani_puri, Small paani_puris, Food paani_puri, Food paani_puris, pakode, pakodas, Large pakode, Large pakodas, Small pakode, Small pakodas, Food pakode, Food pakodas, pav_bhaji, pav_bhajis, Large pav_bhaji, Large pav_bhajis, Small pav_bhaji, Small pav_bhajis, Food pav_bhaji, Food pav_bhajis, pizza, pizzas, Large pizza, Large pizzas, Small pizza, Small pizzas, Food pizza, Food pizzas, samosa, samosas, Large samosa, Large samosas, Small samosa, Small samosas, Food samosa, Food samosas, sushi, sushis, Large sushi, Large sushis, Small sushi, Small sushis, Food sushi, Food sushis

# dict_size(f272)
print(aOcheck_accuracy("WithoutIP/food34/f272.csv", f272))


# %%
f306 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Medium Baked Potato"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Medium Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Food Donut", "Food Donuts", "Medium Donut"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Food Fries", "Food Fry", "Medium Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Medium Hot Dog"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Food Sandwich", "Food Sandwiches", "Medium Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Food Taco", "Food Tacos", "Medium Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Food Taquito", "Food Taquitos", "Medium Taquito"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies", "Small apple_pie", "Small apple_pies", "Food apple_pie", "Food apple_pies", "Medium apple_pie"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers", "Small burger", "Small burgers", "Food burger", "Food burgers", "Medium burger"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans", "Small butter_naan", "Small butter_naans", "Food butter_naan", "Food butter_naans", "Medium butter_naan"],
    "chai": ["chai", "chais", "Large chai", "Large chais", "Small chai", "Small chais", "Food chai", "Food chais", "Medium chai"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis", "Small chapati", "Small chapatis", "Food chapati", "Food chapatis", "Medium chapati"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes", "Small cheesecake", "Small cheesecakes", "Food cheesecake", "Food cheesecakes", "Medium cheesecake"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries", "Small chicken_curry", "Small chicken_curries", "Food chicken_curry", "Food chicken_curries", "Medium chicken_curry"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures", "Small chole_bhature", "Small chole_bhatures", "Food chole_bhature", "Food chole_bhatures", "Medium chole_bhature"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis", "Small dal_makhani", "Small dal_makhanis", "Food dal_makhani", "Food dal_makhanis", "Medium dal_makhani"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas", "Small dhokla", "Small dhoklas", "Food dhokla", "Food dhoklas", "Medium dhokla"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices", "Small fried_rice", "Small fried_rices", "Food fried_rice", "Food fried_rices", "Medium fried_rice"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams", "Small ice_cream", "Small ice_creams", "Food ice_cream", "Food ice_creams", "Medium ice_cream"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis", "Small idli", "Small idlis", "Food idli", "Food idlis", "Medium idli"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis", "Small jalebi", "Small jalebis", "Food jalebi", "Food jalebis", "Medium jalebi"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll", "Small kaathi_rolls", "Small kaathi_roll", "Food kaathi_rolls", "Food kaathi_roll", "Medium kaathi_rolls"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers", "Small kadai_paneer", "Small kadai_paneers", "Food kadai_paneer", "Food kadai_paneers", "Medium kadai_paneer"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis", "Small kulfi", "Small kulfis", "Food kulfi", "Food kulfis", "Medium kulfi"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas", "Small masala_dosa", "Small masala_dosas", "Food masala_dosa", "Food masala_dosas", "Medium masala_dosa"],
    "momos": ["momos", "momo", "Large momos", "Large momo", "Small momos", "Small momo", "Food momos", "Food momo", "Medium momos"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes", "Small omelette", "Small omelettes", "Food omelette", "Food omelettes", "Medium omelette"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris", "Small paani_puri", "Small paani_puris", "Food paani_puri", "Food paani_puris", "Medium paani_puri"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas", "Small pakode", "Small pakodas", "Food pakode", "Food pakodas", "Medium pakode"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis", "Small pav_bhaji", "Small pav_bhajis", "Food pav_bhaji", "Food pav_bhajis", "Medium pav_bhaji"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas", "Small pizza", "Small pizzas", "Food pizza", "Food pizzas", "Medium pizza"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas", "Small samosa", "Small samosas", "Food samosa", "Food samosas", "Medium samosa"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis", "Small sushi", "Small sushis", "Food sushi", "Food sushis", "Medium sushi"]
}

dict_size(f306)
print(aOcheck_accuracy("WithoutIP/food34/f306.csv", f306))
# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Medium Baked Potato, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Medium Crispy Chicken, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Food Donut, Food Donuts, Medium Donut, Fries, Fry, Large Fries, Large Fry, Small Fries, Small Fry, Food Fries, Food Fry, Medium Fries, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Food Hot Dog, Food Hot Dogs, Medium Hot Dog, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Food Sandwich, Food Sandwiches, Medium Sandwich, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Food Taco, Food Tacos, Medium Taco, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Food Taquito, Food Taquitos, Medium Taquito, apple_pie, apple_pies, Large apple_pie, Large apple_pies, Small apple_pie, Small apple_pies, Food apple_pie, Food apple_pies, Medium apple_pie, burger, burgers, Large burger, Large burgers, Small burger, Small burgers, Food burger, Food burgers, Medium burger, butter_naan, butter_naans, Large butter_naan, Large butter_naans, Small butter_naan, Small butter_naans, Food butter_naan, Food butter_naans, Medium butter_naan, chai, chais, Large chai, Large chais, Small chai, Small chais, Food chai, Food chais, Medium chai, chapati, chapatis, Large chapati, Large chapatis, Small chapati, Small chapatis, Food chapati, Food chapatis, Medium chapati, cheesecake, cheesecakes, Large cheesecake, Large cheesecakes, Small cheesecake, Small cheesecakes, Food cheesecake, Food cheesecakes, Medium cheesecake, chicken_curry, chicken_curries, Large chicken_curry, Large chicken_curries, Small chicken_curry, Small chicken_curries, Food chicken_curry, Food chicken_curries, Medium chicken_curry, chole_bhature, chole_bhatures, Large chole_bhature, Large chole_bhatures, Small chole_bhature, Small chole_bhatures, Food chole_bhature, Food chole_bhatures, Medium chole_bhature, dal_makhani, dal_makhanis, Large dal_makhani, Large dal_makhanis, Small dal_makhani, Small dal_makhanis, Food dal_makhani, Food dal_makhanis, Medium dal_makhani, dhokla, dhoklas, Large dhokla, Large dhoklas, Small dhokla, Small dhoklas, Food dhokla, Food dhoklas, Medium dhokla, fried_rice, fried_rices, Large fried_rice, Large fried_rices, Small fried_rice, Small fried_rices, Food fried_rice, Food fried_rices, Medium fried_rice, ice_cream, ice_creams, Large ice_cream, Large ice_creams, Small ice_cream, Small ice_creams, Food ice_cream, Food ice_creams, Medium ice_cream, idli, idlis, Large idli, Large idlis, Small idli, Small idlis, Food idli, Food idlis, Medium idli, jalebi, jalebis, Large jalebi, Large jalebis, Small jalebi, Small jalebis, Food jalebi, Food jalebis, Medium jalebi, kaathi_rolls, kaathi_roll, Large kaathi_rolls, Large kaathi_roll, Small kaathi_rolls, Small kaathi_roll, Food kaathi_rolls, Food kaathi_roll, Medium kaathi_rolls, kadai_paneer, kadai_paneers, Large kadai_paneer, Large kadai_paneers, Small kadai_paneer, Small kadai_paneers, Food kadai_paneer, Food kadai_paneers, Medium kadai_paneer, kulfi, kulfis, Large kulfi, Large kulfis, Small kulfi, Small kulfis, Food kulfi, Food kulfis, Medium kulfi, masala_dosa, masala_dosas, Large masala_dosa, Large masala_dosas, Small masala_dosa, Small masala_dosas, Food masala_dosa, Food masala_dosas, Medium masala_dosa, momos, momo, Large momos, Large momo, Small momos, Small momo, Food momos, Food momo, Medium momos, omelette, omelettes, Large omelette, Large omelettes, Small omelette, Small omelettes, Food omelette, Food omelettes, Medium omelette, paani_puri, paani_puris, Large paani_puri, Large paani_puris, Small paani_puri, Small paani_puris, Food paani_puri, Food paani_puris, Medium paani_puri, pakode, pakodas, Large pakode, Large pakodas, Small pakode, Small pakodas, Food pakode, Food pakodas, Medium pakode, pav_bhaji, pav_bhajis, Large pav_bhaji, Large pav_bhajis, Small pav_bhaji, Small pav_bhajis, Food pav_bhaji, Food pav_bhajis, Medium pav_bhaji, pizza, pizzas, Large pizza, Large pizzas, Small pizza, Small pizzas, Food pizza, Food pizzas, Medium pizza, samosa, samosas, Large samosa, Large samosas, Small samosa, Small samosas, Food samosa, Food samosas, Medium samosa, sushi, sushis, Large sushi, Large sushis, Small sushi, Small sushis, Food sushi, Food sushis, Medium sushi


# %%
f340 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Food Donut", "Food Donuts", "Medium Donut", "Medium Donuts"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Food Fries", "Food Fry", "Medium Fries", "Medium Fry"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Food Sandwich", "Food Sandwiches", "Medium Sandwich", "Medium Sandwiches"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Food Taco", "Food Tacos", "Medium Taco", "Medium Tacos"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Food Taquito", "Food Taquitos", "Medium Taquito", "Medium Taquitos"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies", "Small apple_pie", "Small apple_pies", "Food apple_pie", "Food apple_pies", "Medium apple_pie", "Medium apple_pies"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers", "Small burger", "Small burgers", "Food burger", "Food burgers", "Medium burger", "Medium burgers"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans", "Small butter_naan", "Small butter_naans", "Food butter_naan", "Food butter_naans", "Medium butter_naan", "Medium butter_naans"],
    "chai": ["chai", "chais", "Large chai", "Large chais", "Small chai", "Small chais", "Food chai", "Food chais", "Medium chai", "Medium chais"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis", "Small chapati", "Small chapatis", "Food chapati", "Food chapatis", "Medium chapati", "Medium chapatis"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes", "Small cheesecake", "Small cheesecakes", "Food cheesecake", "Food cheesecakes", "Medium cheesecake", "Medium cheesecakes"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries", "Small chicken_curry", "Small chicken_curries", "Food chicken_curry", "Food chicken_curries", "Medium chicken_curry", "Medium chicken_curries"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures", "Small chole_bhature", "Small chole_bhatures", "Food chole_bhature", "Food chole_bhatures", "Medium chole_bhature", "Medium chole_bhatures"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis", "Small dal_makhani", "Small dal_makhanis", "Food dal_makhani", "Food dal_makhanis", "Medium dal_makhani", "Medium dal_makhanis"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas", "Small dhokla", "Small dhoklas", "Food dhokla", "Food dhoklas", "Medium dhokla", "Medium dhoklas"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices", "Small fried_rice", "Small fried_rices", "Food fried_rice", "Food fried_rices", "Medium fried_rice", "Medium fried_rices"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams", "Small ice_cream", "Small ice_creams", "Food ice_cream", "Food ice_creams", "Medium ice_cream", "Medium ice_creams"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis", "Small idli", "Small idlis", "Food idli", "Food idlis", "Medium idli", "Medium idlis"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis", "Small jalebi", "Small jalebis", "Food jalebi", "Food jalebis", "Medium jalebi", "Medium jalebis"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll", "Small kaathi_rolls", "Small kaathi_roll", "Food kaathi_rolls", "Food kaathi_roll", "Medium kaathi_rolls", "Medium kaathi_roll"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers", "Small kadai_paneer", "Small kadai_paneers", "Food kadai_paneer", "Food kadai_paneers", "Medium kadai_paneer", "Medium kadai_paneers"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis", "Small kulfi", "Small kulfis", "Food kulfi", "Food kulfis", "Medium kulfi", "Medium kulfis"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas", "Small masala_dosa", "Small masala_dosas", "Food masala_dosa", "Food masala_dosas", "Medium masala_dosa", "Medium masala_dosas"],
    "momos": ["momos", "momo", "Large momos", "Large momo", "Small momos", "Small momo", "Food momos", "Food momo", "Medium momos", "Medium momo"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes", "Small omelette", "Small omelettes", "Food omelette", "Food omelettes", "Medium omelette", "Medium omelettes"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris", "Small paani_puri", "Small paani_puris", "Food paani_puri", "Food paani_puris", "Medium paani_puri", "Medium paani_puris"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas", "Small pakode", "Small pakodas", "Food pakode", "Food pakodas", "Medium pakode", "Medium pakodas"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis", "Small pav_bhaji", "Small pav_bhajis", "Food pav_bhaji", "Food pav_bhajis", "Medium pav_bhaji", "Medium pav_bhajis"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas", "Small pizza", "Small pizzas", "Food pizza", "Food pizzas", "Medium pizza", "Medium pizzas"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas", "Small samosa", "Small samosas", "Food samosa", "Food samosas", "Medium samosa", "Medium samosas"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis", "Small sushi", "Small sushis", "Food sushi", "Food sushi", "Medium sushi", "Medium sushis"]
}

# Baked Potato, Baked Potatoes, Large Baked Potato, Large Baked Potatoes, Small Baked Potato, Small Baked Potatoes, Food Baked Potato, Food Baked Potatoes, Medium Baked Potato, Medium Baked Potatoes, Crispy Chicken, Crispy Chickens, Large Crispy Chicken, Large Crispy Chickens, Small Crispy Chicken, Small Crispy Chickens, Food Crispy Chicken, Food Crispy Chickens, Medium Crispy Chicken, Medium Crispy Chickens, Donut, Donuts, Large Donut, Large Donuts, Small Donut, Small Donuts, Food Donut, Food Donuts, Medium Donut, Medium Donuts, Fries, Fry, Large Fries, Large Fry, Small Fries, Small Fry, Food Fries, Food Fry, Medium Fries, Medium Fry, Hot Dog, Hot Dogs, Large Hot Dog, Large Hot Dogs, Small Hot Dog, Small Hot Dogs, Food Hot Dog, Food Hot Dogs, Medium Hot Dog, Medium Hot Dogs, Sandwich, Sandwiches, Large Sandwich, Large Sandwiches, Small Sandwich, Small Sandwiches, Food Sandwich, Food Sandwiches, Medium Sandwich, Medium Sandwiches, Taco, Tacos, Large Taco, Large Tacos, Small Taco, Small Tacos, Food Taco, Food Tacos, Medium Taco, Medium Tacos, Taquito, Taquitos, Large Taquito, Large Taquitos, Small Taquito, Small Taquitos, Food Taquito, Food Taquitos, Medium Taquito, Medium Taquitos, apple_pie, apple_pies, Large apple_pie, Large apple_pies, Small apple_pie, Small apple_pies, Food apple_pie, Food apple_pies, Medium apple_pie, Medium apple_pies, burger, burgers, Large burger, Large burgers, Small burger, Small burgers, Food burger, Food burgers, Medium burger, Medium burgers, butter_naan, butter_naans, Large butter_naan, Large butter_naans, Small butter_naan, Small butter_naans, Food butter_naan, Food butter_naans, Medium butter_naan, Medium butter_naans, chai, chais, Large chai, Large chais, Small chai, Small chais, Food chai, Food chais, Medium chai, Medium chais, chapati, chapatis, Large chapati, Large chapatis, Small chapati, Small chapatis, Food chapati, Food chapatis, Medium chapati, Medium chapatis, cheesecake, cheesecakes, Large cheesecake, Large cheesecakes, Small cheesecake, Small cheesecakes, Food cheesecake, Food cheesecakes, Medium cheesecake, Medium cheesecakes, chicken_curry, chicken_curries, Large chicken_curry, Large chicken_curries, Small chicken_curry, Small chicken_curries, Food chicken_curry, Food chicken_curries, Medium chicken_curry, Medium chicken_curries, chole_bhature, chole_bhatures, Large chole_bhature, Large chole_bhatures, Small chole_bhature, Small chole_bhatures, Food chole_bhature, Food chole_bhatures, Medium chole_bhature, Medium chole_bhatures, dal_makhani, dal_makhanis, Large dal_makhani, Large dal_makhanis, Small dal_makhani, Small dal_makhanis, Food dal_makhani, Food dal_makhanis, Medium dal_makhani, Medium dal_makhanis, dhokla, dhoklas, Large dhokla, Large dhoklas, Small dhokla, Small dhoklas, Food dhokla, Food dhoklas, Medium dhokla, Medium dhoklas, fried_rice, fried_rices, Large fried_rice, Large fried_rices, Small fried_rice, Small fried_rices, Food fried_rice, Food fried_rices, Medium fried_rice, Medium fried_rices, ice_cream, ice_creams, Large ice_cream, Large ice_creams, Small ice_cream, Small ice_creams, Food ice_cream, Food ice_creams, Medium ice_cream, Medium ice_creams, idli, idlis, Large idli, Large idlis, Small idli, Small idlis, Food idli, Food idlis, Medium idli, Medium idlis, jalebi, jalebis, Large jalebi, Large jalebis, Small jalebi, Small jalebis, Food jalebi, Food jalebis, Medium jalebi, Medium jalebis, kaathi_rolls, kaathi_roll, Large kaathi_rolls, Large kaathi_roll, Small kaathi_rolls, Small kaathi_roll, Food kaathi_rolls, Food kaathi_roll, Medium kaathi_rolls, Medium kaathi_roll, kadai_paneer, kadai_paneers, Large kadai_paneer, Large kadai_paneers, Small kadai_paneer, Small kadai_paneers, Food kadai_paneer, Food kadai_paneers, Medium kadai_paneer, Medium kadai_paneers, kulfi, kulfis, Large kulfi, Large kulfis, Small kulfi, Small kulfis, Food kulfi, Food kulfis, Medium kulfi, Medium kulfis, masala_dosa, masala_dosas, Large masala_dosa, Large masala_dosas, Small masala_dosa, Small masala_dosas, Food masala_dosa, Food masala_dosas, Medium masala_dosa, Medium masala_dosas, momos, momo, Large momos, Large momo, Small momos, Small momo, Food momos, Food momo, Medium momos, Medium momo, omelette, omelettes, Large omelette, Large omelettes, Small omelette, Small omelettes, Food omelette, Food omelettes, Medium omelette, Medium omelettes, paani_puri, paani_puris, Large paani_puri, Large paani_puris, Small paani_puri, Small paani_puris, Food paani_puri, Food paani_puris, Medium paani_puri, Medium paani_puris, pakode, pakodas, Large pakode, Large pakodas, Small pakode, Small pakodas, Food pakode, Food pakodas, Medium pakode, Medium pakodas, pav_bhaji, pav_bhajis, Large pav_bhaji, Large pav_bhajis, Small pav_bhaji, Small pav_bhajis, Food pav_bhaji, Food pav_bhajis, Medium pav_bhaji, Medium pav_bhajis, pizza, pizzas, Large pizza, Large pizzas, Small pizza, Small pizzas, Food pizza, Food pizzas, Medium pizza, Medium pizzas, samosa, samosas, Large samosa, Large samosas, Small samosa, Small samosas, Food samosa, Food samosas, Medium samosa, Medium samosas, sushi, sushis, Large sushi, Large sushis, Small sushi, Small sushis, Food sushi, Food sushi, Medium sushi, Medium sushis

# dict_size(f306)
print(aOcheck_accuracy("WithoutIP/food34/f306.csv", f340))


# %%
f372 = {
    "Baked Potato": ["Baked Potato", "Baked Potatoes", "Large Baked Potato", "Large Baked Potatoes", "Small Baked Potato", "Small Baked Potatoes", "Food Baked Potato", "Food Baked Potatoes", "Medium Baked Potato", "Medium Baked Potatoes", "Tiny Baked Potato"],
    "Crispy Chicken": ["Crispy Chicken", "Crispy Chickens", "Large Crispy Chicken", "Large Crispy Chickens", "Small Crispy Chicken", "Small Crispy Chickens", "Food Crispy Chicken", "Food Crispy Chickens", "Medium Crispy Chicken", "Medium Crispy Chickens", "Tiny Crispy Chicken"],
    "Donut": ["Donut", "Donuts", "Large Donut", "Large Donuts", "Small Donut", "Small Donuts", "Food Donut", "Food Donuts", "Medium Donut", "Medium Donuts", "Tiny Donut"],
    "Fries": ["Fries", "Fry", "Large Fries", "Large Fry", "Small Fries", "Small Fry", "Food Fries", "Food Fry", "Medium Fries", "Medium Fry", "Tiny Fries"],
    "Hot Dog": ["Hot Dog", "Hot Dogs", "Large Hot Dog", "Large Hot Dogs", "Small Hot Dog", "Small Hot Dogs", "Food Hot Dog", "Food Hot Dogs", "Medium Hot Dog", "Medium Hot Dogs", "Tiny Hot Dog"],
    "Sandwich": ["Sandwich", "Sandwiches", "Large Sandwich", "Large Sandwiches", "Small Sandwich", "Small Sandwiches", "Food Sandwich", "Food Sandwiches", "Medium Sandwich", "Medium Sandwiches", "Tiny Sandwich"],
    "Taco": ["Taco", "Tacos", "Large Taco", "Large Tacos", "Small Taco", "Small Tacos", "Food Taco", "Food Tacos", "Medium Taco", "Medium Tacos", "Tiny Taco"],
    "Taquito": ["Taquito", "Taquitos", "Large Taquito", "Large Taquitos", "Small Taquito", "Small Taquitos", "Food Taquito", "Food Taquitos", "Medium Taquito", "Medium Taquitos", "Tiny Taquito"],
    "apple_pie": ["apple_pie", "apple_pies", "Large apple_pie", "Large apple_pies", "Small apple_pie", "Small apple_pies", "Food apple_pie", "Food apple_pies", "Medium apple_pie", "Medium apple_pies", "Tiny apple_pie"],
    "burger": ["burger", "burgers", "Large burger", "Large burgers", "Small burger", "Small burgers", "Food burger", "Food burgers", "Medium burger", "Medium burgers", "Tiny burger"],
    "butter_naan": ["butter_naan", "butter_naans", "Large butter_naan", "Large butter_naans", "Small butter_naan", "Small butter_naans", "Food butter_naan", "Food butter_naans", "Medium butter_naan", "Medium butter_naans", "Tiny butter_naan"],
    "chai": ["chai", "chais", "Large chai", "Large chais", "Small chai", "Small chais", "Food chai", "Food chais", "Medium chai", "Medium chais", "Tiny chai"],
    "chapati": ["chapati", "chapatis", "Large chapati", "Large chapatis", "Small chapati", "Small chapatis", "Food chapati", "Food chapatis", "Medium chapati", "Medium chapatis", "Tiny chapati"],
    "cheesecake": ["cheesecake", "cheesecakes", "Large cheesecake", "Large cheesecakes", "Small cheesecake", "Small cheesecakes", "Food cheesecake", "Food cheesecakes", "Medium cheesecake", "Medium cheesecakes", "Tiny cheesecake"],
    "chicken_curry": ["chicken_curry", "chicken_curries", "Large chicken_curry", "Large chicken_curries", "Small chicken_curry", "Small chicken_curries", "Food chicken_curry", "Food chicken_curries", "Medium chicken_curry", "Medium chicken_curries", "Tiny chicken_curry"],
    "chole_bhature": ["chole_bhature", "chole_bhatures", "Large chole_bhature", "Large chole_bhatures", "Small chole_bhature", "Small chole_bhatures", "Food chole_bhature", "Food chole_bhatures", "Medium chole_bhature", "Medium chole_bhatures", "Tiny chole_bhature"],
    "dal_makhani": ["dal_makhani", "dal_makhanis", "Large dal_makhani", "Large dal_makhanis", "Small dal_makhani", "Small dal_makhanis", "Food dal_makhani", "Food dal_makhanis", "Medium dal_makhani", "Medium dal_makhanis", "Tiny dal_makhani"],
    "dhokla": ["dhokla", "dhoklas", "Large dhokla", "Large dhoklas", "Small dhokla", "Small dhoklas", "Food dhokla", "Food dhoklas", "Medium dhokla", "Medium dhoklas", "Tiny dhokla"],
    "fried_rice": ["fried_rice", "fried_rices", "Large fried_rice", "Large fried_rices", "Small fried_rice", "Small fried_rices", "Food fried_rice", "Food fried_rices", "Medium fried_rice", "Medium fried_rices", "Tiny fried_rice"],
    "ice_cream": ["ice_cream", "ice_creams", "Large ice_cream", "Large ice_creams", "Small ice_cream", "Small ice_creams", "Food ice_cream", "Food ice_creams", "Medium ice_cream", "Medium ice_creams", "Tiny ice_cream"],
    "idli": ["idli", "idlis", "Large idli", "Large idlis", "Small idli", "Small idlis", "Food idli", "Food idlis", "Medium idli", "Medium idlis", "Tiny idli"],
    "jalebi": ["jalebi", "jalebis", "Large jalebi", "Large jalebis", "Small jalebi", "Small jalebis", "Food jalebi", "Food jalebis", "Medium jalebi", "Medium jalebis", "Tiny jalebi"],
    "kaathi_rolls": ["kaathi_rolls", "kaathi_roll", "Large kaathi_rolls", "Large kaathi_roll", "Small kaathi_rolls", "Small kaathi_roll", "Food kaathi_rolls", "Food kaathi_roll", "Medium kaathi_rolls", "Medium kaathi_roll", "Tiny kaathi_rolls"],
    "kadai_paneer": ["kadai_paneer", "kadai_paneers", "Large kadai_paneer", "Large kadai_paneers", "Small kadai_paneer", "Small kadai_paneers", "Food kadai_paneer", "Food kadai_paneers", "Medium kadai_paneer", "Medium kadai_paneers", "Tiny kadai_paneer"],
    "kulfi": ["kulfi", "kulfis", "Large kulfi", "Large kulfis", "Small kulfi", "Small kulfis", "Food kulfi", "Food kulfis", "Medium kulfi", "Medium kulfis", "Tiny kulfi"],
    "masala_dosa": ["masala_dosa", "masala_dosas", "Large masala_dosa", "Large masala_dosas", "Small masala_dosa", "Small masala_dosas", "Food masala_dosa", "Food masala_dosas", "Medium masala_dosa", "Medium masala_dosas", "Tiny masala_dosa"],
    "momos": ["momos", "momo", "Large momos", "Large momo", "Small momos", "Small momo", "Food momos", "Food momo", "Medium momos", "Medium momo", "Tiny momos"],
    "omelette": ["omelette", "omelettes", "Large omelette", "Large omelettes", "Small omelette", "Small omelettes", "Food omelette", "Food omelettes", "Medium omelette", "Medium omelettes", "Tiny omelette"],
    "paani_puri": ["paani_puri", "paani_puris", "Large paani_puri", "Large paani_puris", "Small paani_puri", "Small paani_puris", "Food paani_puri", "Food paani_puris", "Medium paani_puri", "Medium paani_puris", "Tiny paani_puri"],
    "pakode": ["pakode", "pakodas", "Large pakode", "Large pakodas", "Small pakode", "Small pakodas", "Food pakode", "Food pakodas", "Medium pakode", "Medium pakodas", "Tiny pakode"],
    "pav_bhaji": ["pav_bhaji", "pav_bhajis", "Large pav_bhaji", "Large pav_bhajis", "Small pav_bhaji", "Small pav_bhajis", "Food pav_bhaji", "Food pav_bhajis", "Medium pav_bhaji", "Medium pav_bhajis", "Tiny pav_bhaji"],
    "pizza": ["pizza", "pizzas", "Large pizza", "Large pizzas", "Small pizza", "Small pizzas", "Food pizza", "Food pizzas", "Medium pizza", "Medium pizzas", "Tiny pizza"],
    "samosa": ["samosa", "samosas", "Large samosa", "Large samosas", "Small samosa", "Small samosas", "Food samosa", "Food samosas", "Medium samosa", "Medium samosas", "Tiny samosa"],
    "sushi": ["sushi", "sushis", "Large sushi", "Large sushis", "Small sushi", "Small sushis", "Food sushi", "Food sushis", "Medium sushi", "Medium sushis", "Tiny sushi"]
}

# baked potato, baked potatoes, large baked potato, large baked potatoes, small baked potato, small baked potatoes, food baked potato, food baked potatoes, medium baked potato, medium baked potatoes, tiny baked potato, crispy chicken, crispy chickens, large crispy chicken, large crispy chickens, small crispy chicken, small crispy chickens, food crispy chicken, food crispy chickens, medium crispy chicken, medium crispy chickens, tiny crispy chicken, donut, donuts, large donut, large donuts, small donut, small donuts, food donut, food donuts, medium donut, medium donuts, tiny donut, fries, fry, large fries, large fry, small fries, small fry, food fries, food fry, medium fries, medium fry, tiny fries, hot dog, hot dogs, large hot dog, large hot dogs, small hot dog, small hot dogs, food hot dog, food hot dogs, medium hot dog, medium hot dogs, tiny hot dog, sandwich, sandwiches, large sandwich, large sandwiches, small sandwich, small sandwiches, food sandwich, food sandwiches, medium sandwich, medium sandwiches, tiny sandwich, taco, tacos, large taco, large tacos, small taco, small tacos, food taco, food tacos, medium taco, medium tacos, tiny taco, taquito, taquitos, large taquito, large taquitos, small taquito, small taquitos, food taquito, food taquitos, medium taquito, medium taquitos, tiny taquito, apple_pie, apple_pies, large apple_pie, large apple_pies, small apple_pie, small apple_pies, food apple_pie, food apple_pies, medium apple_pie, medium apple_pies, tiny apple_pie, burger, burgers, large burger, large burgers, small burger, small burgers, food burger, food burgers, medium burger, medium burgers, tiny burger, butter_naan, butter_naans, large butter_naan, large butter_naans, small butter_naan, small butter_naans, food butter_naan, food butter_naans, medium butter_naan, medium butter_naans, tiny butter_naan, chai, chais, large chai, large chais, small chai, small chais, food chai, food chais, medium chai, medium chais, tiny chai, chapati, chapatis, large chapati, large chapatis, small chapati, small chapatis, food chapati, food chapatis, medium chapati, medium chapatis, tiny chapati, cheesecake, cheesecakes, large cheesecake, large cheesecakes, small cheesecake, small cheesecakes, food cheesecake, food cheesecakes, medium cheesecake, medium cheesecakes, tiny cheesecake, chicken_curry, chicken_curries, large chicken_curry, large chicken_curries, small chicken_curry, small chicken_curries, food chicken_curry, food chicken_curries, medium chicken_curry, medium chicken_curries, tiny chicken_curry, chole_bhature, chole_bhatures, large chole_bhature, large chole_bhatures, small chole_bhature, small chole_bhatures, food chole_bhature, food chole_bhatures, medium chole_bhature, medium chole_bhatures, tiny chole_bhature, dal_makhani, dal_makhanis, large dal_makhani, large dal_makhanis, small dal_makhani, small dal_makhanis, food dal_makhani, food dal_makhanis, medium dal_makhani, medium dal_makhanis, tiny dal_makhani, dhokla, dhoklas, large dhokla, large dhoklas, small dhokla, small dhoklas, food dhokla, food dhoklas, medium dhokla, medium dhoklas, tiny dhokla, fried_rice, fried_rices, large fried_rice, large fried_rices, small fried_rice, small fried_rices, food fried_rice, food fried_rices, medium fried_rice, medium fried_rices, tiny fried_rice, ice_cream, ice_creams, large ice_cream, large ice_creams, small ice_cream, small ice_creams, food ice_cream, food ice_creams, medium ice_cream, medium ice_creams, tiny ice_cream, idli, idlis, large idli, large idlis, small idli, small idlis, food idli, food idlis, medium idli, medium idlis, tiny idli, jalebi, jalebis, large jalebi, large jalebis, small jalebi, small jalebis, food jalebi, food jalebis, medium jalebi, medium jalebis, tiny jalebi, kaathi_rolls, kaathi_roll, large kaathi_rolls, large kaathi_roll, small kaathi_rolls, small kaathi_roll, food kaathi_rolls, food kaathi_roll, medium kaathi_rolls, medium kaathi_roll, tiny kaathi_rolls, kadai_paneer, kadai_paneers, large kadai_paneer, large kadai_paneers, small kadai_paneer, small kadai_paneers, food kadai_paneer, food kadai_paneers, medium kadai_paneer, medium kadai_paneers, tiny kadai_paneer, kulfi, kulfis, large kulfi, large kulfis, small kulfi, small kulfis, food kulfi, food kulfis, medium kulfi, medium kulfis, tiny kulfi, masala_dosa, masala_dosas, large masala_dosa, large masala_dosas, small masala_dosa, small masala_dosas, food masala_dosa, food masala_dosas, medium masala_dosa, medium masala_dosas, tiny masala_dosa, momos, momo, large momos, large momo, small momos, small momo, food momos, food momo, medium momos, medium momo, tiny momos, omelette, omelettes, large omelette, large omelettes, small omelette, small omelettes, food omelette, food omelettes, medium omelette, medium omelettes, tiny omelette, paani_puri, paani_puris, large paani_puri, large paani_puris, small paani_puri, small paani_puris, food paani_puri, food paani_puris, medium paani_puri, medium paani_puris, tiny paani_puri, pakode, pakodas, large pakode, large pakodas, small pakode, small pakodas, food pakode, food pakodas, medium pakode, medium pakodas, tiny pakode, pav_bhaji, pav_bhajis, large pav_bhaji, large pav_bhajis, small pav_bhaji, small pav_bhajis, food pav_bhaji, food pav_bhajis, medium pav_bhaji, medium pav_bhajis, tiny pav_bhaji, pizza, pizzas, large pizza, large pizzas, small pizza, small pizzas, food pizza, food pizzas, medium pizza, medium pizzas, tiny pizza, samosa, samosas, large samosa, large samosas, small samosa, small samosas, food samosa, food samosas, medium samosa, medium samosas, tiny samosa, sushi, sushis, large sushi, large sushis, small sushi, small sushis, food sushi, food sushis, medium sushi, medium sushis, tiny sushi

dict_size(f372)
print(aOcheck_accuracy("WithoutIP/food34/f372.csv", f372))

# %% [markdown]
# ## Weather11

# %%
w11 = {
    "dew" : ["dew"],
    "fogsmog" : ["fogsmog"],
    "frost": ["frost"],
    "glaze" : ["glaze"],
    "hail" : ["hail"],
    "lightning" : ["lightning"],
    "rain": ["rain"],
    "rainbow" : ["rainbow"],
    "rime": ["rime"],
    "sandstorm" : ["sandstorm"],
    "snow": ["snow"]
}

# dew, fogsmog, frost, glaze, hail, lightning, rain, rainbow, rime, sandstorm, snow

dict_size(w11)
print(aOcheck_accuracy("WithoutIP/weather11/w11.csv", w11))

# %%
w22 = {
    "dew": ["dew", "dews"],
    "fogsmog": ["fogsmog", "fogsmogs"],
    "frost": ["frost", "frosts"],
    "glaze": ["glaze", "glazes"],
    "hail": ["hail", "hails"],
    "lightning": ["lightning", "lightnings"],
    "rain": ["rain", "rains"],
    "rainbow": ["rainbow", "rainbows"],
    "rime": ["rime", "rimes"],
    "sandstorm": ["sandstorm", "sandstorms"],
    "snow": ["snow", "snows"]
}

# dew, dews, fogsmog, fogsmogs, frost, frosts, glaze, glazes, hail, hails, lightning, lightnings, rain, rains, rainbow, rainbows, rime, rimes, sandstorm, sandstorms, snow, snows

# dict_size(w22)
print(aOcheck_accuracy("WithoutIP/weather11/w22.csv", w22))


# %%
w33 = {
    "dew": ["dew", "dews", "Large dew"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog"],
    "frost": ["frost", "frosts", "Large frost"],
    "glaze": ["glaze", "glazes", "Large glaze"],
    "hail": ["hail", "hails", "Large hail"],
    "lightning": ["lightning", "lightnings", "Large lightning"],
    "rain": ["rain", "rains", "Large rain"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow"],
    "rime": ["rime", "rimes", "Large rime"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm"],
    "snow": ["snow", "snows", "Large snow"]
}

# dew, dews, Large dew, fogsmog, fogsmogs, Large fogsmog, frost, frosts, Large frost, glaze, glazes, Large glaze, hail, hails, Large hail, lightning, lightnings, Large lightning, rain, rains, Large rain, rainbow, rainbows, Large rainbow, rime, rimes, Large rime, sandstorm, sandstorms, Large sandstorm, snow, snows, Large snow

# dict_size(w33)
print(aOcheck_accuracy("WithoutIP/weather11/w33.csv", w33))


# %%
w44 = {
    "dew": ["dew", "dews", "Large dew", "Large dews"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog", "Large fogsmogs"],
    "frost": ["frost", "frosts", "Large frost", "Large frosts"],
    "glaze": ["glaze", "glazes", "Large glaze", "Large glazes"],
    "hail": ["hail", "hails", "Large hail", "Large hails"],
    "lightning": ["lightning", "lightnings", "Large lightning", "Large lightnings"],
    "rain": ["rain", "rains", "Large rain", "Large rains"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow", "Large rainbows"],
    "rime": ["rime", "rimes", "Large rime", "Large rimes"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm", "Large sandstorms"],
    "snow": ["snow", "snows", "Large snow", "Large snows"]
}

# dew, dews, Large dew, Large dews, fogsmog, fogsmogs, Large fogsmog, Large fogsmogs, frost, frosts, Large frost, Large frosts, glaze, glazes, Large glaze, Large glazes, hail, hails, Large hail, Large hails, lightning, lightnings, Large lightning, Large lightnings, rain, rains, Large rain, Large rains, rainbow, rainbows, Large rainbow, Large rainbows, rime, rimes, Large rime, Large rimes, sandstorm, sandstorms, Large sandstorm, Large sandstorms, snow, snows, Large snow, Large snows

# dict_size(w44)
print(aOcheck_accuracy("WithoutIP/weather11/w44.csv", w44))


# %%
w55 = {
    "dew": ["dew", "dews", "Large dew", "Large dews", "Small dew"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog", "Large fogsmogs", "Small fogsmog"],
    "frost": ["frost", "frosts", "Large frost", "Large frosts", "Small frost"],
    "glaze": ["glaze", "glazes", "Large glaze", "Large glazes", "Small glaze"],
    "hail": ["hail", "hails", "Large hail", "Large hails", "Small hail"],
    "lightning": ["lightning", "lightnings", "Large lightning", "Large lightnings", "Small lightning"],
    "rain": ["rain", "rains", "Large rain", "Large rains", "Small rain"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow", "Large rainbows", "Small rainbow"],
    "rime": ["rime", "rimes", "Large rime", "Large rimes", "Small rime"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm", "Large sandstorms", "Small sandstorm"],
    "snow": ["snow", "snows", "Large snow", "Large snows", "Small snow"]
}

# dew, dews, Large dew, Large dews, Small dew, fogsmog, fogsmogs, Large fogsmog, Large fogsmogs, Small fogsmog, frost, frosts, Large frost, Large frosts, Small frost, glaze, glazes, Large glaze, Large glazes, Small glaze, hail, hails, Large hail, Large hails, Small hail, lightning, lightnings, Large lightning, Large lightnings, Small lightning, rain, rains, Large rain, Large rains, Small rain, rainbow, rainbows, Large rainbow, Large rainbows, Small rainbow, rime, rimes, Large rime, Large rimes, Small rime, sandstorm, sandstorms, Large sandstorm, Large sandstorms, Small sandstorm, snow, snows, Large snow, Large snows, Small snow

# dict_size(w55)
print(aOcheck_accuracy("WithoutIP/weather11/w55.csv", w55))


# %%
w66 = {
    "dew": ["dew", "dews", "Large dew", "Large dews", "Small dew", "Small dews"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog", "Large fogsmogs", "Small fogsmog", "Small fogsmogs"],
    "frost": ["frost", "frosts", "Large frost", "Large frosts", "Small frost", "Small frosts"],
    "glaze": ["glaze", "glazes", "Large glaze", "Large glazes", "Small glaze", "Small glazes"],
    "hail": ["hail", "hails", "Large hail", "Large hails", "Small hail", "Small hails"],
    "lightning": ["lightning", "lightnings", "Large lightning", "Large lightnings", "Small lightning", "Small lightnings"],
    "rain": ["rain", "rains", "Large rain", "Large rains", "Small rain", "Small rains"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow", "Large rainbows", "Small rainbow", "Small rainbows"],
    "rime": ["rime", "rimes", "Large rime", "Large rimes", "Small rime", "Small rimes"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm", "Large sandstorms", "Small sandstorm", "Small sandstorms"],
    "snow": ["snow", "snows", "Large snow", "Large snows", "Small snow", "Small snows"]
}

# dew, dews, Large dew, Large dews, Small dew, Small dews, fogsmog, fogsmogs, Large fogsmog, Large fogsmogs, Small fogsmog, Small fogsmogs, frost, frosts, Large frost, Large frosts, Small frost, Small frosts, glaze, glazes, Large glaze, Large glazes, Small glaze, Small glazes, hail, hails, Large hail, Large hails, Small hail, Small hails, lightning, lightnings, Large lightning, Large lightnings, Small lightning, Small lightnings, rain, rains, Large rain, Large rains, Small rain, Small rains, rainbow, rainbows, Large rainbow, Large rainbows, Small rainbow, Small rainbows, rime, rimes, Large rime, Large rimes, Small rime, Small rimes, sandstorm, sandstorms, Large sandstorm, Large sandstorms, Small sandstorm, Small sandstorms, snow, snows, Large snow, Large snows, Small snow, Small snows

# dict_size(w66)
print(aOcheck_accuracy("WithoutIP/weather11/w66.csv", w66))


# %%
w77 = {
    "dew": ["dew", "dews", "Large dew", "Large dews", "Small dew", "Small dews", "Medium dew"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog", "Large fogsmogs", "Small fogsmog", "Small fogsmogs", "Medium fogsmog"],
    "frost": ["frost", "frosts", "Large frost", "Large frosts", "Small frost", "Small frosts", "Medium frost"],
    "glaze": ["glaze", "glazes", "Large glaze", "Large glazes", "Small glaze", "Small glazes", "Medium glaze"],
    "hail": ["hail", "hails", "Large hail", "Large hails", "Small hail", "Small hails", "Medium hail"],
    "lightning": ["lightning", "lightnings", "Large lightning", "Large lightnings", "Small lightning", "Small lightnings", "Medium lightning"],
    "rain": ["rain", "rains", "Large rain", "Large rains", "Small rain", "Small rains", "Medium rain"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow", "Large rainbows", "Small rainbow", "Small rainbows", "Medium rainbow"],
    "rime": ["rime", "rimes", "Large rime", "Large rimes", "Small rime", "Small rimes", "Medium rime"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm", "Large sandstorms", "Small sandstorm", "Small sandstorms", "Medium sandstorm"],
    "snow": ["snow", "snows", "Large snow", "Large snows", "Small snow", "Small snows", "Medium snow"]
}

# dew, dews, Large dew, Large dews, Small dew, Small dews, Medium dew, fogsmog, fogsmogs, Large fogsmog, Large fogsmogs, Small fogsmog, Small fogsmogs, Medium fogsmog, frost, frosts, Large frost, Large frosts, Small frost, Small frosts, Medium frost, glaze, glazes, Large glaze, Large glazes, Small glaze, Small glazes, Medium glaze, hail, hails, Large hail, Large hails, Small hail, Small hails, Medium hail, lightning, lightnings, Large lightning, Large lightnings, Small lightning, Small lightnings, Medium lightning, rain, rains, Large rain, Large rains, Small rain, Small rains, Medium rain, rainbow, rainbows, Large rainbow, Large rainbows, Small rainbow, Small rainbows, Medium rainbow, rime, rimes, Large rime, Large rimes, Small rime, Small rimes, Medium rime, sandstorm, sandstorms, Large sandstorm, Large sandstorms, Small sandstorm, Small sandstorms, Medium sandstorm, snow, snows, Large snow, Large snows, Small snow, Small snows, Medium snow

# dict_size(w77)
print(aOcheck_accuracy("WithoutIP/weather11/w77.csv", w77))


# %%
w88 = {
    "dew": ["dew", "dews", "Large dew", "Large dews", "Small dew", "Small dews", "Medium dew", "Medium dews"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog", "Large fogsmogs", "Small fogsmog", "Small fogsmogs", "Medium fogsmog", "Medium fogsmogs"],
    "frost": ["frost", "frosts", "Large frost", "Large frosts", "Small frost", "Small frosts", "Medium frost", "Medium frosts"],
    "glaze": ["glaze", "glazes", "Large glaze", "Large glazes", "Small glaze", "Small glazes", "Medium glaze", "Medium glazes"],
    "hail": ["hail", "hails", "Large hail", "Large hails", "Small hail", "Small hails", "Medium hail", "Medium hails"],
    "lightning": ["lightning", "lightnings", "Large lightning", "Large lightnings", "Small lightning", "Small lightnings", "Medium lightning", "Medium lightnings"],
    "rain": ["rain", "rains", "Large rain", "Large rains", "Small rain", "Small rains", "Medium rain", "Medium rains"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow", "Large rainbows", "Small rainbow", "Small rainbows", "Medium rainbow", "Medium rainbows"],
    "rime": ["rime", "rimes", "Large rime", "Large rimes", "Small rime", "Small rimes", "Medium rime", "Medium rimes"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm", "Large sandstorms", "Small sandstorm", "Small sandstorms", "Medium sandstorm", "Medium sandstorms"],
    "snow": ["snow", "snows", "Large snow", "Large snows", "Small snow", "Small snows", "Medium snow", "Medium snows"]
}

# dew, dews, Large dew, Large dews, Small dew, Small dews, Medium dew, Medium dews, fogsmog, fogsmogs, Large fogsmog, Large fogsmogs, Small fogsmog, Small fogsmogs, Medium fogsmog, Medium fogsmogs, frost, frosts, Large frost, Large frosts, Small frost, Small frosts, Medium frost, Medium frosts, glaze, glazes, Large glaze, Large glazes, Small glaze, Small glazes, Medium glaze, Medium glazes, hail, hails, Large hail, Large hails, Small hail, Small hails, Medium hail, Medium hails, lightning, lightnings, Large lightning, Large lightnings, Small lightning, Small lightnings, Medium lightning, Medium lightnings, rain, rains, Large rain, Large rains, Small rain, Small rains, Medium rain, Medium rains, rainbow, rainbows, Large rainbow, Large rainbows, Small rainbow, Small rainbows, Medium rainbow, Medium rainbows, rime, rimes, Large rime, Large rimes, Small rime, Small rimes, Medium rime, Medium rimes, sandstorm, sandstorms, Large sandstorm, Large sandstorms, Small sandstorm, Small sandstorms, Medium sandstorm, Medium sandstorms, snow, snows, Large snow, Large snows, Small snow, Small snows, Medium snow, Medium snows

# dict_size(w88)
print(aOcheck_accuracy("WithoutIP/weather11/w88.csv", w88))


# %%
w99 = {
    "dew": ["dew", "dews", "Large dew", "Large dews", "Small dew", "Small dews", "Medium dew", "Medium dews", "Weather dew"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog", "Large fogsmogs", "Small fogsmog", "Small fogsmogs", "Medium fogsmog", "Medium fogsmogs", "Weather fogsmog"],
    "frost": ["frost", "frosts", "Large frost", "Large frosts", "Small frost", "Small frosts", "Medium frost", "Medium frosts", "Weather frost"],
    "glaze": ["glaze", "glazes", "Large glaze", "Large glazes", "Small glaze", "Small glazes", "Medium glaze", "Medium glazes", "Weather glaze"],
    "hail": ["hail", "hails", "Large hail", "Large hails", "Small hail", "Small hails", "Medium hail", "Medium hails", "Weather hail"],
    "lightning": ["lightning", "lightnings", "Large lightning", "Large lightnings", "Small lightning", "Small lightnings", "Medium lightning", "Medium lightnings", "Weather lightning"],
    "rain": ["rain", "rains", "Large rain", "Large rains", "Small rain", "Small rains", "Medium rain", "Medium rains", "Weather rain"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow", "Large rainbows", "Small rainbow", "Small rainbows", "Medium rainbow", "Medium rainbows", "Weather rainbow"],
    "rime": ["rime", "rimes", "Large rime", "Large rimes", "Small rime", "Small rimes", "Medium rime", "Medium rimes", "Weather rime"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm", "Large sandstorms", "Small sandstorm", "Small sandstorms", "Medium sandstorm", "Medium sandstorms", "Weather sandstorm"],
    "snow": ["snow", "snows", "Large snow", "Large snows", "Small snow", "Small snows", "Medium snow", "Medium snows", "Weather snow"]
}

# dew, dews, Large dew, Large dews, Small dew, Small dews, Medium dew, Medium dews, Weather dew, fogsmog, fogsmogs, Large fogsmog, Large fogsmogs, Small fogsmog, Small fogsmogs, Medium fogsmog, Medium fogsmogs, Weather fogsmog, frost, frosts, Large frost, Large frosts, Small frost, Small frosts, Medium frost, Medium frosts, Weather frost, glaze, glazes, Large glaze, Large glazes, Small glaze, Small glazes, Medium glaze, Medium glazes, Weather glaze, hail, hails, Large hail, Large hails, Small hail, Small hails, Medium hail, Medium hails, Weather hail, lightning, lightnings, Large lightning, Large lightnings, Small lightning, Small lightnings, Medium lightning, Medium lightnings, Weather lightning, rain, rains, Large rain, Large rains, Small rain, Small rains, Medium rain, Medium rains, Weather rain, rainbow, rainbows, Large rainbow, Large rainbows, Small rainbow, Small rainbows, Medium rainbow, Medium rainbows, Weather rainbow, rime, rimes, Large rime, Large rimes, Small rime, Small rimes, Medium rime, Medium rimes, Weather rime, sandstorm, sandstorms, Large sandstorm, Large sandstorms, Small sandstorm, Small sandstorms, Medium sandstorm, Medium sandstorms, Weather sandstorm, snow, snows, Large snow, Large snows, Small snow, Small snows, Medium snow, Medium snows, Weather snow

# dict_size(w99)
print(aOcheck_accuracy("WithoutIP/weather11/w99.csv", w99))


# %%
w110 = {
    "dew": ["dew", "dews", "Large dew", "Large dews", "Small dew", "Small dews", "Medium dew", "Medium dews", "Weather dew", "Weather dews"],
    "fogsmog": ["fogsmog", "fogsmogs", "Large fogsmog", "Large fogsmogs", "Small fogsmog", "Small fogsmogs", "Medium fogsmog", "Medium fogsmogs", "Weather fogsmog", "Weather fogsmogs"],
    "frost": ["frost", "frosts", "Large frost", "Large frosts", "Small frost", "Small frosts", "Medium frost", "Medium frosts", "Weather frost", "Weather frosts"],
    "glaze": ["glaze", "glazes", "Large glaze", "Large glazes", "Small glaze", "Small glazes", "Medium glaze", "Medium glazes", "Weather glaze", "Weather glazes"],
    "hail": ["hail", "hails", "Large hail", "Large hails", "Small hail", "Small hails", "Medium hail", "Medium hails", "Weather hail", "Weather hails"],
    "lightning": ["lightning", "lightnings", "Large lightning", "Large lightnings", "Small lightning", "Small lightnings", "Medium lightning", "Medium lightnings", "Weather lightning", "Weather lightnings"],
    "rain": ["rain", "rains", "Large rain", "Large rains", "Small rain", "Small rains", "Medium rain", "Medium rains", "Weather rain", "Weather rains"],
    "rainbow": ["rainbow", "rainbows", "Large rainbow", "Large rainbows", "Small rainbow", "Small rainbows", "Medium rainbow", "Medium rainbows", "Weather rainbow", "Weather rainbows"],
    "rime": ["rime", "rimes", "Large rime", "Large rimes", "Small rime", "Small rimes", "Medium rime", "Medium rimes", "Weather rime", "Weather rimes"],
    "sandstorm": ["sandstorm", "sandstorms", "Large sandstorm", "Large sandstorms", "Small sandstorm", "Small sandstorms", "Medium sandstorm", "Medium sandstorms", "Weather sandstorm", "Weather sandstorms"],
    "snow": ["snow", "snows", "Large snow", "Large snows", "Small snow", "Small snows", "Medium snow", "Medium snows", "Weather snow", "Weather snows"]
}

# dew, dews, Large dew, Large dews, Small dew, Small dews, Medium dew, Medium dews, Weather dew, Weather dews, fogsmog, fogsmogs, Large fogsmog, Large fogsmogs, Small fogsmog, Small fogsmogs, Medium fogsmog, Medium fogsmogs, Weather fogsmog, Weather fogsmogs, frost, frosts, Large frost, Large frosts, Small frost, Small frosts, Medium frost, Medium frosts, Weather frost, Weather frosts, glaze, glazes, Large glaze, Large glazes, Small glaze, Small glazes, Medium glaze, Medium glazes, Weather glaze, Weather glazes, hail, hails, Large hail, Large hails, Small hail, Small hails, Medium hail, Medium hails, Weather hail, Weather hails, lightning, lightnings, Large lightning, Large lightnings, Small lightning, Small lightnings, Medium lightning, Medium lightnings, Weather lightning, Weather lightnings, rain, rains, Large rain, Large rains, Small rain, Small rains, Medium rain, Medium rains, Weather rain, Weather rains, rainbow, rainbows, Large rainbow, Large rainbows, Small rainbow, Small rainbows, Medium rainbow, Medium rainbows, Weather rainbow, Weather rainbows, rime, rimes, Large rime, Large rimes, Small rime, Small rimes, Medium rime, Medium rimes, Weather rime, Weather rimes, sandstorm, sandstorms, Large sandstorm, Large sandstorms, Small sandstorm, Small sandstorms, Medium sandstorm, Medium sandstorms, Weather sandstorm, Weather sandstorms, snow, snows, Large snow, Large snows, Small snow, Small snows, Medium snow, Medium snows, Weather snow, Weather snows

# dict_size(w110)
print(aOcheck_accuracy("WithoutIP/weather11/w110.csv", w110))


# %% [markdown]
# ## Sports 15

# %%
s15 = {"american_football" : ["american_football"],
       "baseball" : ["baseball"],
       "basketball" : ["basketball"],
       "billiard_ball" : ["billiard_ball"],
       "bowling_ball" : ["bowling_ball"],
       "cricket_ball" : ["cricket_ball"],
       "football" : ["football"],
       "golf_ball" : ["golf_ball"],
       "hockey_ball" : ["hockey_ball"],
       "hockey_puck" : ["hockey_puck"],
       "rugby_ball" : ["rugby_ball"],
       "shuttlecock" : ["shuttlecock"],
       "table_tennis_ball" : ["table_tennis_ball"],
       "tennis_ball" : ["tennis_ball"],
       "volleyball" : ["volleyball"]}

# american_football, baseball, basketball, billiard_ball, bowling_ball, cricket_ball, football, golf_ball, hockey_ball, hockey_puck, rugby_ball, shuttlecock, table_tennis_ball, tennis_ball, volleyball

dict_size(s15)
print(aOcheck_accuracy("WithoutIP/sports15/s15.csv", s15))

# %%
s30 = {
    "american_football": ["american_football", "american_footballs"],
    "baseball": ["baseball", "baseballs"],
    "basketball": ["basketball", "basketballs"],
    "billiard_ball": ["billiard_ball", "billiard_balls"],
    "bowling_ball": ["bowling_ball", "bowling_balls"],
    "cricket_ball": ["cricket_ball", "cricket_balls"],
    "football": ["football", "footballs"],
    "golf_ball": ["golf_ball", "golf_balls"],
    "hockey_ball": ["hockey_ball", "hockey_balls"],
    "hockey_puck": ["hockey_puck", "hockey_pucks"],
    "rugby_ball": ["rugby_ball", "rugby_balls"],
    "shuttlecock": ["shuttlecock", "shuttlecocks"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls"],
    "tennis_ball": ["tennis_ball", "tennis_balls"],
    "volleyball": ["volleyball", "volleyballs"]
}

# american_football, american_footballs, baseball, baseballs, basketball, basketballs, billiard_ball, billiard_balls, bowling_ball, bowling_balls, cricket_ball, cricket_balls, football, footballs, golf_ball, golf_balls, hockey_ball, hockey_balls, hockey_puck, hockey_pucks, rugby_ball, rugby_balls, shuttlecock, shuttlecocks, table_tennis_ball, table_tennis_balls, tennis_ball, tennis_balls, volleyball, volleyballs

# dict_size(s30)
print(aOcheck_accuracy("WithoutIP/sports15/s30.csv", s30))


# %%
s45 = {
    "american_football": ["american_football", "american_footballs", "Large american_football"],
    "baseball": ["baseball", "baseballs", "Large baseball"],
    "basketball": ["basketball", "basketballs", "Large basketball"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball"],
    "football": ["football", "footballs", "Large football"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball"]
}

# american_football, american_footballs, Large american_football, baseball, baseballs, Large baseball, basketball, basketballs, Large basketball, billiard_ball, billiard_balls, Large billiard_ball, bowling_ball, bowling_balls, Large bowling_ball, cricket_ball, cricket_balls, Large cricket_ball, football, footballs, Large football, golf_ball, golf_balls, Large golf_ball, hockey_ball, hockey_balls, Large hockey_ball, hockey_puck, hockey_pucks, Large hockey_puck, rugby_ball, rugby_balls, Large rugby_ball, shuttlecock, shuttlecocks, Large shuttlecock, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, tennis_ball, tennis_balls, Large tennis_ball, volleyball, volleyballs, Large volleyball

# dict_size(s45)
print(aOcheck_accuracy("WithoutIP/sports15/s45.csv", s45))


# %%
s60 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls"],
    "football": ["football", "footballs", "Large football", "Large footballs"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, baseball, baseballs, Large baseball, Large baseballs, basketball, basketballs, Large basketball, Large basketballs, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, football, footballs, Large football, Large footballs, golf_ball, golf_balls, Large golf_ball, Large golf_balls, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, volleyball, volleyballs, Large volleyball, Large volleyballs

# dict_size(s60)
print(aOcheck_accuracy("WithoutIP/sports15/s60.csv", s60))


# %%
s75 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, baseball, baseballs, Large baseball, Large baseballs, Small baseball, basketball, basketballs, Large basketball, Large basketballs, Small basketball, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, football, footballs, Large football, Large footballs, Small football, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball

# dict_size(s75)
print(aOcheck_accuracy("WithoutIP/sports15/s75.csv", s75))


# %%
s90 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, football, footballs, Large football, Large footballs, Small football, Small footballs, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs

# dict_size(s90)
print(aOcheck_accuracy("WithoutIP/sports15/s90.csv", s90))

# %%
s105 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball

# dict_size(s105)
print(aOcheck_accuracy("WithoutIP/sports15/s105.csv", s105))

# %%
s120 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football", "Medium american_footballs"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball", "Medium baseballs"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball", "Medium basketballs"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball", "Medium billiard_balls"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball", "Medium bowling_balls"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball", "Medium cricket_balls"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football", "Medium footballs"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball", "Medium golf_balls"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball", "Medium hockey_balls"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck", "Medium hockey_pucks"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball", "Medium rugby_balls"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock", "Medium shuttlecocks"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball", "Medium table_tennis_balls"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball", "Medium tennis_balls"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball", "Medium volleyballs"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, Medium american_footballs, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, Medium baseballs, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, Medium basketballs, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, Medium billiard_balls, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, Medium bowling_balls, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, Medium cricket_balls, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, Medium footballs, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, Medium golf_balls, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, Medium hockey_balls, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, Medium hockey_pucks, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, Medium rugby_balls, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, Medium shuttlecocks, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, Medium table_tennis_balls, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, Medium tennis_balls, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball, Medium volleyballs

# dict_size(s120)
print(aOcheck_accuracy("WithoutIP/sports15/s120.csv", s120))


# %%
s135 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football", "Medium american_footballs", "Sports american_football"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball", "Medium baseballs", "Sports baseball"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball", "Medium basketballs", "Sports basketball"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball", "Medium billiard_balls", "Sports billiard_ball"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball", "Medium bowling_balls", "Sports bowling_ball"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball", "Medium cricket_balls", "Sports cricket_ball"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football", "Medium footballs", "Sports football"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball", "Medium golf_balls", "Sports golf_ball"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball", "Medium hockey_balls", "Sports hockey_ball"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck", "Medium hockey_pucks", "Sports hockey_puck"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball", "Medium rugby_balls", "Sports rugby_ball"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock", "Medium shuttlecocks", "Sports shuttlecock"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball", "Medium table_tennis_balls", "Sports table_tennis_ball"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball", "Medium tennis_balls", "Sports tennis_ball"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball", "Medium volleyballs", "Sports volleyball"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, Medium american_footballs, Sports american_football, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, Medium baseballs, Sports baseball, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, Medium basketballs, Sports basketball, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, Medium billiard_balls, Sports billiard_ball, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, Medium bowling_balls, Sports bowling_ball, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, Medium cricket_balls, Sports cricket_ball, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, Medium footballs, Sports football, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, Medium golf_balls, Sports golf_ball, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, Medium hockey_balls, Sports hockey_ball, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, Medium hockey_pucks, Sports hockey_puck, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, Medium rugby_balls, Sports rugby_ball, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, Medium shuttlecocks, Sports shuttlecock, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, Medium table_tennis_balls, Sports table_tennis_ball, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, Medium tennis_balls, Sports tennis_ball, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball, Medium volleyballs, Sports volleyball

# dict_size(s135)
print(aOcheck_accuracy("WithoutIP/sports15/s135.csv", s135))


# %%
s150 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football", "Medium american_footballs", "Sports american_football", "Sports american_footballs"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball", "Medium baseballs", "Sports baseball", "Sports baseballs"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball", "Medium basketballs", "Sports basketball", "Sports basketballs"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball", "Medium billiard_balls", "Sports billiard_ball", "Sports billiard_balls"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball", "Medium bowling_balls", "Sports bowling_ball", "Sports bowling_balls"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball", "Medium cricket_balls", "Sports cricket_ball", "Sports cricket_balls"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football", "Medium footballs", "Sports football", "Sports footballs"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball", "Medium golf_balls", "Sports golf_ball", "Sports golf_balls"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball", "Medium hockey_balls", "Sports hockey_ball", "Sports hockey_balls"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck", "Medium hockey_pucks", "Sports hockey_puck", "Sports hockey_pucks"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball", "Medium rugby_balls", "Sports rugby_ball", "Sports rugby_balls"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock", "Medium shuttlecocks", "Sports shuttlecock", "Sports shuttlecocks"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball", "Medium table_tennis_balls", "Sports table_tennis_ball", "Sports table_tennis_balls"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball", "Medium tennis_balls", "Sports tennis_ball", "Sports tennis_balls"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball", "Medium volleyballs", "Sports volleyball", "Sports volleyballs"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, Medium american_footballs, Sports american_football, Sports american_footballs, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, Medium baseballs, Sports baseball, Sports baseballs, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, Medium basketballs, Sports basketball, Sports basketballs, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, Medium billiard_balls, Sports billiard_ball, Sports billiard_balls, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, Medium bowling_balls, Sports bowling_ball, Sports bowling_balls, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, Medium cricket_balls, Sports cricket_ball, Sports cricket_balls, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, Medium footballs, Sports football, Sports footballs, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, Medium golf_balls, Sports golf_ball, Sports golf_balls, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, Medium hockey_balls, Sports hockey_ball, Sports hockey_balls, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, Medium hockey_pucks, Sports hockey_puck, Sports hockey_pucks, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, Medium rugby_balls, Sports rugby_ball, Sports rugby_balls, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, Medium shuttlecocks, Sports shuttlecock, Sports shuttlecocks, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, Medium table_tennis_balls, Sports table_tennis_ball, Sports table_tennis_balls, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, Medium tennis_balls, Sports tennis_ball, Sports tennis_balls, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball, Medium volleyballs, Sports volleyball, Sports volleyballs

# dict_size(s150)
print(aOcheck_accuracy("WithoutIP/sports15/s150.csv", s150))


# %%
s165 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football", "Medium american_footballs", "Sports american_football", "Sports american_footballs", "Round american_football"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball", "Medium baseballs", "Sports baseball", "Sports baseballs", "Round baseball"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball", "Medium basketballs", "Sports basketball", "Sports basketballs", "Round basketball"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball", "Medium billiard_balls", "Sports billiard_ball", "Sports billiard_balls", "Round billiard_ball"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball", "Medium bowling_balls", "Sports bowling_ball", "Sports bowling_balls", "Round bowling_ball"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball", "Medium cricket_balls", "Sports cricket_ball", "Sports cricket_balls", "Round cricket_ball"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football", "Medium footballs", "Sports football", "Sports footballs", "Round football"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball", "Medium golf_balls", "Sports golf_ball", "Sports golf_balls", "Round golf_ball"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball", "Medium hockey_balls", "Sports hockey_ball", "Sports hockey_balls", "Round hockey_ball"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck", "Medium hockey_pucks", "Sports hockey_puck", "Sports hockey_pucks", "Round hockey_puck"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball", "Medium rugby_balls", "Sports rugby_ball", "Sports rugby_balls", "Round rugby_ball"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock", "Medium shuttlecocks", "Sports shuttlecock", "Sports shuttlecocks", "Round shuttlecock"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball", "Medium table_tennis_balls", "Sports table_tennis_ball", "Sports table_tennis_balls", "Round table_tennis_ball"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball", "Medium tennis_balls", "Sports tennis_ball", "Sports tennis_balls", "Round tennis_ball"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball", "Medium volleyballs", "Sports volleyball", "Sports volleyballs", "Round volleyball"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, Medium american_footballs, Sports american_football, Sports american_footballs, Round american_football, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, Medium baseballs, Sports baseball, Sports baseballs, Round baseball, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, Medium basketballs, Sports basketball, Sports basketballs, Round basketball, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, Medium billiard_balls, Sports billiard_ball, Sports billiard_balls, Round billiard_ball, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, Medium bowling_balls, Sports bowling_ball, Sports bowling_balls, Round bowling_ball, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, Medium cricket_balls, Sports cricket_ball, Sports cricket_balls, Round cricket_ball, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, Medium footballs, Sports football, Sports footballs, Round football, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, Medium golf_balls, Sports golf_ball, Sports golf_balls, Round golf_ball, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, Medium hockey_balls, Sports hockey_ball, Sports hockey_balls, Round hockey_ball, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, Medium hockey_pucks, Sports hockey_puck, Sports hockey_pucks, Round hockey_puck, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, Medium rugby_balls, Sports rugby_ball, Sports rugby_balls, Round rugby_ball, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, Medium shuttlecocks, Sports shuttlecock, Sports shuttlecocks, Round shuttlecock, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, Medium table_tennis_balls, Sports table_tennis_ball, Sports table_tennis_balls, Round table_tennis_ball, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, Medium tennis_balls, Sports tennis_ball, Sports tennis_balls, Round tennis_ball, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball, Medium volleyballs, Sports volleyball, Sports volleyballs, Round volleyball

# dict_size(s165)
print(aOcheck_accuracy("WithoutIP/sports15/s165.csv", s165))


# %%
s180 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football", "Medium american_footballs", "Sports american_football", "Sports american_footballs", "Round american_football", "Round american_footballs"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball", "Medium baseballs", "Sports baseball", "Sports baseballs", "Round baseball", "Round baseballs"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball", "Medium basketballs", "Sports basketball", "Sports basketballs", "Round basketball", "Round basketballs"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball", "Medium billiard_balls", "Sports billiard_ball", "Sports billiard_balls", "Round billiard_ball", "Round billiard_balls"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball", "Medium bowling_balls", "Sports bowling_ball", "Sports bowling_balls", "Round bowling_ball", "Round bowling_balls"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball", "Medium cricket_balls", "Sports cricket_ball", "Sports cricket_balls", "Round cricket_ball", "Round cricket_balls"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football", "Medium footballs", "Sports football", "Sports footballs", "Round football", "Round footballs"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball", "Medium golf_balls", "Sports golf_ball", "Sports golf_balls", "Round golf_ball", "Round golf_balls"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball", "Medium hockey_balls", "Sports hockey_ball", "Sports hockey_balls", "Round hockey_ball", "Round hockey_balls"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck", "Medium hockey_pucks", "Sports hockey_puck", "Sports hockey_pucks", "Round hockey_puck", "Round hockey_pucks"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball", "Medium rugby_balls", "Sports rugby_ball", "Sports rugby_balls", "Round rugby_ball", "Round rugby_balls"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock", "Medium shuttlecocks", "Sports shuttlecock", "Sports shuttlecocks", "Round shuttlecock", "Round shuttlecocks"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball", "Medium table_tennis_balls", "Sports table_tennis_ball", "Sports table_tennis_balls", "Round table_tennis_ball", "Round table_tennis_balls"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball", "Medium tennis_balls", "Sports tennis_ball", "Sports tennis_balls", "Round tennis_ball", "Round tennis_balls"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball", "Medium volleyballs", "Sports volleyball", "Sports volleyballs", "Round volleyball", "Round volleyballs"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, Medium american_footballs, Sports american_football, Sports american_footballs, Round american_football, Round american_footballs, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, Medium baseballs, Sports baseball, Sports baseballs, Round baseball, Round baseballs, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, Medium basketballs, Sports basketball, Sports basketballs, Round basketball, Round basketballs, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, Medium billiard_balls, Sports billiard_ball, Sports billiard_balls, Round billiard_ball, Round billiard_balls, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, Medium bowling_balls, Sports bowling_ball, Sports bowling_balls, Round bowling_ball, Round bowling_balls, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, Medium cricket_balls, Sports cricket_ball, Sports cricket_balls, Round cricket_ball, Round cricket_balls, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, Medium footballs, Sports football, Sports footballs, Round football, Round footballs, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, Medium golf_balls, Sports golf_ball, Sports golf_balls, Round golf_ball, Round golf_balls, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, Medium hockey_balls, Sports hockey_ball, Sports hockey_balls, Round hockey_ball, Round hockey_balls, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, Medium hockey_pucks, Sports hockey_puck, Sports hockey_pucks, Round hockey_puck, Round hockey_pucks, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, Medium rugby_balls, Sports rugby_ball, Sports rugby_balls, Round rugby_ball, Round rugby_balls, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, Medium shuttlecocks, Sports shuttlecock, Sports shuttlecocks, Round shuttlecock, Round shuttlecocks, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, Medium table_tennis_balls, Sports table_tennis_ball, Sports table_tennis_balls, Round table_tennis_ball, Round table_tennis_balls, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, Medium tennis_balls, Sports tennis_ball, Sports tennis_balls, Round tennis_ball, Round tennis_balls, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball, Medium volleyballs, Sports volleyball, Sports volleyballs, Round volleyball, Round volleyballs

# dict_size(s180)
print(aOcheck_accuracy("WithoutIP/sports15/s180.csv", s180))


# %%
s195 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football", "Medium american_footballs", "Sports american_football", "Sports american_footballs", "Round american_football", "american_football for Sports"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball", "Medium baseballs", "Sports baseball", "Sports baseballs", "Round baseball", "baseball for Sports"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball", "Medium basketballs", "Sports basketball", "Sports basketballs", "Round basketball", "basketball for Sports"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball", "Medium billiard_balls", "Sports billiard_ball", "Sports billiard_balls", "Round billiard_ball", "billiard_ball for Sports"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball", "Medium bowling_balls", "Sports bowling_ball", "Sports bowling_balls", "Round bowling_ball", "bowling_ball for Sports"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball", "Medium cricket_balls", "Sports cricket_ball", "Sports cricket_balls", "Round cricket_ball", "cricket_ball for Sports"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football", "Medium footballs", "Sports football", "Sports footballs", "Round football", "football for Sports"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball", "Medium golf_balls", "Sports golf_ball", "Sports golf_balls", "Round golf_ball", "golf_ball for Sports"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball", "Medium hockey_balls", "Sports hockey_ball", "Sports hockey_balls", "Round hockey_ball", "hockey_ball for Sports"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck", "Medium hockey_pucks", "Sports hockey_puck", "Sports hockey_pucks", "Round hockey_puck", "hockey_puck for Sports"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball", "Medium rugby_balls", "Sports rugby_ball", "Sports rugby_balls", "Round rugby_ball", "rugby_ball for Sports"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock", "Medium shuttlecocks", "Sports shuttlecock", "Sports shuttlecocks", "Round shuttlecock", "shuttlecock for Sports"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball", "Medium table_tennis_balls", "Sports table_tennis_ball", "Sports table_tennis_balls", "Round table_tennis_ball", "table_tennis_ball for Sports"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball", "Medium tennis_balls", "Sports tennis_ball", "Sports tennis_balls", "Round tennis_ball", "tennis_ball for Sports"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball", "Medium volleyballs", "Sports volleyball", "Sports volleyballs", "Round volleyball", "volleyball for Sports"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, Medium american_footballs, Sports american_football, Sports american_footballs, Round american_football, american_football for Sports, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, Medium baseballs, Sports baseball, Sports baseballs, Round baseball, baseball for Sports, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, Medium basketballs, Sports basketball, Sports basketballs, Round basketball, basketball for Sports, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, Medium billiard_balls, Sports billiard_ball, Sports billiard_balls, Round billiard_ball, billiard_ball for Sports, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, Medium bowling_balls, Sports bowling_ball, Sports bowling_balls, Round bowling_ball, bowling_ball for Sports, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, Medium cricket_balls, Sports cricket_ball, Sports cricket_balls, Round cricket_ball, cricket_ball for Sports, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, Medium footballs, Sports football, Sports footballs, Round football, football for Sports, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, Medium golf_balls, Sports golf_ball, Sports golf_balls, Round golf_ball, golf_ball for Sports, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, Medium hockey_balls, Sports hockey_ball, Sports hockey_balls, Round hockey_ball, hockey_ball for Sports, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, Medium hockey_pucks, Sports hockey_puck, Sports hockey_pucks, Round hockey_puck, hockey_puck for Sports, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, Medium rugby_balls, Sports rugby_ball, Sports rugby_balls, Round rugby_ball, rugby_ball for Sports, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, Medium shuttlecocks, Sports shuttlecock, Sports shuttlecocks, Round shuttlecock, shuttlecock for Sports, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, Medium table_tennis_balls, Sports table_tennis_ball, Sports table_tennis_balls, Round table_tennis_ball, table_tennis_ball for Sports, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, Medium tennis_balls, Sports tennis_ball, Sports tennis_balls, Round tennis_ball, tennis_ball for Sports, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball, Medium volleyballs, Sports volleyball, Sports volleyballs, Round volleyball, volleyball for Sports

# dict_size(s195)
print(aOcheck_accuracy("WithoutIP/sports15/s195.csv", s195))


# %%
s210 = {
    "american_football": ["american_football", "american_footballs", "Large american_football", "Large american_footballs", "Small american_football", "Small american_footballs", "Medium american_football", "Medium american_footballs", "Sports american_football", "Sports american_footballs", "Round american_football", "american_football for Sports", "american_footballs for Sports"],
    "baseball": ["baseball", "baseballs", "Large baseball", "Large baseballs", "Small baseball", "Small baseballs", "Medium baseball", "Medium baseballs", "Sports baseball", "Sports baseballs", "Round baseball", "baseball for Sports", "baseballs for Sports"],
    "basketball": ["basketball", "basketballs", "Large basketball", "Large basketballs", "Small basketball", "Small basketballs", "Medium basketball", "Medium basketballs", "Sports basketball", "Sports basketballs", "Round basketball", "basketball for Sports", "basketballs for Sports"],
    "billiard_ball": ["billiard_ball", "billiard_balls", "Large billiard_ball", "Large billiard_balls", "Small billiard_ball", "Small billiard_balls", "Medium billiard_ball", "Medium billiard_balls", "Sports billiard_ball", "Sports billiard_balls", "Round billiard_ball", "billiard_ball for Sports", "billiard_balls for Sports"],
    "bowling_ball": ["bowling_ball", "bowling_balls", "Large bowling_ball", "Large bowling_balls", "Small bowling_ball", "Small bowling_balls", "Medium bowling_ball", "Medium bowling_balls", "Sports bowling_ball", "Sports bowling_balls", "Round bowling_ball", "bowling_ball for Sports", "bowling_balls for Sports"],
    "cricket_ball": ["cricket_ball", "cricket_balls", "Large cricket_ball", "Large cricket_balls", "Small cricket_ball", "Small cricket_balls", "Medium cricket_ball", "Medium cricket_balls", "Sports cricket_ball", "Sports cricket_balls", "Round cricket_ball", "cricket_ball for Sports", "cricket_balls for Sports"],
    "football": ["football", "footballs", "Large football", "Large footballs", "Small football", "Small footballs", "Medium football", "Medium footballs", "Sports football", "Sports footballs", "Round football", "football for Sports", "footballs for Sports"],
    "golf_ball": ["golf_ball", "golf_balls", "Large golf_ball", "Large golf_balls", "Small golf_ball", "Small golf_balls", "Medium golf_ball", "Medium golf_balls", "Sports golf_ball", "Sports golf_balls", "Round golf_ball", "golf_ball for Sports", "golf_balls for Sports"],
    "hockey_ball": ["hockey_ball", "hockey_balls", "Large hockey_ball", "Large hockey_balls", "Small hockey_ball", "Small hockey_balls", "Medium hockey_ball", "Medium hockey_balls", "Sports hockey_ball", "Sports hockey_balls", "Round hockey_ball", "hockey_ball for Sports", "hockey_balls for Sports"],
    "hockey_puck": ["hockey_puck", "hockey_pucks", "Large hockey_puck", "Large hockey_pucks", "Small hockey_puck", "Small hockey_pucks", "Medium hockey_puck", "Medium hockey_pucks", "Sports hockey_puck", "Sports hockey_pucks", "Round hockey_puck", "hockey_puck for Sports", "hockey_pucks for Sports"],
    "rugby_ball": ["rugby_ball", "rugby_balls", "Large rugby_ball", "Large rugby_balls", "Small rugby_ball", "Small rugby_balls", "Medium rugby_ball", "Medium rugby_balls", "Sports rugby_ball", "Sports rugby_balls", "Round rugby_ball", "rugby_ball for Sports", "rugby_balls for Sports"],
    "shuttlecock": ["shuttlecock", "shuttlecocks", "Large shuttlecock", "Large shuttlecocks", "Small shuttlecock", "Small shuttlecocks", "Medium shuttlecock", "Medium shuttlecocks", "Sports shuttlecock", "Sports shuttlecocks", "Round shuttlecock", "shuttlecock for Sports", "shuttlecocks for Sports"],
    "table_tennis_ball": ["table_tennis_ball", "table_tennis_balls", "Large table_tennis_ball", "Large table_tennis_balls", "Small table_tennis_ball", "Small table_tennis_balls", "Medium table_tennis_ball", "Medium table_tennis_balls", "Sports table_tennis_ball", "Sports table_tennis_balls", "Round table_tennis_ball", "table_tennis_ball for Sports", "table_tennis_balls for Sports"],
    "tennis_ball": ["tennis_ball", "tennis_balls", "Large tennis_ball", "Large tennis_balls", "Small tennis_ball", "Small tennis_balls", "Medium tennis_ball", "Medium tennis_balls", "Sports tennis_ball", "Sports tennis_balls", "Round tennis_ball", "tennis_ball for Sports", "tennis_balls for Sports"],
    "volleyball": ["volleyball", "volleyballs", "Large volleyball", "Large volleyballs", "Small volleyball", "Small volleyballs", "Medium volleyball", "Medium volleyballs", "Sports volleyball", "Sports volleyballs", "Round volleyball", "volleyball for Sports", "volleyballs for Sports"]
}

# american_football, american_footballs, Large american_football, Large american_footballs, Small american_football, Small american_footballs, Medium american_football, Medium american_footballs, Sports american_football, Sports american_footballs, Round american_football, american_football for Sports, american_footballs for Sports, baseball, baseballs, Large baseball, Large baseballs, Small baseball, Small baseballs, Medium baseball, Medium baseballs, Sports baseball, Sports baseballs, Round baseball, baseball for Sports, baseballs for Sports, basketball, basketballs, Large basketball, Large basketballs, Small basketball, Small basketballs, Medium basketball, Medium basketballs, Sports basketball, Sports basketballs, Round basketball, basketball for Sports, basketballs for Sports, billiard_ball, billiard_balls, Large billiard_ball, Large billiard_balls, Small billiard_ball, Small billiard_balls, Medium billiard_ball, Medium billiard_balls, Sports billiard_ball, Sports billiard_balls, Round billiard_ball, billiard_ball for Sports, billiard_balls for Sports, bowling_ball, bowling_balls, Large bowling_ball, Large bowling_balls, Small bowling_ball, Small bowling_balls, Medium bowling_ball, Medium bowling_balls, Sports bowling_ball, Sports bowling_balls, Round bowling_ball, bowling_ball for Sports, bowling_balls for Sports, cricket_ball, cricket_balls, Large cricket_ball, Large cricket_balls, Small cricket_ball, Small cricket_balls, Medium cricket_ball, Medium cricket_balls, Sports cricket_ball, Sports cricket_balls, Round cricket_ball, cricket_ball for Sports, cricket_balls for Sports, football, footballs, Large football, Large footballs, Small football, Small footballs, Medium football, Medium footballs, Sports football, Sports footballs, Round football, football for Sports, footballs for Sports, golf_ball, golf_balls, Large golf_ball, Large golf_balls, Small golf_ball, Small golf_balls, Medium golf_ball, Medium golf_balls, Sports golf_ball, Sports golf_balls, Round golf_ball, golf_ball for Sports, golf_balls for Sports, hockey_ball, hockey_balls, Large hockey_ball, Large hockey_balls, Small hockey_ball, Small hockey_balls, Medium hockey_ball, Medium hockey_balls, Sports hockey_ball, Sports hockey_balls, Round hockey_ball, hockey_ball for Sports, hockey_balls for Sports, hockey_puck, hockey_pucks, Large hockey_puck, Large hockey_pucks, Small hockey_puck, Small hockey_pucks, Medium hockey_puck, Medium hockey_pucks, Sports hockey_puck, Sports hockey_pucks, Round hockey_puck, hockey_puck for Sports, hockey_pucks for Sports, rugby_ball, rugby_balls, Large rugby_ball, Large rugby_balls, Small rugby_ball, Small rugby_balls, Medium rugby_ball, Medium rugby_balls, Sports rugby_ball, Sports rugby_balls, Round rugby_ball, rugby_ball for Sports, rugby_balls for Sports, shuttlecock, shuttlecocks, Large shuttlecock, Large shuttlecocks, Small shuttlecock, Small shuttlecocks, Medium shuttlecock, Medium shuttlecocks, Sports shuttlecock, Sports shuttlecocks, Round shuttlecock, shuttlecock for Sports, shuttlecocks for Sports, table_tennis_ball, table_tennis_balls, Large table_tennis_ball, Large table_tennis_balls, Small table_tennis_ball, Small table_tennis_balls, Medium table_tennis_ball, Medium table_tennis_balls, Sports table_tennis_ball, Sports table_tennis_balls, Round table_tennis_ball, table_tennis_ball for Sports, table_tennis_balls for Sports, tennis_ball, tennis_balls, Large tennis_ball, Large tennis_balls, Small tennis_ball, Small tennis_balls, Medium tennis_ball, Medium tennis_balls, Sports tennis_ball, Sports tennis_balls, Round tennis_ball, tennis_ball for Sports, tennis_balls for Sports, volleyball, volleyballs, Large volleyball, Large volleyballs, Small volleyball, Small volleyballs, Medium volleyball, Medium volleyballs, Sports volleyball, Sports volleyballs, Round volleyball, volleyball for Sports, volleyballs for Sports

# dict_size(s210)
print(aOcheck_accuracy("WithoutIP/sports15/s210.csv", s210))


# %% [markdown]
# # Points to Plot

# %%
# aO_counts = {
#     4 : [aObase_accuracy("animal4/AO.csv")],
#     8 : [aOcheck_accuracy("animal4/AO8.csv", dict_8)],
#     12 : [aOcheck_accuracy("animal4/AO12.csv", dict_12)],
#     16 : [aOcheck_accuracy("animal4/AO16.csv", dict_16)],
#     20 : [aOcheck_accuracy("animal4/AO20.csv", dict_20)],
#     24 : [aOcheck_accuracy("animal4/AO24.csv", dict_24)],
#     32 : [aOcheck_accuracy("animal4/AO32.csv", dict_32)],
#     36 : [aOcheck_accuracy("animal4/AO36.csv", dict_36)],
#     40 : [aOcheck_accuracy("animal4/AO40.csv", dict_40)],
#     44 : [aOcheck_accuracy("animal4/AO44.csv", dict_44)],
#     48 : [aOcheck_accuracy("animal4/AO48.csv", dict_48)],
#     52 : [aOcheck_accuracy("animal4/AO52.csv", dict_52)],
#     56 : [aOcheck_accuracy("animal4/AO56.csv", dict_56)],
#     60 : [aOcheck_accuracy("animal4/AO60.csv", dict_60)]
# }

# v7_counts = {
#     7 : [96.73],
#     14 : [84.45],
#     21 : [88.35],  
#     42 : [93.47],
#     49 : [93.5],
#     56 : [95.17],
#     63 : [93.74],
#     70 : [95.08]
# }

# cd_counts = {
#     2: [CDcheck_accuracy('CatsvsDogs/cd2.csv', CDdict2 )],
#     4: [CDcheck_accuracy('CatsvsDogs/cd4.csv', CDdict4)],
#     6: [CDcheck_accuracy('CatsvsDogs/cd6.csv', CDdict6)],
#     8: [CDcheck_accuracy('CatsvsDogs/cd8.csv', CDdict8)],
#     10: [CDcheck_accuracy('CatsvsDogs/cd10.csv', CDdict10)],
#     12: [CDcheck_accuracy('CatsvsDogs/cd12.csv', CDdict12)],
#     14: [CDcheck_accuracy('CatsvsDogs/cd14.csv', CDdict14)],
#     16: [CDcheck_accuracy('CatsvsDogs/cd16.csv', CDdict16)],
#     18: [CDcheck_accuracy('CatsvsDogs/cd18.csv', CDdict18)],
#     20: [CDcheck_accuracy('CatsvsDogs/cd20.csv', CDdict20)],
#     22: [CDcheck_accuracy('CatsvsDogs/cd22.csv', CDdict22)],
#     24: [CDcheck_accuracy('CatsvsDogs/cd24.csv', CDdict24)],
#     26: [CDcheck_accuracy('CatsvsDogs/cd26.csv', CDdict26)],
#     28: [CDcheck_accuracy('CatsvsDogs/cd28.csv', CDdict28)],
#     30: [CDcheck_accuracy('CatsvsDogs/cd30.csv', CDdict30)],
#     32: [CDcheck_accuracy('CatsvsDogs/cd32.csv', CDdict32)],
#     36: [CDcheck_accuracy('CatsvsDogs/cd36.csv', CDdict36)],
#     38: [CDcheck_accuracy('CatsvsDogs/cd38.csv', CDdict38)],
#     42: [CDcheck_accuracy('CatsvsDogs/cd42.csv', CDdict42)],
#     44: [CDcheck_accuracy('CatsvsDogs/cd44.csv', CDdict44)],
#     48: [CDcheck_accuracy('CatsvsDogs/cd48.csv', CDdict48)],
#     50: [CDcheck_accuracy('CatsvsDogs/cd50.csv', CDdict50)],
#     52: [CDcheck_accuracy('CatsvsDogs/cd52.csv', CDdict52)],
#     54: [CDcheck_accuracy('CatsvsDogs/cd54.csv', CDdict54)],
#     56: [CDcheck_accuracy('CatsvsDogs/cd56.csv', CDdict56)]
# }

# %%
print("\n Vegetable 15 \n")

# veg_counts = {
#     15 : [aOcheck_accuracy("WithoutIP/Vegetable15/v15.csv", veg15)],
#     30 : [aOcheck_accuracy("WithoutIP/Vegetable15/v30.csv", veg30)],
#     45 : [aOcheck_accuracy("WithoutIP/Vegetable15/v45.csv", veg45)],
#     60 : [aOcheck_accuracy("WithoutIP/Vegetable15/v60.csv", veg60)],
#     75 : [aOcheck_accuracy("WithoutIP/Vegetable15/v75.csv", veg75)],
#     90 : [aOcheck_accuracy("WithoutIP/Vegetable15/v90.csv", veg90)],
#     105 : [aOcheck_accuracy("WithoutIP/Vegetable15/v105.csv", veg105)]
# }

# card_counts = {
#     4 : card_accuracy("Card15/cards4.csv", cards4),
#     8 : card_accuracy("Card15/cards8.csv", cards8),
#     12 : card_accuracy("Card15/cards12.csv", cards12),
#     16 : card_accuracy("Card15/cards16.csv", cards16),
#     20 : card_accuracy("Card15/cards20.csv", cards20),
#     24 : card_accuracy("Card15/cards24.csv", cards24),
#     28 : card_accuracy("Card15/cards28.csv", cards28),
#     32 : card_accuracy("Card15/cards32.csv", cards32),
#     36 : card_accuracy("Card15/cards36.csv", cards36),
#     40 : card_accuracy("Card15/cards40.csv", cards40),
#     44 : card_accuracy("Card15/cards44.csv", cards44),
#     48 : card_accuracy("Card15/cards48.csv", cards48)
    
# }

print("\n Animal 80 \n")
animal80_counts = {
    80 : aOcheck_accuracy("animal80/a80.csv", a80),
    160 : aOcheck_accuracy("animal80/a160.csv", a160),
    240 : aOcheck_accuracy("animal80/a240.csv", a240),
    320 : aOcheck_accuracy("animal80/a320.csv", a320),
    400 : aOcheck_accuracy("animal80/a400.csv", a400)
}

print("\n Food 10 \n")
food10_counts = {10 : [aOcheck_accuracy("WithoutIP/food10/f10.csv", f10)],
                 20 : [aOcheck_accuracy("WithoutIP/food10/f20.csv", f20)],
                 30 : [aOcheck_accuracy("WithoutIP/food10/f30.csv",f30)],
                 40 : [aOcheck_accuracy("WithoutIP/food10/f40.csv",f40)],
                 50 : [aOcheck_accuracy("WithoutIP/food10/f50.csv",f50)],
                 60 : [aOcheck_accuracy("WithoutIP/food10/f60.csv",f60)],
                 70 : [aOcheck_accuracy("WithoutIP/food10/f70.csv",f70)],
                 80 : [aOcheck_accuracy("WithoutIP/food10/f80.csv",f80)],
                 90 : [aOcheck_accuracy("WithoutIP/food10/f90.csv",f90)],
                 100 : [aOcheck_accuracy("WithoutIP/food10/f100.csv",f100)]
                 }

# print(aOcheck_accuracy("food10/f20.csv", f20))


# %%
print("\n Vehicle 20 \n")

v20_counts = {
    20 : [aOcheck_accuracy("WithoutIP/vehicle20/v20.csv", v20)],
    40 : [aOcheck_accuracy("WithoutIP/vehicle20/v40.csv", v40)],
    60 : [aOcheck_accuracy("WithoutIP/vehicle20/v60.csv", v60)],
    80 : [aOcheck_accuracy("WithoutIP/vehicle20/v80.csv", v80)],
    100 : [aOcheck_accuracy("WithoutIP/vehicle20/v100.csv", v100)],
    120 : [aOcheck_accuracy("WithoutIP/vehicle20/v120.csv", v120)],
    140 : [aOcheck_accuracy("WithoutIP/vehicle20/v140.csv", v140)],
    160 : [aOcheck_accuracy("WithoutIP/vehicle20/v160.csv", v160)],
    180 : [aOcheck_accuracy("WithoutIP/vehicle20/v180.csv", v180)],
    200 : [aOcheck_accuracy("WithoutIP/vehicle20/v200.csv", v200)]
}

print("\n Flowers 10 \n")
flowers10_counts = {
    10 : [flowers_accuracy("WithoutIP/flowers10/f10.csv", fl10)],
    20 : [flowers_accuracy("WithoutIP/flowers10/f20.csv", fl20)],
    30 : [flowers_accuracy("WithoutIP/flowers10/f30.csv", fl30)],
    40 : [flowers_accuracy("WithoutIP/flowers10/f40.csv", fl40)],
    50 : [flowers_accuracy("WithoutIP/flowers10/f50.csv", fl50)],
    60 : [flowers_accuracy("WithoutIP/flowers10/f60.csv", fl60)],
    70 : [flowers_accuracy("WithoutIP/flowers10/f70.csv", fl70)],
    80 : [flowers_accuracy("WithoutIP/flowers10/f80.csv", fl80)],
    90 : [flowers_accuracy("WithoutIP/flowers10/f90.csv", fl90)],
    100 : [flowers_accuracy("WithoutIP/flowers10/f100.csv", fl100)]
}

print("\n Fruits 10 \n")
fruits10_counts = {
    10: [aOcheck_accuracy("WithoutIP/fruits10/fr10.csv", fr10)],
    20: [aOcheck_accuracy("WithoutIP/fruits10/fr20.csv", fr20)],
    30: [aOcheck_accuracy("WithoutIP/fruits10/fr30.csv", fr30)],
    40: [aOcheck_accuracy("WithoutIP/fruits10/fr40.csv", fr40)],
    50: [aOcheck_accuracy("WithoutIP/fruits10/fr50.csv", fr50)],
    60: [aOcheck_accuracy("WithoutIP/fruits10/fr60.csv", fr60)],
    70: [aOcheck_accuracy("WithoutIP/fruits10/fr70.csv", fr70)],
    80: [aOcheck_accuracy("WithoutIP/fruits10/fr80.csv", fr80)],
    90: [aOcheck_accuracy("WithoutIP/fruits10/fr90.csv", fr90)],
    100: [aOcheck_accuracy("WithoutIP/fruits10/fr100.csv", fr100)]
}

# %%
print("\n Food 34 \n")
food34_counts = {
    34 : aOcheck_accuracy("WithoutIP/food34/f34.csv", f34),
    68 : aOcheck_accuracy("WithoutIP/food34/f68.csv", f68),
    102 : aOcheck_accuracy("WithoutIP/food34/f102.csv", f102),
    136 : aOcheck_accuracy("WithoutIP/food34/f136.csv", f136),
    170 : aOcheck_accuracy("WithoutIP/food34/f170.csv", f170),
    204 : aOcheck_accuracy("WithoutIP/food34/f204.csv", f204),
}

print("\n Weather 11 \n")
weather11_counts = {
    11 : aOcheck_accuracy("WithoutIP/weather11/w11.csv", w11),
    22 : aOcheck_accuracy("WithoutIP/weather11/w22.csv", w22),
    33 : aOcheck_accuracy("WithoutIP/weather11/w33.csv", w33),
    44 : aOcheck_accuracy("WithoutIP/weather11/w44.csv", w44),
    55 : aOcheck_accuracy("WithoutIP/weather11/w55.csv", w55),
    66 : aOcheck_accuracy("WithoutIP/weather11/w66.csv", w66),
    77 : aOcheck_accuracy("WithoutIP/weather11/w77.csv", w77)
}

print("\n Sports 15 \n")
sports15_counts = {
    15 : aOcheck_accuracy("WithoutIP/sports15/s15.csv", s15),
    30 : aOcheck_accuracy("WithoutIP/sports15/s30.csv", s30),
    45 : aOcheck_accuracy("WithoutIP/sports15/s45.csv", s45),
    60 : aOcheck_accuracy("WithoutIP/sports15/s60.csv", s60),
    75 : aOcheck_accuracy("WithoutIP/sports15/s75.csv", s75),
    90 : aOcheck_accuracy("WithoutIP/sports15/s90.csv", s90),
    105 : aOcheck_accuracy("WithoutIP/sports15/s105.csv", s105)
}

# %% [markdown]
# # Graphing

# %% [markdown]
# ## Individual Accuracies

# %% [markdown]
# ### Animal 80

# %%
a80_acc = float(aOcheck_accuracy("animal80/a80.csv", a80))
a160_acc = float(aOcheck_accuracy("animal80/a160.csv", a160))
a240_acc = float(aOcheck_accuracy("animal80/a240.csv", a240))
a320_acc = float(aOcheck_accuracy("animal80/a320.csv", a320))
a400_acc = float(aOcheck_accuracy("animal80/a400.csv", a400))
a480_acc = float(aOcheck_accuracy("animal80/a480.csv", a480))
a560_acc = float(aOcheck_accuracy("animal80/a560.csv", a560))

animal80_accList = [a80_acc, a160_acc, a240_acc, a320_acc, a400_acc, a480_acc, a560_acc]

# %% [markdown]
# ### Flowers 10

# %%
f10_acc = float(flowers_accuracy("WithoutIP/flowers10/f10.csv", fl10))
f20_acc = float(flowers_accuracy("WithoutIP/flowers10/f20.csv", fl20))
f30_acc = float(flowers_accuracy("WithoutIP/flowers10/f30.csv", fl30))
f40_acc = float(flowers_accuracy("WithoutIP/flowers10/f40.csv", fl40))
f50_acc = float(flowers_accuracy("WithoutIP/flowers10/f50.csv", fl50))
f60_acc = float(flowers_accuracy("WithoutIP/flowers10/f60.csv", fl60))
f70_acc = float(flowers_accuracy("WithoutIP/flowers10/f70.csv", fl70))
f80_acc = float(flowers_accuracy("WithoutIP/flowers10/f80.csv", fl80))
f90_acc = float(flowers_accuracy("WithoutIP/flowers10/f90.csv", fl90))
f100_acc = float(flowers_accuracy("WithoutIP/flowers10/f100.csv", fl100))
f110_acc = float(flowers_accuracy("WithoutIP/flowers10/fl110.csv", fl110))
f120_acc = float(flowers_accuracy("WithoutIP/flowers10/fl120.csv", fl120))
f130_acc = float(flowers_accuracy("WithoutIP/flowers10/fl130.csv", fl130))
f140_acc = float(flowers_accuracy("WithoutIP/flowers10/fl140.csv", fl140))

flowers10_accList = [f10_acc, f20_acc, f30_acc, f40_acc, f50_acc, f60_acc, f70_acc, f80_acc, f90_acc, f100_acc, f110_acc, f120_acc, f130_acc, f140_acc]

# %% [markdown]
# ### Food 10

# %%
#food10
f10_acc = float(aOcheck_accuracy("WithoutIP/food10/f10.csv", f10))
f20_acc = float(aOcheck_accuracy("WithoutIP/food10/f20.csv", f20))
f30_acc = float(aOcheck_accuracy("WithoutIP/food10/f30.csv", f30))
f40_acc = float(aOcheck_accuracy("WithoutIP/food10/f40.csv", f40))
f50_acc = float(aOcheck_accuracy("WithoutIP/food10/f50.csv", f50))
f60_acc = float(aOcheck_accuracy("WithoutIP/food10/f60.csv", f60))
f70_acc = float(aOcheck_accuracy("WithoutIP/food10/f70.csv", f70))
f80_acc = float(aOcheck_accuracy("WithoutIP/food10/f80.csv", f80))
f90_acc = float(aOcheck_accuracy("WithoutIP/food10/f90.csv", f90))
f100_acc = float(aOcheck_accuracy("WithoutIP/food10/f100.csv", f100))
f110_acc = float(aOcheck_accuracy("WithoutIP/food10/f110.csv", f110))
f120_acc = float(aOcheck_accuracy("WithoutIP/food10/f120.csv", f120))
f130_acc = float(aOcheck_accuracy("WithoutIP/food10/f130.csv", f130))
f140_acc = float(aOcheck_accuracy("WithoutIP/food10/f140.csv", f140))
f150_acc = float(aOcheck_accuracy("WithoutIP/food10/f150.csv", f150))
f160_acc = float(aOcheck_accuracy("WithoutIP/food10/f160.csv", f160))
fx170_acc = float(aOcheck_accuracy("WithoutIP/food10/f170.csv", fx170))
f180_acc = float(aOcheck_accuracy("WithoutIP/food10/f180.csv", f180))

food10_accList = [f10_acc, f20_acc, f30_acc, f40_acc, f50_acc, f60_acc, f70_acc, f80_acc, f90_acc, f100_acc, f110_acc, f120_acc, f130_acc, f140_acc, f150_acc, f160_acc, fx170_acc, f180_acc]

# %% [markdown]
# ### Food 34

# %%
f34_acc = float(aOcheck_accuracy("WithoutIP/food34/f34.csv", f34))
f68_acc = float(aOcheck_accuracy("WithoutIP/food34/f68.csv", f68))
f102_acc = float(aOcheck_accuracy("WithoutIP/food34/f102.csv", f102))
f136_acc = float(aOcheck_accuracy("WithoutIP/food34/f136.csv", f136))
f170_acc = float(aOcheck_accuracy("WithoutIP/food34/f170.csv", f170))
f204_acc = float(aOcheck_accuracy("WithoutIP/food34/f204.csv", f204))
f236_acc = float(aOcheck_accuracy("WithoutIP/food34/f238.csv", f238))
f272_acc = float(aOcheck_accuracy("WithoutIP/food34/f272.csv", f272))
f306_acc = float(aOcheck_accuracy("WithoutIP/food34/f306.csv", f306))
f340_acc = float(aOcheck_accuracy("WithoutIP/food34/f340.csv", f340))
f372_acc = float(aOcheck_accuracy("WithoutIP/food34/f372.csv", f372))

food34_accList = [f34_acc, f68_acc, f102_acc, f136_acc, f170_acc, f204_acc, f236_acc, f272_acc, f306_acc, f340_acc, f372_acc]

# %% [markdown]
# ### Fruits 10

# %%
fr10_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr10.csv", fr10))
fr20_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr20.csv", fr20))
fr30_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr30.csv", fr30))
fr40_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr40.csv", fr40))
fr50_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr50.csv", fr50))
fr60_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr60.csv", fr60))
fr70_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr70.csv", fr70))
fr80_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr80.csv", fr80))
fr90_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr90.csv", fr90))
fr100_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr100.csv", fr100))
fr110_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr110.csv", fr110))
fr120_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr120.csv", fr120))
fr130_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr130.csv", fr130))
fr140_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr140.csv", fr140))
fr150_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr150.csv", fr150))
fr160_acc = float(aOcheck_accuracy("WithoutIP/fruits10/fr160.csv", fr160))

fruits10_accList = [fr10_acc, fr20_acc, fr30_acc, fr40_acc, fr50_acc, fr60_acc, fr70_acc, fr80_acc, fr90_acc, fr100_acc, fr110_acc, fr120_acc, fr130_acc, fr140_acc, fr150_acc, fr160_acc]

# %% [markdown]
# ### Sports 15

# %%
s15_acc = float(aOcheck_accuracy("WithoutIP/sports15/s15.csv", s15))
s30_acc = float(aOcheck_accuracy("WithoutIP/sports15/s30.csv", s30))
s45_acc = float(aOcheck_accuracy("WithoutIP/sports15/s45.csv", s45))
s60_acc = float(aOcheck_accuracy("WithoutIP/sports15/s60.csv", s60))
s75_acc = float(aOcheck_accuracy("WithoutIP/sports15/s75.csv", s75))
s90_acc = float(aOcheck_accuracy("WithoutIP/sports15/s90.csv", s90))
s105_acc = float(aOcheck_accuracy("WithoutIP/sports15/s105.csv", s105))
s120_acc = float(aOcheck_accuracy("WithoutIP/sports15/s120.csv", s120))
s135_acc = float(aOcheck_accuracy("WithoutIP/sports15/s135.csv", s135))
s150_acc = float(aOcheck_accuracy("WithoutIP/sports15/s150.csv", s150))
s165_acc = float(aOcheck_accuracy("WithoutIP/sports15/s165.csv", s165))
s180_acc = float(aOcheck_accuracy("WithoutIP/sports15/s180.csv", s180))
s195_acc = float(aOcheck_accuracy("WithoutIP/sports15/s195.csv", s195))
s210_acc = float(aOcheck_accuracy("WithoutIP/sports15/s210.csv", s210))

sports15_accList = [s15_acc, s30_acc, s45_acc, s60_acc, s75_acc, s90_acc, s105_acc, s120_acc, s135_acc, s150_acc, s165_acc, s180_acc, s195_acc, s210_acc]

# %% [markdown]
# ### Vehicle 20

# %%
v20_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v20.csv", v20))
v40_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v40.csv", v40))
v60_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v60.csv", v60))
v80_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v80.csv", v80))
v100_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v100.csv", v100))
v120_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v120.csv", v120))
v140_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v140.csv", v140))
v160_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v160.csv", v160))
v180_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v180.csv", v180))
v200_acc = float(aOcheck_accuracy("WithoutIP/vehicle20/v200.csv", v200))

vehicle20_accList = [v20_acc, v40_acc, v60_acc, v80_acc, v100_acc, v120_acc, v140_acc, v160_acc, v180_acc, v200_acc]

# %% [markdown]
# ### Weather 11

# %%
w11_acc = float(aOcheck_accuracy("WithoutIP/weather11/w11.csv", w11))
w22_acc = float(aOcheck_accuracy("WithoutIP/weather11/w22.csv", w22))
w33_acc = float(aOcheck_accuracy("WithoutIP/weather11/w33.csv", w33))
w44_acc = float(aOcheck_accuracy("WithoutIP/weather11/w44.csv", w44))
w55_acc = float(aOcheck_accuracy("WithoutIP/weather11/w55.csv", w55))
w66_acc = float(aOcheck_accuracy("WithoutIP/weather11/w66.csv", w66))
w77_acc = float(aOcheck_accuracy("WithoutIP/weather11/w77.csv", w77))
w88_acc = float(aOcheck_accuracy("WithoutIP/weather11/w88.csv", w88))
w99_acc = float(aOcheck_accuracy("WithoutIP/weather11/w99.csv", w99))
w110_acc = float(aOcheck_accuracy("WithoutIP/weather11/w110.csv", w110))

weather11_accList = [w11_acc, w22_acc, w33_acc, w44_acc, w55_acc, w66_acc, w77_acc, w88_acc, w99_acc, w110_acc]

# %%
def append_accuracies(category_counts, label, color, marker):
    amount_categories = []
    accuracies = []

    # Calculate accuracy for each category count
    for count, accuracy in category_counts.items():
        if isinstance(accuracy, list):
            for each in accuracy:
                amount_categories.append(count)
                accuracies.append(each)
        else:
            amount_categories.append(count)
            accuracies.append(accuracy)

    # Debug print
    print(len(amount_categories), len(accuracies))
    
    # Plot data with the specified label and color
    plt.plot(amount_categories, accuracies, marker=marker, linestyle='None', color=color, label=label)


# %% [markdown]
# ## Graphs < 10

# %%
# plt.figure(figsize=(10, 6))
# plt.xlabel('Number of Categories')
# plt.ylabel('Accuracy (%)')
# plt.title('Accuracy vs. Number of Categories')
# plt.grid()
# plt.legend()

# #Calling function
# append_accuracies(aO_counts,"Animals4", "blue", "o")
# append_accuracies(v7_counts,"Vehicles7", "green", "^")
# append_accuracies(cd_counts,"Cats vs Dogs", "red", "s")
# append_accuracies(card_counts,"Cards4", "orange", "P")


# a4_patch = mpatches.Patch(color='blue', label='4 Animals')
# v7_patch = mpatches.Patch(color='green', label='7 Vehicles')
# cd_patch = mpatches.Patch(color='red', label='Cats vs Dogs')
# card_patch = mpatches.Patch(color='orange', label='4 Suits of Cards')



# plt.legend(handles=[a4_patch, v7_patch, cd_patch, card_patch])

# #Axis ranges

# # plt.xlim(0, 80)  
# # plt.ylim(0, 100)

# plt.show()

# %% [markdown]
# ## Initial Categories >= 10

# %%
plt.figure(figsize=(10, 6))
plt.xlabel('Number of Categories')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy vs. Number of Categories')
plt.grid()
plt.legend()

#Calling function
# append_accuracies(veg_counts,"Vegetables15", "green", "D")
append_accuracies(animal80_counts,"Animal80", "black", "X")
append_accuracies(food10_counts, "food10", "blue", "*" )
append_accuracies(v20_counts,"Vehicle20", "red", "^")
append_accuracies(flowers10_counts, "flowers10", "purple", "P")
append_accuracies(fruits10_counts, "fruits10", "orange", "o")
append_accuracies(food34_counts, "food34", "yellow", "s")
append_accuracies(weather11_counts, "weather11", "pink", "x")
append_accuracies(sports15_counts, "sports15", "cyan", "D")

# veg_patch = mpatches.Patch(color='green', label='15 Vegetables')
a80_patch = mpatches.Patch(color='black', label='80 Animals')
f10_patch = mpatches.Patch(color = 'blue', label='10 Foods')
v20_patch = mpatches.Patch(color = 'red', label='20 Vehicles')
fl10_patch = mpatches.Patch(color = 'purple', label='10 Flowers')
fruits10_patch = mpatches.Patch(color = 'orange', label='10 Fruits')
food34_patch = mpatches.Patch(color = 'yellow', label='34 Foods')
weather11_patch = mpatches.Patch(color = 'pink', label='11 Weather')
sports15_patch = mpatches.Patch(color = 'cyan', label='15 Sports')

plt.legend(handles=[a80_patch, f10_patch, v20_patch, fl10_patch, 
                    fruits10_patch, food34_patch, weather11_patch, sports15_patch])

#Axis ranges
# plt.xlim(0, 80)  
# plt.ylim(0, 100)

plt.show()

# %% [markdown]
# # Accuracy Trends Across Datasets

# %%
import matplotlib.pyplot as plt

iterations = list(range(1, 19))  # Define a larger range to cover all possible lengths

datasets = {
    "animal80": animal80_accList,
    
    "food10": food10_accList,

    "vehicle20": vehicle20_accList,

    "flowers10": flowers10_accList,

    "fruits10": fruits10_accList,

    "food34": food34_accList,

    "weather11": weather11_accList,

    "sports15": sports15_accList
}

plt.figure(figsize=(12, 6))

for dataset_name, accuracies in datasets.items():
    x_values = iterations[:len(accuracies)]  # Match the length of iterations to the dataset
    plt.plot(x_values, accuracies, label=dataset_name, marker='o')

plt.xlabel('Number of Redundant Categories Added', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.title('Accuracy Trends Across Datasets', fontsize=14)
plt.grid(True)
plt.legend(title="Datasets", fontsize=10)

plt.show()


# %% [markdown]
# # Overall Increase per each new Semantic Category

# %%
# Pad the shorter list with NaN to make lengths equal
max_length = max(len(flowers10_accList), len(food10_accList), len(fruits10_accList), len(sports15_accList), len(vehicle20_accList), len(food34_accList), len(weather11_accList), len(animal80_accList))


sports15_accList += [np.nan] * (max_length - len(sports15_accList))
vehicle20_accList += [np.nan] * (max_length - len(vehicle20_accList))
flowers10_accList += [np.nan] * (max_length - len(flowers10_accList))
food10_accList += [np.nan] * (max_length - len(food10_accList))
fruits10_accList += [np.nan] * (max_length - len(fruits10_accList))
food34_accList += [np.nan] * (max_length - len(food34_accList))
weather11_accList += [np.nan] * (max_length - len(weather11_accList))
animal80_accList += [np.nan] * (max_length - len(animal80_accList))

data = {
    "Sports15": sports15_accList,
    "Vehicle20": vehicle20_accList,
    "Flowers10": flowers10_accList,
    "Food10": food10_accList,
    "Fruits10": fruits10_accList,
    "Food34": food34_accList,
    "Weather11": weather11_accList,
    "Animal80": animal80_accList
}

df = pd.DataFrame(data)

df_diff = df.diff().iloc[1:]  # First row will be NaN because there's no previous value
df_diff["Average Change"] = df_diff.mean(axis=1)  

plt.figure(figsize=(10, 6))
plt.plot(df_diff.index, df_diff["Average Change"], marker='o', label='Average Accuracy Change', color='blue')

plt.axhline(0, color='red', linestyle='--', linewidth=1)  
plt.xlabel('Iteration (Number of Categories Added)', fontsize=12)
plt.ylabel('Average Accuracy Change (%)', fontsize=12)
plt.title('Average Accuracy Increase or Decrease per Iteration', fontsize=14)
plt.grid(True)
plt.legend(fontsize=10)

plt.show()

# %% [markdown]
# ## Cumulative Accuracy Increase Over Iterations

# %%
# Calculate cumulative accuracy increase
df_diff["Cumulative Change"] = df_diff["Average Change"].cumsum()

plt.figure(figsize=(10, 6))
plt.plot(df_diff.index, df_diff["Cumulative Change"], marker='o', label='Cumulative Accuracy Increase', color='green')

plt.axhline(0, color='red', linestyle='--', linewidth=1)  # Horizontal line at 0 for reference
plt.xlabel('Iteration (Number of Categories Added)', fontsize=12)
plt.ylabel('Cumulative Accuracy Increase (%)', fontsize=12)
plt.title('Cumulative Accuracy Increase Over Iterations', fontsize=14)
plt.grid(True)
plt.legend(fontsize=10)

plt.show()

# %% [markdown]
# ## Cumulative Accuracy Increase Over Iterations Before 7

# %%
df_diff_filtered = df_diff.iloc[:6]  # Keep rows before 7

plt.figure(figsize=(10, 6))
plt.plot(df_diff_filtered.index, df_diff_filtered["Cumulative Change"], marker='o', label='Cumulative Accuracy Increase', color='green')

plt.axhline(0, color='red', linestyle='--', linewidth=1)  # Horizontal line at 0 for reference
plt.xlabel('Iteration (Number of Categories Added)', fontsize=12)
plt.ylabel('Cumulative Accuracy Increase (%)', fontsize=12)
plt.title('Cumulative Accuracy Increase Over Iterations (After 6 Iterations)', fontsize=14)
plt.grid(True)
plt.legend(fontsize=10)

plt.show()

# %% [markdown]
# ## Cumulative Accuracy Increase Over Iterations After 7

# %%
df_diff_filtered = df_diff.iloc[7:]  # Keep only rows from 7 on

plt.figure(figsize=(10, 6))
plt.plot(df_diff_filtered.index, df_diff_filtered["Cumulative Change"], marker='o', label='Cumulative Accuracy Increase', color='green')

plt.axhline(0, color='red', linestyle='--', linewidth=1) 
plt.xlabel('Iteration (Number of Categories Added)', fontsize=12)
plt.ylabel('Cumulative Accuracy Increase (%)', fontsize=12)
plt.title('Cumulative Accuracy Increase Over Iterations (After 6 Iterations)', fontsize=14)
plt.grid(True)
plt.legend(fontsize=10)

plt.show()





# %% [markdown]
# ### The above shows, accuracy increase plateaus

# %% [markdown]
# ## Average Total Increase (at peak accuracy)

# %%
average_changes = df.apply(lambda x: max(x.dropna()) - x.dropna().iloc[0])

print("Max Increase per Set:")
print(average_changes)

print("\n\n")
print("Average Increase Across Sets:")

average_allLarge = average_changes.sum() / len(average_changes)
print(average_allLarge)

# %% [markdown]
# ## Samall vs Large Initial Categories

# %%
card_accList = analysistopy.card_accList
v7_accList = analysistopy.v7_accList
aO_accList = analysistopy.aO_accList
catDog_accList = analysistopy.catDog_accList

# print(card_accList)
# print(v7_accList)
# print(aO_accList)
# print(catDog_accList)

# %%
# Pad the shorter list with NaN to make lengths equal
max_lengthSmall = max(len(card_accList), len(v7_accList), len(aO_accList), len(catDog_accList))

card_accList += [np.nan] * (max_lengthSmall - len(card_accList))
v7_accList += [np.nan] * (max_lengthSmall - len(v7_accList))
aO_accList += [np.nan] * (max_lengthSmall - len(aO_accList))
catDog_accList += [np.nan] * (max_lengthSmall - len(catDog_accList))

dataSmall = {
    "Card4": card_accList,
    "Veg7": v7_accList,
    "Animal4": aO_accList,
    "CatDog": catDog_accList
}

small_df = pd.DataFrame(dataSmall)

# %% [markdown]
# ## Average Total Increase (at peak accuracy)

# %%
average_changesSmall = small_df.apply(lambda x: max(x.dropna()) - x.dropna().iloc[0])

print("Max Increase per Set (small sets):")
print(average_changesSmall)

average_allSmall = average_changesSmall.sum() / len(average_changesSmall)


# %% [markdown]
# ### Note: around 1/3 the increase when compared to just the larger datasets 

# %%
average_all = (average_changesSmall.sum() + average_changes.sum()) / 12

print("Average increase for small sets: ", average_allSmall)
print("Average increase for larger sets: ", average_allLarge)
print("Average increase for all sets: ", average_all)

# %%
plt.figure(figsize=(10, 6))

x = np.array(["Total", "Large Amount of Initial Categories", "Small Amount of Initial Categories"])
y = np.array([average_all, average_allLarge, average_allSmall])

colors = ['green','purple', 'blue']

plt.bar(x,y, color = colors)


