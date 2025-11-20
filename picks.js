// My Picks Page JavaScript

// Expand/collapse thoughts in recent picks cards
document.querySelectorAll('.expand-btn').forEach(button => {
    button.addEventListener('click', function() {
        const card = this.closest('.pick-card');
        const thoughts = card.querySelector('.pick-thoughts');

        if (thoughts.classList.contains('hidden')) {
            thoughts.classList.remove('hidden');
            this.textContent = 'Less ↑';
        } else {
            thoughts.classList.add('hidden');
            this.textContent = 'More →';
        }
    });
});

// Expand/collapse thoughts in table rows
document.querySelectorAll('.expand-thoughts-btn').forEach(button => {
    button.addEventListener('click', function() {
        const row = this.closest('.table-row');
        const thoughts = row.querySelector('.row-thoughts');

        if (thoughts.classList.contains('hidden')) {
            thoughts.classList.remove('hidden');
            this.textContent = 'Less ↑';
        } else {
            thoughts.classList.add('hidden');
            this.textContent = 'More →';
        }
    });
});

// Filter functionality
const filterButtons = document.querySelectorAll('.filter-btn');
const tableRows = document.querySelectorAll('.table-row');

filterButtons.forEach(button => {
    button.addEventListener('click', function() {
        // Update active button
        filterButtons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');

        const filter = this.getAttribute('data-filter');

        // Filter rows
        tableRows.forEach(row => {
            const medium = row.getAttribute('data-medium');

            if (filter === 'all' || medium === filter) {
                row.style.display = 'block';
            } else {
                row.style.display = 'none';
            }
        });
    });
});
