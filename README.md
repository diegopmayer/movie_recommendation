# Problema
Muito tempo gasto em busca e seleção de vídeos de machine learning

## Por que?
Não encontra-se vídeos adequados ao interesse
Não se sassiste vídeos até o final

## Propostas de Soluções
Recomendação de vídeos adequados ao desejado
No feed aparecer preferencialmente os vídeos desejo
Classificação e Ranking dos vídeos desejados

## Modelagem de Machine Learning
Sistema de Recomendação
Time Series (comparar com recomendação)

## Produção
Ponto de corte - Top N vídeos
Ranking - Ordenar os vídeos mais interessantes primeiros
WebPage - Para apresentar os dados de previsão (links) e Métricas obtidas com Flask ou Django
Docker para simular um ambiente real de servidor no Heroku

## Métricas para Validação
Primária - Dos top N vídeos, quantos são colocados com "Wath Later"
Secundária - Quanto tempo em busca e seleção de vídeos

## se as métricas acima não funcionarem, tentar essas na ordem
Quantidade de vídeos assistidos completos
Tempo e percentual assistindo do vídeo
Quantidade de vídeos curtidos
Mais visualizadas por mim

# Structure Project
First of all, we understood the problem and after we created the scope
and created many notebooks saved in notebooks folder following a "train of thought"
to test and validations hypotheses and answered asks, then 
all notes satisfied than we created the clean_deploy folder to
a structure like default project, with files, functions, etc.
Obs. I deleted the 99% of html files because it's so large, than left
just four files, when you run the notebooks it will save again your
machine.