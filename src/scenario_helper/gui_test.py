import PySimpleGUI as sg

def get_string(c):
    return f"Feature: {c} is going onasdfasdkfjasdfkjasdkjf\nlakjdflajdfajsdjflakdalkclamkdlskmdcaskmdksmdd\n\tdxza\n\tsdf"

def add_new(index):
    return [[sg.Text('FileName'), sg.Column([[]], k='layout_principal', expand_x=True), sg.Text("Feature name"), sg.Button("Delete", key=f"delete-{index}")]]

def ddd():
    layout = [
        [sg.Text('FileName'), sg.Column([[]], k='layout_principal', expand_x=True), sg.Text("Feature name")],
        [sg.Input('dad', enable_events=True, key='-Filename-') ,sg.Column([[]], k='layout_principal', expand_x=True),  sg.Input('mom', enable_events=True, key='Feature name')],
        # [sg.Multiline(get_string(d), font=(20, 20), disabled=True, autoscroll=True, size=(30,10), key='output'), sg.Column([[sg.Button('', enable_events=True, key='instead')], [sg.Button('', enable_events=True, key='instead1')]])],
        [[sg.Column(add_new(0), key='-Column-')],],
        [sg.Button("Add new scenario", key="confirm")],
        []
    ]
    window = sg.Window("Creating scenario", layout, keep_on_top=True, resizable=True, finalize=True)
    while True:             # Event Loop
        index = 1
        event, values = window.read()
        print(event)
        print(values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'confirm':
            window.extend_layout(window["-Column-"], add_new(index))
            index += 1
        if "delete" in event:
            window[event].Widget.master.destroy()

    window.close()

if __name__ == '__main__':
    ddd()
