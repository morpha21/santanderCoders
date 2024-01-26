# Longevidade de Técnicos e Desempenho de Times em um Campeonato

Este projeto visa analisar um conjunto de dados sobre o campeonato brasileiro de futebol de 2019. O objetivo aqui é explorar os dados e descobrir se há relação entre a longevidade de 
um técnico em um time e o desempenho do time no campeonato. Para isto, foi fornecido um arquivo `.json` com os dados. Este projeto encerra o primeiro módulo do curso, Lógica de 
Programação II em Python. O módulo focou apenas na biblioteca padrão do Python e, para não fugir da proposta do módulo, nenhuma biblioteca externa é usada. 

A biblioteca Pandas foi usada apenas para a importação dos dados, conforme recomendado no enunciado do projeto. Tão logo importei os dados, tratei de transformar o DataFrame em uma 
lista de listas, para não correr o risco de obter algum comportamento estranho ao tentar manipular o DataFrame como uma lista. Em seguida, analisei a estrutura dos dados fornecidos e 
criei uma miríade de funções que me permitissem fazer uma análise desses dados. 

Também não foram usados conceitos de programação orientada a objetos. Embora eu creia que fizesse sentido implementar Classes e Métodos, evitei fazer seu uso para não fugir do 
conteúdo ministrado no módulo em questão. O projeto provavelmente ficaria melhor organizado se as diversas funções criadas fossem alocadas em módulos ou pacotes separados, mas isto 
também não foi abordado no curso até então.

Eu basicamente decidi encarar essas limitações como requisitos do projeto. 


### Estado atual: 

A análise foi iniciada. Já consta nela uma relação de técnicos, o time onde atingiram maior longevidade, e a quantidade de jogos em que atuaram no respectivo time. Há também uma 
relação com a quantidade de pontos por partida que cada técnico obteve para cada time. 

### Por fazer: 

- Analisar a relação entre longevidade dos técnicos e a quantidade de pontos por partida que fazem;
- Analisar a relação entre longevidade dos técnicos e a pontuação do time no campeonato;
- Analisar a relação entre a pontuação do time no campeonato e a quantidade de pontos por partida do técnico mais longevo. 
