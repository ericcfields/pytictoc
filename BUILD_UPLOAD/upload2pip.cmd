cd C:\Users\ecfne\Documents\Eric\Coding\Python\pytictoc
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*