$(".button-update-password").on("click", (e) => {
  e.preventDefault();

  let new_password = $("#password").val();

  let headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };
  let payload = {
    password: new_password,
  };

  if (new_password.length < 7) {
    Swal.fire({
      position: "center",
      icon: "warning",
      iconColor: "#D19C97",
      title: "A senha precisa ser maior que 8 caracteres",
      showConfirmButton: false,
      timer: 1500,
    });
  } else {
    $.ajax({
      type: "POST",
      headers: headers,
      dataType: "json",
      url: "/user/update_password_service/",
      data: payload,
      success: function (response) {
        Swal.fire({
          position: "center",
          icon: "success",
          iconColor: "#D19C97",
          title: response.message,
          showConfirmButton: false,
          timer: 1500,
        });
        $("#password").val("");
      },
      error: function (err) {
        console.log(err.responseJSON);
      },
    });
  }
});
