rmdir /s /q dist
%USERPROFILE%\miniconda3\python.exe setup.py sdist
%USERPROFILE%\miniconda3\python.exe -m twine upload dist/*
