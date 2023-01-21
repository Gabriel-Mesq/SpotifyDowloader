import os

k = l = 0

path = os.chdir("C:\programs\database\Python\spotify-to-mp3-python-master\• outer space •")

for file in os.listdir(path):

    try:

        new = file.rsplit(' ', 1)[0]

        if new.find('-') != -1:
            parts = new.split("-")
            new = (parts[1] + ' - ' + parts[0])[1:]

        if new.find('(Official Video)') != -1:
            new = new.replace('(Official Video)', '')

        elif new.find('(Official Music Video)') != -1:
            new = new.replace('(Official Music Video)', '')

        elif new.find('(Official Audio)') != -1:
            new = new.replace('(Official Audio)', '')   

        elif new.find('(Lyric Video)') != -1:
            new = new.replace('(Lyric Video)', '')   

        elif new.find('(Official Lyric Video)') != -1:
            new = new.replace('(Official Lyric Video)', '')   

        elif new.find('[Official Video]') != -1:
            new = new.replace('[Official Video]', '')   

        elif new.find('(Lyrics)') != -1:
            new = new.replace('(Lyrics)', '')  

        new = new.strip() + ".mp3"        
        os.rename(file, new)

    except:
        print("Erro em:", file, "\n")
        k = k  + 1

print("erros: ", k)
