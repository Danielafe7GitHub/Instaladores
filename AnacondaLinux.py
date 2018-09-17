Instalar Conda
Descarla el instalador de : https://www.anaconda.com/download/#linux
la version 3.6

Seguir los pasos de este pideo... justa hasta que dice:
Thanks for installing anaconda, el resto no es necesario

https://www.youtube.com/watch?v=ENlX90p1hDk


Luego creas un ambiente Virtual:
conda create -n iaEnv python=3.6
conda env list
source activate iaEnv
jupyter notebook // Alli puedes crear una carpeta q aloje todos tus notebooks
source desactivate // Para desactivar el ambiente

Si ya creaste el ambiente, solo ábrelo:

conda env list
source activate iaEnv
jupyter notebook // Alli puedes crear una carpeta q aloje todos tus notebooks
source desactivate // Para desactivar el ambiente


#Instalar paquetes en un ambienyr
source activate iaEnv
conda install -c conda-forge tensorflow 

