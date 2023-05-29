import os
import shutil


HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Área de Trabalho')
NOVA_PASTA = os.path.join(DESKTOP, 'Nova pasta')
OUTRA_PASTA = os.path.join(NOVA_PASTA, 'Outra pasta')

# os.makedirs(OUTRA_PASTA)
print(DESKTOP)
