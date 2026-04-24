import flet as ft

def main(page: ft.Page):
    page.title = "App con botón"

    mensaje = ft.Text("hellooooooo worlddddd !", size=25, color="blue")

    def cambiar_texto(e):
        mensaje.value = "¡que onda noob :V!"
        mensaje.color = "red"
        page.update()

    boton1 = ft.ElevatedButton("no tocar", on_click=cambiar_texto)

    # ✅ Centrado absoluto en pantalla
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        mensaje,
                        boton1
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)
