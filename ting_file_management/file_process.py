from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines_response = txt_importer(path_file)

    for row in instance.dataFiles:
        if path_file in row["nome_do_arquivo"]:
            return ""

    instance.enqueue(
        {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines_response),
            "linhas_do_arquivo": lines_response,
        }
    )
    sys.stdout.write(
        str(
            {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(lines_response),
                "linhas_do_arquivo": lines_response,
            }
        )
    )


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
