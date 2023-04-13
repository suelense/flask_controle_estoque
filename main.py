from flask import Flask, render_template
from src.database.db import *

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'development'
)

routes = {
    "cadastro_route":"/cadastro", "cadastro_controller": Cadastro.as_view("cadastro"),
    "consulta_route":"/consulta", "consulta_controller": Consulta.as_view("consulta"),
    "delete_route": "/delete/product/<int:codigo>", "delete_controller": DeleteProduto.as_view("delete"),
    "entradasaida_route":"/entradasaida", "entradasaida_controller": EntradaSaida.as_view("entradasaida"),

    "index_route":"/", "index_controller": Index.as_view("index"),
    "relatorio_route":"/relatorio", "relatorio_controller": Relatorio.as_view("relatorio"),
    "update_route": "/update/product/<int:codigo>", "update_controller": UpdateProduto.as_view("update"),
}

app.add_url_rule(routes["index_route"], view_func=routes["index_controller"])
app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])
app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])
app.add_url_rule(routes["consulta_route"], view_func=routes["consulta_controller"])
app.add_url_rule(routes["relatorio_route"], view_func=routes["relatorio_controller"])
app.add_url_rule(routes["cadastro_route"], view_func=routes["cadastro_controller"])


HOST = 'localhost'
PORT = 8080
DEBUG = True
if (__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)
