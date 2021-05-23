#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO make class

import sqlite3

"""
class Database:
    def __init(self, name):
        self.name = name
"""

HASHES_DB = "hashes.db"


def create_db():
    """create a db for hashes"""
    conn = None
    try:
        conn = sqlite3.connect(HASHES_DB)
    except sqlite3.Error as e:
        print(e)
        return
    if conn:
        c = conn.cursor()
        """SQL Query
            CREATE TABLE IF NOT EXISTS hashes {
                id INTEGER NOT NULL AUTO_INCREMENT,
                md5 VARCHAR(32) NOT NULL UNIQUE,
                PRIMARY KEY (id)
            };
        """
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS hashes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                md5 VARCHAR(32) NOT NULL UNIQUE
            );
            """
        )
        conn.commit()


def insert_hash(hash_str, hash_type="md5", num=1):
    """insert hash into db"""
    try:
        with sqlite3.connect(f"{HASHES_DB}") as conn:
            cur = conn.cursor()
            if num != 1:
                hash_str = hash_str.replace("'", "('").replace("(',", "'),")
                hash_str = hash_str[:-2] + "');"
                cur.execute(f"INSERT INTO hashes ({hash_type}) VALUES " + hash_str)
            else:
                cur.execute(f"INSERT INTO hashes ({hash_type}) VALUES ('{hash_str}');")
            conn.commit()
    except sqlite3.Error as e:
        print(e)
