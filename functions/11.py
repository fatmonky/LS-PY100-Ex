def extract_region(locale):
    return locale.split('_')[1].split('.')[0]

def extract_language(locale):
    return locale.split('_')[0]

def greet(lang):
    match lang:
        case 'en':
            pass
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
            return "Please choose a country which speaks en, fr, pt, de, sv, af"

def local_greet(locale):
    # use extract_region to parse locale for region
    region = extract_region(locale)
    # use extract_language to parse locale for language
    lang = extract_language(locale)
    # run greet
    if lang == 'en' and region == 'US':
        return "Hey!"
    elif lang == 'en' and region == 'GB':
        return "Hello!"
    elif lang == 'en' and region == 'AU':
        return "Howdy!"
    else:
        return greet(lang)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

# model answer uses match, with language and region.
# then it uses the default case to call and return greet with lang
'''
def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)
'''
