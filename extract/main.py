from playwright.sync_api import Page, sync_playwright

# Função para fazer login na aplicação
def fazer_login(page: Page):
    page.goto('https://app.eload.com.br/')
    page.fill('input[id="email"]', 'seu_usuario')
    page.fill('input[name="senha"]', 'sua_senha')
    page.click('text=Continuar')

# Função para extrair dados após o login
def extrair_dados(page):
    # Exemplo: extrair texto de um elemento
    texto = page.inner_text('seletor_do_elemento')

    # Você pode fazer outras operações de extração aqui

    return texto

# Função principal
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Faz login na aplicação
        fazer_login(page)

        # Agora que estamos logados, podemos extrair os dados
        # dados_extraidos = extrair_dados(page) 
        # print("Dados extraídos:", dados_extraidos)

        browser.close()

if __name__ == "__main__":
    main()
