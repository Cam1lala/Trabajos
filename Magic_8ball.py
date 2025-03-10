import flet as ft
import random

def main(page: ft.Page):

    page.title = "Magic 8-Ball"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_question = ft.TextField(label="Ask a question", autofocus=True)

    lbl_response = ft.Text("", size=40, color=ft.Colors.WHITE)

    responses = [
        "Yes",
        "No",
        "NO",
        "Maybe",
        "Ask again later",
        "Definitely",
        "Certainly not",
        "Maybe not...",
    ]
    
    def ask_8_ball(e):
        response = random.choice(responses)

        lbl_response.value = response

        if response in ["Yes", "Definitely", "Outlook good"]:
            lbl_response.color = ft.Colors.PURPLE
        elif response in ["No", "Don't count on it" "Certainly not"]:
            lbl_response.color = ft.Colors.BLUE
        else:
            lbl_response.color = ft.Colors.ORANGE
            
        page.update()

    btn_ask = ft.ElevatedButton("Ask the 8-Ball", on_click=ask_8_ball)

    page.add(
        ft.Column(
            [
                txt_question,
                btn_ask,
                lbl_response,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=35,
        )
    )

ft.app(main)