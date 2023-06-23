import {listaLivros} from './livros2.js';


function displayBooks(livros) {
  const container = document.querySelector("#livros-container");
  const temas = {};

  
  livros.forEach((livro) => {
    const tema = livro.tema;

    if (temas[tema]) {
      temas[tema].push(livro);
    } else {
      temas[tema] = [livro];
    }
  });

  
  for (const tema in temas) {
    const livrosDoTema = temas[tema];

    
    const h1 = document.createElement("h1");
    h1.textContent = tema;
    const br = document.createElement("br");
    container.appendChild(br)
    container.appendChild(h1);
    container.appendChild(br)
    
    const DIV = document.createElement("div");

    
    livrosDoTema.forEach((livro) => {
      const a = document.createElement("a");
      const img = document.createElement("img");

      a.setAttribute("href", livro.url);
      img.setAttribute("src", livro.imagem);
      img.setAttribute("alt", livro.nome);
      img.setAttribute("title", livro.nome);
      img.classList.add("livro");

      a.appendChild(img);
      DIV.appendChild(a);
    });
    container.appendChild(DIV)
  }

}


displayBooks(listaLivros);
