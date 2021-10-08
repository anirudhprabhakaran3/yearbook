//script for navbar functionality in mobile version
const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector(".navbar");
const navbarLinks = document.querySelector(".navbar__links");
hamburger.addEventListener("click", () => {
  if (hamburger.classList.contains("hamburger-open")) {
    hamburger.classList.remove("hamburger-open");
    navbar.classList.remove("no-border-radius");
    navbarLinks.classList.remove("mobile_links");
    document.body.classList.remove("no-scroll");
  } else {
    hamburger.classList.add("hamburger-open");
    navbar.classList.add("no-border-radius");
    navbarLinks.classList.add("mobile_links");
    document.body.classList.add("no-scroll");
  }
});
