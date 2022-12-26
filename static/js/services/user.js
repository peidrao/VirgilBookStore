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

$("#form-profile-update").on("submit", (e) => {
  e.preventDefault();

  let formData = $("#form-profile-update").serializeArray();
  let token = formData.shift()["value"];

  formData[4]["value"] = true ? formData[4]["value"] == "on" : false;

  $.ajax({
    type: "POST",
    dataType: "json",
    headers: { "X-CSRFToken": token },
    url: "/user/profile_update/",
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
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});
