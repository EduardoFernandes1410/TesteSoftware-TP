python3 -m coverage run -m unittest discover -b
python3 -m coverage report --include="*TesteSoftware-TP*" --skip-empty -m
python3 -m coverage xml