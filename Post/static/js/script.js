const reactionContainer = document.getElementById('reaction-container');
        const emojiContainer = document.getElementById('emoji-container');
        let showTimeout;

        // Muestra los emojis al pasar el cursor sobre el botón de reacción
        reactionContainer.addEventListener('mouseover', function() {
            clearTimeout(showTimeout); // Cancela el ocultamiento si el usuario vuelve a pasar el cursor
            emojiContainer.style.display = 'flex';
        });

        // Oculta los emojis si el cursor sale del área de los emojis y el botón de reacción
        reactionContainer.addEventListener('mouseleave', function() {
            showTimeout = setTimeout(function() {
                emojiContainer.style.display = 'none';
            }, 300); // Un pequeño retraso para evitar que desaparezca al moverse rápidamente
        });

        // Función para seleccionar la reacción
        function selectReaction(reaction) {
            const reactionText = document.getElementById('reaction-text');
            reactionText.innerHTML = `<i class="far fa-thumbs-up"></i> ${reaction}`;
            reactionText.classList.add('reaction-selected');
            emojiContainer.style.display = 'none'; // Ocultar los emojis después de seleccionar
        }