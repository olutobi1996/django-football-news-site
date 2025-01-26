// Get all elements with the class "btn-edit" and store them in the variable `editButtons`.
const editButtons = document.getElementsByClassName("btn-edit");

// Get the HTML element with the ID "id_body" and store it in the variable `commentText`.
const commentText = document.getElementById("id_body");

// Get the HTML element with the ID "commentForm" and store it in the variable `commentForm`.
const commentForm = document.getElementById("commentForm");

// Get the HTML element with the ID "submitButton" and store it in the variable `submitButton`.
const submitButton = document.getElementById("submitButton");

// Create a new instance of a Bootstrap modal and associate it with the HTML element with the ID "deleteModal".
// const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

// Get all elements with the class "btn-delete" and store them in the variable `deleteButtons`.
// const deleteButtons = document.getElementsByClassName("btn-delete");

// Get the HTML element with the ID "deleteConfirm" and store it in the variable `deleteConfirm`.
// const deleteConfirm = document.getElementById("deleteConfirm");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
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
            const editFormContainer = document.querySelector(`${commentId}`);

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

// Delete button for form
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `${blogSlug}/delete_comment/${commentId}`;
        deleteModal.show();
    });
}