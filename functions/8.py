def greet(lang):
    match lang:
        case 'en':
            return "Hi!"
        case 'fr':
            return "Salut!"
        case 'pt':
            return "Ola!"
        case 'de':
            return "Hallo!"
        case 'sv':
            return "Hej!"
        case 'af':
            return "Haai!"
        case _:
            return "Please choose en, fr, pt, de, sv, af"

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
