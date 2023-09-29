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
* [6-post_email.py](6-post_email.py) -
* [7-error_code.py](7-error_code.py) -
* [8-json_api.py](8-json_api.py) -
* [10-my_github.py](10-my_github.py) -
