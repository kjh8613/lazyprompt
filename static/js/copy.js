document.addEventListener('DOMContentLoaded', () => {
    // Select all code blocks (pre tags)
    const codeBlocks = document.querySelectorAll('pre');

    codeBlocks.forEach((pre) => {
        // Create the copy button
        const button = document.createElement('button');
        button.className = 'copy-btn';
        button.innerText = 'Copy';
        button.setAttribute('aria-label', 'Copy code to clipboard');

        // Logic to copy text
        button.addEventListener('click', async () => {
            const code = pre.querySelector('code');
            const text = code ? code.innerText : pre.innerText;

            try {
                await navigator.clipboard.writeText(text);
                
                // Visual feedback
                button.innerText = 'Copied!';
                button.classList.add('copied');
                
                // Reset after 2 seconds
                setTimeout(() => {
                    button.innerText = 'Copy';
                    button.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Failed to copy!', err);
                button.innerText = 'Error';
            }
        });

        // Wrap pre in a container relative positioning (if not already handled by css)
        // But simply appending to pre works if pre is position: relative
        pre.appendChild(button);
    });
});
