function displyCouponTextResult(data, status) {
  couponTextResult.classList.remove("loading-coupon-text");
  if (status == 200) {
    validCoupon = true;
    couponInput.classList.add("border-green-500");
    couponInput.classList.remove("border-red-500");
    couponTextResult.classList.remove("invalid-coupon-text");
    couponTextResult.classList.add("valid-coupon-text");
  } else {
    validCoupon = false;
    couponInput.classList.remove("border-green-500");
    couponInput.classList.add("border-red-500");
    couponTextResult.classList.remove("valid-coupon-text");
    couponTextResult.classList.add("invalid-coupon-text");
  }
  couponTextResult.textContent = data.detail;
}

function displyCouponLoadingText() {
  couponTextResult.classList.remove("valid-coupon-text");
  couponTextResult.classList.remove("invalid-coupon-text");
  couponTextResult.classList.add("loading-coupon-text");
  couponTextResult.textContent = "validating coupon...";
}

function couponApplied(couponName, couponDiscount) {
  couponAppliedResult.innerHTML = `Coupon <span class="text-green-500" >${couponName}</span> Applied Successfully!`;
  const ParentElement = document.getElementById("parent-element");
  // const AlpineData = ParentElement.__x.$data;
  console.log(Alpine.data("couponDiscount", () => {}));
  console.log(ParentElement.getAttribute("x-data"));
  AlpineData.couponDiscount = result.data.coupon;
  couponApplyBtn.__x.updateElements(couponApplyBtn);
}
