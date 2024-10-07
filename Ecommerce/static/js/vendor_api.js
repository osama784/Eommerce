const products = document.querySelectorAll("#product");

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-CSRFToken": CSRF_TOKEN,
    mode: "same-origin",
  },
};

products.forEach((product) => {
  const createOrRemoveCartItemEndpoint =
    product.dataset.createOrRemoveCartItemUrl;
  const createOrRemoveWishlistItemEndpoint =
    product.dataset.createOrRemoveWishlistItemUrl;
  const createOrRemoveCartItemBtn = product.querySelector(
    "#create-or-remove-cart-item-btn"
  );
  const createOrRemoveWishlistItemBtn = product.querySelector(
    "#create-or-remove-wishlist-item-btn"
  );

  createOrRemoveCartItemBtn.addEventListener("click", () => {
    sendRequest(createOrRemoveCartItemEndpoint, options);
  });
  createOrRemoveWishlistItemBtn.addEventListener("click", () => {
    sendRequest(createOrRemoveWishlistItemEndpoint, options);
  });
});
