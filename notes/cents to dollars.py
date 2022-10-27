#input how many cents someone has
#Tell them/output how much money it is in dollars and cents
def main():
    cents = eval(input("how many cents you got? "))
    Dollars = cents//100
    Cents = cents%100
    if Dollars == 1:
        print("so I can steal", Dollars, "dollar and", Cents, "cents from you")        
    else:
        print("so I can steal", Dollars, "dollars and", Cents, "cents from you")

main()
