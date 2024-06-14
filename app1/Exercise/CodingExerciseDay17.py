import PySimpleGUI as sg
from app1.bonus import converters14

sg.theme("Black")

label1 = sg.Text("Enter feet:")
feet_text = sg.InputText(tooltip="Type feet", key="feet")
label2 = sg.Text("Enter inches:")
inches_text = sg.InputText(tooltip="Type inches", key="inches")
exit_button = sg.Button("Exit")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Convertor", layout=[
    [label1, feet_text],
    [label2, inches_text],
    [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Convert':
           try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                print(feet, inches)
                results = converters14.convert(feet, inches)
                output_label.update(results)
           except ValueError:
               sg.popup("Please provide two numbers")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
