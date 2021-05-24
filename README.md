# Bruteforce HTTP Authentication
Simple tool to bruteforce HTTP authentication forms.

### Supports:

* Basic HTTP authentication
* Digest HTTP authentication

### usage 
```python
python3 python3 bruteforce-http-authentication.py -w http://site.com  -u username -f passwords.txt  -m basic
python3 python3 bruteforce-http-authentication.py -w http://site.com  -u username -f passwords.txt  -m digest
```

### Arguments
```json 
    -w: url (https://test.com)
    -u: username
    -f: dictionary file
    -m: method (basic or digest)
```    
### Requirements
```python
python3 -m pip install -r requirements.txt
```

### Dictionaries
**[SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords)**
