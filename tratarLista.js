import {listaLivros} from './livros2.js';


function displayBooks(livros) {
  const container = document.querySelector("#livros-container");
  const temas = {};

  // Agrupar os livros pelo tema
  livros.forEach((livro) => {
    const tema = livro.tema;

    if (temas[tema]) {
      temas[tema].push(livro);
    } else {
      temas[tema] = [livro];
    }
  });

  // Criar elementos HTML para cada tema e seus respectivos livros
  for (const tema in temas) {
    const livrosDoTema = temas[tema];

    // Criação do elemento h1 para o tema
    const h1 = document.createElement("h1");
    h1.textContent = tema;
    container.appendChild(h1);
    const br = document.createElement("br");
    container.appendChild(br)
    
    const DIV = document.createElement("div");

    // Criação dos elementos HTML para cada livro
    livrosDoTema.forEach((livro) => {
      const a = document.createElement("a");
      const img = document.createElement("img");

      a.setAttribute("href", livro.url);
      img.setAttribute("src", livro.imagem);
      img.setAttribute("alt", livro.nome);
      img.classList.add("livro");

      a.appendChild(img);
      DIV.appendChild(a);
    });
    container.appendChild(DIV)
  }

}


displayBooks(listaLivros);
