import random

win=0
loss=0
tie = 0
anslist = ["kivi","paber","käärid"]
botanswer = random.choice(anslist)

pans = input("Vali <kivi, paber, käärid>")
print(f"\nSa vali {pans}, arvuti vali {botanswer}.\n")

if pans == botanswer:
    print(f"Viik")
    tie+=1
elif pans == "kivi":
    if botanswer == "käärid":
          print("Sa võitsid")
          win+=1
    else:
        print("Sa kaotsid")
        loss+=1
elif pans == "paber":
    if botanswer == "kivi":
          print("Sa võitsid")
          win+=1
    else:
        print("Sa kaosid")
        loss+=1
elif pans == "käärid":
    if botanswer == "paber":
          print("Sa võitsid")
          win+=1
    else:
        print("Sa kaotsid")
        loss+=1
print ("Sul on %d võitu!" % win)
print ("Sul on %d kaotust" % loss)
print ("Sul on %d viiki!" % tie)
