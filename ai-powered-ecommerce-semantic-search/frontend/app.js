const API_BASE_URL = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.querySelector(".searchBox .input");
  const searchButton = document.querySelector(".searchBox .search-logo");
  if (!searchInput || !searchButton) return;

  let resultsPanel = document.getElementById("ai-search-results");
  if (!resultsPanel) {
    resultsPanel = document.createElement("section");
    resultsPanel.id = "ai-search-results";
    resultsPanel.style.cssText = "max-width:1100px;margin:16px auto;padding:16px;background:#fff;border-radius:8px;box-shadow:0 1px 5px #0002;display:none;white-space:pre-wrap;";
    const nav = document.querySelector("header");
    nav.insertAdjacentElement("afterend", resultsPanel);
  }

  async function searchProducts() {
    const query = searchInput.value.trim();
    if (!query) {
      resultsPanel.style.display = "block";
      resultsPanel.textContent = "Please enter a product search query.";
      return;
    }

    resultsPanel.style.display = "block";
    resultsPanel.textContent = "Searching products…";
    try {
      const response = await fetch(`${API_BASE_URL}/search`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
      });
      if (!response.ok) throw new Error(`API returned ${response.status}`);
      const data = await response.json();
      resultsPanel.textContent = data.answer || "No recommendation returned.";
    } catch (error) {
      resultsPanel.textContent = "Could not connect to the AI search API. Start the FastAPI backend and try again.";
      console.error(error);
    }
  }

  searchButton.addEventListener("click", searchProducts);
  searchInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") searchProducts();
  });
});
