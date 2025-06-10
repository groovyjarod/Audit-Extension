import extractBoundingRects from "./extractBoundingRects.mjs"

function drawOverlay (rect, label='issue') {
    const overlay = document.createElement('div')
    overlay.textContent = label
    Object.assign(overlay.style, {
        position: 'absolute',
        top: `${rect.top}px`,
        left: `${rect.left}px`,
        width: `${rect.width}px`,
        height: `${rect.height}px`,
        backgroundColor: `rgba(255, 0, 0, 0.2)`,
        border: '2px dashed red',
        zIndex: 9999,
        color: '#000',
        fontSize: '12px',
        padding: '2px',
        pointerEvents: 'none'
    })

    document.body.appendChild(overlay)
}

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    if (msg.type === 'LOAD_REPORT') {
        const items = extractBoundingRects(msg.report)
        items.forEach(({ boundingRect, explanation }) => {
            drawOverlay(boundingRect, explanation)
        })
    }
})