# to reproduce

```
pip install micropython-esp32-stubs --target typings --no-user

python -m venv .venv

.\.venv\Scripts\activate.ps1
pip install pyright
```

then run

```bash
pyright -t typings .\src\validate_hasable.py
```

See Error

D:\repos\Stubber-test-repos\hashable\src\validate_hasable.py:6:6 - error: Dictionary key must be hashable

peix per type for :
- int, str ....
- str

Fixed by full update of stdlib to 3.11+ ,
and then removing the bulk of features not supported in Micropython ( Manual labor )-: 

Some modules are available on two levels and with multiple names

- `typings/os.pyi`
- `typings/uos.pyi`
- `typings/stdlib/os/__init__.pyi`
- `typings/io.pyi`
- `typings/uio.pyi`
- `typings/stdlib/io.pyi`

Solution

    * import everthing from the stdlib modules in the micropython module level modules 

    File`typings/os.pyi`
		`from stdlib.os import * `

this needs an update in stubber to add addtional glue imports to these modules
and exposed a limitation of libcst which does not copy over `from foo import *` by default

1. os/uos
2. io/uio
3. socket
4. sys

install from branch & folder 
```
pip install git+https://github.com/josverl/micropython-stubs.git@stdlib-updates#subdirectory=publish/micropython-stdlib-stubs --target typings --no-user  
pip install git+https://github.com/josverl/micropython-stubs.git@stdlib-updates#subdirectory=publish/micropython-v1_20_0-esp32-stubs --target typings --no-user  
```

## other issues

##### stdlib/_typeshed - outdated - errors

1. update the _typeshed folder from (pylances copy ot) Typeshed
2. added / updated a series of other modules to resolve as much errors as possible
3. 

FIXED
