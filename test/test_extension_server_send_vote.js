function test_upvote(index) {

    if (solution_values[index] == 1)
        return

    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            console.log(request.response);
        }
    }

    var type = "upvote";
    var link = solution_links[index];
    var value = 1;
    request.open("POST", 'https://ariaabrishamdar.pythonanywhere.com/', true);
    var msg = { type, error_type, link, value };
    var msgjson = JSON.stringify(msg);
    request.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    request.send(msgjson);

    var element = document.getElementById("score-" + index.toString());
    if (element) {
        var text = document.getElementById("score-" + index.toString()).innerHTML;

        var is_negative = false;
        if (text.includes("-"))
            is_negative = true;

        var number = parseInt(text.match(/\d+/)[0]);
        if (is_negative)
            number = -number;

        number += 1;

        document.getElementById("score-" + index.toString()).innerHTML = ("Score: " + number.toString());
    }


    if (solution_values[index] == -1) {
        solution_values[index] = 0;
        upvote(index);
    }
    else
        solution_values[index] = 1;
    return;
}

function test_downvote(index) {

    if (solution_values[index] == -1)
        return

    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            console.log(request.response);
        }
    }

    var type = "downvote";
    var link = solution_links[index];
    var value = -1;
    request.open("POST", 'https://ariaabrishamdar.pythonanywhere.com/', true);
    var msg = { type, error_type, link, value };
    var msgjson = JSON.stringify(msg);
    request.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    request.send(msgjson);

    var element = document.getElementById("score-" + index.toString());
    if (element) {
        var text = document.getElementById("score-" + index.toString()).innerHTML;

        var is_negative = false;
        if (text.includes("-"))
            is_negative = true;

        var number = parseInt(text.match(/\d+/)[0]);
        if (is_negative)
            number = -number;

        number -= 1;

        document.getElementById("score-" + index.toString()).innerHTML = ("Score: " + number.toString());
    }

    if (solution_values[index] == 1) {
        solution_values[index] = 0;
        downvote(index);
    }
    else
        solution_values[index] = -1;
    return;
}


var error_type = "SyntaxError";
var solution_links = ["link_1", "link_2", "link_3"];
var solution_values = [0, 0, 0];


test_upvote(1);
test_upvote(2);
test_upvote(2);
test_upvote(2);
test_upvote(3);
test_downvote(2);
test_downvote(3);
test_downvote(2);
test_upvote(3);

error_type = "IndentationError";

test_upvote(1);
test_upvote(2);
test_upvote(2);

error_type = "IndexError";

test_upvote(2);
test_upvote(3);
test_downvote(2);
test_downvote(3);
test_downvote(2);
test_upvote(3);
