# Treino de SQL e Python

Repositório com meus exercícios diários de SQL e Python, organizados por tema. Faz parte de um plano de estudos de 12 semanas (nov/2026 a jan/2027) para me preparar para vagas de estágio e júnior em dados e desenvolvimento Python.

## Sobre mim

Estudante de Sistemas de Informação na UNINASSAU e técnico em Informática. Tenho experiência prática com PHP, SQL Server e desenvolvimento web, e estou aprofundando Python e bancos de dados.

- GitHub: [github.com/JonatanAJ](https://github.com/JonatanAJ)
- LinkedIn: [linkedin.com/in/jonatan-angelim-a10289252](https://www.linkedin.com/in/jonatan-angelim-a10289252/)

## Estrutura do repositório

```
treino-sql-python/
├── README.md
├── gerar_indice.py
├── python/
│   ├── exercism/
│   ├── hackerrank/
│   └── beecrowd/
├── sql/
│   ├── 01-basico/
│   ├── 02-agregacao/
│   ├── 03-joins/
│   ├── 04-subconsultas-cte/
│   ├── 05-funcoes-de-janela/
│   ├── schemas/
│   └── INDICE.md
└── notas/
```

## Como navegar

- **Exercícios de SQL:** [Ver índice dos exercícios de SQL](sql/INDICE.md)
- **Exercícios de Python:** pasta `python/`, separada por plataforma.
- **Banco de treino:** scripts `CREATE TABLE` e `INSERT` em `sql/schemas/`.
- **Anotações e erros que aprendi:** pasta `notas/`.

## Progresso

<!-- PROGRESSO-INICIO -->
Esta parte é preenchida pelo script gerar_indice.py.
<!-- PROGRESSO-FIM -->

## Tecnologias e plataformas

- **Linguagens:** Python, SQL
- **Bancos:** SQL Server, PostgreSQL, SQLite
- **Treino:** Exercism, HackerRank, Beecrowd, LeetCode, SQLBolt

## Padrão dos arquivos SQL

Cada arquivo começa com um cabeçalho de comentários:

```sql
-- Plataforma: nome e número do exercício
-- Link: endereço do exercício
-- Tema: assunto (por exemplo, LEFT JOIN)
-- Ideia: como pensei na solução
-- Erro que cometi: o que errei no começo
```

## Como atualizar o progresso

Na raiz do repositório, rode `python gerar_indice.py`. O script atualiza o arquivo `sql/INDICE.md` e a seção "Progresso" deste README com a contagem de exercícios por tema.
