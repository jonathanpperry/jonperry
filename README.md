How to use the virtual environment:

Virtual environments (shortened as "virtualenv") separate our new project’s Python dependencies from our other projects and from the Python libraries our operating system uses. If you don’t use a virtualenv, there’s a good chance you might break part of your OS.

Install this Python utility, which will allow you to create and manage Python virtual environments. Use the "virtualenv" command to create a new virtual environment, using its sole argument to name your new environment. The instructions to activate your new virtualenv vary by operating system:

# Create a new virtualenv named "myproject"
$ virtualenv myproject
New python executable in myproject/bin/python
Installing setuptools, pip, wheel...done.

# Activate the virtualenv (OS X & Linux)
$ source myproject/bin/activate

# Activate the virtualenv (Windows)
$ myproject\Scripts\activate
You’ll need to activate your virtual environment every time you work on your Python project. In the rare cases when you want to deactivate your virtualenv without closing your terminal session, just use the deactivate command.
