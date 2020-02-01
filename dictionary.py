
words = {
    "hi": 1001,
    "goodbye": 1002,
    "idiot": 9999
}



words_to_check = ["hi", "goodbye", "hello", "idiot", "moron"]
for word in words_to_check:
    if words.get(word):
        print(f"Yes they have used the word '{word}'")
    else:
        print(f"No, they haven't used the word '{word}'")
