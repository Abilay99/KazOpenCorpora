import pymysql as sql
import pymysql.err as err
from pymysql.cursors import DictCursor
class corporaDB():
#DQ - DEREKTER QORY, DQK - DEREKTER QORYNDAGY KESTE, DB - DATA BASE
    __host = ''
    __user = ''
    __password = ''
    def getHost(self):
        return self.__host
    def getUser(self):
        return self.__user
    def getPassword(self):
        return self.__password
    def __init__(self, host = 'localhost', user = 'root', password = ''):
        self.__host = host
        self.__user = user
        self.__password = password
        try:
            self.__mydb = sql.connect(host = self.__host,
            user = self.__user,
            password = self.__password,
            charset = 'utf8mb4',
            cursorclass = DictCursor)
            print(f'serverge bailanys ornatyldy addres: {self.getHost()} user: {self.getUser()} password: {self.getPassword()} ')
        except:
            print(f'serverge bailanys ornatylmady addres: {self.getHost()} user: {self.getUser()} password: {self.getPassword()} ')
    def __del__(self):
        print(f'Destruktor obektilerdi joidy!!!')
    def __tekseruDQ(self):
        try:
            with self.__mydb.cursor() as cr:
                query = """SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'searchengine';
                """
                cr.execute(query)
                tekseru = cr.fetchone()
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
        if tekseru == None:
            return True
        else: 
            return False
    def __tekseruDQK(self):
        try:
            with self.__mydb.cursor() as cr:
                query = """SELECT TABLE_NAME FROM INFORMATION_SCHEMA.PARTITIONS WHERE TABLE_SCHEMA ='searchengine' AND TABLE_NAME in('corpora', 'genres');
                """
                cr.execute(query)
                tekseru = cr.fetchone()
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
        if tekseru == None:
            return True
        else: 
            return False
    def DEREKTER_QORYN_QURU(self):
        try:
            if not self.__tekseruDQ():
                print("'searchengine' derekter qory qurylgan!")
            if not self.__tekseruDQK():
                print("'searchengine' derekter qoryna 'corpora' kestesi qurylgan!")
            while(self.__tekseruDQ()):
                print("'searchengine' derekter qory quryluda...")
                with self.__mydb.cursor() as cr:
                    querydb = """
                    CREATE DATABASE searchengine CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
                    """
                    cr.execute(querydb)
                print("'searchengine' derekter qory quryldy!")
            self.__mydb.commit()
            while(self.__tekseruDQK()):
                print("'searchengine' derekter qoryna 'genres' & 'corpora' kestesi quryluda...")
                with self.__mydb.cursor() as cr:
                    querytable = """
                    CREATE TABLE searchengine.genres(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    rus MEDIUMTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    kz MEDIUMTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    en MEDIUMTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL)
                    ENGINE = INNODB;
                    CREATE TABLE searchengine.corpora(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    title TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    text LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                    lemmas LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    morphanaliz LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    outtext LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    genre_id int,
                    keywords MEDIUMTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    subject MEDIUMTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    url MEDIUMTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                    FOREIGN KEY (genre_id) REFERENCES genres(id))
                    ENGINE = INNODB;
                    """
                    cr.execute(querytable)
                print("'searchengine' derekter qoryna 'corpora' kestesi quryldy!")
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def CORPORA_KESTESINE_ENGIZU(self, TITLE = None, TEXT = "notext", LEMMAS = None, MORPHANALIZ = None, OUTTEXT = None, GENRE_ID=None, KEYWORDS = None, SUBJECT = None, URL = None):
        try:
            if TEXT == "notext":
                raise ValueError("Keshiriniz kestege engizu barysynda TEXT parametrine ma'n engizilmedi")
            else:
                if len(self.__BOS_ID_ORYNDARY())>0:
                    print("Kestede bos oryndar anyqtaldy olar: ", self.__BOS_ID_ORYNDARY(),end=" ")
                    p = input("malimetti osy bos oryndardyn algashqysyna engiziluin jalgastyrasyzba (ia/joq) nemese (i/j): ")
                    if p == 'i' or p == 'ia':
                        with self.__mydb.cursor() as cr:
                            query = "INSERT INTO searchengine.corpora(id, title, text, lemmas, morphanaliz, outtext, genre, keywords, subject, url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                            in_query = (self.__mas2[0], TITLE, TEXT, LEMMAS, MORPHANALIZ, OUTTEXT, GENRE_ID, KEYWORDS, SUBJECT, URL,)
                            cr.execute(query, in_query)
                            print("Malimet %sshi(shy) orynga saqtaldy!"%str(self.__mas2[0]))
                            del self.__mas2[0]
                        self.__mydb.commit()
                    else:
                        with self.__mydb.cursor() as cr:
                            query = "INSERT INTO searchengine.corpora(title, text, lemmas, morphanaliz, outtext, genre_id, keywords, subject, url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                            in_query = (TITLE, TEXT, LEMMAS, MORPHANALIZ, OUTTEXT, GENRE_ID, KEYWORDS, SUBJECT, URL,)
                            cr.execute(query, in_query)
                        self.__mydb.commit()
                        print("Malimet avtomatty turde derekter qorynyn songy orynyna iagni %sshi(shy) saqtaldy!"%str(self.SONGY_ID()))
                else:
                    with self.__mydb.cursor() as cr:
                        query = "INSERT INTO searchengine.corpora(title, text, lemmas, morphanaliz, outtext, genre_id, keywords, subject, url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        in_query = (TITLE, TEXT, LEMMAS, MORPHANALIZ, OUTTEXT, GENRE_ID, KEYWORDS, SUBJECT, URL,)
                        cr.execute(query, in_query)
                        print("Malimet %sshi(shy) orynga saqtaldy!"%str(self.SONGY_ID()))
                    self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def GENRES_KESTESINE_ENGIZU(self, RUS = None, KAZ = None, EN = None):
        try:
            if len(self.__BOS_ID_ORYNDARY())>0:
                print("Kestede bos oryndar anyqtaldy olar: ", self.__BOS_ID_ORYNDARY(),end=" ")
                p = input("malimetti osy bos oryndardyn algashqysyna engiziluin jalgastyrasyzba (ia/joq) nemese (i/j): ")
                if p == 'i' or p == 'ia':
                    with self.__mydb.cursor() as cr:
                        query = "INSERT INTO searchengine.genres(id, rus, kz, en) VALUES(%s, %s, %s, %s);"
                        in_query = (self.__mas2[0], RUS, KAZ, EN,)
                        cr.execute(query, in_query)
                        print("Malimet %sshi(shy) orynga saqtaldy!"%str(self.__mas2[0]))
                        del self.__mas2[0]
                    self.__mydb.commit()
                else:
                    with self.__mydb.cursor() as cr:
                        query = "INSERT INTO searchengine.genres(rus, kz, en) VALUES(%s, %s, %s);"
                        in_query = (RUS, KAZ, EN,)
                        cr.execute(query, in_query)
                    self.__mydb.commit()
                    print("Malimet avtomatty turde derekter qorynyn songy orynyna iagni %sshi(shy) saqtaldy!"%str(self.SONGY_ID_GENRES()))
            else:
                with self.__mydb.cursor() as cr:
                    query = "INSERT INTO searchengine.genres(rus, kz, en) VALUES(%s, %s, %s);"
                    in_query = (RUS, KAZ, EN,)
                    cr.execute(query, in_query)
                    print("Malimet %sshi(shy) orynga saqtaldy!"%str(self.SONGY_ID_GENRES()))
                self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def Corpora_column_morph_emty(self):
        try:
            with self.__mydb.cursor() as cr:
                query = "SELECT id, text FROM searchengine.corpora where morphanaliz is null;"
                cr.execute(query)
                res = cr.fetchall()
                return res
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def KESTENI_TAZARTU(self):
        try:
            with self.__mydb.cursor() as cr:
                query = "TRUNCATE TABLE searchengine.corpora"
                cr.execute(query)
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def KESTEGE_BAGAN_QOSU(self,aty_tipi_qosymshalar):
        try:
            with self.__mydb.cursor() as cr:
                query = """ALTER TABLE searchengine.corpora ADD %s;"""%aty_tipi_qosymshalar
                cr.execute(query)
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def Selects(self, start_with = 0, count_def = 25):
        try:
            with self.__mydb.cursor() as cr:
                query = f"SELECT id, outtext FROM searchengine.corpora LIMIT {start_with}, {count_def};"
                cr.execute(query)
                res = cr.fetchall()
                return res
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def SelectsText(self, start_with = 0, count_def = 25):
        try:
            with self.__mydb.cursor() as cr:
                query = f"SELECT `id`, `text` FROM searchengine.corpora LIMIT {start_with}, {count_def};"
                cr.execute(query)
                res = cr.fetchall()
                return res
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def SelectsForAnalyze(self, gid = 1):
        try:
            with self.__mydb.cursor() as cr:
                query = f"SELECT C.text, G.kz FROM searchengine.corpora as C join searchengine.genres as G on(C.genre_id = G.id) where G.id = {gid};"
                cr.execute(query)
                res = cr.fetchall()
                return res
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))

    def for_count_lemmas(self, phrase = ""):
        try:
            with self.__mydb.cursor() as cr:
                query = f"SELECT COUNT(id) as sany FROM `searchengine`.`corpora` WHERE MATCH(lemmas) AGAINST('{phrase}');"
                cr.execute(query)
                res = cr.fetchall()
                return res
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def Count_corpora(self):
        try:
            with self.__mydb.cursor() as cr:
                query = f"SELECT count(id) as sany FROM searchengine.corpora;"
                cr.execute(query)
                res = cr.fetchall()
                return res
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def Count_genres(self):
        try:
            with self.__mydb.cursor() as cr:
                query = f"SELECT count(id) as sany FROM searchengine.genres;"
                cr.execute(query)
                res = cr.fetchall()
                return res
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def DEREKTER_QORYN_JABU(self):
        try:
            self.__mydb.close()
        except:
            print("Qate: {}".format(err.error_map))
    def DEREKTER_QORYN_OSHIRU(self):
        try:
            if not self.__tekseruDQ():
                with self.__mydb.cursor() as cr:
                    query = "DROP DATABASE searchengine;"
                    cr.execute(query)
                    if self.__tekseruDQ():
                        print("'searchengine' derekter qory oshirildi!")
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    
    def KESTENI_OSHIRU(self):
        try:
            if not self.__tekseruDQ() and not self.__tekseruDQK():
                with self.__mydb.cursor() as cr:
                    query = "DROP TABLE searchengine.corpora;"
                    cr.execute(query)
                    if self.__tekseruDQK():
                        print("'searchengine' derekter qorydagy 'corpora' kestesi oshirildi!")
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))

    def KESTENI_JANARTU(self, bagan_aty = None, bagan_mani = None, bagan_id = None):
        try:
            if not self.__tekseruDQ() and not self.__tekseruDQK():
                with self.__mydb.cursor() as cr:
                    query = f"""UPDATE searchengine.corpora SET `{bagan_aty}` = '{bagan_mani}' WHERE `id` = {bagan_id};"""
                    cr.execute(query)
                    print(f"bagan id = {bagan_id} janartyldy!")
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def ID_BOIYNSHA_OSHIRU(self, identifikator = 0):
        try:
            with self.__mydb.cursor() as cr:
                query = "SELECT * FROM searchengine.corpora WHERE searchengine.corpora.id = %s;"
                cr.execute(query, identifikator)
                tekseru = cr.fetchone()
            if tekseru != None:
                p = input("Izdegen id derekter qorynan tabyldy iagni:\n%s\noshirudi jalgastyrasyzba (ia/joq) nemese (i/j): "%tekseru)
                if p == 'i' or p == 'ia':
                    with self.__mydb.cursor() as cr:
                        query = "DELETE FROM searchengine.corpora WHERE searchengine.corpora.id = %s;"
                        cr.execute(query, identifikator)
                        print("Oshirildi!")
                else:
                    print("Malimet oz kuiin saqtap qaldy!")
            else:
                print("Keshiriniz mundai id derekter qorynan tabylmady!")
            self.__mydb.commit()
        except:
            print("Qate: {}".format(err.error_map))
    def __BOS_ID_ORYNDARY(self):
        try:
            with self.__mydb.cursor() as cr:
                query = "SELECT id FROM searchengine.corpora;"
                cr.execute(query)
                res = cr.fetchall()
                mas = [] 
                for i in res:
                    mas.append(i.get("id",""))
                i = 0
                k = 1
                self.__mas2 = []
                while(i < len(mas)):
                    if k != mas[i]:
                        self.__mas2.append(k)
                        i -= 1
                    i += 1
                    k += 1
            self.__mydb.commit()
            return self.__mas2
        except:
            print("Qate: {}".format(err.error_map))
    def SONGY_ID_GENRES(self):
        try:
            with self.__mydb.cursor() as cr:
                query = "SELECT MAX(id) FROM searchengine.genres;"
                cr.execute(query)
                res = cr.fetchone()
                n = int(res.get("MAX(id)",""))
            self.__mydb.commit()
            return n
        except:
            print("Qate: {}".format(err.error_map))
    def SONGY_ID_CORPORA(self):
        try:
            with self.__mydb.cursor() as cr:
                query = "SELECT MAX(id) FROM searchengine.corpora;"
                cr.execute(query)
                res = cr.fetchone()
                n = int(res.get("MAX(id)",""))
            self.__mydb.commit()
            return n
        except:
            print("Qate: {}".format(err.error_map))
