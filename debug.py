import pyglet

# completely useless, the built-in text renderer is pretty good of the bat
class Debug_text(pyglet.text.Label):
    def __init__(self, text='', font_name=None, font_size=None, bold=False, italic=False, stretch=False, color=..., x=0, y=0, width=None, height=None, anchor_x='left', anchor_y='baseline', align='left', multiline=False, dpi=None, batch=None, group=None):
        super().__init__(text, font_name, font_size, bold, italic, stretch, color, x, y, width, height, anchor_x, anchor_y, align, multiline, dpi, batch, group)

