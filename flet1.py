import flet as ft

def main(page: ft.Page):
    page.title = "няняня:2"
    page.add(ft.Text("Привет, мир!", size=24, weight=ft.FontWeight.BOLD))

ft.app(target=main)
