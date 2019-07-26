import time

start_time = time.time()

# New approach: use a balanced binary search tree for O(n log n) time complexity
# Consideration: Do both lists use capitalization equally? Yes. But in unknown data sets, should convert to all caps to avoid missed duplicates from casing differences. Can use upper() when creating tree, and .title() before printing duplicate list
# Edge Case: One or both lists are empty? Still prints nothing.
# Edge Case: No duplicates found. Print nothing or error message?




# Open each file and read list, converting to a balanced BST
f = open('names_3.txt', 'r')
names_1 = f.read().split("\n")  # Shortened test list of names
f.close()

f = open('names_4.txt', 'r')
names_2 = f.read().split("\n")  # Shortened test list of names
f.close()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

duplicates = []

# Iterate through name_1, searching for match in name_2
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# 64 duplicates:
# Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines, Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs, Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts, Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias, Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris, Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre, Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle, Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto, Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause, Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran, Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates, Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach, River Johnson, Ali Collier

# Original runtime: 10.137041330337524 seconds