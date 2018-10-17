# Teste de Visualização de Dados

## 1. Introdução
O problema proposto foi bem simples e na minha concepção pensei os seguintes pontos:

1. Os dados de percentuais deveriam ser exibidos em pie chart ou uma variante do box plot, para melhor poder comparar as parcelas da porcentagem.
2. Os dados de médiam deveriam ser exibidos "crus", sem a necessidade de um gráfico em si.
3. Os tops 10 em formato de barra horizontal, para poder aproveitar melhor a legenda, que no caso, seria o nome do app.
4. Um filtro customizado e que agregasse os 5 id's que foram passados no documento.
5. Dei a preferência ao metabase por rodar 'out of box', e por ter uma prototipagem rápida.

## 2. Execução do Teste
1. Baixar o metadata para a pasta do projeto.

2. Executar o metadata:
```java
java -jar metadata
```
Se tudo ocorrer normalmente, o dashboard poderá ser acessado no endereço `https:\\localhost:3000`. Fiz o teste e não foi necessário digitar usuário e senha, pois a sessão está salva no metabase.db, mas se for necessário, favor entrar em contato.

## 3. Considerações finais
Foi minha primeira experiência com o Metabase, porém o dashboard ficou simples demais para o que eu tinha em mente. Fiz um protótipo no `Apache Superset`, mas decidi não disponibilizar. Acredito que esse problema não aconteceria se eu estivesse utilizando ferramentas mais conceituadas como Tableau ou Power BI.
Gostaria que o filtro fosse mais intuitivo bastando apenas selecionar um combo box, mas não consegui implementar, logo o usuário deve digitar ou colar os id's que pretende filtrar, o que é pessimo do ponto de vista de UX.

![screenshot](https://github.com/jfalves/cognitivo.ai/blob/master/data_visualization/doc/screenshot.png)
