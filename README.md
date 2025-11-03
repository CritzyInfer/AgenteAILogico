Transformação de texto em CPC (Cálculo Proposicional Clássico) em LN (Linguagem Natural)

Trabalho realizado na faculdade Uni-Facef de Franca-SP
Curso: Ciências da computação
Integrantes: Pedro H. S. Rodrigues


1-Introdução
	O código é feito para que transforme termos lógicos em frases como:	

2- Funcionamento
	O código funciona de maneira simples e com sistema de baixa complexidade usando Python. Para que seja feito a tradução de LN para CPC, o código pede para que o usuário digite uma frase, em seguida, a frase é separada em duas partes, sendo elas “Frase1” e “Frase2”, após a separação, o código analisa as frases e o conectivo aplicado (exemplo: Frase digitada: “O dia está quente e ensolarado”; Aqui a frase 1 é “O dia está quente”, o conectivo sendo o “e” e a frase 2 “ensolarado”). Seguindo para depois da análise, o código, de forma simples, troca as frases por letras já pré-determinadas e o conectivo por um símbolo que o represente(C v Q). A negação também é identificada pelo código ao ler a palavra “Não”, que adiciona ‘~’ à frente da letra para que seja identificada como negada.
	A outra parte do código, o inverso da que foi explicada anteriormente, é a transformação de CPC para LN. Aqui, assim como na anterior, possui elementos pré determinados, as frases em LN. O usuário é proposto a digitar duas letras de cada vez e após isso, selecione o conectivo, o código lê as letras e símbolos de negação, e transforma em uma frase específica para aquela junção (Exemplo: C v E pode se tornar C= “o dia está calmo”  e E = “está com tempo de chuva”).

3-Melhorias e limitações
	Não é usado nenhum tipo de Inteligência Artificial (IA) para que as frases sejam traduzidas, o que limita as possibilidades de frase para que substituam o CPC na Linguagem Natural. A solução também apresenta um código simples em funcionamento, sendo construído apenas com “IF 's” e sobreposição de elementos. Porém, a possibilidade de melhora é quase infinita, podendo usar mais Python para que seja melhorado, ou até mesmo outras linguagens ou ferramentas, como API 's de softwares (GPT).
