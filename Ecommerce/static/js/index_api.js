const products = document.querySelectorAll("#product");

products.forEach((product) => {
  const createOrRemoveCartItemEndpoint =
    product.dataset.createOrRemoveCartItemUrl;
  const createOrRemoveWishlistItemEnpoint =
    product.dataset.createOrRemoveWishlistItemUrl;
  const addToCartBtn = product.querySelector("#add-to-cart-btn");
  const addToWishlistBtns = product.querySelectorAll("#add-to-wishlist-btn");

  let addedToCart = product.dataset.addedToCart;

  addToCartBtn.addEventListener("click", () => {
    if (addedToCart == "True") return;
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": CSRF_TOKEN,
        mode: "same-origin",
      },
    };

    sendRequest(createOrRemoveCartItemEndpoint, options).then((result) => {
      if (result.status == 201) {
        addedToCart = "True";
      }
    });
  });

  addToWishlistBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": CSRF_TOKEN,
          mode: "same-origin",
        },
      };
      sendRequest(createOrRemoveWishlistItemEnpoint, options);
    });
  });
});
