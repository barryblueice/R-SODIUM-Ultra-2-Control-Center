import flet as ft
from pathlib import Path

light_theme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary="#36454F",
        on_primary="#FFFFFF",
        secondary="#6C757D",
        on_secondary="#FFFFFF",
        surface="#F0F0F0",
        on_surface="#F0F0F0"
    ),
    use_material3=True
)

dark_theme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary="#FFFFFF",
        on_primary="#FFFFFF",
        secondary="#FFFFFF",
        on_secondary="#FFFFFF",
        surface="#282C30",
        on_surface="#282C30"
    ),
    use_material3=True
)

def main(page: ft.Page):
    page.title = "R-SODIUM Ultra 2 Control Center"
    page.window.width = 700
    page.window.height = 600
    page.window.resizable = False
    page.window.center()

    page.theme = light_theme
    page.dark_theme = dark_theme
    page.theme_mode = ft.ThemeMode.LIGHT

    is_light = True

    page_home = ft.Container(padding=20, content=ft.Column([ft.Text("Overview", size=24)]))
    page_enclosure_settings = ft.Container(padding=20, content=ft.Column([ft.Text("Enclosure Setting", size=24)]))
    page_controller = ft.Container(padding=20, content=ft.Column([ft.Text("Controller Setting", size=24)]))
    page_oled = ft.Container(padding=20, content=ft.Column([ft.Text("OLED Display Setting", size=24)]))
    page_software_settings = ft.Container(padding=20, content=ft.Column([ft.Text("Center Setting", size=24)]))
    page_about = ft.Container(padding=20, content=ft.Column([ft.Text("About", size=24)]))

    main_content = ft.Stack([page_home, page_enclosure_settings, page_controller, page_oled, page_software_settings, page_about])
    for i, c in enumerate(main_content.controls):
        c.visible = (i == 0)

    def on_nav_change(idx):
        for i, c in enumerate(main_content.controls):
            c.visible = (i == idx)
        page.update()

    theme_icon_switcher = ft.AnimatedSwitcher(
        duration=200,
        reverse_duration=200,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        content=ft.Icon(ft.Icons.WB_SUNNY_OUTLINED, size=30)
    )

    def toggle_theme(e):
        nonlocal is_light
        is_light = not is_light
        theme_icon_switcher.content = ft.Icon(
            ft.Icons.WB_SUNNY_OUTLINED if is_light else ft.Icons.MODE_NIGHT,
            size=30
        )

        page.theme_mode = ft.ThemeMode.LIGHT if is_light else ft.ThemeMode.DARK
        active_scheme = (page.theme if page.theme_mode == ft.ThemeMode.LIGHT else page.dark_theme).color_scheme
        sidebar.bgcolor = active_scheme.surface
        page.update()


    sidebar = ft.Container(
        width=80,
        padding=20,
        border_radius=10,
        bgcolor = page.theme.color_scheme.surface,
        content=ft.Column(
            [
                ft.IconButton(ft.Icons.HOME, icon_size=30, tooltip="Overview", on_click=lambda e: on_nav_change(0), padding=0),
                ft.IconButton(ft.Icons.API, icon_size=30, tooltip="Enclosure Mode Setting", on_click=lambda e: on_nav_change(1), padding=0),
                ft.IconButton(ft.Icons.APP_SHORTCUT, icon_size=30, tooltip="Controller Setting", on_click=lambda e: on_nav_change(2), padding=0),
                ft.IconButton(ft.Icons.SMART_DISPLAY, icon_size=30, tooltip="OLED Display Setting", on_click=lambda e: on_nav_change(3), padding=0),
                ft.IconButton(ft.Icons.SETTINGS, icon_size=30, tooltip="Center Setting", on_click=lambda e: on_nav_change(4), padding=0),
                ft.IconButton(ft.Icons.INFO, icon_size=30, tooltip="About", on_click=lambda e: on_nav_change(5), padding=0),

                ft.Column([], expand=True),

                ft.IconButton(
                    content=theme_icon_switcher,
                    tooltip="Theme Switch",
                    on_click=toggle_theme,
                    padding=0
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=20
        )
    )

    page.add(ft.Row([sidebar, main_content], expand=True))

ft.app(target=main)
