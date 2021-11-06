function wait_for_run_button() {

    var element = document.getElementById("run-btn");
    if (!element) {
        setTimeout(wait_for_run_button, 10);
        return;
    }
    document.getElementById("run-btn").addEventListener("click", clicked);
}


function clicked() {
    check_for_changes()
}


function check_for_changes() {

    var content = document.getElementById("wrap").innerText;

    var list = document.querySelectorAll(".warning,.error");

    var error_message = "";

    if (list.length <= 0) {
      setTimeout(check_for_changes, 100);
      return;
    }

    for (let i = 0; i < list.length; i++) {
      error_message += list[i].innerText;
    }


    var editor = document.getElementById("editor");
    var code = editor.getElementsByClassName("ace_layer ace_text-layer")[0].innerText;


    setTimeout(send_text_to_server.bind(null, error_message, code), 250);
}


function send_text_to_server(error, code) {

    var request = new XMLHttpRequest();

     request.onreadystatechange = function() {
        if (request.readyState === 4) {
            set_output_text(request.response);
        }
     }

    request.open("POST", 'https://ariaabrishamdar.pythonanywhere.com/', true);
    var msg = { error, code };
    var msgjson = JSON.stringify(msg);
    request.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    request.send(msgjson);
}


function set_output_text(text) {

    var output_text = text;
    var current_content = document.getElementById("wrap").innerHTML;
    document.getElementById("wrap").innerHTML =  current_content +'<p id="term-output">\n\n' + output_text + '</p>';

    wait_for_run_button()
}



wait_for_run_button()

document.getElementById("d").style.height = "calc(100% - 2.5px)";
