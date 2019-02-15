class Radiobutton:
    def __init__(self, radioid, name, value, text, checked=''):
        self.radioid = radioid
        self.name = name
        self.value = value
        self.text = text
        self.checked = checked

#{%macro select(value, text, selected)%}
class Selectbutton:
    def __init__(self, value, text, selected):
        self.value = value
        self.text = text
        self.selected = selected
        
class Rec:
    def __init__(self, title, url, children=[]):
        self.title = title
        self.url = url
        self.children = children