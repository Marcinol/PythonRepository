
def umyjRece():
    print("Wkladam rece do wody")
    print("Myje mydlem")
    print("Plucze rece", "\n")

def zjedz(produkty):
    print("Nakładam", produkty[0])
    print("Nakładam", produkty[1])
    print("Nakładam", produkty[2])
    print("Zjadam z apetytem", "\n")

produktyNaObiad = ["kotlet", "ziemniaki", "sałatke"]
produktyNaDeser = ["szarlotke", "kompot", "lody"]

# wywolanie funkcji
umyjRece()
zjedz(produktyNaObiad)
zjedz(produktyNaDeser)
umyjRece()