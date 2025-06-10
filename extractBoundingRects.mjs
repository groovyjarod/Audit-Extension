export default function extractBoundingRects(report) {
    const results = []

    for (const key in report) {
        const audit = report[key]
        if (!audit.items) continue

        audit.items.forEach(item => {
            if (item.boundingRect) {
                results.push({
                    boundingRect: item.boundingRect,
                    explanation: audit.title || key
                })
            }

            if (item.subItems?.items) {
                items.subItems.items.forEach(sub => {
                    if (sub.relatedNode?.boundingRect) {
                        results.push({
                            boundingRect: sub.relatedNode.boundingRect,
                            explanation: audit.title || key
                        })
                    }
                })
            }
        })
    }

    return results
}