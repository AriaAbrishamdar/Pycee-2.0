function wait_for_run_button() {

    var element = document.getElementById("run-btn");
    if (!element) {
        setTimeout(wait_for_run_button, 10);
        return;
    }
    document.getElementById("run-btn").addEventListener("click", clicked);
}


function clicked() {

    check_for_changes();
}


function check_for_changes() {



    var content = document.getElementById("wrap").innerText;

    var start_index = content.indexOf("Traceback (most recent call last):");
    var end_index = content.indexOf("** Process exited");

    if ((start_index == -1) || (end_index == -1)) {
        setTimeout(check_for_changes, 10);
        return;
    }

    var editor = document.getElementById("editor");
    var code = editor.getElementsByClassName("ace_layer ace_text-layer")[0].innerText;

    var error_message = content.substr(start_index, end_index-start_index-2);
    send_text_to_server(error_message, code);
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
    document.getElementById("wrap").innerHTML =  current_content +'<p id="term-output">\n\n===============================\n' + output_text + '</p>';

    wait_for_run_button()
}



wait_for_run_button()
