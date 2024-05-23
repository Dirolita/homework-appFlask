
document.addEventListener('DOMContentLoaded', function() {
    // Obtener el username desde el input hidden
    const username = document.getElementById('username').value;

    // Obtener todos los botones de eliminar y agregar un evento onclick a cada uno
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const confirmationPopup = document.getElementById("confirmation-popup");
    const close = document.querySelector('.close');
    const cancel = document.querySelector('.cancel');
    const btnConfirm = document.getElementById('confirmDeleteBtn');
    
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const taskIndex = this.getAttribute('data-task-index');
            showPopUp(taskIndex);
        });
    });

    close.addEventListener('click', closePopUp);
    cancel.addEventListener('click', closePopUp);
    btnConfirm.addEventListener('click', confirmDelete);

    function showPopUp(taskIndex) {
        console.log('Pop-up mostrado');
        console.log(taskIndex);
        confirmationPopup.setAttribute('data-task-index', taskIndex);
        confirmationPopup.style.display = 'block';
    }

    function closePopUp() {
        confirmationPopup.style.display = 'none';
    }

    function confirmDelete() {
        const taskIndex = confirmationPopup.getAttribute('data-task-index');
        const deleteActionUrl = `/delete_task/${username}/${taskIndex}`;
        console.log('Deleting task with index:', taskIndex);
        fetch(deleteActionUrl, { method: 'POST' })
            .then(response => {
                if (response.ok) {
                    // Actualizar la página después de la eliminación exitosa
                    window.location.reload();
                } else {
                    console.error('Error al eliminar la tarea');
                }
            })
            .catch(error => console.error('Error en la solicitud:', error));
    }
});
