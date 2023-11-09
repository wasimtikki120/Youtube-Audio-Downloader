import moviepy.editor as mp

clip = mp.AudioFileClip(r"C:\Users\Awaise\Desktop\wasim\Youtube Audio Downloader\Ruaan Song Lyrical Tiger 3 Salman Khan,Katrina Kaif Pritam Arijit Singh Irshad Kamil.webm").subclip()
clip.write_audiofile("C:\Users\Awaise\Desktop\wasim\Youtube Audio Downloader")
clip.close()