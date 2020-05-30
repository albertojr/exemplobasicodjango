# exemplobasicodjango
projeto básico em Django 3, ensinando a somar 2 valores e exibir em outro field.

Como instalar o projeto no linux?
 1º - Criar o ambiente virtual com o seguinte comando:
    virtualenv nomemáquinavirtual
    
 2º Utilizar o PIP, para instalar o requeriments:
    pip install -r requirements
    
3º Realizar o migrations para criar o admin e models da app:
    python manage.py migrate

4º Criar o seu usuário admin, com o comando:
    python manage.py creatsuperuser

5º Em seguida, basta colocar o nome do usuário, e-mail e password.

6º Por fim, basta rodar o projeto:
  python manage.py runserver
