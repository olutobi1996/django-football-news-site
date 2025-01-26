/**
 * @jest-environment jsdom
 */

import '@testing-library/jest-dom';
import { fireEvent } from '@testing-library/dom';

// Mock Bootstrap Modal
global.bootstrap = {
  Modal: jest.fn(() => ({
    show: jest.fn(),
  })),
};

// HTML structure to mock the DOM
const mockHTML = `
  <div id="id_body"></div>
  <form id="commentForm"></form>
  <button id="submitButton"></button>
  <div id="deleteModal"></div>
  <a id="deleteConfirm"></a>
  <button class="btn-edit" data-comment_id="#edit1">Edit 1</button>
  <button class="btn-delete" data-comment_id="1">Delete 1</button>
  <div id="edit1"></div>
`;

describe('Comment Handlers', () => {
  beforeEach(() => {
    document.body.innerHTML = mockHTML;
  });

  it('should set up edit button click listeners and fetch edit form on click', async () => {
    const editButtons = document.querySelectorAll('.btn-edit');
    const editFormContainer = document.querySelector('#edit1');

    // Mock the fetch API
    global.fetch = jest.fn(() =>
      Promise.resolve({
        text: () => Promise.resolve('<form>Edit Form HTML</form>'),
      })
    );

    // Attach event listeners (this mimics your code execution)
    require('./commentHandlers');

    // Simulate clicking the first edit button
    const firstEditButton = editButtons[0];
    fireEvent.click(firstEditButton);

    // Wait for the fetch to complete
    await new Promise(process.nextTick);

    // Verify that the fetch API was called with the correct URL
    expect(global.fetch).toHaveBeenCalledWith('/edit_comment/undefined/#edit1/');

    // Verify that the edit form's HTML was injected into the container
    expect(editFormContainer.innerHTML).toBe('<form>Edit Form HTML</form>');
  });

  it('should set up delete button click listeners and update the modal confirm link', () => {
    const deleteButtons = document.querySelectorAll('.btn-delete');
    const deleteConfirm = document.getElementById('deleteConfirm');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));

    // Attach event listeners (this mimics your code execution)
    require('./commentHandlers');

    // Simulate clicking the first delete button
    const firstDeleteButton = deleteButtons[0];
    fireEvent.click(firstDeleteButton);

    // Verify that the delete confirm href was updated
    expect(deleteConfirm.href).toContain('/delete_comment/1');

    // Verify that the modal's `show` method was called
    expect(deleteModal.show).toHaveBeenCalled();
  });

  it('should add DOMContentLoaded event listener', () => {
    // Mock `addEventListener`
    const addEventListenerSpy = jest.spyOn(document, 'addEventListener');

    // Attach event listeners (this mimics your code execution)
    require('./commentHandlers');

    // Verify that DOMContentLoaded was added as an event listener
    expect(addEventListenerSpy).toHaveBeenCalledWith(
      'DOMContentLoaded',
      expect.any(Function)
    );
  });
});
