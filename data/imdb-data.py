from statistics import mean, median

def reader(filename):
    file = open(filename, "r", encoding="utf-8")
    for row in file:
        yield row

def main():
    # Create the generator, and save in the __data__ variable
    data = reader("data.tsv")

    genres = {}

    # Kick the generator, so we skip the first item
    first_row = next(data)
    print(first_row)

    # Loop through the yielded items, one at a time
    for row in data:
        items = row.strip("\n").split("\t")

        if len(items) == 9:
            genre_string = items[8]
            for genre in genre_string.split(","):
                if genre in genres.keys():
                    genres[genre] += 1
                else:
                    genres[genre] = 1

    with open("imdb-data-results.txt", "w") as file:
        file.write("\n".join(list(map(str, genres.items()))))

main()
