import flet as ft

def main(page: ft.Page):
    page.title = "App con botón"

    mensaje = ft.Text("hellooooooo worlddddd !", size=25, color="blue")
    boton1 = ft.ElevatedButton("no tocar")

    def cambiar_texto(e):
        if mensaje.value == "hellooooooo worlddddd !":
            mensaje.value = "¡que onda noob :V!"
            mensaje.color = "red"
            boton1.text = "te dije que no toques"   
        else:
            mensaje.value = "hellooooooo worlddddd !"
            mensaje.color = "blue"
            boton1.text = "no tocar"       
        page.update()

    boton1.on_click = cambiar_texto

    page.add(
        ft.Row(
            [
                ft.Column(
                    [mensaje, boton1],
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
