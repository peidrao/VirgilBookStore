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
