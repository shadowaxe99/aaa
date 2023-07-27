```javascript
function checkScreenSize() {
    var chatInterface = document.getElementById('chatInterface');
    var codeOutputArea = document.getElementById('codeOutputArea');

    if (window.innerWidth <= 768) {
        chatInterface.style.width = "100%";
        codeOutputArea.style.width = "100%";
    } else {
        chatInterface.style.width = "50%";
        codeOutputArea.style.width = "50%";
    }
}

window.addEventListener('resize', checkScreenSize);
window.addEventListener('load', checkScreenSize);
```