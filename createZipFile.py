import os
import zipfile

# File structure
file_structure = {
    "manifest.json": """{
        "name": "Accessibility Audit Highlighter",
        "version": "1.0",
        "manifest_version": 3,
        "permissions": ["scripting", "activeTab"],
    "action": {
        "default_popup": "popup.html"
    },
    "content_scripts": [
        {
        "matches": ["<all_urls>"],
        "js": ["content.js"]
        }
    ]
}""",

    "popup.html": """<!DOCTYPE html>
<html>
  <head>
    <title>Audit Loader</title>
    <style>
      body { font-family: Arial, sans-serif; padding: 10px; }
      input { margin-top: 10px; }
    </style>
  </head>
  <body>
    <h3>Load Audit JSON</h3>
    <input type="file" id="fileInput" accept=".json" />
    <script src="popup.js" type="module"></script>
  </body>
</html>
""",

    "popup.js": """document.getElementById('fileInput').addEventListener('change', async (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const text = await file.text();
  const report = JSON.parse(text);

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { type: 'LOAD_REPORT', report });
  });
});
""",

    "content.js": """function drawOverlay(rect, label = "Issue") {
  const overlay = document.createElement('div');
  overlay.textContent = label;

  Object.assign(overlay.style, {
    position: 'absolute',
    top: `${rect.top}px`,
    left: `${rect.left}px`,
    width: `${rect.width}px`,
    height: `${rect.height}px`,
    backgroundColor: 'rgba(255, 0, 0, 0.2)',
    border: '2px dashed red',
    zIndex: 9999,
    color: '#000',
    fontSize: '12px',
    padding: '2px',
    pointerEvents: 'none'
  });

  document.body.appendChild(overlay);
}

function extractBoundingRects(report) {
  const results = [];

  for (const key in report) {
    const audit = report[key];
    if (!audit.items) continue;

    audit.items.forEach(item => {
      if (item.boundingRect) {
        results.push({
          boundingRect: item.boundingRect,
          explanation: audit.title || key
        });
      }

      if (item.subItems?.items) {
        item.subItems.items.forEach(sub => {
          if (sub.relatedNode?.boundingRect) {
            results.push({
              boundingRect: sub.relatedNode.boundingRect,
              explanation: audit.title || key
            });
          }
        });
      }
    });
  }

  return results;
}

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === 'LOAD_REPORT') {
    const items = extractBoundingRects(msg.report);
    items.forEach(({ boundingRect, explanation }) => {
      drawOverlay(boundingRect, explanation);
    });
  }
});
"""
}

# Create zip file
zip_path = "/mnt/data/audit-highlighter-extension.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for filename, content in file_structure.items():
        zipf.writestr(filename, content)

zip_path
