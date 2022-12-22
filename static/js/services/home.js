$(".button-offers").click((e) => {
  e.preventDefault();
  const email = $(".input-offers").val();

  $.ajax({
    type: "POST",
    dataType: "json",
    url: "/user/profile_offers/",
    data: { email: email },
    success: function (response) {
      Swal.fire({
        position: "center",
        icon: "success",
        title: response.message,
        showConfirmButton: false,
        timer: 1500,
      });
      $(".input-offers").val("");
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});

$(".form-newsletter").on("submit", (e) => {
  e.preventDefault();

  var formValues = $(".form-newsletter").serializeArray();

  console.log(formValues);
});
