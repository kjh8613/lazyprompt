document.addEventListener('DOMContentLoaded', async () => {
    const searchInput = document.getElementById('searchInput');
    const postGrid = document.getElementById('postGrid');

    if (!searchInput || !postGrid) return;

    let posts = [];

    // Fetch the JSON index
    try {
        const res = await fetch('/index.json');
        if (!res.ok) throw new Error('Failed to fetch search index');
        posts = await res.json();
    } catch (err) {
        console.error(err);
        return; // Fail silently or show error
    }

    // Filter function
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();

        const filtered = posts.filter(post => {
            return post.title.toLowerCase().includes(query) ||
                post.summary.toLowerCase().includes(query);
        });

        renderPosts(filtered);
    });

    // Sidebar Search Trigger
    const sidebarTrigger = document.getElementById('sidebarSearchTrigger');
    if (sidebarTrigger) {
        sidebarTrigger.addEventListener('click', (e) => {
            e.preventDefault();
            // If on homepage, focus input
            if (searchInput) {
                searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
                setTimeout(() => searchInput.focus(), 500); // Wait for scroll
            } else {
                // If on another page, redirect to home (simple)
                window.location.href = '/#searchInput';
            }
        });
    }

    // Render function
    function renderPosts(results) {
        postGrid.innerHTML = ''; // Clear current

        if (results.length === 0) {
            postGrid.innerHTML = '<p class="no-results">No prompts found matching your query.</p>';
            return;
        }

        results.forEach(post => {
            const article = document.createElement('article');
            article.className = 'card';

            let imageHtml = '';
            if (post.image) {
                imageHtml = `<div class="card-image" style="background-image: url('${post.image}');"></div>`;
            }

            article.innerHTML = `
                <a href="${post.permalink}">
                    ${imageHtml}
                    <div class="card-content">
                        <h3>${post.title}</h3>
                        <p>${post.summary.substring(0, 100)}${post.summary.length > 100 ? '...' : ''}</p>
                        <span class="date">${post.date}</span>
                    </div>
                </a>
            `;
            postGrid.appendChild(article);
        });
    }
});
