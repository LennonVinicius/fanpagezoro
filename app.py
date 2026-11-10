import os

import pymysql
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

load_dotenv()
app = Flask(__name__)


def conectar_banco():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT', '3306')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5,
    )


@app.route('/')
def inicio():
    return render_template('index.html', titulo='Início')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Sobre')


@app.route('/espadas')
def espadas():
    return render_template('espadas.html', titulo='Espadas')


@app.route('/galeria')
def galeria():
    return render_template('galeria.html', titulo='Galeria')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        personagem = request.form.get('personagem_favorito', '').strip()

        if not nome or not email or not personagem:
            return render_template(
                'cadastro.html',
                titulo='Cadastro',
                erro='Preencha todos os campos.',
                nome=nome,
                email=email,
                personagem=personagem,
            ), 400

        conexao = conectar_banco()
        try:
            with conexao.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO fas (nome, email, personagem_favorito) VALUES (%s, %s, %s)',
                    (nome, email, personagem),
                )
            conexao.commit()
        finally:
            conexao.close()

        return redirect(url_for('listar', cadastrado=1))

    return render_template('cadastro.html', titulo='Cadastro')


@app.route('/listar')
def listar():
    conexao = conectar_banco()
    try:
        with conexao.cursor() as cursor:
            cursor.execute('SELECT id, nome, email, personagem_favorito FROM fas ORDER BY id DESC')
            fas = cursor.fetchall()
    finally:
        conexao.close()

    return render_template('listar.html', titulo='Fãs cadastrados', fas=fas)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
