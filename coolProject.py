#Abdullah Sultan
#5/26/2025, 8:02AM
#fun coding project while in chilean philosophy

def calculateAura(phrase):
    aura = 0
    phrase = phrase.lower()
    if phrase == "sigma":
        aura += 10000
    elif phrase == "skibidi":
        aura -= 10000
    elif phrase == "yogurt":
        print("gurt: sybau")
        aura += 20000
    elif phrase == "rizzler":
        aura -= 7000
    elif phrase == "rizz":
        aura += 3000
    elif phrase == "goon":
        aura += 2000
    elif phrase == "gooner":
        aura -= 1000
    elif phrase == "unempluzz":
        print("You lost all of your aura. SYBAU.")
    print(f"You now have {aura} aura. ")
    return aura
    






def main():
    userInput = "x"
    
    while userInput != "q":    
        userInput = input("Enter a phrase to determine your aura, or enter 'q' to quit: ")
        aura = calculateAura(userInput)
    
    if userInput == "q":
        if aura >= 20000:
            print(f"YOU ARE A SUPER SIGMA!")
        elif aura <= 0:
            print("You are a GOONER.")
        elif aura <= -1000:
            print("You are UNEMPLUZZ.")
main()
