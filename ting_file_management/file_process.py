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
    if len(instance.dataFiles) == 0:
        return sys.stdout.write("Não há elementos\n")

    file_removed = instance.dequeue()["nome_do_arquivo"]

    return sys.stdout.write(f"Arquivo {file_removed} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
