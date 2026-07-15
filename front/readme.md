# Alura Album - Gigantes da Química

Este projeto é um **álbum de figurinhas virtual interativo** focado em grandes químicos da história e suas descobertas revolucionárias. Ele foi construído para simular a experiência física de folhear um álbum e colar figurinhas, homenageando cientistas renomados como Antoine Lavoisier, Marie Curie, Dmitri Mendeleev, John Dalton, Linus Pauling e Louis Pasteur, além de suas contribuições fundamentais para a ciência.

## 🚀 Objetivo do Projeto

O objetivo principal é criar uma interface frontend moderna, responsiva e dinâmica que consome uma API backend de figurinhas (ou utiliza dados locais com geração dinâmica de SVGs como fallback offline) para renderizar os cromos colecionáveis, proporcionando uma experiência de usuário rica com animações premium e efeitos sonoros interativos.

---

## 📂 Estrutura e Funcionalidade dos Arquivos

O projeto no frontend é composto por três arquivos principais:

### 1. 📄 [index.html](index.html)
Define a estrutura semântica da aplicação e as páginas do álbum:
- **Capa & Contracapa:** Apresenta o título com efeitos estéticos e elementos visuais de química (átomos/elementos).
- **Páginas Internas:** Cada página é dedicada a um químico célebre (Lavoisier, Curie, Mendeleev, Dalton, Pauling e Pasteur) contendo um slot especial para o retrato do cientista e slots para suas principais contribuições.
- **Elementos de Controle:** Botões para navegação manual de páginas e controle de som (ativar/desativar).
- **Dependências:** Importa a biblioteca de efeitos de transição de páginas (`page-flip.browser.min.js`), as fontes do Google Fonts (`Inter` e `Outfit`) e o arquivo de estilos local.

### 2. 🎨 [style.css](style.css)
Responsável pelo visual moderno, responsivo e pelas animações da aplicação:
- **Paleta de Cores Magenta:** Tons escuros de magenta, roxo e preto com contrastes vibrantes em fuchsia e rosa neon.
- **Efeitos Dinâmicos (Micro-animações):** 
  - Títulos com efeito *glitch* animado.
  - Brilho metálico simulado no selo da capa.
  - Cartões flutuantes tridimensionais na capa contendo símbolos químicos.
  - Esfera/átomo central com anéis em rotação 3D.
- **Efeito de Dobra de Página:** Sombras sutis que imitam a lombada e a curvatura de páginas físicas.
- **Responsividade:** Regras CSS específicas para ajustar o tamanho do álbum em telas menores e convertê-lo em exibição de página única em dispositivos móveis.

### 3. ⚙️ [app.js](app.js)
Contém toda a lógica e interatividade do lado do cliente:
- **Integração com API & Sistema de Fallback:** Tenta buscar a lista de figurinhas em tempo real através do backend API (`GET http://localhost:8000/figurinhas`). Se a API estiver offline, utiliza uma base de dados local onde os químicos carregam retratos ilustrados de forma local e as descobertas geram dinamicamente imagens em formato SVG (Data URL) com temas de química.
- **Biblioteca PageFlip:** Configura e gerencia a física de folhear o álbum com suporte para arrastar no mouse ou em telas de toque (touch).
- **Web Audio API:** Sintetiza digitalmente o efeito som de papel sendo virado aplicando envelopes de volume e filtros dinâmicos sobre ruído branco.
- **Navegação:** Mapeia a navegação pelas teclas direcionais do teclado (Setas Esquerda/Direita) e cliques nos botões de controle de tela.

---

## 🛠️ Como Executar o Projeto

1. Abra o arquivo `index.html` em seu navegador.
2. Para uma experiência completa de colagem de figurinhas, recomenda-se rodar o projeto por meio de um servidor local (ex: extensão *Live Server* do VS Code ou `python -m http.server 3000` no terminal).
3. Caso queira usar o backend, ative a API (por padrão em `http://localhost:8000`). Se a API não estiver rodando, o álbum usará automaticamente os dados locais com retratos de químicos e ilustrações geradas dinamicamente.
