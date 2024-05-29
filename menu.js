
document.addEventListener("DOMContentLoaded", function() {
    var currentPage = "/" + window.location.pathname.split("/").pop() + ".html"; // Obtener el nombre del archivo actual

    var links = document.querySelectorAll("nav a");

    links.forEach(function(link) {
        // Comprobar si el href del enlace coincide con la página actual
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }
    });
});

var currentPage = "/" +  window.location.pathname.split("/").pop() + ".html";
console.log(currentPage)

var links = document.querySelectorAll("nav a");

links.forEach(function(link) {
   
    console.log(link.getAttribute("href"))
    });