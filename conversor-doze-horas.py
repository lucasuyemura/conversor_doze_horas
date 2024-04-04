def ConversorDozeHoras():
  hora = int(input("Digite a hora para conversão: "))
  minuto = int(input("Digite o minuto da hora analisada: "))

  match hora:
    case 12:
      conversor_para_doze = hora - 12
      valor_doze_horas_formatado = f"0{conversor_para_doze}:{minuto} P.M"
      return print(valor_doze_horas_formatado)

    case hora if hora < 12:
      conversor_am = hora + 12
      valor_do_tempo_formatado = f"{conversor_am}:{minuto} P.M"  
      return print(valor_do_tempo_formatado)

    case _:
      conversor_pm = hora - 12
      valor_do_tempo_formatado = f"{conversor_pm}:{minuto} A.M"
      return print(valor_do_tempo_formatado)

ConversorDozeHoras()

