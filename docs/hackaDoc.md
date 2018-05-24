# Continuous Integration, Unit Tests, and Documentation

## Continuous Integration

In github DIRAC is using `Travis` to run unit tests, pylint, doc creation and formatting check for every pull request.

Travis is configured with a `yml` file
https://github.com/DIRACGrid/DIRAC/blob/integration/.travis.yml
```yml
language: python
python:
  - "2.7"
# command to install dependencies
install: "pip install -r requirements.txt"
# command to run tests
script:
  - export PYTHONPATH=${PWD%/*}
  - ls $PYTHONPATH
  - py.test
after_success:
- coveralls
```

### Coverage

Coverage information is stored via `coveralls` github integration:
https://coveralls.io/github/DIRACGrid/DIRAC

See where unit tests are needed.


## Unit tests

Independent test of some small piece of code. No dependency on external
packages, running services, databases, file system...

To run unit tests in DIRAC:
```bash
cd $DIRAC
py.test
```
py.test parses folders and looks for tests. Configured in `pytest.ini`.

### Unit test template

File Test_module.py
```python
"""Test some module"""

import unittest
import sys

from mock import MagicMock as Mock, patch

from MyProject import module

class TestModule( unittest.TestCase ):
  """Test the module.class"""

  def setUp( self ):
    """ called before each test is started  """
    self.module_patcher = patch.dict( sys.modules,{ 'MySQLdb': Mock() } )
    self.module_patcher.start()

  def tearDown( self ):
    """ called at the end of the test, cleanup resources"""
    self.module_patcher.stop()

  def test_init( self ):
    """ test init function of module.class """
    myclass = module.Class()
    self.assertIsInstance( myclass, module.Class )
    self.assertFalse( myclass.parameter )

  def test_init_2( self ):
    """ test init function of module.class """

    with patch( "module.Class.setParameter", new=Mock(return_value=true)):
      myclass = module.Class()

    self.assertIsInstance( myclass, module.Class )
    self.assertTrue( myclass.parameter )

## not needed when using py.test to run
if __name__ == "__main__":
  SUITE = unittest.defaultTestLoader.loadTestsFromTestCase( TestModule )
  TESTRESULT = unittest.TextTestRunner( verbosity = 3 ).run( SUITE )


```



## Documentation

Documentation is created with `sphinx`

```bash
pip install sphinx
```

To create it locally:
```bash
cd $DIRAC/docs
#export READTHEDOCS=True ## if you want to create code documentation as well, runs MakeDoc.py
 make html
firefox build/html/index.html
```
see `DIRAC/docs/source/conf.py` for the configuration

Code documentation is automatically created via script

### Documentation for extensions:

Inside sphinx external documentations can be automatically linked.

e.g.: iLCDirac documentation links against DIRAC base classes:

http://lcd-data.web.cern.ch/lcd-data/doc/ilcdiracdoc/DOC/ILCDIRAC/Interfaces/API/NewInterface/Job.html


### Online Documentation

Online documentation is automatically created on `readthedocs.org`, integrated via github.

http://dirac.readthedocs.io/en/latest/


### Tasks:

#### Testing

* Add CI to your DIRAC extension, start writing some tests, pylint, ...

* Try to add a test for you favorite untested piece of DIRAC

#### Docs

* Command reference is not yet automatically generated. The script
  DIRAC/docs/Tools/buildScriptDoc.py exists but calling it inside `readthedocs`
  needs to be fixed (though some information for commands hand-crafted and
  cannot be automatically created)

* Release notes could also be added to the documentation page. There is code
  that generates `rst` files from the DIRAC release notes already. With some
  adaption this could be added to the configuration as well

