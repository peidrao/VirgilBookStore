$(".input-coupon-active").on("click", (e) => {
  let couponId = e.currentTarget.id;
  let checked = $(`#${couponId}`).prop("checked");

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "PATCH",
    dataType: "json",
    url: `/coupons/${couponId}/update/status`,
    data: { checked: checked },
    headers: headers,
    success: function (response) {
      window.location.reload();
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});

$("#form-coupon-update").on("submit", (e) => {
  e.preventDefault();
  let form = $("#form-coupon-update").serializeArray();
  form.shift();
  let couponId = form.shift().value;

  let formObject = form.reduce(function (a, x) {
    a[x.name] = x.value;
    return a;
  }, {});

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "PATCH",
    dataType: "json",
    url: `/coupons/${couponId}`,
    data: JSON.stringify(formObject),
    headers: headers,
    success: function (response) {
      console.log(response);
      window.location.reload();
    },
    error: function (err) {
      console.log(err.responseJSON);
    },
  });
});
