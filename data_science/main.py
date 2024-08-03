import flet as ft

def main(page: ft.page):
    main_column = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.HIDDEN,
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.TextField(),
                        ft.Row(
                            controls=[
                                ft.Text('2.0+'),
                                ft.Slider(expand=True),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.Text('2.0+'),
                                ft.Slider(expand=True),
                            ],
                        ),
                        ft.Row(
                            controls=[
                                ft.Text('2.0+'),
                                ft.Slider(expand=True),
                            ],
                        ),
                    ],
                ),
                padding=25,
                bgcolor=ft.colors.GREY,
                border_radius=5
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Switch(),
                                ft.Slider(),
                            ]
                        ),
                        padding=25,
                        bgcolor=ft.colors.GREY,
                        border_radius=5,
                        expand=True
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Switch(),
                                ft.Slider(),
                            ]
                        ),
                        padding=25,
                        bgcolor=ft.colors.GREY,
                        border_radius=5,
                        expand=True
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Switch(),
                                ft.Slider(),
                            ]
                        ),
                        padding=25,
                        bgcolor=ft.colors.GREY,
                        border_radius=5,
                        expand=True
                    ),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Switch(),
                                ft.Slider(),
                            ]
                        ),
                        padding=25,
                        bgcolor=ft.colors.GREY,
                        border_radius=5,
                        expand=True
                    )
                ]
            )
        ],
    )
    page.add(main_column)

ft.app(target=main)