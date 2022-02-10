# fui auxiliado por Felippe Correa
def exists_word(word, instance):
    response = list()

    for file in instance.dataFiles:
        word_occurrence = []

        for str_word in file["linhas_do_arquivo"]:

            if word.lower() in str_word.lower():
                word_occurrence.append({"linha": str_word.count(word)})

                response.append(
                    {
                        "palavra": word,
                        "arquivo": file["nome_do_arquivo"],
                        "ocorrencias": word_occurrence,
                    }
                )
    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
