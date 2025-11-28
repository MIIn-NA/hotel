class Dashboard:
    def __init__(self, title: str, theme: str, version: str):
        self.title = title
        self.theme = theme
        self.version = version

    def switch_theme(self, theme: str) -> None:
        self.theme = theme.strip().lower()

    def info(self) -> str:
        return f"{self.title} [{self.theme}] v{self.version}"
