
Para criar o ambiente virtual: execute python3 -m venv venv na raíz do projeto.
Para acessar o ambiente virtual, executar \venv\Scripts\activate na raíz do projeto.
Para baixar bibliotecas necessárias, encaminhar para a pasta src (cd /src) e executar pip install -r requirements.txt na raíz do projeto: 
Depois, encaminhar para a pasta src (cd /src) e executar python3 -m flask --app app  run --host 0.0.0.0 --port 8000

Na pasta src existe a pasta templates (com os arquivos html), uma pasta static (com o arquivo css), o app.py e o banco de dados em json (database.json).
