INSTALLATION GUIDE 
Install the packages using pip
"pip install git+https://github.com/sumersb/jsonapi.git#egg=jsonapi"

Then import the package into your file

"from jsonapi.jsonapi import * "


To test, cd into root directory and run python3 -m unittests

Should describe the package, provide installation instructions and some code samples.

This package has functions using a child class of JSONEncoder and JSONDecoder that allow the conversion of complex and ranges to and from JSON



Calling dumps on a complex object complex(1,2) will convert it to the following JSON

dumps(complex(1, 2)) -> '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'



Calling dumps on range object will convert it to JSON

dumps(range(1, 99, -1)) ->{"start": 1, "stop": 99, "step": -1, "__extended_json_type__": "range"}'



The same can be done vice versa by converting the JSON string to python objects using loads

loads('{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}') -> complex(1,2)

loads({"start": 1, "stop": 99, "step": -1, "__extended_json_type__": "range"}') -> range(1,99,-1)


