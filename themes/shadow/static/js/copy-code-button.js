// https://github.com/dguo/dannyguo.com/blob/main/content/blog/how-to-add-copy-to-clipboard-buttons-to-code-blocks-in-hugo.md

function addCopyButtons(clipboard) {
    document.querySelectorAll('pre > code').forEach(function (codeBlock) {
        var button = document.createElement('button');
        button.className = 'copy-code-button';
        button.type = 'button';
        button.innerText = '📎 Copy';

        button.addEventListener('click', function () {
            var codeBlockCopy = Object.entries(codeBlock.children).filter( ([key, span]) => span.className != 'ln').map( ([key, span]) => { return span });
            var domElements = [];
            codeBlockCopy.forEach((node) => {
                node.className == 'hl' ? 
                    domElements.push(
                        ... Object.entries(node.children)
                        .filter( ([_, span]) => span.className != 'ln')
                        .map( ([_, span]) => { return span.innerText })
                    ) : 
                    domElements.push(
                        node.innerText
                    );
            });
            var codeContent = domElements.join("");

            clipboard.writeText(codeContent).then(function () {
                /* Chrome doesn't seem to blur automatically,
                   leaving the button in a focused state. */
                button.blur();

                button.innerText = '🦸 Copied!';

                setTimeout(function () {
                    button.innerText = '📎 Copy';
                }, 2000);
            }, function (error) {
                button.innerText = 'Error';
                console.error(error);
            });
        });
        var pre = codeBlock.parentNode;
        if (pre.parentNode.classList.contains('highlight')) {
            var highlight = pre.parentNode;
            highlight.parentNode.insertBefore(button, highlight);
        } else {
            pre.parentNode.insertBefore(button, pre);
        }
    });
}

if (navigator && navigator.clipboard) {
    addCopyButtons(navigator.clipboard);
} else {
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/clipboard-polyfill/2.7.0/clipboard-polyfill.promise.js';
    script.integrity = 'sha256-waClS2re9NUbXRsryKoof+F9qc1gjjIhc2eT7ZbIv94=';
    script.crossOrigin = 'anonymous';
    script.onload = function() {
        addCopyButtons(clipboard);
    };

    document.body.appendChild(script);
}