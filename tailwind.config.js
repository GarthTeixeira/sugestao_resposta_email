/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./api/templates/**/*.{html,js}"],
  output: "./api/static/css/output.css",
  theme: {
    extend: {
      fontFamily: {
        sans: ['Roboto', 'ui-sans-serif', 'system-ui'], 
        grotesk: ['Space Grotesk', 'sans-serif'], 
        orbitron: ['Orbitron', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

