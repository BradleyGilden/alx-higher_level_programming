# Python Networks v0

This directory deals with studying http protocols and their methods using pythons `urlib` and `request` package.

## Directory Files

* [0-hbtn_status.py](0-hbtn_status.py) -  a Python script that fetches https://alx-intranet.hbtn.io/status
  * You must use the package urllib
  * You are not allowed to import any packages other than urllib
  * The body of the response must be displayed like the following example (tabulation before -)
  * You must use a with statement
  * ```
    guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
    Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
    guillaume@ubuntu:~/0x11$ 
    ```
* [1-hbtn_header.py](1-hbtn_header.py) - Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
* [2-post_email.py](2-post_email.py) - a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
* [3-error_code.py](3-error_code.py) - Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
* [4-hbtn_status.py](4-hbtn_status.py) - a Python script that fetches https://alx-intranet.hbtn.io/status.
You must use the package requests
* [5-hbtn_header.py](5-hbtn_header.py) - a Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header. You must use requests
* [6-post_email.py](6-post_email.py) - a Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response. You must use requests
* [7-error_code.py](7-error_code.py) - a Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
* [8-json_api.py](8-json_api.py) - a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
  * The letter must be sent in the variable q
  * If no argument is given, set q=""
  * If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
  * Otherwise:
    * Display Not a valid JSON if the JSON is invalid
    * Display No result if the JSON is empty
* [10-my_github.py](10-my_github.py) - a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
  * You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
  * The first argument will be your username
  * The second argument will be your password (in your case, a personal access token as password)
  * You must use the package requests and sys
