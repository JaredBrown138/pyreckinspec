from dearpygui import core, simple

with simple.window("Example Window"):
    core.add_text("Hello world!")

core.start_dearpygui()