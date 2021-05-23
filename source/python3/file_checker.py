import hashlib
import sys
import webbrowser as web

from hashes import database as db

DATABASE_PATH = "./hashes/hashes.db"
# Search VirusTotal for more details
# Not using API
VIRUSTOTAL_URL = "https://www.virustotal.com/gui/search/"


def hash_file(filename):
    """generates hash of file to check"""
    with open(filename, "rb") as f:
        file = f.read()
        md5_hash = hashlib.md5(file)
        """
        # For future hashes
        sha1_hash = hashlib.sha1(file)
        sha256_hash = hashlib.sha256(file)
        md5, sha1, sha256 = (
            md5_hash.hexdigest(),
            sha1_hash.hexdigest(),
            sha256_hash.hexdigest(),
        )
        """
    return md5_hash.hexdigest()


"""
# Gets the fuzzy hash of the file from non-native library (ssdeep)
def fuzzy_hash(filename):
    return ssdeep.hash_from_file(filename)
"""


def check_file(filename):
    md5 = hash_file(filename)
    print(f"File Hash: {md5}")
    result = db.check_hash(md5, HASHES_DB=DATABASE_PATH)
    if len(result) > 0:
        print(result)
        print("File is malware")
        web.open(VIRUSTOTAL_URL + md5)


def main(filename):
    check_file(filename)


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except Exception as e:
        print(e)
