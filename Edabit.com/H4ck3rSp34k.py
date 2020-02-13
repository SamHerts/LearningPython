"""
    Create a function that takes a string as an argument and returns 
    a coded (h4ck3r 5p34k) version of the string.
    ---Replace all 'a's with 4, 'e's with 3, 'i's with 1, 'o's with 0, and 's's with 5.
"""

def hacker_speak(txt):
    choices = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5'}
    a=0
    newlst = list(txt)
    while  a < len(newlst):
        newlst[a] = choices.get(newlst[a], newlst[a])
        a+=1
    return "".join(newlst)

print(hacker_speak("Hello World"))
