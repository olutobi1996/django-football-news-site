const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-edit");
  editButtons.forEach((button) => {
      button.addEventListener("click", (event) => {
          const commentId = button.getAttribute("data-comment_id");
          const editFormContainer = document.querySelector(`#editFormContainer${commentId}`);
          // Fetch and display form dynamically
          fetch(`/edit_comment/${slug}/${commentId}/`)
              .then((response) => response.text())
              .then((html) => {
                  editFormContainer.innerHTML = html;
              })
              .catch((error) => console.error("Error fetching form:", error));
      });
  });
});

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }