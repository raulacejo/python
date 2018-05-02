# source: http://www.pythondiario.com/2017/10/descargando-videos-de-youttube-con.html
# librería: https://pypi.python.org/pypi/pafy

# obtener el titulo de un vídeo.
# para ver la descripción el procedimiento es el mismo, pero usamos el método "description"

import pafy
url_video = "https://www.youtube.com/watch?v=JkK8g6FMEXE"
video = pafy.new(url_video)
print(video.title)

# otros metodos

import pafy
url_video = "https://www.youtube.com/watch?v=JkK8g6FMEXE"
video = pafy.new(url_video)
video.viewcount #Este método nos devuelve el numero de visitas del vídeo
video.category #Este método nos devuelve el tipo de categoría del vídeo
video.author #Este método nos devuelve el nombre del canal que subió el vídeo
video.duration #Este método nos devuelve la duración del vídeo
video.published #Este método nos devuelve la fecha en la que fue publicado el vídeo
video.likes #Este método nos devuelve el numero de likes del vídeo
vdieo.dislikes #Este método nos devuelve el numero de dislike del vídeo
video.keywords #Este método nos devuelve una lista con todas las etiquetas del vídeo
video.thumb #Este método nos devuelve una url la cual es la miniatura del vídeo
video.videoid #Este método nos devuelve el identificador del vídeo

# descargar vídeo
# el método getbest nos devuelve la mejor resolución del vídeo, argumento "preftype" con el formato del vídeo

import pafy
video = pafy.new("https://www.youtube.com/watch?v=JkK8g6FMEXE")
best = video.getbest(preftype="mp4")
best.download()

# descargar audio

import pafy
video = pafy.new("https://www.youtube.com/watch?v=JkK8g6FMEXE")
bestaudio = video.getbestaudio()
bestaudio.download()

