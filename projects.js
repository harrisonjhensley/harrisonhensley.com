// Projects Page JavaScript

// Expand/collapse full text for each project
document.querySelectorAll('.expand-text-btn').forEach(button => {
    button.addEventListener('click', function() {
        const card = this.closest('.project-card');
        const fullText = card.querySelector('.project-full-text');

        if (fullText.classList.contains('hidden')) {
            fullText.classList.remove('hidden');
            this.textContent = 'Hide Info ↑';
        } else {
            fullText.classList.add('hidden');
            this.textContent = 'More Info';
            // Scroll back to the top of the card when collapsing
            card.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Search functionality
let currentSearchTerm = '';

// Search input
const searchInput = document.getElementById('searchInput');
if (searchInput) {
    searchInput.addEventListener('input', function() {
        currentSearchTerm = this.value.toLowerCase();
        applyFilters();
    });
}

// Apply search filter
function applyFilters() {
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        const title = card.querySelector('h2').textContent.toLowerCase();
        const summary = card.querySelector('.project-summary').textContent.toLowerCase();
        const metaTags = Array.from(card.querySelectorAll('.meta-tag')).map(tag => tag.textContent.toLowerCase());

        // Check search term
        let searchMatch = currentSearchTerm === '' ||
                         title.includes(currentSearchTerm) ||
                         summary.includes(currentSearchTerm) ||
                         metaTags.some(tag => tag.includes(currentSearchTerm));

        // Show/hide card based on search
        if (searchMatch) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}
