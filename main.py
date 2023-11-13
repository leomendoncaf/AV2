from teacher_crud import TeacherCRUD
from Database import Database

def main():
    # Crie uma instância da classe Database com as informações de conexão do seu banco de dados Neo4j
    db = Database("neo4j+s://5bc4cfc7789cb49fed5331331086c4bc.neo4jsandbox.com:7687", "root", "password")

    # Crie uma instância da classe TeacherCRUD
    teacher_crud = TeacherCRUD(db)

    while True:
        print("Escolha uma opção:")
        print("1. Criar Teacher")
        print("2. Ler Teacher")
        print("3. Deletar Teacher")
        print("4. Atualizar CPF do Teacher")
        print("5. Sair")

        choice = input("Opção: ")

        if choice == "1":
            name = input("Nome: ")
            ano_nasc = int(input("Ano de nascimento: "))
            cpf = input("CPF: ")
            teacher_crud.create(name, ano_nasc, cpf)
            print("Teacher criado com sucesso!")

        elif choice == "2":
            name = input("Nome do Teacher a ser lido: ")
            result = teacher_crud.read(name)
            print(result)

        elif choice == "3":
            name = input("Nome do Teacher a ser deletado: ")
            teacher_crud.delete(name)
            print("Teacher deletado com sucesso!")

        elif choice == "4":
            name = input("Nome do Teacher a ser atualizado: ")
            new_cpf = input("Novo CPF: ")
            result = teacher_crud.update(name, new_cpf)
            print("CPF atualizado com sucesso!")

        elif choice == "5":
            break

    db.close()

if __name__ == "__main__":
    main()
