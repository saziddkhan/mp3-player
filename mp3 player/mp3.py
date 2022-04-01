import PySimpleGUI as sg
import vlc

controls = [sg.Button("play"), sg.Button("pause"), sg.Button("stop")]
layout = [ [sg.FileBrowse(key="-MP3-", enable_events=True)], controls]
player = None

window = sg.Window("MP3 Player", layout)

while True: 
    event, values = window.read()  
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    if event == "-MP3-":
      
        player = vlc.MediaPlayer(values['-MP3-'])
     
    if event == "play" and  player is not None:
        player.play()
    if event == "pause" and  player is not None:
        player.pause()
    if event == "stop" and  player is not None:
        player.stop()

        window.close()
        


