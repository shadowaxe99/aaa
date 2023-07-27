```javascript
// Theme options
const themes = {
    light: {
        '--background-color': '#ffffff',
        '--text-color': '#000000'
    },
    dark: {
        '--background-color': '#000000',
        '--text-color': '#ffffff'
    },
    // Add more themes here
};

// Function to change theme
function changeTheme(themeName) {
    const theme = themes[themeName];
    if (!theme) {
        console.error(`Theme "${themeName}" does not exist.`);
        return;
    }

    for (let property in theme) {
        document.documentElement.style.setProperty(property, theme[property]);
    }
}

// Event listener for theme selection
document.getElementById('theme-selection').addEventListener('change', function() {
    changeTheme(this.value);
});
```