import Database

class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = (
            f"CREATE (t:Teacher {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}}) "
            "RETURN t"
        )
        result = self.db.execute(query)
        return result

    def read(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t"
        result = self.db.execute(query)
        return result

    def delete(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) DETACH DELETE t"
        self.db.execute(query)

    def update(self, name, new_cpf):
        query = (
            f"MATCH (t:Teacher {{name: '{name}'}}) "
            f"SET t.cpf = '{new_cpf}' "
            "RETURN t"
        )
        result = self.db.execute(query)
        return result
