# Read the Docs testing

* Hosted: https://eimrek-rtd-tests.readthedocs.io/
* Overridden `robots.txt`: https://eimrek-rtd-tests.readthedocs.io/robots.txt

Has a subproject in this repo: https://github.com/eimrek/rtd-tests-subproject

Build docs locally:

```
cd docs
pip install -r requirements.txt
make html
open ./build/html/index.html
```

Based on tutorial: https://docs.readthedocs.io/en/stable/tutorial/


Rtd page: https://readthedocs.org/projects/eimrek-rtd-tests/