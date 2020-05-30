# Exemplo básico com Django Admin:

## projeto básico em Django 3, ensinando a somar 2 valores no Admin e exibir em outro field.

#### Como instalar o projeto no linux ubuntu?
* Criar o ambiente virtual com o seguinte comando:

    virtualenv nomemáquinavirtual
    
* Utilizar o PIP, para instalar o requeriments:

    pip install -r requirements
    
* Realizar o migrations para criar o admin e models da app:

    python manage.py migrate

* Criar o seu usuário admin, com o comando:

    python manage.py createsuperuser

* Em seguida, basta colocar o nome do usuário, e-mail e password.

* Por fim, basta rodar o projeto:

  python manage.py runserver
