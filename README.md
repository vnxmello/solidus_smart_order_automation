# Solidus Smart Automation

## Sobre o Projeto
Este é um script de automação web em **Python** que utiliza a biblioteca **Selenium** para interagir com o sistema **Solidus Smart**. A ferramenta foi desenvolvida para automatizar o processo massivo de liberação de encomendas, otimizando o fluxo de trabalho.

**Funcionalidades Principais:**
- **Login Automatizado**: Acessa o sistema Solidus Smart com credenciais de usuário e seleciona a filial correta.
- **Navegação e Processamento**: Navega para a página de liberação de encomendas.
- **Lógica de Decisão**: Analisa a descrição dos itens de cada encomenda e, com base em critérios específicos (como a presença de `*` ou `**`), decide se a encomenda deve ser autorizada ou rejeitada.
- **Execução Sequencial**: Processa as encomendas em ordem inversa (do final para o início da página, ou seja, do mais antigo pro mais recente), salvando as alterações no sistema.

A ferramenta é distribuída como um **executável (`.exe`)**, o que a torna uma solução de fácil uso e distribuição para equipes que não possuem conhecimento em programação, sem a necessidade de instalar o Python ou outras dependências.

---

## Tecnologias e Pré-requisitos
A versão compilada desta ferramenta **não exige a instalação do Python ou de bibliotecas** pelo usuário final. A única dependência externa necessária é o navegador **Google Chrome**, pois o executável já inclui o `Chromedriver` necessário.

Para usuários que desejam executar o código-fonte, as seguintes bibliotecas Python são utilizadas:

 **selenium**: Para controle e automação do navegador.
 **time**: Para pausas programadas.
