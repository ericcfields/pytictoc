cd C:\Users\fieldsec\OneDrive - Westminster College\Documents\ECF\Coding\Python\pytictoc
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*
