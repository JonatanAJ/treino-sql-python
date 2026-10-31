from pathlib import Path

INICIO = "<!-- PROGRESSO-INICIO -->"
FIM = "<!-- PROGRESSO-FIM -->"


def contar_sql():
    linhas = ["| Tema | Exercícios |", "|---|---|"]
    total = 0
    for pasta in sorted(Path("sql").iterdir()):
        if pasta.is_dir() and pasta.name != "schemas":
            qtd = len(list(pasta.glob("*.sql")))
            total += qtd
            linhas.append(f"| {pasta.name} | {qtd} |")
    return linhas, total


def contar_python():
    pasta = Path("python")
    if not pasta.exists():
        return 0
    arquivos = [
        f for f in pasta.rglob("*.py") if not f.name.endswith("_test.py")
    ]
    return len(arquivos)


def atualizar_readme(tabela, total_sql, total_py):
    readme = Path("README.md")
    texto = readme.read_text(encoding="utf-8")

    if INICIO not in texto or FIM not in texto:
        print("Marcadores não encontrados no README. Nada foi alterado.")
        return

    bloco = "\n".join([
        INICIO,
        *tabela,
        "",
        f"**Total:** {total_sql} exercícios de SQL (meta: 100) "
        f"e {total_py} de Python (meta: 60).",
        FIM,
    ])

    antes = texto.split(INICIO, 1)[0]
    depois = texto.split(FIM, 1)[1]
    readme.write_text(antes + bloco + depois, encoding="utf-8")


tabela, total_sql = contar_sql()
total_py = contar_python()

Path("sql/INDICE.md").write_text("\n".join(tabela), encoding="utf-8")
atualizar_readme(tabela, total_sql, total_py)

print(f"SQL: {total_sql} | Python: {total_py}")