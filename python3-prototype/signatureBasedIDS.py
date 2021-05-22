# Native imports
import sys
import hashlib
import sqlite3
# 3rd Party Imports (pip3 install {import} )
import ssdeep

HASHES_DB = "hashes.db" 

# prints how to use this script
def usage():
    use = f"python3 demo-signatureBasedIDS.py (file)"
    print(f"Usage: ")
    print(use)

# Initalize the DB by DB NAME
def initDB(dbName):
    with sqlite3.connect(f"{HASHES_DB}") as conn:
        cur = conn.cursor()

        cur.execute('''Create Table md5_hashes
        (ID INTEGER PRIMARY KEY,
        MD5 varchar(32) NOT NULL);
        ''')

        conn.commit()

# Insert to md5 hashes database
def insertToDB(hash_str):
    with sqlite3.connect(f"{HASHES_DB}") as conn:
        cur = conn.cursor() 

        cur.execute(f"INSERT INTO md5_hashes values {hash_str!r}")
        conn.commit()


# Creates a bogus registory of malicious md5 hashs
def get_repository():
    # populated a set of md5 hashes of "malicious files"
    return {"d5570e17ad969b17a817936ae4381bee", "e599eb9a0140ce7a5efc2859520a5b03"}


# get hash of file (natively python3)
def file_hash(file):
    md5_hash = hashlib.md5(file)
    sha1_hash = hashlib.sha1(file)
    sha256_hash = hashlib.sha256(file)

    md5, sha1, sha256 = (
        md5_hash.hexdigest(),
        sha1_hash.hexdigest(),
        sha256_hash.hexdigest(),
    )
    # print(f"md5: {md5}\nsha1: {sha1}\nsha256: {sha256}")
    return md5, sha1, sha256


# Gets the fuzzy hash of the file from non-native library (ssdeep)
def fuzzy_hash(filename):
    return ssdeep.hash_from_file(filename)


def main(filename):
    # Creates a <dict> object with the name hash (hashes of the file will be stored here)
    hash = {}

    # open the file in read bytes mode and calculate the hash of the file
    with open(filename, "rb") as f:
        md5, sha1, sha256 = file_hash(f.read())
        hash["md5"] = md5
        hash["sha1"] = sha1
        hash["sha256"] = sha256

    print(hash)
    print(f"ssdeep from {filename} = {fuzzy_hash(filename)}")
    malSet = get_repository()

    # Will iterate thru the hashes in the dictionary to find if any match the malicious data set
    for key in hash:
        if hash[key] in malSet:
            print("Malware")
            break


if __name__ == "__main__":

    try:
        arg1 = sys.argv[1]
    except:
        usage()

    main(arg1)
