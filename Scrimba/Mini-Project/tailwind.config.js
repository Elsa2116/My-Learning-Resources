// tailwind.config.js
module.exports = {
  content: ["./*.html"], // Adjust to your HTML file paths
  theme: {
    screens: {
      sm: "480px",
      md: "768px",
      lg: "976",
      xl: "1440",
    },
    extend: {
      colors: {
        strongCyan: "hsl(171,66%,44%)",
        lightBlue: "hsl(233,1005,6950)",
        grayishBlue: "hsl(201,11%,66%)",
        darkGrayishBlue: "hsl(210,105,33%)",
      },
      fontFamily: {
        sans: ["Bai Jamjuree", "sans-serif"],
      },
    },
  },
  plugins: [],
};
