$(document).ready(function () {
  console.log("Oi");
});

$(".button-offers").click((e) => {
  e.preventDefault();
  const email = $(".input-offers").val();

  $.ajax({
    type: "POST",
    dataType: "json",
    url: "/user/profile_offers/",
    data: JSON.stringify({ email: email }),
    success: function (response) {
      console.log(response);
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});
