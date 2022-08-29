import pyperclip as clip
import re

phoneNumRegex = re.compile(r'1\d{10}')
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

clipText = str(clip.paste())
# print(clipText)
matches = []
for groups in phoneNumRegex.findall(clipText):
    matches.append(groups)

for groups in emailRegex.findall(clipText):
    matches.append(groups[0])


clip.copy("\n".join(matches))
# print(matches)



