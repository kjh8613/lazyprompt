// search.js - Global + Scoped Search Handler
(function () {
    const globalInput = document.getElementById('globalSearchInput');
    const sidebarTrigger = document.getElementById('sidebarSearchTrigger');
    const scopedInput = document.getElementById('scopedSearchInput');
    const postGrid = document.querySelector('.post-grid');

    if (!globalInput && !scopedInput) return;

    // Global Search (Homepage)
    if (globalInput) {
        // Capture initial HTML for restoration
        const initialHTML = postGrid ? postGrid.innerHTML : '';
        const initialPagination = document.querySelector('.pagination');

        // Toggle pagination visibility
        const togglePagination = (show) => {
            if (initialPagination) initialPagination.style.display = show ? 'flex' : 'none';
        }

        let posts = [];
        const debugMsg = document.createElement('div');
        debugMsg.style.cssText = "text-align:center; font-size:12px; color:gray; margin-top:5px;";
        globalInput.parentNode.appendChild(debugMsg);
        debugMsg.innerText = "Loading search index...";

        // FETCH APPROACH ONLY
        fetch('/index.json')
            .then(res => {
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                return res.json();
            })
            .then(data => {
                posts = data;
                debugMsg.style.color = "green";
                debugMsg.innerText = `System: Ready. ${posts.length} prompts loaded.`;
                setTimeout(() => debugMsg.remove(), 3000);
            })
            .catch(e => {
                debugMsg.style.color = "red";
                debugMsg.innerText = `System Error: ${e.message}`;
                console.error("Search index load failed:", e);
            });

        // Perform Search Function
        function performSearch(shouldScroll) {
            const query = globalInput.value.trim().toLowerCase();

            // If query is empty, restore original content
            if (query.length === 0) {
                if (postGrid) postGrid.innerHTML = initialHTML;
                togglePagination(true);
                return;
            }

            togglePagination(false);

            const results = posts.filter(post =>
                post.title.toLowerCase().includes(query) ||
                post.summary.toLowerCase().includes(query)
            );

            if (!postGrid) return;

            if (results.length === 0) {
                postGrid.innerHTML = '<p style="text-align: center; color: #777;">No prompts found matching your query.</p>';
            } else {
                postGrid.innerHTML = results.map(post => `
                    <a href="${post.permalink}" class="card">
                        ${post.image ? `<div class="card-img"><img src="${post.image}" alt="${post.title}"></div>` : ''}
                        <div class="card-body">
                            <h3>${post.title}</h3>
                            <p>${post.summary}</p>
                            <span class="date">${post.date}</span>
                        </div>
                    </a>
                `).join('');
            }

            if (shouldScroll) {
                postGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }

        // Event: input (live search, no scroll)
        globalInput.addEventListener('input', () => performSearch(false));

        // Event: Enter key (scroll)
        globalInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                performSearch(true);
            }
        });

        // Sidebar Search Icon Trigger
        if (sidebarTrigger) {
            sidebarTrigger.addEventListener('click', (e) => {
                e.preventDefault();
                globalInput.focus();
                globalInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            });
        }
    }

    // Scoped Search (Category Pages)
    if (scopedInput && postGrid) {
        const allCards = Array.from(postGrid.querySelectorAll('.card'));

        scopedInput.addEventListener('input', () => {
            const query = scopedInput.value.trim().toLowerCase();

            if (query.length === 0) {
                allCards.forEach(card => card.style.display = '');
                return;
            }

            allCards.forEach(card => {
                const title = card.querySelector('h3')?.innerText.toLowerCase() || '';
                const summary = card.querySelector('p')?.innerText.toLowerCase() || '';
                card.style.display = (title.includes(query) || summary.includes(query)) ? '' : 'none';
            });
        });

        scopedInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                postGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    }
})();
