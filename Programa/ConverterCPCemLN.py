letra1 = input("Digite a primeira letra da função lógica (adicione ~ para negar): ")
letra2 = input("Didite a segunda letra da função lógica (adicione ~ para negar): ")
operador = input("Digite o operador logico (E, OU, SE, SE ... ENTÂO: ").lower()


print("Logica:", letra1, operador, letra2)



def AliceHael(operador):
    
    if "e" in operador:    
        letra1E = "O céu está lindo "
        letra2E = " está chovendo"
        resultadoAILONESERGIO = ("Resultado: " + letra1E + operador + letra2E)
        print(resultadoAILONESERGIO)
        
    elif "ou" in operador:
        letra1OU =  "Esta chovendo "
        letra2OU = " o ceu esta limpo"
        resultadoChurusbango = ("Resultado: " + letra1OU + operador + letra2OU)
        print(resultadoChurusbango)
        
    elif "se" == operador:
        letra1SE = "está calor"
        letra2SE = "tomarei um copo d'agua"
        resultadoFeijaocomFarinha = ("Resultado: " + "Se" + letra1SE + letra2SE)
        print(resultadoFeijaocomFarinha)
    
    elif "se ... então" in operador:
        letra1SEENT =  "choveu de madrugada "
        letra2SEENT = " a rua esta molhada"
        resultadoAlekFumaca = ("Resultado: " + "Se" + letra1SEENT + "então" + letra2SEENT)
        print(resultadoAlekFumaca)
        
    return

def OgroBlue(letra1, letra2, operador):
    
    if "~" in letra1 and "e" in operador:    
        letra1En1 = "Não tem comida "
        letra2En1 = " iremos ao mercado"
        resultadoGames = ("Resultado: " + letra1En1 + operador + letra2En1)
        print(resultadoGames)
        
    elif "~" in letra2 and "e" in operador:
        letra1En2 =  "Ligamos para o numero "
        letra2En2 = " ninguem nos atendeu"
        resultadoChurrasco = ("Resultado: " + letra1En2 + operador + letra2En2)
        print(resultadoChurrasco)
        
    elif "~" in letra1 and "ou" in operador:
        letra1OUn1 = "Não esta dando certo "
        letra2OUn1 = " errei em algo"
        resultadoPython = ("Resultado: " + letra1OUn1 + operador + letra2OUn1)
        print(resultadoPython)
        
    elif "~" in letra2 and "ou" in operador:
        letra1OUn2 = "A mosca morreu "
        letra2OUn2 = " fugiu do quarto"
        resultadoLobotomia = ("Resultado: "+ letra1OUn2 + operador + letra2OUn2)
        print(resultadoLobotomia)
        
     
    elif "~" in letra1 and "se" in operador:
        letra1SEn1 =  "não podemos comprar isso "
        letra2SEn1 = " estamos sem dinheiro"
        resultadoCNH = ("Resultado: " + "Se" + letra1SEn1 + letra2SEn1)
        print(resultadoCNH)
    
    elif "~" in letra2 and "se" in operador:
        letra1SEn2 =  "você fizer isso "
        letra2SEn2 = " irá se arrepender"
        resultadoWarH40 = ("Resultado: " + "Se" + letra1SEn2 + letra2SEn2)
        print(resultadoWarH40)
        
    elif "~" in letra1 and "se ... então" in operador:
        letra1SEENTn1 = "não tem controle sobre isso "
        letra2SEENTn1 = " mude sua estrategia"
        resultadoMitAia = ("Resultado: " + "Se" + letra1SEENTn1 + "então" + letra2SEENTn1)
        print(resultadoMitAia)
        
    elif "~" in letra2 and "se ... então" in operador:
        letra1SEENTn2 = "esta programando com sono "
        letra2SEENTn2 = " não tera nomes normais"
        resultadoCirrose = ("Resultado: " + "Se" + letra1SEENTn2 + "então" + letra2SEENTn2)
        print(resultadoCirrose)
        
    
    


if "~" in letra1 or "~" in letra2:
    prob = OgroBlue(letra1, letra2, operador)
else:
    tran = AliceHael(operador)