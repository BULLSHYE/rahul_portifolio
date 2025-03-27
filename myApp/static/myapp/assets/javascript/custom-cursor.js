document.addEventListener("DOMContentLoaded", function () {
  const cursor = document.querySelector(".cursor");
  const iframeContainers = document.querySelectorAll(".iframe-container");

  if (cursor && iframeContainers.length > 0) {
    iframeContainers.forEach((iframeContainer) => {
      iframeContainer.addEventListener("mouseenter", () => {
        cursor.style.opacity = "0"; // Hide cursor
      });

      iframeContainer.addEventListener("mouseleave", () => {
        cursor.style.opacity = "1"; // Show cursor
      });
    });
  }
});
