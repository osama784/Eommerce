function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const ORIGIN_SITE = window.location.origin;
const CSRF_TOKEN = getCookie("csrftoken");

// standard function for sending requests
function sendRequest(endpoint, options) {
  fetch(endpoint, options)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

/*
 handling:
    - removing cart items from the table.
    - updating the quantity of a certain item
*/

const cartItems = document.querySelectorAll("#cart-item");

cartItems.forEach((item) => {
  const removeBtn = item.querySelector("#remove-btn");
  const updateQuantitybtn = item.querySelector("#update-quantity-btn");
  const removeItemEndpoint = ORIGIN_SITE + item.dataset.removeCartItemUrl;
  const updateQuantityEndpoint = ORIGIN_SITE + item.dataset.updateQuantityUrl;
  removeBtn.addEventListener("click", () => {
    const options = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": CSRF_TOKEN,
        mode: "same-origin",
      },
    };
    sendRequest(removeItemEndpoint, options);
  });

  updateQuantitybtn.addEventListener("click", () => {
    const quantity = item.querySelector("#quantity").value;
    const data = {
      quantity: quantity,
    };
    const options = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": CSRF_TOKEN,
        mode: "same-origin",
      },
      body: JSON.stringify(data),
    };
    sendRequest(updateQuantityEndpoint, options);
  });
});

const clearCartBtn = document.querySelector("#clear-cart-btn");

clearCartBtn.addEventListener("click", () => {
  const clearCartEndpoint = clearCartBtn.dataset.clearCartUrl;
  const options = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": CSRF_TOKEN,
      mode: "same-origin",
    },
  };
  sendRequest(clearCartEndpoint, options);
});
