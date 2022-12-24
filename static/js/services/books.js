$(".remove-book").on("click", (e) => {
  e.preventDefault();
  let book_id = e.currentTarget.id;
  console.log(book_id);
});
