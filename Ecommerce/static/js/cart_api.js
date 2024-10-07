/*
 handling:
    - removing cart items from the table.
    - updating the quantity of a certain item
*/

const cartItems = document.querySelectorAll("#cart-item");

cartItems.forEach((item) => {
  const removeBtn = item.querySelector("#remove-btn");
  const updateQuantitybtn = item.querySelector("#update-quantity-btn");
  const removeItemEndpoint = item.dataset.removeCartItemUrl;
  const updateQuantityEndpoint = item.dataset.updateQuantityUrl;
  removeBtn.addEventListener("click", () => {
    const options = {
      method: "POST",
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

/*
handling coupon input:
  - valid coupon
  - invlaid coupon
  - loadin coupon
*/

const couponForm = document.getElementById("coupon-form");
const couponInput = couponForm.querySelector("#coupon-input");
const couponApplyBtn = couponForm.querySelector("#coupon-apply-btn");
const couponTextResult = document.getElementById("coupon-text-result");
const couponAppliedResult = document.querySelector("#coupon-applied-result");
const couponChangeEndpoint = couponInput.dataset.couponChangeUrl;
const couponApplyEndpoint = couponApplyBtn.dataset.couponApplyUrl;
let validCoupon = false;

couponInput.addEventListener("input", () => {
  displyCouponLoadingText();
  const endpoint = `${couponChangeEndpoint}?coupon=${couponInput.value}`;
  const options = {
    method: "GET",
    headers: {
      "Content-type": "application/json",
      "X-CSRFToken": CSRF_TOKEN,
      mode: "same-origin",
    },
  };
  sendRequest(endpoint, options).then((result) => {
    displyCouponTextResult(result.data, result.status);
  });
});

couponApplyBtn.addEventListener("click", () => {
  if (!validCoupon) {
    return;
  }
  const body = { coupon: couponInput.value };
  const options = {
    method: "POST",
    headers: {
      "Content-type": "application/json",
      "X-CSRFToken": CSRF_TOKEN,
      mode: "same-origin",
    },
    body: JSON.stringify(body),
  };
  sendRequest(couponApplyEndpoint, options).then((result) => {
    if (result.status == 200) {
      couponApplied(couponInput.value);
    }
  });
});

/*
handling: 
  - creating invoice
  - show loading while fetching
*/

const payingConfirmationBtn = document.getElementById(
  "paying-confirmation-btn"
);
const payingConfirmationEndpoint =
  payingConfirmationBtn.dataset.createInvoiceUrl;

console.log(payingConfirmationBtn);
console.log(payingConfirmationEndpoint);

payingConfirmationBtn.addEventListener("click", () => {
  const options = {
    method: "POST",
    headers: {
      "Content-type": "application/json",
      "X-CSRFToken": CSRF_TOKEN,
      mode: "same-origin",
    },
  };
  sendRequest(payingConfirmationEndpoint, options);
});
