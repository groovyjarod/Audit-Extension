document.getElementById('fileInput').addEventListener('change', async (e) => {
    const file = e.target.files[0]
    if (!file) return
    const text = await file.text()
    const report = JSON.parse(text)

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { type: 'LOAD_REPORT', report })
    })
})