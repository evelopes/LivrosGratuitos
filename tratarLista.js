import {listaLivros} from './livros.js';


function displayBooks(livro) {
const container = document.querySelector("#livros-container");

livro.forEach((book) => {
  const a = document.createElement("a");
  const img = document.createElement("img");

  a.setAttribute("href", book.url);
  img.setAttribute("src", book.imagem);
  img.setAttribute("alt", book.nome);
  img.classList.add("livro");

  a.appendChild(img);
  container.appendChild(a);
});
}

displayBooks(listaLivros);
