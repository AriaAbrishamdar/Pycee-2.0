function test_number_of_solutions(number_of_solutions, error, code) {

    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            console.log(request.response);
        }
    }
    var type = "find_solutions";
    request.open("POST", 'https://ariaabrishamdar.pythonanywhere.com/', true);
    var msg = { type, error, code, number_of_solutions };
    var msgjson = JSON.stringify(msg);
    request.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    request.send(msgjson);
}



test_number_of_solutions(4, "File "main.py", line 2\n          ^\nSyntaxError: unexpected EOF while parsing", "print(");
test_number_of_solutions(9, "Traceback (most recent call last):\n  File "main.py", line 2, in <module>\n    print(arr[0])\nIndexError: list index out of range", "arr = []\nprint(arr[0])");
test_number_of_solutions(6, "File "main.py", line 1\n    print(1)\n    ^\nIndentationError: unexpected indent", "    print(1)");
