# 🎬 Moviery Project

O **Moviery Project** é uma aplicação desenvolvida para o gerenciamento
de catálogos de filmes, focada em fornecer uma estrutura robusta para a
organização de dados cinematográficos. O projeto utiliza tecnologias
modernas de desenvolvimento web para garantir uma experiência fluida
tanto no consumo da API quanto na persistência dos dados.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

Este projeto foi construído utilizando ferramentas consolidadas do
ecossistema Python:

-   **Linguagem:** Python\
-   **Framework Web:** Django\
-   **API Framework:** Django REST Framework (DRF)\
-   **Banco de Dados:** SQLite (padrão de desenvolvimento)\
-   **Arquitetura:** RESTful API

------------------------------------------------------------------------

## 🛠️ Funcionalidades

O sistema foi implementado seguindo o padrão **CRUD (Create, Read,
Update, Delete)** para garantir o gerenciamento completo da biblioteca
de filmes:

-   **Gerenciamento de Filmes:** Cadastro, listagem, atualização e
    exclusão de títulos.\
-   **Serialização de Dados:** Utilização de Serializers do DRF para
    garantir que a comunicação via JSON seja eficiente e tipada.\
-   **Rotas HTTP:** Endpoints estruturados para facilitar a integração
    com diferentes front-ends.\
-   **Persistência:** Garantia de integridade dos dados através de
    migrações estruturadas no banco de dados.

------------------------------------------------------------------------

## ⚙️ Como Executar o Projeto

Para rodar este projeto localmente, siga os passos abaixo:

### 1️⃣ Clone o repositório

``` bash
git clone https://github.com/ElissonDouglas/moviery_project.git
```

### 2️⃣ Crie e ative um ambiente virtual

``` bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3️⃣ Instale as dependências

``` bash
pip install -r requirements.txt
```

### 4️⃣ Execute as migrações do banco de dados

``` bash
python manage.py migrate
```

### 5️⃣ Inicie o servidor de desenvolvimento

``` bash
python manage.py runserver
```

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

O projeto segue os padrões de organização do Django, focando na
separação de responsabilidades e na manutenibilidade do código:

-   `models.py`: Definição das tabelas e relacionamentos.\
-   `serializers.py`: Lógica de transformação de dados.\
-   `views.py`: Processamento das requisições e regras de negócio.\
-   `urls.py`: Mapeamento das rotas da API.
