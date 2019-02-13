class Radiobutton:
    def __init__(self, radioid, name, value, text, checked=''):
        self.radioid = radioid
        self.name = name
        self.value = value
        self.text = text
        self.checked = checked

lst = []
for i in range(1,6):
    radioid = 'radiobutton' + str(i)
    name = 'radioname'
    value = 'radiovalue' + str(i)
    text = str(i) + '번째 option'
    checked = ''
    if i == 4:
        checked = 'checked'
    lst.append(Radiobutton(radioid, name, value, text, checked))

print(lst)