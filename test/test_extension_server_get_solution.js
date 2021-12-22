function test_get_solutions(error, code) {

    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            console.log(request.response.items.length);
        }
    }
    var number_of_solutions = 3;
    var type = "find_solutions";
    request.open("POST", 'https://ariaabrishamdar.pythonanywhere.com/', true);
    var msg = { type, error, code, number_of_solutions };
    var msgjson = JSON.stringify(msg);
    request.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    request.send(msgjson);
}



test_get_solutions("File "main.py", line 2\n          ^\nSyntaxError: unexpected EOF while parsing", "print(");
test_get_solutions("Traceback (most recent call last):\n  File "main.py", line 2, in <module>\n    print(arr[0])\nIndexError: list index out of range", "arr = []\nprint(arr[0])");
test_get_solutions("File "main.py", line 1\n    print(1)\n    ^\nIndentationError: unexpected indent", "    print(1)");
