document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is connected');
});

document.querySelectorAll(".project-card").forEach(card => {
    const link = 
    card.getAttribute("data-link");
    if (link) {
        card.style.cursor = "pointer";
        card.addEventListener("click", (e) => {
            if (e.target.tagName === "A")
                return;
            window.open(link, "_blank");
        });
            
            }
});