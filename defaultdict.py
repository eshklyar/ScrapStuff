from collections import defaultdict

def greet(language):
    lang_list = [("english", "Welcome")
    , ("czech", "Vitejte")
    , ("danish", "Velkomst")
    , ("dutch", "Welkom")
    , ("estonian", "Tere tulemast")
    , ("finnish", "Tervetuloa")
    , ("flemish", "Welgekomen")
    , ("french", "Bienvenue")
    , ("german", "Willkommen")
    , ("irish", "Failte")
    , ("italian", "Benvenuto")
    , ("latvian", "Gaidits")
    , ("lithuanian", "Laukiamas")
    , ("polish", "Witamy")
    , ("spanish", "Bienvenido")
    , ("swedish", "Valkommen")
    , ("welsh", "Croeso")]

    lang_dict = dict(lang_list)
    langs = defaultdict(lambda: ("Welcome"), lang_dict)

    return langs[language]
#         return lang_dict.get(language, "Welcome")
print(greet('czech'))

 # better way is to use lang_dict.get(language, "Welcome")