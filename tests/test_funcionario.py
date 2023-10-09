from app.funcionario import Funcionario

colaborador = Funcionario("Sofia","Gerente",3000)

def test_verificarDados():
    assert colaborador.dados() == "Sofia seu cargo é Gerente e seu salário é 3000"

def test_calcularBonus():
    assert colaborador.calcularBonus() >= 300
    # valor de calcularBonus será maior ou igual a 300.

# python -m pytest test_funcionario.py < = executar esse comando no terminal

def test_registrarPonto():
    assert colaborador.registrarPonto() == "Ponto registrado na data 2023-10-09"