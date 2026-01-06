# Capítulo 39 - Sockets em Python
# Um Socket é um endpoint em um link de comunicação entre processos separados.
# Em Python, sockets são objetos que fornecem uma maneira de trocar informação
# entre dois processos de maneira direta e independente de plataforma.
# ---------------------------------------
# Comunicação Socket com Socket
# Quando fois processos de nível de sistema operacional querem se comunicar,
# eles podem fazê-lo através de sockets. Cada processo tem um socket que é
# conectado ao socket do outro. Então, um processo pode escrever informação no
# socket, enquanto o segundo processo pode ler informação do socket.
# Associado com cada socket estão dois fluxos, um para entrada e um para saída.
# Assim, para passar informação de um processo para outro, deve-se escrever
# informação para o fluxo de saída de um objeto socket e lê-lo do fluxo de
# entrada de outro objeto socket (assumindo que ambos estão conectados).
# Vários tipos diferentes de sockets estão disponíveis, mas nesse capítulo vamos
# focar no TCP/IP. Um socket assim é orientado-a-conexão que fornecerá uma
# garantia de entrega dos dados (ou notificação em caso de falha na entrega).
# TCP/IP é uma suite de protocolos de comunicação usados para interconectar
# dispositivos de rede na internet ou em uma intranet privada. TCP/IP especifica
# como dados são trocados entre programas pela internet fornecendo comunicações
# end-to-end que identificam como os dados deveriam ser divididos em pacotes
# (packets), endereçados, transmitidos, roteados(routed) e recebidos no destino.
# ---------------------------------------------
# Preparando uma conexão
# Para preparar uma conexão, um processo deve estar executando um programa que
# esteja esperando por uma conexão enquando o outro deve tentar conectar com o
# primeiro programa. O primeiro é chamado como socket servidor e o segundo
# apenas socket. Para o segundo processo se conectar com o primeiro, deve saber
# qual máquina o primeiro está executando e qual porta está conectado.
# Por exemplo, na figura socketconection.png o socket servidor se conecta com
# a porta 8084. Por sua vez, o socket cliente se conecta à máquina na qual o
# servidor está executando e à porta 8084 daquela máquina.
# Nada acontece até que o socket servidor aceite a conexão. Naquele ponto, os
# sockets estão conectados, e os fluxos de sockets estão ligados um com o outro.
# Isto significa que o fluxo de saída do servidor está conectado ao fluxo de
# entrada do socket cliente e vice versa.
# -----------------------------------------------
# Uma aplicação de exemplo de cliente servidor
# O diagrama socketconection.png ilustra a estrutura básica do sistema que vamos
# tentar construir. Haverá um objeto servidor executando na máquina e um objeto
# cliente executando em outra. O cliente conectará ao servidor usando sockets
# para poder obter informação.
# A aplicação real sendo implementada neste exemplo é uma aplicação de busca de
# endereços. Os endereços dos empregados de uma empresa são armazenados em um
# dicionário. Este dicionário é configurado no programa do servidor mas poderia
# igualmente ser armazenado em uma base de dados etc. Quando um cliente se conecta
# com o servidor, pode obter o endereço do escritório de um empregado.
#
