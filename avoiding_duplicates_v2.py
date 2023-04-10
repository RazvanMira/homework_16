def read_unique_words() -> list:
    result = []

    while True:
        user_input = input("Please type in a word: ")
        if user_input == "":
            break
        if user_input not in result:
            result.append(user_input)
    
    return result


def main():
    result = read_unique_words()

    for item in result:
        print(item)


if __name__ == "__main__":
    main()