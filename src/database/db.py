import pymysql
from flask.views import MethodView
from flask import request, render_template, redirect, flash


mysql = pymysql.connect(
    host='localhost',
    port=3306, user='root',
    passwd='158942eE*',
    database='controle_de_estoque'
    )
    
class UpdateProduto(MethodView):
    def get(self, codigo):
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM produtos WHERE codigo =%s", (codigo,))
            product = cur.fetchone()
            return render_template('update.html', product = product)

    def post(self, codigo):
        produtocodigo = request.form['codigo']
        descricao = request.form['descricao']

        with mysql.cursor()as cur:
            try:
                cur.execute("UPDATE produtos SET codigo =%s, descricao =%s WHERE codigo =%s", (produtocodigo, descricao, codigo))
                cur.connection.commit()
                flash('Produto atualizado com sucesso!', 'success')
            except:
                flash('Erro na atualização', 'error')
            return redirect("/consulta")

class Relatorio(MethodView):
    def get(self):
        codigo = request.args['codigo']
        if codigo == '*':
            with mysql.cursor() as cur:
                cur.execute("SELECT * FROM produtos")
                data = cur.fetchall()
        else:
            with mysql.cursor() as cur:
                cur.execute("SELECT * FROM produtos WHERE codigo =%s", (codigo))
                data = cur.fetchall()
        return render_template('relatorio.html', data = data)

class Consulta(MethodView):
    def get(self):
        return render_template('consulta.html')
    
class Movimento(MethodView):
    def get(self):
        return render_template('movimento.html')
    
class Cadastro(MethodView):    
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produtos")
            data = cur.fetchall()
        return render_template('cadastro.html', data = data)
    
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
            return redirect("/cadastro")
        
class Index(MethodView):
    def get(self):
        return render_template('index.html')
    
class EntradaSaida(MethodView):
    def get(self):
        codigo = request.args['codigo']
        with mysql.cursor()as cur:
            cur.execute("SELECT * FROM produtos WHERE codigo =%s", (codigo))
            product = cur.fetchone()
            return render_template('entradasaida.html', product = product)

    def post(self):
        codigo = request.args['codigo']
        opcao = request.args['opcao']
        quant = request.form['quantidade']
        if opcao == 'entrada':
            with mysql.cursor()as cur:
                try:
                    cur.execute("UPDATE produtos SET quantidade = quantidade + %s WHERE codigo =%s", (quant, codigo))
                    cur.connection.commit()
                    flash('Produto atualizado com sucesso!', 'success')
                except:
                    flash('Erro na atualização', 'error')
                return redirect("/relatorio?codigo=10")
        else:
            with mysql.cursor()as cur:
                try:
                    cur.execute("UPDATE produtos SET quantidade = quantidade - %s WHERE codigo =%s", (quant, codigo))
                    cur.connection.commit()
                    flash('Produto atualizado com sucesso!', 'success')
                except:
                    flash('Erro na atualização', 'error')
                return redirect("/relatorio?codigo=['codigo']")