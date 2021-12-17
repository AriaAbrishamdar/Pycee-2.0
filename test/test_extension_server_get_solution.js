function test(error, code) {

    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            console.log(request.response);
        }
    }
    var type = "find_solutions";
    request.open("POST", 'https://ariaabrishamdar.pythonanywhere.com/', true);
    var msg = { type, error, code };
    var msgjson = JSON.stringify(msg);
    request.setRequestHeader('Content-type', 'application/json;charset=UTF-8');
    request.send(msgjson);
}



test("File "main.py", line 2\n          ^\nSyntaxError: unexpected EOF while parsing", "print(");
test("Traceback (most recent call last):\n  File "main.py", line 2, in <module>\n    print(arr[0])\nIndexError: list index out of range", "arr = []\nprint(arr[0])");
test("  File "main.py", line 1\n    print(1)\n    ^\nIndentationError: unexpected indent", "    print(1)");
