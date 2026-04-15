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


document.addEventListener('DOMContentLoaded',
     () => {
    const faders = 
    document.querySelectorAll('.fade-in');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

faders.forEach(el => observer.observe(el));
     });
     

     const toggleBtn = document.getElementById('darkModeToggle');
     if (toggleBtn) {
         toggleBtn.addEventListener('click', () => {
             document.body.classList.toggle('dark-mode');
             if (document.body.classList.contains('dark-mode')) {
                 localStorage.setItem('theme', 'dark');
             } else {
                 localStorage.setItem('theme', 'light');
             }
         });    }

         if (localStorage.getItem('theme') === 'dark') {
             document.body.classList.add('dark-mode');
         }


         const searchInput = 
            document.getElementById('projectSearch');


               