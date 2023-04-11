from flask.views import MethodView
from flask import request, render_template, redirect, flash
from src.db import mysql


class IndexControler(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produtos")
            data = cur.fetchall()
        return render_template('public/index.html', data = data)
    
    def post(self):
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        quantidade = request.form['quantidade']

        with mysql.cursor()as cur:
            try:
                cur.execute("INSERT INTO produtos VALUES(%s,%s,%s)", (codigo, descricao, quantidade))
                cur.connection.commit()
                flash('Produto cadastrado com sucesso!', 'success')
            except:
                flash('Erro no cadastro', 'error')
            return redirect('/')

class DeleteProdutoController(MethodView):
    def post(self, codigo):
         with mysql.cursor()as cur:
            try:
                cur.execute("DELETE FROM produtos WHERE codigo =%s", (codigo,))
                cur.connection.commit()
                flash('Produto deletado com sucesso!', 'success')
            except:
                flash('Erro na exclusão', 'error')
            return redirect('/')

class UpdateProdutoController(MethodView):
    def get(self, codigo):
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM produtos WHERE codigo =%s", (codigo,))
            product = cur.fetchone()
            return render_template('public/update.html', product = product)

    def post(self, codigo):
        produtocodigo = request.form['codigo']
        descricao = request.form['descricao']
        quantidade = request.form['quantidade']

        with mysql.cursor()as cur:
            try:
                cur.execute("UPDATE produtos SET codigo =%s, descricao =%s, quantidade =%s WHERE codigo =%s", (produtocodigo, descricao, quantidade, codigo))
                cur.connection.commit()
                flash('Produto atualizado com sucesso!', 'success')
            except:
                flash('Erro na atualização', 'error')
            return redirect("/")

class ConsultaController(MethodView):
    def consulta():
        return render_template('templates/consulta.html')
    