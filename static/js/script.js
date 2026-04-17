// Check that the JavaScript file is properly linked and running.

document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is connected');
});

// Make project cards clickable and open the live demo link
// Prevents opening a second link if the user clicks an anchor tag inside the card

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

// Fade in page element as they appear on screen while scrolling

document.addEventListener('DOMContentLoaded',
     () => {
    const faders = 
    document.querySelectorAll('.fade-in');

        // Observe elements with the fade-in class and reveal them when they enter the viewport

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
     
// Toggle dark mode and save the users theme preference in local storage

     const toggleBtn = document.getElementById('darkModeToggle');
     if (toggleBtn) {
         toggleBtn.addEventListener('click', () => {
             document.body.classList.toggle('dark-mode');

// Apply saved dark mode preference when the page reloads

             if (document.body.classList.contains('dark-mode')) {
                 localStorage.setItem('theme', 'dark');
             } else {
                 localStorage.setItem('theme', 'light');
             }
         });    }

         if (localStorage.getItem('theme') === 'dark') {
             document.body.classList.add('dark-mode');
         }

// Select project search inputs, filter buttons, and all project cards

         const searchInput = 
            document.getElementById('projectSearch');
const filterButtons = 
document.querySelectorAll('.filter-btn');
const projectCards = 
document.querySelectorAll('.project-card');

let activeFilter = 'All';

// Filter projects based on search text and selected category
// Also shows a message if no matching projects are found

function filterProjects() {
    const searchText = searchInput ? searchInput.value.toLowerCase() : '';
    let visibleCount = 0;

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
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });
    const noResults = document.getElementById('noResults');
if (noResults) {
    noResults.style.display = visibleCount === 0 ? 'block' : 'none';
}
}

// Run filtering whenever the user types in the search box

if (searchInput) {
    searchInput.addEventListener('input', filterProjects);
}

// Update the active category filter when a filter button is clicked

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        activeFilter = button.getAttribute('data-filter');
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        filterProjects();
    });
});        



