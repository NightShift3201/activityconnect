document.getElementById("price-form").onsubmit = function() {
    var minPrice = document.getElementById("min-price").value;
    var maxPrice = document.getElementById("max-price").value;
    var existingQuery = window.location.search;
    var newQuery = "&min_price=" + minPrice + "&max_price=" + maxPrice;
    
    if (existingQuery.length === 0) {
      window.location.search = "?" + newQuery;
    } else {
      window.location.search = existingQuery + newQuery;
    }
    return false;
  };

  document.getElementById("age-form").onsubmit = function() {
    var minAge = document.getElementById("min-age").value;
    var maxAge = document.getElementById("max-age").value;
    var existingQuery = window.location.search;
    var newQuery = "&min_age=" + minAge + "&max_age=" + maxAge;
    
    if (existingQuery.length === 0) {
      window.location.search = "?" + newQuery;
    } else {
      window.location.search = existingQuery + newQuery;
    }
    return false;
  };



  document.getElementById("reset-filter-btn").addEventListener("click", function() {
    window.location.search = "";
  });