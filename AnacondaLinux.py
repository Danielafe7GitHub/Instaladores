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


#Instalar paquetes en un ambiente
#Ve que ese link sea para tu versión de python Ejem python 3.6
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.10.1-cp36-cp36m-linux_x86_64.whl

#Instaldo tensorflow hay que reinstalar jupyter notebook
pip install --ignore-installed ipython
pip install --ignore-installed jupyter


#En ese mismo ambiente instalamos NLTK
conda install -c anaconda nltk



