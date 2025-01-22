// Get all elements with the class "btn-edit" and store them in the variable `editButtons`.
const editButtons = document.getElementsByClassName("btn-edit");

// Get the HTML element with the ID "id_body" and store it in the variable `commentText`.
const commentText = document.getElementById("id_body");

// Get the HTML element with the ID "commentForm" and store it in the variable `commentForm`.
const commentForm = document.getElementById("commentForm");

// Get the HTML element with the ID "submitButton" and store it in the variable `submitButton`.
const submitButton = document.getElementById("submitButton");

// Create a new instance of a Bootstrap modal and associate it with the HTML element with the ID "deleteModal".
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

// Get all elements with the class "btn-delete" and store them in the variable `deleteButtons`.
const deleteButtons = document.getElementsByClassName("btn-delete");

// Get the HTML element with the ID "deleteConfirm" and store it in the variable `deleteConfirm`.
const deleteConfirm = document.getElementById("deleteConfirm");

// Add an event listener to the DOM that triggers once the content is fully loaded.
document.addEventListener("DOMContentLoaded", function () {
    // Select all elements with the class "btn-edit" and store them in a NodeList `editButtons`.
    const editButtons = document.querySelectorAll(".btn-edit");

    // Loop through each button in the NodeList.
    editButtons.forEach((button) => {
        // Add a click event listener to the current button.
        button.addEventListener("click", (event) => {
            // Get the value of the data-comment_id attribute from the button.
            const commentId = button.getAttribute("data-comment_id");

            // Use the commentId to find the associated container for the edit form.
            const editFormContainer = document.querySelector(`#editFormContainer${commentId}`);

            // Dynamically fetch the edit form's HTML from the server.
            fetch(`/edit_comment/${slug}/${commentId}/`) // Adjust the `slug` variable as needed.
                .then((response) => response.text()) // Convert the server's response to plain text (HTML).
                .then((html) => {
                    // Inject the fetched HTML into the edit form container.
                    editFormContainer.innerHTML = html;
                })
                .catch((error) => console.error("Error fetching form:", error)); // Log any errors that occur.
        });
    });
});

// Add another event listener to execute when the DOM content is loaded.
document.addEventListener('DOMContentLoaded', function () {
    // Get the HTML element with the ID "deleteModal".
    const deleteModal = document.getElementById('deleteModal');

    // Get the HTML element with the ID "deleteCommentForm".
    const deleteForm = document.getElementById('deleteCommentForm');

    // Add an event listener to the modal that triggers when it is about to be shown.
    deleteModal.addEventListener('show.bs.modal', function (event) {
        // Get the button that triggered the modal display.
        const button = event.relatedTarget;

        // Extract the comment ID from the data-comment_id attribute of the button.
        const commentId = button.getAttribute('data-comment_id');

        // Extract the post slug from the data-post_slug attribute of the button.
        const postSlug = button.getAttribute('data-post_slug');

        // Construct the URL for deleting the comment using the post slug and comment ID.
        const deleteUrl = `/post/${postSlug}/delete_comment/${commentId}/`; // Update URL based on your URL pattern.

        // Update the action attribute of the delete form with the constructed URL.
        deleteForm.setAttribute('action', deleteUrl);
    });
});