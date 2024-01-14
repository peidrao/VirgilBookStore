def create_book_payload(request):
    is_publish = True if request.data.get("is_publish") == "on" else False
    amount = 0 if request.data.get("amount") == "" else int(request.data.get("amount"))

    data = {
        "writer": int(request.data.get("writer", None)),
        "genre": int(request.data.get("genre", None)),
        "title": request.data.get("title"),
        "description": request.data.get("description"),
        "price": request.data.get("price"),
        "keywords": request.data.get("keywords"),
        "amount": amount,
        "is_publish": is_publish,
    }
    return data
