import os

#VERIFICA O TIPO DE MIDIA
def verifica_midia(fdmidia): 
    file = fdmidia+".jpeg"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".jpg"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".gif"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".png"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".bmp"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".tif"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".psd"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".exif"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".raw"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".avi"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".wmv"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".mov"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".mkv"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".mp4"
    if os.path.exists(file):
        return(file)
    file = fdmidia+".mp4"
    if os.path.exists(file):
        return(file)
    return("sem")