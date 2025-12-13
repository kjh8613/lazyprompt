document.addEventListener('DOMContentLoaded', async () => {
    // 1. Sidebar Trigger Logic (Fixed)
    const sidebarTrigger = document.getElementById('sidebarSearchTrigger');
    if (sidebarTrigger) {
        sidebarTrigger.addEventListener('click', (e) => {
            e.preventDefault();
            const homeInput = document.getElementById('searchInput'); // Global on Home
            // If we are on homepage
            if (homeInput) {
                homeInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
                setTimeout(() => homeInput.focus(), 500);
            } else {
                // If on other page, decide: redirect to home search OR focus category search if exists?
                // Request says "Search in Category". But sidebar "Search" usually implies Global Site Search.
                // Let's redirect to Home for global search as per standard UX.
                window.location.href = '/#searchInput';
            }
        });
    }

    // 2. Global Search (Homepage)
    const globalInput = document.getElementById('searchInput');
    const postGrid = document.getElementById('postGrid');

    if (globalInput && postGrid) {
        let posts = [];
        try {
            const res = await fetch('/index.json');
            if (res.ok) posts = await res.json();
        } catch (e) { console.error("Search Index Error", e); }

        // Function: Perform Search
        const performSearch = (shouldScroll = false) => {
            const query = globalInput.value.toLowerCase();
            const filtered = posts.filter(post =>
                post.title.toLowerCase().includes(query) ||
                post.summary.toLowerCase().includes(query)
            );
            renderGlobalPosts(filtered, postGrid);

            // Scroll to results ONLY if explicitly requested (e.g. Enter pressed)
            if (shouldScroll && query.length > 0) {
                postGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        };

        // Event: Typing (Real-time) - NO SCROLL
        globalInput.addEventListener('input', () => performSearch(false));

        // Event: Enter Key - SCROLL
        globalInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                performSearch(true);
                globalInput.blur(); // Dismiss keyboard on mobile
            }
        });

        // Event: Click Search Icon - SCROLL
        const searchBtn = document.querySelector('.search-icon-btn');
        if (searchBtn) {
            searchBtn.addEventListener('click', () => performSearch(true));
        }
    }

    // 3. Scoped Search (Category Pages) - Client Side Filtering of rendered cards
    // Since category pages already have the posts rendered, we don't need to fetch JSON.
    // We can just filter the DOM elements for instant speed.
    const categoryInput = document.getElementById('categorySearchInput');
    const categoryGrid = document.getElementById('categoryPostGrid');

    if (categoryInput && categoryGrid) {
        const cards = Array.from(categoryGrid.getElementsByClassName('card'));

        categoryInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();

            cards.forEach(card => {
                const title = card.getAttribute('data-title') || "";
                const summary = card.getAttribute('data-summary') || "";

                if (title.includes(query) || summary.includes(query)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    function renderGlobalPosts(results, container) {
        container.innerHTML = '';
        if (results.length === 0) {
            container.innerHTML = '<p class="no-results" style="text-align:center; color:#888;">No prompts found matching your query.</p>';
            return;
        }
        results.forEach(post => {
            // Reconstruct Card HTML
            const article = document.createElement('article');
            article.className = 'card';
            let imageHtml = post.image ? `<div class="card-image" style="background-image: url('${post.image}');"></div>` : '';
            article.innerHTML = `
                <a href="${post.permalink}">
                    ${imageHtml}
                    <div class="card-content">
                        <h3>${post.title}</h3>
                        <p>${post.summary ? post.summary.substring(0, 100) + '...' : ''}</p>
                        <span class="date">${post.date}</span>
                    </div>
                </a>
            `;
            container.appendChild(article);
        });
    }
});
