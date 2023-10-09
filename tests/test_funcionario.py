from app.funcionario import Funcionario

colaborador = Funcionario("Sofia","Gerente",3000)

def test_verificarDados():
    assert colaborador.dados() == "Sofia seu cargo é Gerente e seu salário é 3000"

