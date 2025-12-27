const toggle = document.getElementById('dark-mode-toggle');
if (toggle) {
    const sunIcon = toggle.querySelector('.sun-icon');
    const moonIcon = toggle.querySelector('.moon-icon');

    const updateIcons = (theme) => {
        if (theme === 'dark') {
            sunIcon.style.display = 'block';
            moonIcon.style.display = 'none';
        } else {
            sunIcon.style.display = 'none';
            moonIcon.style.display = 'block';
        }
    };

    toggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcons(newTheme);
    });

    // Load saved theme
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateIcons(savedTheme);
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
