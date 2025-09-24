# Capítulo 25 - Módulo e pacotes de Python
# Módulos e pacotes são dois construtos usados em Python
# para organizar programas maiores. Este capítulo introduz módulos
# em Python, como eles são acessados, definidos e como Python
# encontra módulos etc.
#------------------------------------------
# Módulos
# Um módulo lhe permite agrupar funções relacionadas, classes
# e código em geral. Você pode pensar em um módulo como sendo uma
# espécie de biblioteca de código (apesar de, na verdade,
# muitas bibliotecas são, elas mesmas, compostas de muitos
# módulos como, por exemplo, uma biblioteca pode ter extensões
# ou opcionais para sua funcionalidade central).
# É útil organizar seu código em módulos quando o código
# ou se torna grande ou quando você gostaria de reutilizar
# alguns elementos do código base em múltiplos projetos.
# Dividindo um corpo grande de código de um único arquivo lhe ajuda
# a simplificar a manutenção, compreensibilidade, teste, reutilização,
# e escopo do código. Esses são explicados abaixo:
#   * Simplicidade - Focar em um subconjunto de um problema geral
#       nos ajuda a desenvolver soluções que funcionam para o 
#       subconjunto e podem ser combinadas para resolver o problema
#       geral. Isto significa que módulos individuais podem ser
#       mais simples que a solução geral.
#   * Manutenção -  Módulos tipicamente tornam mais fácil definir limites
#       lógicos entre um corpo de código e outro. Isto significa que é
#       mais fácil ver o que compreende um módulo e verificar que
#       o módulo funciona de maneira apropriada mesmo quando modificado.
#       Também ajuda a distinguir um corpo de código de outro, tornando
#       mais fácil encontrar onde mudancas devreia ir
#   * Teste -   Como um módulo pode ser feito independente um do outro
#       há menos dependências e cruzamentos. Isto significa que um 
#       módulo pode ser testado em isolamento e mesmo antes de outros módulos,
#       e a aplicação geral, terem sido escritas.
#   * Reusabilidade -   Definir uma função ou classe em um módulo significa
#       que é mais fácil reutilizá-la em outro módulo, como os limites
#       entre um módulo e outro são claros.
#   * Escopo -  Módulos