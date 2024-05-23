
document.addEventListener("DOMContentLoaded", function() {
    var currentPage = window.location.pathname.split("/").pop(); // Obtener el nombre del archivo actual

    var paginas = ["index.html", "Catalogo.html", "nosotros.html", "FQ.html"]
    var ids = ["indexLink", "catalogoLink", "nosotrosLink", "FQLink"]

    
    for (var i = 0; i < 4; i++) {
        if (paginas[i] == currentPage){
            document.getElementById(ids[i]).classList.add("active");
        }
    }
});