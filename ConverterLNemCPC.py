def NegaLoca(frase, NEG):
    Cortes = frase.split()
    indice = frase.find(NEG)

    if "não" in Cortes and indice != -1:
        IndiceNegaLoca = Cortes.index("não")
        if IndiceNegaLoca + 1 < len(Cortes):
            return frase[len(NEG):].strip()
    return None


def PabloVitar(corte, corteAnt, operador, temNegacao=False):
    corteSimbolo = "C"
    corteAntSimbolo = "Q"

    
    if (temNegacao + corte):
        corteAntSimbolo = "~" + corteSimbolo
        
    elif (temNegacao + corteAnt):
        corteAntSimbolo = "~" + corteAntSimbolo

    
    if operador == " e ":
        simbolo = "∧"
    elif operador == " ou ":
        simbolo = "∨"
    elif operador == " então ":
        simbolo = "→"
    elif operador == " se e somente se ":
        simbolo = "↔"
    else:
        simbolo = "?"

    return f"{corteAntSimbolo} {simbolo} {corteSimbolo}"


frase = input("Digite sua frase: ").lower()


E = " e "
OU = " ou"
NEG = "não"
IMPLIC = " então "
BICON = " se e somente se "


Negona = NegaLoca(frase, NEG)
temNegacao = Negona is not None


if E in frase:
    indiceE = frase.find(E)
    if indiceE != -1:
        corte = frase[indiceE + len(E):]
        corteAnt = frase[:indiceE]
        print("Corte:", corte)
        print("CorteAnterior:", corteAnt)
        print("Forma lógica:", PabloVitar(corte, corteAnt, E, temNegacao))


if OU in frase:
    indiceOU = frase.find(OU)
    if indiceOU != -1:
        corte = frase[indiceOU + len(OU):]
        corteAnt = frase[:indiceOU]
        print("Corte:", corte)
        print("CorteAnterior:", corteAnt)
        print("Forma lógica:", PabloVitar(corte, corteAnt, OU, temNegacao))


if "se " in frase and IMPLIC in frase:
    indiceSE = frase.find(IMPLIC)
    if indiceSE != -1:
        corte = frase[indiceSE + len(IMPLIC):]
        corteAnt = frase[:indiceSE]
        print("Corte:", corte)
        print("CorteAnterior:", corteAnt)
        print("Forma lógica:", PabloVitar(corte, corteAnt, IMPLIC, temNegacao))


if "se " in frase and "somente se" in frase:
    indiceBICON = frase.find(BICON)
    if indiceBICON != -1:
        corte = frase[indiceBICON + len(BICON):]
        corteAnt = frase[:indiceBICON]
        print("Corte:", corte)
        print("CorteAnterior:", corteAnt)
        print("Forma lógica:", PabloVitar(corte, corteAnt, BICON, temNegacao))
