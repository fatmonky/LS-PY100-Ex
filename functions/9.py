def extract_language(locale):
    return locale.split('_')[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

'''
My wrong answer, which is a hardcode: 
def extract_language(locale):
    match locale:
        case 'en_US.UTF-8':
            return 'en'
        case 'en_GB.UTF-8':
            return 'en'
        case 'ko_KR.UTF-16':
            return 'ko'
        case _:
            return "no locale."

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko
'''

