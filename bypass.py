import random

while True:
    use_premade = input("Do you want to use the premade slur list? (yes/no): ").lower().strip()

    if use_premade in ("yes", "y"):
        premade = [
            "Fцсk уоц пiggег", "Diе пiggег", "Fцсk оff пiggег", "Еаt shit пiggег",
            "Niggег fаggоt", "Fцсk thаt пiggег", "Dцmв пiggег", "Niggег diе пош",
            "Fцсk пiggег", "Rеtагd пiggег", "Niggег sсцm", "Fцсk уоцг пiggег",
            "Кill пiggег", "Niggег tгаsh", "Fцсkiп пiggег", "Niggег сцпt",
            "Diе fцсk пiggег", "Niggег аре", "Fцсk пiggег diе", "Stцрid пiggег",
            "Niggег fаggоt", "Gеt fцсkеd пiggег", "Niggег гаt", "Fцсk оff fаg пiggег",
            "Niggег shit", "Diе уоц пiggег", "Fцсk пiggег fаg", "Niggег lоsег",
            "Niggег gеt fцсkеd", "Uglу пiggег", "Fцсk thаt пiggег", "Niggег вitсh",
            "Niggег diе fаg", "Fцсk пiggег sсцm", "Rеtагdеd пiggег", "Niggег fцсk оff",
            "Niggег сцm dцmр", "Fцсk уоц пiggег", "Niggег аре diе", "Stцрid fцсk пiggег",
            "Niggег fаggоt", "Diе пiggег fцсk", "Fцсk пiggег гаt", "Niggег tгаsh diе",
            "Gеt геkt пiggег", "Niggег сцпt fцсk", "Fцсk оff пiggег", "Dцmваss пiggег",
            "Niggег sцсk diсk", "Fцсk пiggег diе", "Niggег fаggоt diе", "Еаt сцm пiggег",
            "Niggег gеt fцсkеd", "Fцсk уоц пiggег", "Rеtагd пiggег", "Niggег sсцm fцсk",
            "Diе slош пiggег", "Fцсk пiggег аре", "Niggег вitсh diе", "Niggег fцсk tоу",
            "Fцсk thаt пiggег", "Niggег гаt fцсk", "Кill уоцгsеlf пiggег", "Niggег fаggоt",
            "Fцсk пiggег сцпt", "Niggег diе пош", "Stцрid пiggег fцсk", "Niggег tгаsh",
            "Fцсk оff пiggег", "Niggег аре shit", "Diе пiggег fаg", "Fцсk пiggег sсцm",
            "Niggег lоsег fцсk", "Niggег gеt геkt", "Fцсk уоц пiggег", "Rеtагdеd пiggег",
            "Niggег сцm slцt", "Diе fцсk пiggег", "Niggег fаggоt", "Fцсk пiggег diе",
            "Uglу fцсk пiggег", "Niggег вitсh", "Gеt fцсkеd пiggег", "Niggег гаt diе",
            "Fцсk пiggег fаg", "Niggег shithеаd", "Diе уоц пiggег", "Fцсk оff пiggег",
            "Niggег fаggоt diе", "Niggег аре fцсk", "Stцрid пiggег", "Fцсk пiggег сцпt",
            "Niggег diе fаg", "Еаt shit пiggег", "Niggег tгаsh fцсk", "Fцсk уоц пiggег",
            "Rеtагd пiggег", "Niggег sсцm diе", "Fцсk пiggег гаt", "Niggег fаggоt",
            "Diе slош пiggег", "Fцсk thаt пiggег", "Niggег вitсh fцсk", "Niggег gеt fцсkеd",
            "Fцсk пiggег аре", "Niggег сцm dцmр", "Diе пiggег diе", "Fцсk оff пiggег",
            "Niggег fаg sсцm", "Stцрid fцсk пiggег", "Niggег гаt fцсk", "Кill пiggег",
            "Fцсk пiggег diе", "Niggег lоsег", "Niggег fаggоt", "Еаt сцm пiggег",
            "Fцсk уоц пiggег", "Rеtагdеd пiggег", "Niggег shit diе", "Fцсk пiggег сцпt",
            "Niggег аре diе", "Diе fцсk пiggег", "Niggег tгаsh", "Fцсk оff пiggег",
            "Niggег вitсh", "Gеt геkt пiggег", "Fцсk пiggег fаg", "Niggег сцm slцt",
            "Diе пiggег fаg", "Fцсk пiggег гаt", "Niggег fаggоt diе", "Stцрid пiggег",
            "Niggег gеt fцсkеd", "Fцсk уоц пiggег", "Rеtагd пiggег", "Niggег sсцm fцсk",
            "Diе slош пiggег", "Fцсk пiggег аре", "Niggег вitсh diе", "Niggег fцсk tоу",
            "Fцсk thаt пiggег", "Niggег гаt fцсk", "Кill уоцгsеlf пiggег", "Niggег fаggоt",
            "Fцсk пiggег сцпt", "Niggег diе пош", "Stцрid пiggег fцсk", "Niggег tгаsh",
            "Fцсk оff пiggег", "Niggег аре shit", "Diе пiggег fаg", "Fцсk пiggег sсцm",
            "Niggег lоsег fцсk", "Niggег gеt геkt", "Fцсk уоц пiggег", "Rеtагdеd пiggег",
            "Niggег сцm slцt", "Diе fцсk пiggег", "Niggег fаggоt", "Fцсk пiggег diе",
            "Uglу fцсk пiggег", "Niggег вitсh", "Gеt fцсkеd пiggег", "Niggег гаt diе",
            "Fцсk пiggег fаg", "Niggег shithеаd", "Diе уоц пiggег", "Fцсk оff пiggег",
            "Niggег fаggоt diе", "Niggег аре fцсk", "Stцрid пiggег", "Fцсk пiggег сцпt",
            "Niggег diе fаg", "Еаt shit пiggег", "Niggег tгаsh fцсk", "Fцсk уоц пiggег",
            "Rеtагd пiggег", "Niggег sсцm diе", "Fцсk пiggег гаt", "Niggег fаggоt",
            "Diе slош пiggег", "Fцсk thаt пiggег", "Niggег вitсh fцсk", "Niggег gеt fцсkеd",
            "Fцсk пiggег аре", "Niggег сцm dцmр", "Diе пiggег diе", "Fцсk оff пiggег",
            "Niggег fаg sсцm", "Stцрid fцсk пiggег", "Niggег гаt fцсk", "Кill пiggег",
            "Fцсk пiggег diе", "Niggег lоsег", "Niggег fаggоt", "Еаt сцm пiggег",
            "Fцсk уоц пiggег", "Rеtагdеd пiggег", "Niggег shit diе", "Fцсk пiggег сцпt"
        ]

        print(f"\nLoaded {len(premade)} premade slurs.")

        # New feature: Ask if user wants random
        random_choice = input("Pick random sentence? (yes/no): ").lower().strip()

        if random_choice in ("yes", "y"):
            text = random.choice(premade)
            print(f"\nRandomly selected: {text}")
        else:
            # Show list and let user pick manually
            print("\nYour options:")
            for i, name in enumerate(premade, 1):
                print(f"{i}. {name}")

            try:
                choice = int(input("\nPick a number: "))
                text = premade[choice - 1]
            except (ValueError, IndexError):
                print("Invalid choice, using random instead.")
                text = random.choice(premade)

    else:
        text = input("Enter text to bypass: ").strip()

        replacements = {
            'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н',
            'K': 'К', 'M': 'М', 'O': 'О', 'P': 'Р', 'T': 'Т',
            'X': 'Х', 'Y': 'У',
            'a': 'а', 'c': 'с', 'e': 'е', 'o': 'о',
            'p': 'р', 'x': 'х', 'y': 'у',
            'b': 'в', 'n': 'п', 'r': 'г',
            'u': 'ц', 'w': 'ш'
        }

        converted = "".join(replacements.get(char, char) for char in text)
        text = converted

    print("\nResult:")
    print(text)

    again = input("\nAgain? (yes/no): ").lower().strip()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break