/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/templates/**/*.html',
    './src/templates/foods/index.html',
    './src/templates/**/**/**/*.html',
    './src/static/**/*.js',
    './src/**/*.py'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

