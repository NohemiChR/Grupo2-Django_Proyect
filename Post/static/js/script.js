// Selecciona todos los contenedores de reacciones
const reactionContainers = document.querySelectorAll(".reaction-container");

// Recorre cada contenedor de reacciones y asigna los eventos
reactionContainers.forEach((container) => {
  const emojiContainer = container.querySelector(".emoji-reactions");
  const reactionText = container.querySelector(".reaction-text");

  // Mostrar emojis al hacer hover en el contenedor de reacciones
  container.addEventListener("mouseover", function () {
    clearTimeout(container.showTimeout); // Cancela el ocultamiento si el usuario vuelve a pasar el cursor
    emojiContainer.style.display = "flex";
  });

  // Ocultar emojis cuando el cursor salga del contenedor de reacciones
  container.addEventListener("mouseleave", function () {
    container.showTimeout = setTimeout(function () {
      emojiContainer.style.display = "none";
    }, 300); // Un pequeño retraso para evitar que desaparezca inmediatamente
  });

  // Agregar evento para seleccionar la reacción
  const emojis = emojiContainer.querySelectorAll("img");
  // Agregar evento para seleccionar la reacción
  emojis.forEach((emoji) => {
    emoji.addEventListener("click", function () {
      const reaction = emoji.getAttribute("title");
      reactionText.innerHTML = `<i class="far fa-thumbs-up"></i> ${reaction}`;
      reactionText.classList.add("reaction-selected");
      emojiContainer.style.display = "none"; // Ocultar emojis después de seleccionar

      // Hacer la petición POST con la reacción seleccionada
      const postId = container.dataset.postId; // Debes asegurarte de tener el postId en el contenedor
      fetch(`/post/${postId}/react/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
        },
        body: new URLSearchParams({
          reaction: emoji.getAttribute("alt"), // Enviar el tipo de reacción
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "ok") {
            console.log("Reacción guardada:", data.reaction);
          } else {
            console.error("Error al guardar la reacción");
          }
        });
    });
  });
});
