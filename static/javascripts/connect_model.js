let searchQuery = summary+'';

window.onload = () => {
    searchQuery = summary;
    generateHTML(searchQuery);
    console.log(searchQuery);
};


function generateHTML(results) {
    const BodyDiv = document.getElementById('results-body');
    let HTML = `
        <div class="item">
          
          <p class="item-data"> ${results}</p>
        </div>
      `;

    BodyDiv.innerHTML = HTML;
  }