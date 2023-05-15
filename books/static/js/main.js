// main.js

// Function to handle the click event on the "Delete" button
function handleDelete(authorId) {
  // Send an AJAX request to delete the author
  $.ajax({
    url: `/authors/${authorId}/delete/`,
    method: 'POST',
    data: {
      csrfmiddlewaretoken: '{{ csrf_token }}'
    },
    success: function(response) {
      // Redirect to the author list page after successful deletion
      window.location.href = '/authors/';
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
}

// Function to handle the form submission for updating an author
function handleUpdate(authorId) {
  // Get the form data
  var formData = {
    first_name: $('#first_name').val(),
    last_name: $('#last_name').val(),
    email: $('#email').val(),
    csrfmiddlewaretoken: '{{ csrf_token }}'
  };

  // Send an AJAX request to update the author
  $.ajax({
    url: `/authors/${authorId}/update/`,
    method: 'POST',
    data: formData,
    success: function(response) {
      // Redirect to the author detail page after successful update
      window.location.href = `/authors/${authorId}/`;
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
}

// Function to handle the form submission for adding a new author
function handleAddAuthor() {
  // Get the form data
  var formData = {
    first_name: $('#first_name').val(),
    last_name: $('#last_name').val(),
    email: $('#email').val(),
    csrfmiddlewaretoken: '{{ csrf_token }}'
  };

  // Send an AJAX request to add the author
  $.ajax({
    url: '/authors/add/',
    method: 'POST',
    data: formData,
    success: function(response) {
      // Redirect to the author list page after successful addition
      window.location.href = '/authors/';
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
}
