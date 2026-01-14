// Simple animation on scroll
window.addEventListener("scroll", () => {
  document.querySelectorAll(".feature").forEach(feature => {
    const position = feature.getBoundingClientRect().top;
    if (position < window.innerHeight - 100) {
      feature.style.transform = "translateY(0)";
      feature.style.opacity = "1";
    }
  });
});
document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();
  alert("Thank you! Your message has been sent.");
  this.reset();
});
