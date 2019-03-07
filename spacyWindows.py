Crear un ambiente virtual en conda 
#En mi caso fue en u ambiente ya con NLTK
conda install tqdm
conda install -c spacy spacy 

#Este paso debe hacer con permiso de administrador 
#Con cmder :
#1: Win + Alt + p y allí seleccionas run as administrator

#2 abres otro tipo de consola : Shift + Alt + 1 ...aqui NO conda activate NOmbre
python -m spacy download en
#HAY QUE volver a cargar el ambiente en la nueva terminal .. AQUÍ SIII
conda activate Nombre 
#walá!!! is done.

Fuentes:
https://www.youtube.com/watch?v=cgwDB1THUBY&list=PLJ39kWiJXSiz1LK8d_fyxb7FTn4mBYOsD
http://cmder.net/
