O projeto foi desenvolvido com Python3.6 no ambiente Linux.

Estamos utilizando o banco de dados MySQL para armazenar os dados, existe
variáveis de ambiente para acessar corretamente o banco MySQL, definimos também uma
variável `USE_MYSQL` para caso não seja setada utilizar o SqLite como opção.
Todos os detalhes dessas variáveis estão abaixo

Existe bastantes componentes que estão na `bill_of_materials.csv` mas não
existe no csv de componentes o `comp_boss.csv`, esses componentes foram
ignorados na hora da inserção

Variáveis de ambiente
---
- `USE_MYSQL` - Pode ser definida como 1 ou 0, no caso de 0 ou da não definição dessa variável será usado o sqlite como base de dados
- `MYSQL_USER` - Usuário com permissão de escrita no MySql
- `MYSQL_PWD` - Senha do usuário acima
- `MYSQL_HOST` - Ip ou dominio do MySQL
- `MYSQL_DB_NAME` - Nome do banco de dados

Instalando o projeto
---

    pip install -r requirements.txt


Criando todas as tabelas necessárias
---

    python3.6 -m cognitivo.scripts.create_database


Manipulando dados de comp_boss.csv
---

    python3.6 -m cognitivo.scripts.comp_boss


Manipulando dados de bill_of_materials.csv
---

    python3.6 -m cognitivo.scripts.bill_of_materials


Manipulando dados de price_quote.csv
---

    python3.6 -m cognitivo.scripts.price_quote


Modelo de dados final
---

![Diagram](diagram.png "Diagram")
