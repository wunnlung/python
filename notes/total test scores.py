def main():
    x = eval(input("how many students? "))
    holder = 0
    inp = 0
    for i in range(x):
        inp = eval(input("what is student "+str(i+1)+"s grade? "))
        holder = holder + inp
    #print(holder/x)
    print("show\nfeet\n.\n.\n.\nNOW")
main()
