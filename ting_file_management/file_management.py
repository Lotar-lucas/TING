# import sys


# def txt_importer(path_file):
#     if path_file.endswith(".txt"):
#         return sys.stderr.write("Formato inválido\n")

#

import os
import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    extension = os.path.splitext(path_file)
    if extension[1] != ".txt":
        return sys.stderr.write("Formato inválido\n")

    # Fui auxiliado por Felippe Correa
    try:
        data = open(path_file)
        with data as data_content:
            return data_content.read().splitlines()
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")