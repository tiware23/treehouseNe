def sillycase(single):
    value = int(len(single))
    div = round(value / 2)
    print(single[:div].lower() + single[div:].upper() )

sillycase(input("Give me the word: "))
