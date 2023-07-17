#Import PySimpleGUI
import PySimpleGUI as sg
 
#Draw the button
layout = [[sg.Button('Hello, New Stack', size=(20,4))]]

#Draw the button
layout = [[sg.Button('a', size=(20,4))]]
 
#Draw the window
window = sg.Window('GUI SAMPLE', layout, size=(480,320))
 
#Define what happens when the button is clicked
event, values = window.read()