module.exports = {
  content: ['./index.html', './en/index.html'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#0066ff',
        secondary: '#161B25',
        ctaGradientStart: '#176ae5',
        ctaGradientEnd: '#0066ff',
      },
      keyframes: {
        fadeInUp: {
          "0%": {
            opacity: "0",
            transform: "translate3d(0, 5vh, 0)",
          },
          "100%": {
            opacity: "1",
            transform: "translateZ(0)",
          },
        },
      },
      animation: {
        fadeInUp: 'fadeInUp 1s ease-in-out',
      },
      fontFamily: {
        fa: ['Vazirmatn RD VF', 'Vazirmatn RD'],
      },
    },
  },
  plugins: [],
};
