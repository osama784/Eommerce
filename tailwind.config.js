/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./Ecommerce/**/*.{html,js}",
    // "./node_modules/tw-elements/js/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        body: ["Roboto"],
      },
    },
  },
  darkMode: "class",
};
