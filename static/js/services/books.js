$(".remove-book").on("click", (e) => {
  e.preventDefault();
  let book_id = e.currentTarget.id;

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  Swal.fire({
    title: "Tem certeza que deseja remover este livro?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sim",
    cancelButtonText: "Nao",
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        type: "DELETE",
        dataType: "json",
        url: `/book/remove/${book_id}`,
        headers: headers,
        success: function (response) {
          Swal.fire("Removido!", "Livro removido", "success");
          location.reload();
        },

        error: function (err) {
          console.log(err.responseJSON);
        },
      });
    }
  });
});

$("#form-book-create").on("submit", (e) => {
  e.preventDefault();
  let form = $("#form-book-create").serialize();

  let headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "POST",
    headers: headers,
    dataType: "json",
    data: form,
    url: "/book/create",
    success: function (response) {
      Swal.fire("Success!", "Book successfully added", "success");
    },
    error: function (err) {
      Swal.fire({
        title: "error",
        icon: "warning",
        text: err.responseJSON,
      });
    },
  });
});

$(".button-export-csv").on("click", () => {
  let headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "GET",
    headers: headers,
    dataType: "json",
    url: "/book/export",
    success: function (response) {
      console.log(response);
    },
    error: function (err) {
      Swal.fire({
        title: "error",
        icon: "warning",
        text: err.responseJSON,
      });
    },
  });
});

$("#form-book-update").on("submit", (e) => {
  e.preventDefault();
  let form = $("#form-book-update").serializeArray();
  let token = form.shift().value;
  let id = form.shift().value;

  let headers = {
    "X-CSRFToken": token,
  };
  console.log(id);
  console.log(token);

  $.ajax({
    type: "PATCH",
    headers: headers,
    dataType: "json",
    data: form,
    url: `/book/update/service/${id}/`,
    success: function (response) {
      Swal.fire("Success!", "Book successfully added", "success");
    },
    error: function (err) {
      Swal.fire({
        title: "error",
        icon: "warning",
        text: err.responseJSON,
      });
    },
  });
});
