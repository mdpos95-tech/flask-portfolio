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
const filterButtons = 
document.querySelectorAll('.filter-btn');
const projectCards = 
document.querySelectorAll('.project-card');

let activeFilter = 'All';

function filterProjects() {
    const searchText = searchInput ? searchInput.value.toLowerCase() : '';

    projectCards.forEach(card => {
        const category = 
        card.getAttribute('data-category');
        const title = 
        (card.getAttribute('data-title') || '').toLowerCase();
        const description =
        (card.getAttribute('data-description') || '').toLowerCase();

        const tech = 
        (card.getAttribute('data-tech') || '').toLowerCase();
        const matchesFilter = activeFilter === 'All' || category === activeFilter || 
        tech.includes(activeFilter.toLowerCase());
        const matchesSearch = title.includes(searchText) || description.includes(searchText) || tech.includes(searchText);

        if (matchesFilter && matchesSearch) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

if (searchInput) {
    searchInput.addEventListener('input', filterProjects);
}
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        activeFilter = button.getAttribute('data-filter');
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        filterProjects();
    });
});        