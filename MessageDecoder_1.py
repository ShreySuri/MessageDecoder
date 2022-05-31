

composite = int(input(print("Enter the coded message. ")))

characters = 0

while composite >= 100 ** characters:
    characters = characters + 1


for i in range (0, characters):
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
    elif remainder == "15":
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
    elif remainder == "38":
        print("r")
    elif remainder == "39":
        print("s")
    elif remainder == "40":
        print("t")
    elif remainder == "41":
        print("u")
    elif remainder == "42":
        print("v")
    elif remainder == "43":
        print("w")
    elif remainder == "44":
        print("x")
    elif remainder == "45":
        print("y")
    elif remainder == "46":
        print("z")

    elif remainder == "47":
        print("A")
    elif remainder == "48":
        print("B")
    elif remainder == "49":
        print("C")
    elif remainder == "50":
        print("D")
    elif remainder == "51":
        print("E")
    elif remainder == "52":
        print("F")
    elif remainder == "53":
        print("G")
    elif remainder == "54":
        print("H")
    elif remainder == "55":
        print("I")
    elif remainder == "56":
        print("J")
    elif remainder == "57":
        print("K")
    elif remainder == "58":
        print("L")
    elif remainder == "59":
        print("M")
    elif remainder == "60":
        print("N")
    elif remainder == "61":
        print("O")
    elif remainder == "62":
        print("P")
    elif remainder == "63":
        print("Q")
    elif remainder == "64":
        print("R")
    elif remainder == "65":
        print("S")
    elif remainder == "66":
        print("T")
    elif remainder == "67":
        print("U")
    elif remainder == "68":
        print("V")
    elif remainder == "69":
        print("W")
    elif remainder == "70":
        print("X")
    elif remainder == "71":
        print("Y")
    elif remainder == "72":
        print("Z")

    elif remainder == "73":
        print("'")
    elif remainder == "74":
        print(",")
    elif remainder == "75":
        print("/")
    elif remainder == "76":
        print("")
    elif remainder == "77":
        print(":")
    elif remainder == "78":
        print(";")
    elif remainder == "79":
        print(".")
    elif remainder == "80":
        print("!")
    elif remainder == "81":
        print("?")
    else:
        print("You have typed an unrecognized symbol")
    
    composite = quotient
  
