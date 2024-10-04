# Projeto de Upload de Imagens

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

python -m venv venv
venv\Scripts\activate

3. Instalar as dependências

pip install -r [requirements.txt]

4. Configurar as variáveis de ambiente

AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=SEU_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME=SEU_BUCKET_NAME
AWS_S3_REGION_NAME=REGIAO

5. Aplicar as migrações do banco de dados

 python [manage.py]

 6. Rodar o servidor de desenvolvimento
python [manage.py]


7. Acessar a aplicação
Abra o navegador e acesse http://127.0.0.1:8000/

.
├── home/
│   ├── [__init__.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cmauro%5C%5CDesktop%5C%5Cupload%5C%5Cvenv%5C%5CLib%5C%5Csite-packages%5C%5Cpip%5C%5C_internal%5C%5Creq%5C%5C__init__.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fvenv%2FLib%2Fsite-packages%2Fpip%2F_internal%2Freq%2F__init__.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fvenv%2FLib%2Fsite-packages%2Fpip%2F_internal%2Freq%2F__init__.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── [__init__.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cmauro%5C%5CDesktop%5C%5Cupload%5C%5Cvenv%5C%5CLib%5C%5Csite-packages%5C%5Cpip%5C%5C_internal%5C%5Creq%5C%5C__init__.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fvenv%2FLib%2Fsite-packages%2Fpip%2F_internal%2Freq%2F__init__.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fvenv%2FLib%2Fsite-packages%2Fpip%2F_internal%2Freq%2F__init__.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_myfile_arquivo.py
│   ├── models.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── status.html
│   ├── tests.py
│   ├── views.py
├── [manage.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cmauro%5C%5CDesktop%5C%5Cupload%5C%5Cmanage.py%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fmanage.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
├── media/
│   ├── img/
├── [requirements.txt](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cmauro%5C%5CDesktop%5C%5Cupload%5C%5Crequirements.txt%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Frequirements.txt%22%2C%22scheme%22%3A%22file%22%7D%7D)
├── upload_imagens/
│   ├── [__init__.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cmauro%5C%5CDesktop%5C%5Cupload%5C%5Cvenv%5C%5CLib%5C%5Csite-packages%5C%5Cpip%5C%5C_internal%5C%5Creq%5C%5C__init__.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fvenv%2FLib%2Fsite-packages%2Fpip%2F_internal%2Freq%2F__init__.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fvenv%2FLib%2Fsite-packages%2Fpip%2F_internal%2Freq%2F__init__.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
│   ├── asgi.py
│   ├── [settings.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cmauro%5C%5CDesktop%5C%5Cupload%5C%5Cupload_imagens%5C%5Csettings.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fupload_imagens%2Fsettings.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmauro%2FDesktop%2Fupload%2Fupload_imagens%2Fsettings.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
│   ├── urls.py
│   ├── wsgi.py
├── venv/
│   ├── Include/
│   ├── Lib/
│   │   ├── site-packages/
│   ├── Scripts/
│   ├── pyvenv.cfg

Configurações Adicionais
Para configurar o armazenamento no Amazon S3, edite o arquivo settings.py conforme necessário.

Contribuição
Sinta-se à vontade para contribuir com o projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

Licença
Este projeto está licenciado sob a licença MIT.



Certifique-se de substituir `<URL_DO_REPOSITORIO>`, `<NOME_DO_REPOSITORIO>`, `SEU_ACCESS_KEY_ID`, `SEU_SECRET_ACCESS_KEY`, `SEU_BUCKET_NAME` e `REGIAO` com as informações apropriadas.



 
