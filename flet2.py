import flet as ft

def main(page: ft.Page):
    page.title = "няняня:2"
    name_field = ft.TextField(label="Введите ваше имя")
    page.add(name_field)

ft.app(target=main)