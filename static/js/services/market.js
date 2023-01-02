$(".remove-wishlist").on("click", (e) => {
  e.preventDefault();
  let wishlistId = e.currentTarget.id;

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  Swal.fire({
    title: "Are you sure you want to remove this book",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes",
    cancelButtonText: "Not",
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        type: "DELETE",
        dataType: "json",
        url: `/wishlist/remove/${wishlistId}`,
        headers: headers,
        success: function (response) {
          console.log(response);
          Swal.fire("Success!", response, "success");
          window.location.reload();
        },
        error: function (err) {
          console.log(err.responseJSON);
        },
      });
    }
  });
});

$(".remove-cart").on("click", (e) => {
  e.preventDefault();
  let cart = e.currentTarget.id;
  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  Swal.fire({
    title: "Are you sure you want to remove this book",
    icon: "question",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes",
    cancelButtonText: "Not",
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        type: "DELETE",
        dataType: "json",
        url: `/cart/${cart}`,
        headers: headers,
        success: function (response) {
          console.log(response);
          Swal.fire("Success!", response, "success");
          window.location.reload();
        },
        error: function (err) {
          console.log(err.responseJSON);
        },
      });
    }
  });
});

$(".btn-plus").click(function () {
  let id = this.id;
  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "PUT",
    dataType: "json",
    url: `/cart/${id}`,
    data: { action: "plus" },
    headers: headers,
    success: function (response) {
      $(".discount-price").text(`R$ ${response.discount}`);
      $(`#book-total-price-${id}`).text(`R$ ${response.total}`);
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});
