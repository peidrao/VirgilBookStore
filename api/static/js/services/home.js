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
        iconColor: "#D19C97",
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

$("#form-newsletter").on("submit", (e) => {
  e.preventDefault();

  let formData = $("#form-newsletter").serializeArray();
  formData.shift();

  $.ajax({
    type: "POST",
    dataType: "json",
    url: "/user/profile_newsletter/",
    data: formData,
    success: function (response) {
      Swal.fire({
        position: "center",
        icon: "success",
        iconColor: "#D19C97",
        title: response.message,
        showConfirmButton: false,
        timer: 1500,
      });
      $("#form-newsletter")[0].reset();
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});
