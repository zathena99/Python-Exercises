#StackExample

movies = []
snacks = []

for i in range(3):
    movie = input("Enter movie " + str(i + 1) + " of 3: ")
    movies.append(movie)

for i in range(3):
    snack = input("Enter snack " + str(i + 1) + " of 3: ")
    snacks.append(snack)

print("Movies to watch are: ")
for movie in movies:
    print(movie)

print("Snacks available are: ")
for snack in snacks:
    print(snack)

while snacks:
    print("Snacks remaining:", snacks)
    response = input("Press S each time you finish a snack: ")

    if response.upper() == "S":
        snack = snacks.pop()

print("No more snacks.")