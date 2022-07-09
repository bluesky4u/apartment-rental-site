/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'hero-background': "linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55)), url(~/assets/img/estate.jpg)",
      }
    },
  },
  plugins: [],
}
