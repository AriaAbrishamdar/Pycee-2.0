// --- SOLUTIONS --- ///
    // change function - solutions
    function change_solutions(_value){
      document.getElementById("number_of_solutions").innerText = "Solutions: " + String(_value);
      document.getElementById("solution_slider").value = _value;

      chrome.storage.sync.set({solutions: _value}, function() {});
    }

    // on change - solutions
    document.getElementById("solution_slider").onchange = function() {
      var value = document.getElementById("solution_slider").value;
      change_solutions(value);
    };

    // initial set - solutions
    chrome.storage.sync.get(['solutions'], function(result) {
      if (typeof result.solutions === 'undefined')
        change_solutions(3);
      else
        change_solutions(result.solutions);
    });



// --- ENABLED --- ///
    // change function - enabled
    function change_enabled(_value){
      document.getElementById("enabled").checked = _value;

      chrome.storage.sync.set({enabled: _value}, function() {});
    }

    // on change - enabled
    document.getElementById("enabled").onchange = function() {
      var value = document.getElementById("enabled").checked;
      change_enabled(value);
    };

    // initial set - enabled
    chrome.storage.sync.get(['enabled'], function(result) {
      if (typeof result.enabled === 'undefined')
        change_enabled(true);
      else
        change_enabled(result.enabled);
    });
