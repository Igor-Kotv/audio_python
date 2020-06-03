from filesize_fun import filesize_fun 
sr=input("Enter Sample Rate (Hz): ")
rms=input("Enter RMS (dBFS): ")
T=input("Enter Duration Time (seconds): ")
nCh=input("Enter N - channels (N - mono audio files) (1-5): ")
filesize_fun(sr, rms, T, nCh)


