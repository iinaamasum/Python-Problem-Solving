import pyjokes


def tell_some_jokes(lang):
    print(pyjokes.get_joke(language=lang))


while True:
    print("\n1 -> tell jokes.")
    print("0 -> exit\n")
    val = int(input("Enter choice: "))
    print()
    if val == 0:
        break
    if val == 1:
        print("Select Language: ")
        print("1 -> en")
        print("2 -> de")
        print("3 -> es\n")

        choice = int(input("Enter Language: "))
        if choice == 1:
            lang = "en"
        elif choice == 2:
            lang = "de"
        elif choice == 3:
            lang = "es"

        tell_some_jokes(lang)
