# Algoritmos de Redução de Dimensionalidade - Trabalho de Conclusão de Curso (TCC)

Este repositório contém os algoritmos utilizados em meu Trabalho de Conclusão de Curso (TCC) para realizar testes de técnicas de redução de dimensionalidade. A pesquisa focou em técnicas de redução de dimensionalidade para avaliar a eficácia de diferentes abordagens. Baseando-se em um código previamente desenvolvido que utilizou PCA (Análise de Componentes Principais) e regressão logística para análise de evasão de estudantes ([disponível aqui](https://www.kaggle.com/code/eduardomarinho44/dropout-students-logistic-regression-and-pca)), realizamos uma série de testes utilizando a mesma base de dados.

## Objetivos

1. **Reproduzir e adaptar o código original**: 
   - Realizamos a reprodução dos experimentos do código original, seguido de adaptações para nossa análise específica.

2. **Desenvolver uma nova abordagem usando t-SNE**: 
   - Implementamos o algoritmo t-SNE para a redução de dimensionalidade, explorando diferentes parâmetros para avaliar sua eficácia em comparação com o PCA.

3. **Comparar os resultados**: 
   - Geramos e analisamos gráficos com parâmetros originais e ajustados para ambos os algoritmos, comparando os resultados obtidos.

## Algoritmos Utilizados

- **PCA (Análise de Componentes Principais)**: 
  - Utilizado para redução de dimensionalidade antes da aplicação da regressão logística.

- **t-SNE (Stochastic Neighbor Embedding)**: 
  - Implementado como uma alternativa ao PCA para a redução de dimensionalidade, com o objetivo de capturar relações mais complexas entre os dados.
