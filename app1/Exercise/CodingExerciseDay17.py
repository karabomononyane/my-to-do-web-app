import PySimpleGUI as sg
from app1.bonus import converters14

label1 = sg.Text("Enter feet:")
feet_text = sg.InputText(tooltip="Type feet", key="feet")
label2 = sg.Text("Enter inches:")
inches_text = sg.InputText(tooltip="Type inches", key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Convertor", layout=[
    [label1, feet_text],
    [label2, inches_text],
    [convert_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Convert':
            feet = float(values["feet"])
            inches = float(values["inches"])
            print(feet, inches)
            results = converters14.convert(feet, inches)
            output_label.update(results)
        case sg.WIN_CLOSED:
            break

window.close()
