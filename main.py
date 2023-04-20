import PySimpleGUI as sg
import zip_extractor

sg.theme("Black")

label1 = sg.Text("Select file to extract: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="zip_file")
label2 = sg.Text("Select destination Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="blue")

window = sg.Window("File Extractor", layout=[[label1, input1, choose_button1],
                                             [label2, input2, choose_button2],
                                             [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Extract":
            if not values["zip_file"]:
                sg.popup("Please select file zip first.", font=("Helvetica", 11))
            elif not values["folder"]:
                sg.popup("Please select folder first.", font=("Helvetica", 11))
            else:
                archivepath = values['zip_file']
                dest_dir = values['folder']
                zip_extractor.extract_archive(archivepath, dest_dir)
                window['output'].update(value="Extraction Completed!")
        case sg.WIN_CLOSED:
            break

window.close()
