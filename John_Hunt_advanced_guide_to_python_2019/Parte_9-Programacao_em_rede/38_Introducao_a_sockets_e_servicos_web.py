# Capítulo 38 - Introução a sockets e serviços web

# Nos próximos dois capítulos exploraremos as abordagens baseadas em sockets e
# serviços wev para comunicações interprocessos. Estes processos podem estar
# executando no mesmo computador ou em diferentes computadore sna mesma área
# de rede local ou podem estar geograficamente distantes. Em todos os casos, a
# informação é enviada por um programa executando em um processo para outro
# programa executando em um processo separao por sockets da internet.
# -----------------------------------------
# Sockets
# Os sockets, ou sockets do Protocolo de Internet(IP), fornecem uma interface
# de programação para a stack do protocolo de rede que é gerenciada pelo
# sistema operacional. Usando essa API significaque o programador é abstraído
# dos detalhes de nível baixo de como dados são trocados entre processos em
# computadores (possivelmente) diferentes e pode, em vez disso, focar nos
# aspectos de nível mais alto de sua solução.
# Existem alguns tipos diferentes de sockets IP disponíveis, mas o foco deste
# livro são Sockets de Fluxo (Stream Sockets). Um socket de fluxo usa o protocolo
# de controle de transmissão(Transmission Control Protocol, TCP) para enviar
# mensagens, Tais sockets são comumente referidos como sockets TCP/IP.
# TCP fornece a transmissão de dados ordenada e confiável através da conexão
# entre dois dispositivos (ou hospedeiros/hosts). Isto pode ser importante
# pois TCP garante que, para cada mensagem enviada, todas as mensagens não
# apenas chegarão ao destino, mas que também chegarão na ordem correta.
# Uma alternativa comum ao TCP é o Protocolo de Datagrama do Usuário(User
# Datagram Protocol, UDP). O UDP não dá qualquer garantia de entrega(isto é,
# mensagens podem ser perdidas ou podem chegar fora de ordem). Entretanto,
# UDP é um protocolo mais simples e pode ser útil para sistemas de broadcast,
# onde múltiplos clientes podem precisar receber os dados publicados por um
# hospedeiro (em particular, se a perda de dados não é um problema).
# -------------------------------------------------
# Serviços web
# Um Serviço Web é um serviço oferecido por um computador hóspede que pode
# ser invocado por um cliente remoto usando o Protocolo de Transferência de
# Hipertexto (Hypertext Transfer Protocol, HTTP). HTTP pode ser executado
# sobre qualquer protocolo de transporte de fluxo confiável, apesar de ser
# normalmente usado com o TCP/IP. Foi originalmente desenvolvido para permitir
# que dados sejam transferidos entre um servidor HTTP e um navegador da web
# para que dados possam ser apresentados de uma forma legível para humanos
# para o usuário. Entetanto, quando usado com um serviço web, é usado para suportar
# a comunicação de programa para programa entre um cliente e um servidor usando
# formatos de dados legíveis por máquina. Atualmente, este formato é tipicamente
# JSON(Java Script Object Notation), apesar de XML ter sido bastante usado no passado.

# ------------------------------------------------
# Serviços de endereçamento
# Todo dispositivo(hóspede) conectado à internet tem uma identidade única (estamos
# ignorando redes privadas aqui). Esta identidade única é representada como um
# endereço de IP. Usando um endereço de IP podemos nos conectar com um socket
# de um hóspede específico em qualquer lugar na internet. Portanto, é possível
# conectar com vários tipos de dispositivos diferentes desta maneira, desde
# impressoras até caixas registradoras, de geladeiras até servidores, mainframes,
# PCs etc.
# Os endereços de IP tem um formato comum como 144.124.16.237. Um endereço de
# IP versão 4 sempre é um conjunto de 4 números separados por pontos. Cada
# número pode estar na faixa entre 0 e 255, de modo que a faixa completa dos
# endereços de IP é de 0.0.0.0 até 255.255.255.255.
# Um endereço de IP pode ser dividido em duas partes; a parte indicando a rede
# na qual o hóspede está conectado e o ID do host, por exemplo:
# 144.124.16 |.237
# ID rede    |ID hóspede
# Assim:
#   * Os elementos do ID da rede do endereço de IP identifica uma rede específica
#       na qual o hóspede está localizado.
#   * O ID Hóspede é a parte do endereço de IP que especifica um dispositivo
#       específico na rede (como o computador).
# Em qualquer rede podem haver múltiplos hóspedes, cada um com seu próprio
# ID hóspede, mas com um ID de rede compartilhado. Por exemplo, em uma rede
# residencial, poderiam haver:
#   * 192.168.1.1 laptop da Jasmine
#   * 192.168.1.2 PD do Adam
#   * 192.168.1.3 Impressora da casa
#   * 192.168.1.4 Smart TV
# De várias maneiras, os elementos id da rede e id do hóspede de um endereço
# de IP são como o endereço postal para uma casa na rua. O nome da rua equivaleria
# ao ID da rede enquanto o número da casa ao ID do hóspede.
# Neste ponto, poderia estar se perguntando onde as URLs que vemos nos navegadores
# web (como www.bbc.co.uk) entram na história. Eles são nomes textuais que, na
# verdade, mapeiam para um endereço IP. O mapeamento é realizado por uma coisa
# chamada Sistema de Domínio de Nomes (Domain Name System, DNS). Um servidor
# DNS age como um serviço de busca para fornecer o IP de verdade de um nome textual
# de URL em particular. A presença de uma versão textual em inglês do endereço do
# hóspede é porque humanos tem maior facilidade em lembrar um nome significativo
# em vez do que poderiam parecer uma sequência aleatória de números.
# Existem vários sites da web que podem ser usados para ver esses mapeamentos.
# Alguns dos exemplos de como nome textuais em inglês mapeiam com um endereço
# IP são:
#   * www.aber.ac.uk - 144.124.16.237
#   * www.uwe.ac.uk - 164.11.132.96
#   * www.bbc.net.uk - 212.58.249.213
#   * www.gov.uk - 151.101.188.144
# Note que esses mapeamentos eram corretos quando o livro foi escrito; eles
# podem mudar conforme novas entradas são fornecidas aos servidores DNS
# causando com que um nome textual particular seja mapeado a um hóspede físico diferente.
# --------------------------------------------------
# Localhost
# Existe um endereço IP especial que é normalmente disponível em um computador
# hóspede(host) e é muito útil para desenvolvedores e testadores. Ele é:
#   127.0.0.1
# Também conhecido como localhost, o que é mais fácil de lembrar. Ele é usado
# para se referir ao computador em que está atualmente quando um programa é
# executado; isto é, seu computador hóspede local (por isso 'localhost').
# Por exemplo, se quiser iniciar um socket de servidor em seu computador local
# e quer que um programa de cliente socket, executando no mesmo computador, seja
# conectado ao programa servidor, pode dizê-lo para fazer isso conectando-o ao localhost.
# Isto é bastante útil quando ou você não sabe o endereço IP do seu computador
# local ou porquê o código pode ser executado em vários computadores diferentes,
# cada um tendo seu próprio endereço IP. Isto é bastante comum se estiver escrevendo
# código de teste que será usado para desenvolvedores ao executar seus próprios
# testes em máquinas diferentes. Usaremos localhost nos próximos dois capítulos
# como uma maneira de especificar onde procurar por um programa servidor.
# ------------------------------------------------
# Números de 'Porta'?(Port)
# Cada dispositivo/hóspede na internet pode, normalmente, suportar vários
# processos. Portanto, é necessário garantir que cada processo tenha seu próprio
# canal de comunicações. Para fazer isso, cada hóspede tem disponível a ele
# múltiplas portas às quais um programa pode se conectar. Por exemplo, porta 80
# é geralmente salva para servidores web HTTP, enquanto porta 25 é reservada
# para servidores SMTP. Isto significa que se um cliente quer conectar a um
# servidor HTTP em um computador particular, então deve especificar a porta 80
# e não a 25 naquele hóspede.
# Um número de porta é escrito após o endereço IP do hóspede e separado do
# endereço por dois pontos, por exemplo:
#   * www.aber.ac.uk:80 -> indica a porta 80 na máquina hóspede que irá,
#       normalmente, estar executando um servidor HTTP, neste caso para
#       a Universidade Aberystwyth,
#   * www.uwe.ac.uk:25 -> indica a porta 25 em um hóspede executando na Universidade
#       do Oeste da Inglaterra, Bristol. Porta 25 é normalmente reservada para
#       servidores SMTP(Simple Mail Transfer Protocol).
# Números de porta no sistema IP são números de 16 bits na faixa 0-65536.
# Geralmente, números abaixo de 1024 são reservados para serviços pré-definidos
# (que significa que você deveria evitar usá-los a menos que queira comunicar-se
# com um daqueles serviços, como o email SMTP, ftp etc). Portanto, é comum escolher
# uma porta acima de 1024 ao configurar seus próprios serviços.
# --------------------------------------------------
# IPv4 versus IPv6
# O que foi descrito neste capítulo em termos de endereços IP é, de fato, baseado
# no IPv4. Esta versão do Protocolo de Internet foi desenvolvida durante os
# anos 70(1970-1980) e publicadas pelo IETF(Internet Engineering Task Force)
# em setembro de 1981 (substituindo uma definição anterior publicada em 01/1980).
# Esta versão do padrão usa 32 bits binários para cada elemento dos endereços
# hóspedes (por isso 0 - 255). Isto dá um total de 4,29 bilhões de endereços
# únicos possíveis. Em 1981, isso parecia um número gigantesco, e era certamente
# suficiente na época para a internet.
# Desde 1981, a internet se tornou a espinha dorsal não só da própria World
# Wide Web, mas também do conceito da Internet das Coisas (na qual todo dispositivo
# possível poderia conectar-se à internet, desde a geladeira até sistemas de
# aquecimento ou uma torradeira). Esta explosão potencial dos dispositivos/hóspedes
# endereçáveis na internet levou, no meio dos anos 90, a preocupações sobre a
# eventual falta de endereços IP usando o IPv4. Por isso, o IETF projetou uma
# nova versão do Protocolo da Internet: o Protocolo da Internet versão 6(IPv6).
# Ele foi ratificado como um Padrão da Internet em Julho de 2017.
# IPv6 usa endereços de 128 bits para cada elemento em um endereço hóspede. Também
# usa 8 grupos de números (em vez de 4) que são separados por dois pontos. Cada
# grupo de números tem 4 dígitos hexadecimais. Um exemplo é:
#   2001:0DB8:AC10:FE01:EF69:B5ED:DD57:2CLE
# A adoção do endereço IPv6 tem sido mais lenta que o esperado originalmente,
# em parte pelos IPv4 e IPv6 não serem interoperáveis, mas também pela utilização
# de endereços IPv4 não ter sido tão rápida como muitos temiam originalmente.
# -------------------------------------------------
# Sockets e Serviços Web em Python
# Os próximos dois capítulos discutem como sockets e serviços web podem ser
# implementados em Python. O primeiro capítulo discute ambos sockets gerais e
# sockets de servidores HTTP. O o segundo olha como a biblioteca Flask pode ser
# usada para criar serviços da web que executem em HTTP usando sockets TCP/IP.

# <https://codebeautify.org/website-to-ip-address> Site de mapeamento de URLS a endereços de IP.
