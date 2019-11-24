# puf-reader
 
run the following line in terminal to install prerequisite packages.

```{bash}
pip install -r requirements.txt
```

```{python}
python3 run.py
```

to proceed the code to read the puf.

**Note: the reading from web camera function is developing 

-----

The code will convert the optical image puf which stored in `./dendrites` to be unique ID.
The reading can either be randomly or denterminstic, which reading starts from a specific location or direction. It can also change the output format or a specific length. The IDs hashed by SHA-512 and reading pixels.

* binary 
* decimal
* hex
* character
