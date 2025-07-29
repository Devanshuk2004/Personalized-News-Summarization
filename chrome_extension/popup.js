document.getElementById("summarizeBtn").addEventListener("click", async () => {
  document.getElementById("output").innerText = "Fetching text from page...";

  // Get page text using content script
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript(
      {
        target: { tabId: tabs[0].id },
        func: () => document.body.innerText  // Extract all text from the page
      },
      async (results) => {
        const pageText = results[0].result;

        document.getElementById("output").innerText = "Sending to API...";
        
        // Send to your FastAPI backend
        try {
          const response = await fetch("http://127.0.0.1:8002/analyze_news", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: pageText, max_length: 150, min_length: 30 })
          });

          if (!response.ok) throw new Error("API error");

          const data = await response.json();
          document.getElementById("output").innerText =
            `Summary:\n${data.summary}\n\nBias:\nFavorable: ${data.bias_scores.favorable_bias}\nUnfavorable: ${data.bias_scores.unfavorable_bias}`;
        } catch (err) {
          document.getElementById("output").innerText = "Error: " + err.message;
        }
      }
    );
  });
});
