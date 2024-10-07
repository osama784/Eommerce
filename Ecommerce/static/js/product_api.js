const product = document.getElementById("product");

const createOrRemoveCartItemEndpoint =
  product.dataset.createOrRemoveCartItemUrl;
const createOrRemoveWishlistItemEndpoint =
  product.dataset.createOrRemoveWishlistItemUrl;
const createOrRemoveCartItemBtn = product.querySelector(
  "#create-or-remove-cart-item-btn"
);
const createOrRemoveWishlitItemBtn = product.querySelector(
  "#create-or-remove-wishlist-item-btn"
);

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

createOrRemoveWishlitItemBtn.addEventListener("click", () => {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": CSRF_TOKEN,
      mode: "same-origin",
    },
  };
  sendRequest(createOrRemoveWishlistItemEndpoint, options);
});

const createReviewForm = document.getElementById("create-review-form");

if (createReviewForm) {
  const createReviewEndpoint = createReviewForm.dataset.createReviewUrl;
  createReviewForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = {
      rating: createReviewForm.rating.value,
      body: createReviewForm.body.value,
    };
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": CSRF_TOKEN,
        mode: "same-origin",
      },
      body: JSON.stringify(data),
    };
    sendRequest(createReviewEndpoint, options);
  });
}
