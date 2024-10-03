# Read the Docs testing

* Tutorial: https://docs.readthedocs.io/en/stable/tutorial/
* Hosted: https://eimrek-rtd-tests.readthedocs.io/
* Overridden `robots.txt`: https://eimrek-rtd-tests.readthedocs.io/robots.txt

Build docs locally:

```
pip install -e .
cd docs
pip install -r requirements.txt
make html
open build/html/index.html
```
