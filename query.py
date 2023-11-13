# Importe a classe Database
import Database

# Crie uma instância da classe Database com as informações de conexão do seu banco de dados Neo4j
db = Database("neo4j+s://5bc4cfc7789cb49fed5331331086c4bc.neo4jsandbox.com:7687", "root", "password")

# Questão 01

# a. Busque pelo professor "Teacher" cujo nome seja "Renzo", retorne o ano_nasc e o CPF.
query_a = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.CPF"
result_a = db.execute(query_a)
print("Resultado da consulta (a):")
print(result_a)

# b. Busque pelos professores "Teacher" cujo nome comece com a letra "M", retorne o name e o cpf.
query_b = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.CPF"
result_b = db.execute(query_b)
print("Resultado da consulta (b):")
print(result_b)

# c. Busque pelos nomes de todas as cidades "City" e retorne-os.
query_c = "MATCH (c:City) RETURN c.name"
result_c = db.execute(query_c)
print("Resultado da consulta (c):")
print(result_c)

# d. Busque pelas escolas "School", onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.
query_d = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
result_d = db.execute(query_d)
print("Resultado da consulta (d):")
print(result_d)

# Questão 02

# a. Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
query_a = (
    "MATCH (t:Teacher) "
    "WITH COLLECT(t) AS teachers "
    "WITH REDUCE(min_age = teachers[0].ano_nasc, t IN teachers | "
    "CASE WHEN t.ano_nasc < min_age THEN t.ano_nasc ELSE min_age END) AS min_year, "
    "REDUCE(max_age = teachers[0].ano_nasc, t IN teachers | "
    "CASE WHEN t.ano_nasc > max_age THEN t.ano_nasc ELSE max_age END) AS max_year "
    "RETURN min_year, max_year"
)
result_a = db.execute(query_a)
print("Resultado da consulta (a):")
print(result_a)

# b. Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade "population".
query_b = "MATCH (c:City) RETURN AVG(c.population) AS average_population"
result_b = db.execute(query_b)
print("Resultado da consulta (b):")
print(result_b)

# c. Encontre a cidade cujo CEP seja igual a "37540-000" e retorne o nome com todas as letras "a" substituídas por "A".
query_c = "MATCH (c:City {CEP: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A') AS modified_name"
result_c = db.execute(query_c)
print("Resultado da consulta (c):")
print(result_c)

# d. Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
query_d = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2) AS third_character"
result_d = db.execute(query_d)
print("Resultado da consulta (d):")
print(result_d)

# Feche a conexão com o banco de dados quando terminar
db.close()
