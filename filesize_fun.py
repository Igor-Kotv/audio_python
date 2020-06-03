def filesize_fun(sr, rms, T, nCh):

    try:
        sr=int(sr)
        rms=float(rms)
        T=float(T)
        nCh=int(nCh)
    except:
        print("Please, enter numeric values.")
        quit()
    import math
    koef=pow(10, rms/20)*math.sqrt(0.6)
    pa=20*math.log10(koef/(2*pow(10, -5)))
    Bdp=pa/6.02
    if Bdp<16:
        filesize=16*sr*T*nCh/8000000
        print("Bit depth = 16 bits,", "Filesize =", filesize, "MB")
    elif Bdp>16 and Bdp<24:
        filesize=24*sr*T*nCh/8000000
        print("Bit depth = 24 bits,", "Filesize =", filesize, "MB")
    elif Bdp>24 and Bdp<32:
        filesize=32*sr*T*nCh/8000000
        print("Bit depth = 32 bits,", "Filesize =", filesize, "MB")
    

