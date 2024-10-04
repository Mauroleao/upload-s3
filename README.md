# Projeto de Upload de Imagens com integração Storage Local com S3 .

Este projeto é uma aplicação Django para upload de imagens, utilizando o Amazon S3 para armazenamento.

## Pré-requisitos

- Python 3.8+
- Virtualenv
- Git

## Passos para rodar o projeto

### 1. Clonar o repositório

```sh
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```
2. Criar e ativar o ambiente virtual
No Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
No Unix/MacOS:
```sh
python3 -m venv venv
source venv/bin/activate
```

3. Instalar as dependências
```sh
pip install -r requirements.txt
```

4. Configurar as variáveis de ambiente
```sh
AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=SEU_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME=SEU_BUCKET_NAME
AWS_S3_REGION_NAME=REGIAO
 ```

5. Aplicar as migrações do banco de dados
```sh
 python [manage.py]
```

 6. Rodar o servidor de desenvolvimento
python manage.py


7. Acessar a aplicação
   
Abra o navegador e acesse http://127.0.0.1:8000/
```sh
.
├── home/
│   ├── [__init__.py]
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── [__init__.py]
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_myfile_arquivo.py
│   ├── models.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── status.html
│   ├── tests.py
│   ├── views.py
├── [manage.py]
├── media/
│   ├── img/
├── [requirements.txt]
├── upload_imagens/
│   ├── [__init__.py]
│   ├── asgi.py
│   ├── [settings.py]
│   ├── urls.py
│   ├── wsgi.py
├── venv/
│   ├── Include/
│   ├── Lib/
│   │   ├── site-packages/
│   ├── Scripts/
│   ├── pyvenv.cfg

```

Configurações Adicionais
Para configurar o armazenamento no Amazon S3, edite o arquivo settings.py conforme necessário.

Contribuição
Sinta-se à vontade para contribuir com o projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

Licença
Este projeto está licenciado sob a licença MIT.



Certifique-se de substituir `<URL_DO_REPOSITORIO>`, `<NOME_DO_REPOSITORIO>`, `SEU_ACCESS_KEY_ID`, `SEU_SECRET_ACCESS_KEY`, `SEU_BUCKET_NAME` e `REGIAO` com as informações apropriadas.



 
