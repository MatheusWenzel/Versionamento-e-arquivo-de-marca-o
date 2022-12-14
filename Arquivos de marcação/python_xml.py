# importa o xml

# xml_filmes = importa_xml()

xml_filmes = []
# são as tags que foram criadads

# lista é não estruturada pode ter diferentes formatos
xml_filmes['filmes']
xml_filmes['filmes'][0]
xml_filmes['filmes'][0]['id']
xml_filmes['filmes'][0]['nome']
xml_filmes['filmes'][0]['ano_lancamento']


# a classa é estruturada, tem que respeitar o que ta dentro
class Filme:
    def __init__(self, id, nome) -> None:
        self._id = id
        self._nome = nome


f = Filme()
f.nome = "Nome"
f.abobrinha = "123"  # não existe
