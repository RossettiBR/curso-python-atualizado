from pathlib import Path

caminho_completo = Path()
print(caminho_completo.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

print(caminho_arquivo.parent.parent)

ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

arquivo = Path.home() / 'Área de Trabalho' / 'arquivo.txt'
arquivo.touch()
arquivo.write_text('Olá mundo')
arquivo.unlink()
