from pathlib import Path
from tkinter.constants import END
import pymysql
import hashlib
from dotenv import dotenv_values
from termcolor import colored
import configparser




def find_malware_files(self):

    self.scroll_text.delete("1.0", END)
    self.scroll_text.place_forget()
    self.del_scroll_text.place_forget()

    batchSize = 100
    config1 = dotenv_values("dbvalues.env")
    currentpath = self.entry.get()




    def find_hash(filename):
        sha256_hash = hashlib.sha256()

        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        return sha256_hash.hexdigest()




    def check_hashes(hashes):
        connection = pymysql.connect(
            host=config1["DB_HOST"],
            port=int(config1["DB_PORT"]),
            user=config1["DB_USER"],
            password=config1["DB_PASSWORD"],
            database=config1["DB_NAME"],
            cursorclass=pymysql.cursors.SSDictCursor
        )

        with connection.cursor() as cursor:
            hashTuple = "(" + " ,".join(["'" + h +
                                        "'" for h in hashes]) + ")"
            select_hashes_row = "select `hash` from `hashlist` where `hash` in " + hashTuple
            cursor.execute(select_hashes_row)
            existingHashes = [result["hash"] for result in cursor.fetchall()]

            return existingHashes




    def readFolder(folder, isRecursive):
        glob = '**/*' if isRecursive else '*'
        for elem in Path(folder).glob(glob):
            if elem.is_file():
                yield elem.as_posix()




    def generateN(iterable, amount):
        result = []
        try:
            for i in range(amount):
                result.append(next(iterable))
            return result
        except StopIteration:
            return result




    def main():
        number = 0

        if self.choice_for_non_recursive.get():
            filesGenerator = readFolder(currentpath, False)

        else:
            filesGenerator = readFolder(currentpath, True)
        batchNumber = 0
        allMatchedHashes = []


        while True:
            config = configparser.ConfigParser()
            config.read('parameters.ini', encoding= 'utf_8')
            filenames = generateN(filesGenerator, batchSize)

            if (len(filenames) == 0):

                print("No files left to process")

                break
            


            batchNumber += 1

            hashes = [find_hash(f) for f in filenames]

            matchedHashes = check_hashes(hashes)
            allMatchedHashes.extend(matchedHashes)


            if len(matchedHashes)>0:
                for d in matchedHashes:
                    while True:
                        if d in hashes: 
                            position = hashes.index(d)
                            if config["btn_settings"]["width"] == "190":
                                print("Malware file is " + colored(str(filenames[position]), 'red')+"\n")
                                self.scroll_text.configure(fg = "#FF0017")
                                self.scroll_text.insert(5.0, "      File " + str(filenames[position]) + " is malicious!\n")
                            elif config["btn_settings"]["width"] == "210" :
                                print(colored(str(filenames[position]) + " є небезпечним!", 'red'))
                                self.scroll_text.configure(fg = "#FF0017")
                                self.scroll_text.insert(5.0, "      Файл " + str(filenames[position]) + " є небезпечним!\n")
                            number+=1
                            hashes.pop(position)
                            hashes.insert(position, '0')
                        if d not in hashes:
                            break


        if (number == 0 and config["btn_settings"]["width"] == "210"):
            self.scroll_text.configure(fg = "#00AA44")
            self.del_scroll_text.place(x = 18, y = 400)
            self.scroll_text.place(x = 10, y = 300)
            self.scroll_text.insert(5.0, "      Шкідливі файли не знайдено :)")


        elif (number ==0 and config["btn_settings"]["width"] == "190"):
            self.scroll_text.configure(fg = "#00AA44")
            self.scroll_text.insert(5.0, "      Malicious files haven't been found :)")

        self.del_scroll_text.place(x = 18, y = 467)
        self.scroll_text.place(x = 10, y = 350)

    main()





def check_one_file(self):
    self.scroll_text.delete("1.0", END)
    self.scroll_text.place_forget()
    self.del_scroll_text.place_forget()

    currentpath = self.entry.get()

    h = hashlib.sha256()

    with open(currentpath, 'rb') as file:
        while True:

            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

        generated_hash = h.hexdigest()




    def check_hashes():
        config1 = dotenv_values("dbvalues.env")
        config = configparser.ConfigParser()
        config.read('parameters.ini', encoding= 'utf_8')
        number = 0
        connection = pymysql.connect(
            host=config1["DB_HOST"],
            port=int(config1["DB_PORT"]),
            user=config1["DB_USER"],
            password=config1["DB_PASSWORD"],
            database=config1["DB_NAME"],
            cursorclass=pymysql.cursors.SSDictCursor
        )

        with connection.cursor() as cursor:
            insert_query = "SELECT hash FROM `hashlist` WHERE hash = %s"
            cursor.execute(insert_query, generated_hash)
            hash_element = cursor.fetchone()
            if hash_element:
                if config["btn_settings"]["width"] == "190":
                    self.scroll_text.configure(fg = "#FF0017")
                    self.scroll_text.insert(5.0, "      File " + str(currentpath) + " is malicious!\n")
                elif config["btn_settings"]["width"] == "210" :
                    self.scroll_text.configure(fg = "#FF0017")
                    self.scroll_text.insert(5.0, "      Файл " + str(currentpath) + " є небезпечним!\n")
                number+=1


        if (number == 0 and config["btn_settings"]["width"] == "210"):
            self.scroll_text.configure(fg = "#00AA44")
            self.scroll_text.insert(5.0, "      Нічого не виявлено в обраному файлі :)")


        elif (number ==0 and config["btn_settings"]["width"] == "190"):
            self.scroll_text.configure(fg = "#00AA44")
            self.scroll_text.insert(5.0, "      Choosed file is clear :)")

        self.del_scroll_text.place(x = 18, y = 467)
        self.scroll_text.place(x = 10, y = 350)
    
    check_hashes()