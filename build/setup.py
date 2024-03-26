from cx_Freeze import setup, Executable

setup(
    name = "Minesweeper",
    version = "0.1",
    description = "This is a game created with Tkinter",
    executables = [Executable("main.py")]
)