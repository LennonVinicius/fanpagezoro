# Atividade 3 - Zoro Fan Page com Flask

Projeto simples da Atividade 3 usando Flask, templates HTML, Bootstrap e arquivos estáticos.

## Rodar no computador

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000`.

## Rodar na EC2

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git -y
git clone LINK_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
nohup python app.py > app.log 2>&1 &
```

No Security Group da instância, libere TCP na porta 5000.

Depois acesse `http://IP_PUBLICO:5000`.
