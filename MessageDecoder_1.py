

composite = int(input(print("Enter the coded message. ")))

characters = 0

while composite >= 100 ** characters:
    characters = characters + 1

counter = characters

for i in range (0, counter):
    characters = counter - characters
    remainder = composite % 100
    quotient = (composite - remainder)/100
    remainder = str(remainder)
    
    if remainder == "10":
        print("0")
    elif remainder == "11":
        print("1")
    elif remainder == "12":
        print("2")
    elif remainder =="13":
        print("3")
    elif remainder == "14":
        print("4")
    elif remainder == "15"
        print("5")
    elif remainder == "16":
        print("6")
    elif remainder == "17":
        print("7")
    elif remainder == "18":
        print("8")
    elif remainder == "19":
        print("9")

    elif remainder == "20":
        print("a")
    elif remainder == "21":
        print("b")
    elif remainder == "22":
        print("c")
    elif remainder == "23":
        print("d")
    elif remainder == "24":
        print("e")
    elif remainder == "25":
        print("f")
    elif remainder == "26":
        print("g")
    elif remainder == "27":
        print("h")
    elif remainder == "28":
        print("i")
    elif remainder == "29":
        print("j")
    elif remainder == "30":
        print("k")
    elif remainder == "31":
        print("l")
    elif remainder == "32":
        print("m")
    elif remainder == "33":
        print("n")
    elif remainder == "34":
        print("o")
    elif remainder == "35":
        print("p")
    elif remainder == "37":
        print("q")
    
    
    
        print("")
        print("You have typed an unrecognized symbol. Please refresh the program, follow directions, and try again. ")
        
    place_value = place_value - 1
