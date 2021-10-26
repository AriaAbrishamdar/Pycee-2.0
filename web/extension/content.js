
function clicked() {

    document.getElementById("wrap").innerHTML = "";
    check_for_changes();
}

function check_for_changes() {

    if (document.getElementById("wrap").innerHTML == "") {
        setTimeout(check_for_changes, 10);
        return;
    }

    get_text_from_python(document.getElementById("wrap").innerHTML);
}

function wait_for_run_button() {

    document.getElementById("wrap").innerHTML = '<p id="term-output">' + output_text + '</p>';
    var element = document.getElementById("run-btn");
    if (!element) {
        setTimeout(wait_for_run_button, 10);
        return;
    }
    document.getElementById("run-btn").addEventListener("click", clicked);
}

document.getElementById("run-btn").addEventListener("click", clicked);

function get_text_from_python(text) {

    var request = new XMLHttpRequest();

     request.onreadystatechange = function() {
        if (request.readyState === 4) {
            set_output_text(request.response);
        }
     }

    request.open("POST", 'https://ariaabrishamdar.pythonanywhere.com/', true);
    var msg = { text };
    var msgjson = JSON.stringify(msg);
    request.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    console.log(text);
    console.log(msgjson);
    request.send(msgjson);
}

function set_output_text(text) {
  
    output_text = text;
    document.getElementById("wrap").innerHTML = '<p id="term-output">' + output_text + '</p>';
    wait_for_run_button()
}

output_text = "";
