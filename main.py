#NAMA   : Satrio Bintang Pamungkas
#NIM    : 20.83.0552
#KELAS  : Teknik Komputer 2

import json
import mysql.connector
from urllib.request import Request, urlopen
from tabulate import tabulate
import os

db = mysql.connector.connect( #Variabel "db" digunakan untuk menyambungkan file python ini ke database "db_akademik_0552"
    host    = 'localhost',
    user    = 'root',
    passwd  = '',
    database= 'db_akademik_0552'
)

url = Request("https://api.abcfdab.cfd/students", headers={'User-Agent': 'Mozilla/5.0'})
f = urlopen(url,timeout=10)
data = f.read().decode("utf-8")
open_use_json = json.loads(data)
input_all_data = open_use_json["data"]

def proses_tambah(): #Function def proses_tambah() digunakan untuk memasukkan data API dari "https://api.abcfdab.cfd/students" ke database "db_akademik_0552"
    cur = db.cursor()
    sql = ('INSERT INTO tbl_students_0552 (id, nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s, %s)')
    data = input_all_data
    for d in data:
        value = (d["id"], d["nim"], d["nama"], d["jk"], d["jurusan"], d["alamat"])
        cur.execute(sql, value)
        db.commit()

def show_all_data(): #Function def show_all_data() digunakan untuk menampilkan semua data  yang ada pada database "db_akademik_0552" ke terminal dalam bentuk tabel tabulate
    cursor = db.cursor()
    result = cursor.execute("SELECT * FROM tbl_students_0552")
    result = cursor.fetchall()
    cursor.close()
    print(tabulate(result, headers=['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'], tablefmt='pretty'))

def show_data_limit(): #Function def show_data_limit() digunakan untuk menampilkan data yang ada pada database "db_akademik_0552" beradasarkan LIMIT yang ditentukan user
    input_limit = int(input("Masukan Limit : "))
    cursor = db.cursor()
    result = cursor.execute(f"SELECT * FROM tbl_students_0552 LIMIT {input_limit}")
    result = cursor.fetchall()
    cursor.close()
    print(tabulate(result, headers=['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'], tablefmt='pretty'))

def search_by_nim(): #Function def search_by_nim() digunakan untuk menampilkan data yang ada pada database "db_akademik_0552" beradasarkan NIM yang ditentukan user
    input_nim = input("Masukan NIM : ")
    cursor = db.cursor()
    result = cursor.execute(f"SELECT * FROM tbl_students_0552 where nim='{input_nim}'")
    cursor.execute(result)
    result = [cursor.fetchone()]

    if cursor.rowcount < 0:
        print(f"Data NIM {input_nim} tidak ditemukan!")
    else: 
        for data in result:
            if data == None:
                print(f"Data NIM {input_nim} tidak ditemukan!")
                table = [["NA", "NA", "NA", "NA", "NA", "NA"]] 
                headers = ['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat']
                print(tabulate(table, headers, tablefmt="pretty"))
            
            else:
                print(f"Data NIM {input_nim} ditemukan!")
                print(tabulate(result, headers=['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'], tablefmt='pretty'))

def menu():  #Function def menu() digunakan untuk menampilkan menu yang ada
    print("1. Tampilkan semua data")
    print("2. Tampilkan data berdasarkan limit")
    print("3. Cari data berdasarkan NIM")
    print("0. Keluar")

    option = input("Pilih Menu> ")

    os.system("cls")

    if option == "1":
        show_all_data()
    elif option == "2":
        show_data_limit()
    elif option == "3":
        search_by_nim()
    elif option == "0":
        exit()
    else:
        print("Pilih Menu yang valid")

if __name__ == '__main__':
    while(True):
        menu()