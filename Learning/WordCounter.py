def WordCounter():
    text = input("Enter a sentence or paragraph: ")
    words = text.split()
    count = len(words)
    print("Your total words are: ", int(count))

WordCounter()