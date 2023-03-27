# MatrixviewPdf

A easily configureable python web server designed for Health care workers Reporting.

## **Project Directory**

- [app.py](app.py)

  - Python connector file from frontend to backend
  - Uses template files to make frontend dynamic and files concise
- [backend.py](backend.py)

  - Backend python file
  - Connects all frontend inputs to database and backend for security
- [information.json](information.json)

  - File used to configure code easily and efficiently
- [editUser.tpl](/static/editUser.tpl)

  - Changeable HTML file for editing user with changable username with code
- [main.css](/static/main.css)

  - Changable css file that connects to all of the HTML files
- [requirements.txt](requirements.txt)

  - Text file that shows all third party libaries used
- [account.sql](account.sql)

  - SQL Query file that automatically creates the table for account-management
- [Images](/images)

  - Directory that has all Images used for the website
- [pdf](/pdf)

  - Directory for all pdf files to view Report is stored
- [data](/data)

  - Directory where all report Generate is saved
- [static](/static)

  - Directory where all html, css, and js files are stored

## **Prequireiests**

- mySQL Database
- Python3
- pip3
- Linux Operating System
- pdftk software
- Report template must be fillable form
- Name of each Field must be the same as the collection Table Columns
- apache2

## **How to Setup?**

- pip3 install -r requirements.txt
- Create table called account in database
- Create your own Collection Table in the same database
- Update information.json file with correct information
- python3 app.py
- Go to the webserver host and port
- [gmail App Password for SMS](https://support.google.com/accounts/answer/185833?hl=en)
- [Create fillable form with OpenOffice instead of Adobe](http://foersom.com/org/HowTo/OoCreatePdfForm.htmlhttp://foersom.com/org/HowTo/OoCreatePdfForm.html)
