from src.controlers.controle import *
from src.controlers.errors import NotFoundController


routes = {
    "index_route": "/", "index_controler": IndexControler.as_view("index"),
    "not_found_route": 404, "not_found_controller": NotFoundController.as_view("Não econtrado"),
    "delete_route": "/delete/product/<int:codigo>", "delete_controller": DeleteProdutoController.as_view("delete"),
    "update_route": "/update/product/<int:codigo>", "update_controller": UpdateProdutoController.as_view("update"),
    "consulta_route":"/consulta", "consulta_controller": ConsultaController.as_view("consulta")
}
