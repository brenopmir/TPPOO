# TP_POO
Trabalho prático da disciplina POO, sistema de automação residencial com interface Gráfica

Alunos: 
 Breno Pereira Miranda - 2023038930; 
 Davi Nascimento Andrade da Silva - 2023038817; 
 Lucas Abreu Velloso - 2023038795; 


Apresentação do Problema:
Nos últimos anos, principalmente durante a pandemia do Covid-19, houve o surgimento e crescimento explosivo da indústria 4.0. Além disso, houve grande desenvolvimento e popularização das tecnologias da informação, que tomaram papéis importantes em todas as áreas de consumo, auxiliando as pessoas a resolverem diversos problemas e a melhorarem a qualidade de vida. Uma das novas aplicações que surgiu nesse crescimento foi a automação residencial, atra- vés de soluções de engenharia de controle e automação, que permite controlar diversos aspectos de uma casa de forma automática, como iluminação, temperatura, segurança, etc.

A falta de automação residencial pode gerer diversas problematicas como falta de conectividade e personalização , conforto e segurnaça comprometido,além de ineficiencia energetica e consequentimente mais gastos financeiros.

Tendo em vista a relevância do tópico apresentado e a proximidade com nossa área de estudo no curso, decidimos realizar esse trabalho com o objetivo de desenvolver um sistema de automação residencial, que visa controlar e automatizar vários aspectos de uma casa comum, como controlar ativação de luzes, abertura de cortinas, ar condicionado,criação de modos que empregam o conjunto dessas funcionalidades etc.

Visão Geral da Solução:
Nossa solução visa que o usuário consiga controlar , de forma rapida ,facil e totalmente remota, sua casa. O programa ira conseguir controlar,por meio de uma interface gráfica , cada objeto separadamente no cômodo,todas as entidades do programa possuem classes de objetos que são organizadas segundo a lógica de programação orientada a objeto.

Estrutura do Projeto:
O projeto será separado em classes, 7 classes relacionadas ao funcionamento, cada classe irá possuir uma interface (encontrados presente na pasta "Interface") e a implementação das classes (encontrados na pasta "objects"),além de possuir um arquivo planilha.py(encontrados na pasta "objects") que possui a função de inicializar as planilhas e a parte da interface gráfica e a main que interliga todos os processos(ambas encontrada na pasta "Interface_grafica") 


Instruções de Instalação:
O usuário precisará de: 
• Ambiente de edição 
• Instalação do python
• Instalação da biblioteca openpyxl   
• Instalação da biblioteca custom tkinter
• Instalação da biblioteca PIL(Pillow)

Instruções de Uso:
O usuário, através de um menu disponibilizado na interface, terá a oportunidade de interagir com o sistema,ou seja realizar diversas transações pelo botoes e outros objetos iterativos.

Além disso, o usuário terá a capacidade de personalizar cada dispositivo individualmente, alterando seu status, utilizando funcionalidades específicas disponibilizadas para cada dispositivo. Todas essas modificações serão salvas em arquivos Excel, que posteriormente serão transformados em um display interativo.