import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Juros Compostos"
    texto_resultado = ft.Text()
    juros_imagem = ft.Image(src="https://images.static.jeniusbank.com/81bfavdafg0o/7oKNPN3RqmSBPHQpeiPULv/1a4c1252852d9bbd62bc103f33068848/compound-interest-blog-jeniusbank-20230825-1280x721.webp", width=64, height=64)
    container_resultados = ft.Row([
        juros_imagem,texto_resultado
    ])

    capital = ft.TextField(label="Valor inicial (capital)", on_change=lambda e: apenas_numeros(e, capital))

    juros = ft.TextField(label="Taxa de juros (%)", on_change=lambda e: apenas_numeros(e, juros))

    períodos = ft.TextField(label="Número de períodos", on_change=lambda e: apenas_numeros(e, períodos))

    frequencia_juros = ft.Dropdown(options=[
        ft.dropdown.Option("Anual"),
        ft.dropdown.Option("Semestral"),
        ft.dropdown.Option("Trimestral"),
        ft.dropdown.Option("Mensal")
    ], label="Frequência dos juros")


    def valida(capital_value, n_periodos_value, taxa_juros_value):
        capital.error_text = ""
        períodos.error_text = ""
        juros.error_text = ""
        try:
            capital_value = float(capital_value)
            n_periodos_value = int(n_periodos_value)
            taxa_juros_value = float(taxa_juros_value)

            if capital_value <= 0:
                capital.error_text = "O capital deve ser um valor positivo."
                return False
            if n_periodos_value <= 0:
                períodos.error_text = "O número de períodos deve ser um valor positivo."
                return False
            if taxa_juros_value < 0:
                juros.error_text = "A taxa de juros não pode ser negativa."
                return False
            return True
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            return False

    def apenas_numeros(event, campo):
        # Remove caracteres não numéricos, exceto o ponto decimal
        novo_valor = ''.join(c for c in campo.value if c.isdigit() or c == '.')
        campo.value = novo_valor
        page.update()
    def envia(e):


        if valida(capital.value, períodos.value, juros.value):
            capital_valor = float(capital.value)
            n_periodos_valor = int(períodos.value)
            taxa_juros_valor = float(juros.value)

            match frequencia_juros.value:
                case "Anual":
                    n_periodos_valor *= 12
                case "Semestral":
                    n_periodos_valor *= 6
                case "Trimestral":
                    n_periodos_valor *= 3
                case _:
                    n_periodos_valor *= 1

            capital_final = capital_valor * ((1 + (taxa_juros_valor / 100)) ** int(n_periodos_valor))
            texto_resultado.value = f"Seu montante final é R$ {capital_final:.2f}, com R$ {((1 + (taxa_juros_valor / 100)) ** int(n_periodos_valor)):.2f} de juros acumulados"

            page.update()
    botao_calculo = ft.ElevatedButton("Calcular juros compostos", on_click=envia)

    page.add(container_resultados, ft.Row([ft.Column([capital, juros]), ft.Column([períodos, frequencia_juros])]), botao_calculo)


ft.app(main)