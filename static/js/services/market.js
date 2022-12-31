$(".remove-wishlist").on("click", (e) => {
  e.preventDefault();
  let wishlistId = e.currentTarget.id;

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  console.log(wishlistId);
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
        },
        error: function (err) {
          console.log(err.responseJSON);
        },
      });
    }
  });
});
