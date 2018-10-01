# Teste de Engenharia de Dados

## 1. Introdução
A partir do briefing e dos dados nos 3 arquivos foi possível inferir algumas informações:

1. Um fornecedor pode fazer vários orçamentos para a mesma composição de tubos.
2. Uma montagem de tubos é composto por vários componentes.
3. Existe uma relação indireta entre tipos de conexões e tipos de componentes.
4. O código 9999 pode ser considerado como nulo
5. Existem 2 relações many-to-many, entre Supplier e TubeAssembly, Entre TubeAssembly e Component.

A partir disso foi montado o seguinte modelo conceitual:

![alt text](https://raw.githubusercontent.com/jfalves/cognitivo.ai/master/data_engineering/doc/Modelo_Conceitual.png)


## 2. Execução do Teste
O teste tem como requisito o python 3.6 além de outras bibliotecas que serão installadas através do pip:
```python
virtualenv --python=/path_2_python36 venv
source ./venv/bin/activate
 pip install -r requirements.txt
```
Após as depêndencias terem sido instaladas, será necessário rodar o script:
```python
python etl.py
```
Esse procedimento ira gerar a estrutura do banco junto com a carga das tabelas em sqlite. O código é abstrato
o suficiente para ser executado em outros bancos, bastando para isso trocar o dialeto no arquivo `orm\__init__.py`

## 3. Considerações finais
Eu acredito que teria feito um trabalho melhor se tivesse utilizado ferramenta de integração, do qual sou bem mais experiente mas decidi arriscar na sugestão de construir o código em python, o que foi bem divertido por um lado e frustrante por outro.

Seguem abaixo algumas das minhas decisões em relação a arquitetura do etl.
1. criei os modelos de dados no SQLAlchemy para poder abstrair a estrutura do banco de dados, o que a biblioteca faz muito bem.
2. Para abstrair os dados utilizei a biblioteca pandas.
3. Acabei por utilizar o pandas para fazer a persistência, pois ia aumentar um pouco a complexidade.
4. Gostaria de ter colocado um gerenciador de workflow, como airflow, luigi, etc, porém não foi minha prioridade.

Gostaria de ter utlizado os modelos do SQLAlchemy de forma a garantir a inserção de registros automaticamente (relação 1-to-many). Gastei muito tempo nisso e acabeideixando o pandas fazer isso, o que explica a falta de uma função que verifique se o registro já está na base ou não (upsert).
Em relação a criação do modelo conceitual, eu deveria ter especializado a criação da tabela PriceQuote, como podem perceber, tive que colocar várias pks por causa do multinível do bracket_pricing. Isso não seria necessário se eu tivesse especializado PriceQuote separando as informações em duas tabelas. 
