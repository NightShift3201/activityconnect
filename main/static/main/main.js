document.getElementById("price-form").onsubmit = function() {
  var minPrice = document.getElementById("min-price").value;
  var maxPrice = document.getElementById("max-price").value;
  var existingQuery = window.location.search;
  var newQuery = "";
  
  if (existingQuery.includes("min_price=") && existingQuery.includes("max_price=")) {
      existingQuery = existingQuery.replace(/min_price=\d+/, "min_price=" + minPrice);
      existingQuery = existingQuery.replace(/max_price=\d+/, "max_price=" + maxPrice);
      newQuery = existingQuery;
  } else {
      newQuery = existingQuery + "&min_price=" + minPrice + "&max_price=" + maxPrice;
  }
  
  if (existingQuery.length === 0) {
      window.location.search = "?" + newQuery;
  } else {
      window.location.search = newQuery;
  }
  
  return false;
};

document.getElementById("age-form").onsubmit = function() {
    var minAge = document.getElementById("min-age").value;
    var maxAge = document.getElementById("max-age").value;
    var existingQuery = window.location.search;
    var newQuery = "";
    
    if (existingQuery.includes("min_age=") && existingQuery.includes("max_age=")) {
      existingQuery = existingQuery.replace(/min_age=\d+/, "min_age=" + minAge);
      existingQuery = existingQuery.replace(/max_age=\d+/, "max_age=" + maxAge);
      newQuery = existingQuery;
  } else {
      newQuery = existingQuery + "&min_age=" + minAge + "&max_age=" + maxAge;
  }

    if (existingQuery.length === 0) {
      window.location.search = "?" + newQuery;
    } else {
      window.location.search = newQuery;
    }
    return false;
  };

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  if (!urlParams.toString()) {
    document.getElementById("reset-filter-div").style.display = "none";
  }



  document.getElementById("reset-filter-btn").addEventListener("click", function() {
    window.location.search = "";
  });