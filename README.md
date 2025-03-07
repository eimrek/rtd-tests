# Read the Docs testing

Note, this setup is kept as similar to the AiiDA RTD setup as possible (where `aiida-metapkg` is the "main-project" and `aiida-core` is the subproject).

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

After pushing to this repo, RTD will build automatically.

Based on tutorial: https://docs.readthedocs.io/en/stable/tutorial/

RTD page: https://app.readthedocs.org/projects/eimrek-rtd-tests/

# Google search console

To enable Google search console for RTD, the easiest is to use the HTML meta tag verification method ([see here for details](https://support.google.com/webmasters/answer/9008080#meta_tag_verification&zippy=%2Chtml-tag)). Relevant notes:

* The `meta` tag needs to only be added to the page where users are redirected to, when they just use the root domain as the URL. So in our case, **the meta tag needs to be added to the subproject**.

* The meta tag can be added by
  ```
  .. meta::
    :google-site-verification: <your code>
  ```
  in the root `index.rst` file. [See here](https://webmasters.stackexchange.com/questions/142501/how-do-i-add-a-google-search-console-verification-meta-tag-to-a-read-the-docs-pa)

