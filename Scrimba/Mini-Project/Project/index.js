//  JavaScript for Loopstudios Clone

//  Menu Toggle
const menuButton = document.getElementById("menu-button");
const closeMenuButton = document.getElementById("close-menu-button");
const menuOverlay = document.getElementById("menu-overlay");

menuButton.addEventListener("click", () => {
  menuOverlay.classList.add("active");
  document.body.style.overflow = "hidden"; // Prevent scrolling
});

closeMenuButton.addEventListener("click", () => {
  menuOverlay.classList.remove("active");
  document.body.style.overflow = ""; // Restore scrolling
});
