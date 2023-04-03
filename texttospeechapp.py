import PySimpleGUI as sg
import pyttsx3

speaker = pyttsx3.init()

layout =[
    [sg.Text('Enter Text Here: ', text_color='black'),
    sg.InputText(key= '-INPUT-'),
    sg.Text('Select a Voice: ', text_color= 'white',background_color='purple'),
    sg.Radio('Male',"RADIO1", default=True, key='-MALE-'),
    sg.Radio('Female',"RADIO1", key='-FEMALE-'),
     ],

     [sg.Text('VOLUME: '),
      sg.Slider(key='-VOLUME-', range=(0,20), size=(16,12), orientation='horizontal')],
      [sg.Button('Speak',button_color='yellow'), sg.Button('Exit')]
]

window = sg.Window('TEXT TO SPEECH APP', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Exit':
        break
    elif event == 'Speak':
        #Initialize the pyttsx3 engine.
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        volume = engine.getProperty('volume')
        set_volume = values['-VOLUME-']
       #Get the text from the Input box
        text = values['-INPUT-']

        voices = engine.getProperty('voices')

        #Set the voice type
        if values['-MALE-']:
            engine.setProperty('voice', voices[0].id)
        elif values['-FEMALE-']:
            engine.setProperty('voice', voices[1].id)

        engine.setProperty('volume', set_volume )
        engine.say(text)

        engine.runAndWait()


window.close()      