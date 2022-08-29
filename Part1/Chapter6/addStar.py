import pyperclip as clip

originText = clip.paste()

string = ''

for line in originText.split('\n'):
    string += "* " + line + '\n'

resultText = clip.copy(string)
