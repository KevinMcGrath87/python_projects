def calc_tip(amount= input("what is the bill amount?"), split=input("how many people will split the bill?")):
    amount = float(amount)
    split = float(split)
    round(amount, 2)
    twentyPercent = amount*1.2
    eighteenPercent = amount* 1.18
    fifteenPercent = amount * 1.15
    tipOut= []
    tipOut.append(round(twentyPercent/split,2))
    tipOut.append(round(eighteenPercent/split,2))
    tipOut.append(round(fifteenPercent/split,2))
    return(f"per person tip at twenty percent is: {tipOut[0]} at eighteen percent is {tipOut[1]} and fifteen percent is {tipOut[2]}")



print(calc_tip())