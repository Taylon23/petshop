🐾 PetAdote - Plataforma de Adoção de Animais
PetAdote é um site desenvolvido para facilitar a adoção responsável de animais, com foco em gatos e cachorros, mas também permitindo o anúncio de outros animais. A plataforma conecta pessoas que desejam doar pets a futuros tutores, promovendo o amor e o cuidado pelos animais.

🚀 Funcionalidades
Anúncio de Animais para Adoção

Usuários podem cadastrar animais disponíveis para adoção, incluindo fotos, descrições e informações importantes.
Busca de Pets

Sistema de busca segmentado por tipos de animais (Cachorros, Gatos, Outros).
Contato Direto

Usuários interessados podem entrar em contato diretamente com os doadores para combinar a adoção.
Animais em Destaque

Exibição de anúncios em destaque na página inicial para maior visibilidade.
🛠️ Tecnologias Utilizadas
Backend: **Django**
Frontend: **HTML, CSS e JavaScript**
Banco de Dados: **SQLite** (padrão do Django)
Gerenciamento de Dependências: **requirements.txt**


Passo a Passo
Clone o Repositório

bash
git clone https://github.com/seu-usuario/petadote.git
cd petadote
Crie e Ative o Ambiente Virtual

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as Dependências

bash
pip install -r requirements.txt
Execute as Migrações do Banco de Dados

bash
python manage.py makemigrations
python manage.py migrate
Crie um Superusuário (opcional para gerenciar o site)

bash
python manage.py createsuperuser
Execute o Servidor Local

bash
python manage.py runserver
