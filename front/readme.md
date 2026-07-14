# Alura Album - Copa do Mundo Tech

Este projeto é um **álbum de figurinhas virtual interativo** focado em grandes personalidades e tecnologias do mundo da computação e do desenvolvimento de software. Ele foi construído para simular a experiência física de folhear um álbum e colar figurinhas, homenageando figuras da Inteligência Artificial, Python, Bancos de Dados, Sistemas Operacionais e personalidades do ecossistema de tecnologia brasileiro.

## 🚀 Objetivo do Projeto

O objetivo principal é criar uma interface frontend moderna, responsiva e dinâmica que consome uma API backend de figurinhas para renderizar os cromos colecionáveis, proporcionando uma experiência de usuário rica com animações premium e efeitos sonoros interativos.

---

## 📂 Estrutura e Funcionalidade dos Arquivos

O projeto no frontend é composto por três arquivos principais:

### 1. 📄 [index.html](index.html)
Define a estrutura semântica da aplicação e as páginas do álbum:
- **Capa & Contracapa:** Apresenta o título com efeitos estéticos e elementos visuais flutuantes.
- **Páginas Internas:** Divididas por categorias de tecnologia (IA, Python, Banco de Dados, Sistemas Operacionais e Brasil) com grids contendo slots numerados para cada figurinha.
- **Elementos de Controle:** Botões para navegação manual de páginas e controle de som (ativar/desativar).
- **Dependências:** Importa a biblioteca de efeitos de transição de páginas (`page-flip.browser.min.js`), as fontes do Google Fonts (`Inter` e `Outfit`) e o arquivo de estilos local.

### 2. 🎨 [style.css](style.css)
Responsável pelo visual moderno, responsivo e pelas animações da aplicação:
- **Paleta de Cores Premium:** Tons escuros de azul e preto com contrastes em azul neon e ciano.
- **Efeitos Dinâmicos (Micro-animações):** 
  - Títulos com efeito *glitch* animado.
  - Brilho metálico simulado no selo da capa.
  - Cartões flutuantes tridimensionais na capa.
  - Esfera tecnológica central com anéis em rotação 3D.
- **Efeito de Dobra de Página:** Sombras sutis que imitam a lombada e a curvatura de páginas físicas.
- **Responsividade:** Regras CSS específicas para ajustar o tamanho do álbum em telas menores e convertê-lo em exibição de página única em dispositivos móveis.

### 3. ⚙️ [app.js](app.js)
Contém toda a lógica e interatividade do lado do cliente:
- **Integração com API Backend:** Busca a lista de figurinhas em tempo real através do endpoint `GET http://localhost:8000/figurinhas` na função `preencherFigurinhas()`. As figurinhas correspondentes são inseridas de forma dinâmica nos slots, acompanhadas de uma animação suave de "colagem".
- **Biblioteca PageFlip:** Configura e gerencia a física de folhear o álbum com suporte para arrastar no mouse ou em telas de toque (touch).
- **Web Audio API:** Sintetiza digitalmente o efeito sonoro de papel sendo virado (sem carregar arquivos de áudio externos) aplicando envelopes de volume e filtros dinâmicos sobre ruído branco.
- **Navegação:** Mapeia a navegação pelas teclas direcionais do teclado (Setas Esquerda/Direita) e cliques nos botões de controle de tela.

---

## 🛠️ Como Executar o Projeto

1. Certifique-se de que o backend está ativo (por padrão respondendo em `http://localhost:8000`).
2. Abra o arquivo `index.html` em seu navegador. Para uma melhor experiência de desenvolvimento e evitar problemas de CORS, recomenda-se servir o frontend usando uma extensão como a *Live Server* ou um servidor HTTP simples (ex: `python -m http.server 3000`).
