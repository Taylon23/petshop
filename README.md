## 🐾 PetShop
PetShop é um sistema que permite gerenciar doações de animais, onde os usuários podem publicar anúncios para adoção.

## 🚀 Funcionalidades

- Cadastro de anúncios de animais para adoção
- Filtros de busca para facilitar a localização de animais
- Interface amigável e responsiva

## 🛠️ Tecnologias Utilizadas
- Framework: Django
- Frontend: HTML, CSS, Bootstrap
- Banco de Dados: SQLite (pode ser configurado - para PostgreSQL ou MySQL)

## Instalação

Clone o repositorio

```bash
git clone https://github.com/Taylon23/petshop.git
cd petshop

```
Crie e ative um ambiente virtual:

```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  

```
Instale as dependências:

```bash
pip install -r requirements.txt
```
Aplique as migrações:
```bash
python manage.py migrate
```
Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver

```
Acesse o sistema no navegador: http://localhost:8000
