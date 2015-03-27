## ---------------------
## Run with More Detail
## ---------------------
## test is name of .py (module); IsOddTest is name of class
## Shows:
## 	testOne (test.IsOddTests) ... ok
## 	testThree (test.IsOddTests) ... FAIL
## 	testTwo (test.IsOddTests) ... ok
## 	<shows what failed>
## 	Ran <#> tests in <time>.
## 	FAILED (failures=<#>)

python -m unittest -v test.IsOddTests

## ----------------------
## Run only one test
## ----------------------
## test is name of .py (module); IsOddTest is name of class; testOne is name of function
## Shows:
## 	Ran 1 test in 0.000s
##
## 	OK

# python -m unittest test.IsOddTests.testOne