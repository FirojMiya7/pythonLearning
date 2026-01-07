Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.11.0 django-6.0.1 sqlparse-0.5.5 tzdata-2025.3                                       

[notice] A new release of pip is available: 25.1.1 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS D:\3rd Sem\Django> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in d:\3rd sem\django\venv\lib\site-packages (25.1.1)
Collecting pip
  Using cached pip-25.3-py3-none-any.whl.metadata (4.7 kB)
Using cached pip-25.3-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.1.1
    Uninstalling pip-25.1.1:
      Successfully uninstalled pip-25.1.1
Successfully installed pip-25.3
(venv) PS D:\3rd Sem\Django> python -m django --versison
No Django settings specified.
Unknown command: '--versison'
Type 'python -m django help' for usage.
(venv) PS D:\3rd Sem\Django> python -m django --version 
6.0.1
(venv) PS D:\3rd Sem\Django> django startproject FirstProject
django : The term 'django' is not recognized as the name of a cmdlet, function, script file, or operable program. 
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ django startproject FirstProject
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (django:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS D:\3rd Sem\Django> python -m django startproject FirstProject
(venv) PS D:\3rd Sem\Django> cd FirstProject
(venv) PS D:\3rd Sem\Django\FirstProject> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 07, 2026 - 08:09:49
Django version 6.0.1, using settings 'FirstProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
[07/Jan/2026 08:10:08] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[07/Jan/2026 08:10:08] "GET /favicon.ico HTTP/1.1" 404 2214
(venv) PS D:\3rd Sem\Django\FirstProject> cd Django
cd : Cannot find path 'D:\3rd Sem\Django\FirstProject\Django' because it does not exist.
At line:1 char:1
+ cd Django
+ ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (D:\3rd Sem\Django\FirstProject\Django:String) [Set-Location], ItemNot  
   FoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

(venv) PS D:\3rd Sem\Django\FirstProject> cd
(venv) PS D:\3rd Sem\Django\FirstProject> cd d:\3rd\ Sem\Django
Set-Location : A positional parameter cannot be found that accepts argument 'Sem\Django'.
At line:1 char:1
+ cd d:\3rd\ Sem\Django
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-Location], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

(venv) PS D:\3rd Sem\Django\FirstProject> cd D:\3rd Sem\Django\
Set-Location : A positional parameter cannot be found that accepts argument 'Sem\Django\'.
At line:1 char:1
+ cd D:\3rd Sem\Django\
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-Location], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

(venv) PS D:\3rd Sem\Django\FirstProject> D:\3rd Sem\Django 
D:\3rd : The term 'D:\3rd' is not recognized as the name of a cmdlet, function, script file, or operable program. 
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ D:\3rd Sem\Django
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (D:\3rd:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS D:\3rd Sem\Django\FirstProject> cd ..\..
(venv) PS D:\3rd Sem> cd Django
(venv) PS D:\3rd Sem\Django> cd FirstProject
(venv) PS D:\3rd Sem\Django\FirstProject> cd .. 
(venv) PS D:\3rd Sem\Django> django-admin startapp app
(venv) PS D:\3rd Sem\Django> 
 *  History restored 

PS D:\3rd Sem\Django>



