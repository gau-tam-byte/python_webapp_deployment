from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """ converts eng to fr """

    etf = MyMemoryTranslator(source="en", target="fr", str="fr").translate(englishtext)

    return etf

def frenchtoenglish(frenchtext):
    """ converts fr to eng"""
    fte = MyMemoryTranslator(source="french", target="en").translate(frenchtext)
    return fte
