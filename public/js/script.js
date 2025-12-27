const toggle = document.getElementById('dark-mode-toggle');
if (toggle) {
    toggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        // Optional: Save preference to localStorage
        localStorage.setItem('theme', newTheme);
    });

    // Load saved theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    }
}

// Code Copy Button Logic
document.querySelectorAll('pre').forEach((prevBlock) => {
    const button = document.createElement('button');
    button.innerText = 'Copy';
    button.className = 'code-copy-btn';

    button.addEventListener('click', () => {
        const code = prevBlock.querySelector('code').innerText;
        navigator.clipboard.writeText(code).then(() => {
            button.innerText = 'Copied!';
            setTimeout(() => {
                button.innerText = 'Copy';
            }, 2000);
        });
    });

});
