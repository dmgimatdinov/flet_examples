import flet as ft

def main(page: ft.Page):
    page.title = "няняня:4"

    def button_click(e):
        page.add(ft.Text("Кнопка нажата!"))

    button = ft.ElevatedButton("Нажми меня", on_click=button_click)
    page.add(button)

ft.app(target=main)