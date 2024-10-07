const wishlistItems = document.querySelectorAll("#wishlist-item");

wishlistItems.forEach((item) => {
  const createOrRemoveCartItemEndpoint = item.dataset.createOrRemoveCartItemUrl;
  const createOrRemoveCartItemBtn = item.querySelector(
    "#create-or-remove-cart-item-btn"
  );
  const removeWishlistItemEndpoint = item.dataset.removeWishlistItemUrl;
  const removeWishlistItemBtn = item.querySelector("#remove-wishlist-item-btn");

  createOrRemoveCartItemBtn.addEventListener("click", () => {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": CSRF_TOKEN,
        mode: "same-origin",
      },
    };
    sendRequest(createOrRemoveCartItemEndpoint, options);
  });

  removeWishlistItemBtn.addEventListener("click", () => {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": CSRF_TOKEN,
        mode: "same-origin",
      },
    };
    sendRequest(removeWishlistItemEndpoint, options);
  });
});

const clearWishlistBtn = document.getElementById("clear-wishlist-btn");
const clearWishlistEndpoint = clearWishlistBtn.dataset.clearWishlistUrl;

clearWishlistBtn.addEventListener("click", () => {
  const options = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": CSRF_TOKEN,
      mode: "same-origin",
    },
  };
  sendRequest(clearWishlistEndpoint, options);
});
