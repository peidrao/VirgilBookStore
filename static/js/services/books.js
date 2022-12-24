function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(".remove-book").on("click", (e) => {
  e.preventDefault();
  let book_id = e.currentTarget.id;

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  console.log(headers);
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
