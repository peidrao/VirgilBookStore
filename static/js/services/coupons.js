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

$("#form-coupon-add").on("submit", (e) => {
  e.preventDefault();
  let form = $("#form-coupon-add").serializeArray();
  form.shift();

  let formObject = form.reduce(function (a, x) {
    a[x.name] = x.value;
    return a;
  }, {});

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  $.ajax({
    type: "POST",
    dataType: "json",
    url: "/coupons/add/service",
    data: formObject,
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

$(".remove-discount").on("click", (e) => {
  e.preventDefault();
  let couponId = e.currentTarget.id;

  headers = {
    "X-CSRFToken": getCookie("csrftoken"),
  };

  Swal.fire({
    title: "Are you sure you want to remove this coupon",
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
        url: `/coupons/${couponId}`,
        headers: headers,
        success: function (response) {
          location.reload();
        },
        error: function (err) {
          console.log(err.responseJSON);
        },
      });
    }
  });
});
