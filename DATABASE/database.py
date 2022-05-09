import sqlite3
# from DATABASE.database import DATABASE
class DATABASE:
    @staticmethod
    def DataBase():
        try:
            DBMS = sqlite3.connect('DATABASE/NKLPVTLimit.com.db')
            pointer = DBMS.cursor()
            DBMS.row_factory = sqlite3.Row
            cursor = DBMS.cursor()
            return DBMS, pointer, cursor
        except Exception:
            pass





    @staticmethod
    def QuestionNumber():
        DB, pointer, _ = DATABASE.DataBase()
        DBMS = pointer.execute('select QNO, STATUS from QuestionPaper').fetchall()
        return DBMS

    @staticmethod
    def Question(Quiz):
        DB, pointer, _ = DATABASE.DataBase()
        DBMS =pointer.execute(f'select QuestionPaper from QuestionPaper where QNO="{Quiz}" ').fetchone()
        return DBMS

    @staticmethod
    def next_Quiz(Quiz):
        try:
            DB, pointer, _ = DATABASE.DataBase()
            num =pointer.execute(f'select SNO from QuestionPaper where QNO="{Quiz}"').fetchone()
            next_num = num[0] + 1
            Quiz =pointer.execute(f'select QNO from QuestionPaper where SNO="{next_num}"').fetchone()[0]

            return Quiz
        except Exception:
            pass

    @staticmethod
    def last_Quiz(Quiz):
        DB, pointer, _ = DATABASE.DataBase()
        last =pointer.execute(f'select max(SNO) from QuestionPaper').fetchone()[0]
        num = pointer.execute(f'select SNO from QuestionPaper where QNO="{Quiz}"').fetchone()[0]
        if last == num:
            return True
        else:
            return False

    @staticmethod
    def ExamStart(Quiz, Exam_time, Exam_date):
        DB, pointer, _ = DATABASE.DataBase()
        pointer.execute(
            f'''insert into MarkSheet(QNO, ExamStart, ExamDate )VALUES("{Quiz}", "{Exam_time}", "{Exam_date}")''')
        DB.commit()
        SNO = pointer.execute('select max(SNO) from Marksheet').fetchone()[0]

        return SNO

    @staticmethod
    def ExamComplete(SNO, ExamMark, Wrong, Speed, ExamFinish):
        DB, pointer, _ = DATABASE.DataBase()
        pointer.execute(f'''update Marksheet set ExamMark="{ExamMark}" ,
             WrongAns="{Wrong}" , Speed="{Speed}" ,  ExamComplete="{ExamFinish}" where SNO="{SNO}" ''')
        DB.commit()

    @staticmethod
    def RESULT(Quiz):
        DB, pointer, _ = DATABASE.DataBase()
        SNO =pointer.execute(f'SELECT SNO FROM QuestionPaper WHERE QNO="{Quiz}" ').fetchone()[0] + 1
        pointer.execute(f'UPDATE QuestionPaper SET STATUS="UNLOCK" WHERE SNO={SNO} ')
        DB.commit()

    @staticmethod
    def PassMark(Quiz):
        DB, pointer, _ = DATABASE.DataBase()
        DBMS = pointer.execute(f'SELECT PMark FROM QuestionPaper WHERE QNO="{Quiz}" ').fetchone()
        return DBMS[0]

    @staticmethod
    def MarkSheet():
        try:
            DB, pointer, cursor = DATABASE.DataBase()
            DBMS = pointer.execute('''select * from MarkSheet''').fetchall()
            HEADER = cursor.execute('''select * from MarkSheet''').fetchone().keys()
            return HEADER, DBMS

        except Exception:
            return 'Data Not Found !!'

    @staticmethod
    def NewAccount(database, userId, password, account, PERMISSIONS):
        DB, pointer, _ = DATABASE.DataBase()
        pointer.execute(f'''INSERT INTO AccountDataBase(NAME, FATHER, DOB, MOBILE, GMAIL, ADDRESS , UNAME, PASSWORD,
                                    ACCOUNT_TYPE, PERMISSIONS )     VALUES(
                    '{database[0]}','{database[1]}','{database[2]}','{database[3]}', '{database[4]}',
                    '{database[5]},{database[6]},{database[7]},{database[8]},{database[9]}',
                     "{userId}", "{password}", "{account}",'{", ".join(PERMISSIONS)}'
                             )
                     ''')
        DB.commit()

    @staticmethod
    def AccountList():
        try:
            DB, pointer, _ = DATABASE.DataBase()
            DBMS = pointer.execute('''select NAME, UNAME from AccountDataBase''').fetchall()
        except Exception:
            DBMS = None
        return DBMS

    @staticmethod
    def QuestionPaper():
        try:
            DB, pointer, cursor = DATABASE.DataBase()
            DBMS =pointer.execute('''select * from QuestionPaper''').fetchall()
            HEADER = cursor.execute('''select * from QuestionPaper''').fetchone().keys()
            return HEADER, DBMS
        except Exception:
            return 'Data Not Found !!'

    @staticmethod
    def MaxQuiz():
        try:
            DB, pointer, _ = DATABASE.DataBase()
            db = pointer.execute(f'select max(SNO) from QuestionPaper').fetchone()[0]
        except Exception:
            db = 0
        return int(db) + 1

    @staticmethod
    def DelAccount(userId):
        DB, pointer, _ = DATABASE.DataBase()
        pointer.execute(f''' delete from AccountDataBase where UNAME="{userId}" ''')
        DB.commit()

    @staticmethod
    def AccountDetails(userId):
        DB, pointer, _ = DATABASE.DataBase()
        return pointer.execute(f'''select NAME, FATHER, DOB, MOBILE, GMAIL, ADDRESS , ACCOUNT_TYPE, UNAME,
             PASSWORD from AccountDataBase where UNAME="{userId}" ''').fetchone()

    @staticmethod
    def Gmail(gmail):
        DB, pointer, _ = DATABASE.DataBase()
        return pointer.execute(f"select GMAIL from AccountDataBase where GMAIL= '{gmail}' ").fetchone()

    @staticmethod
    def detailsChecking(database):
        DB, pointer, _ = DATABASE.DataBase()
        return pointer.execute(
            f"select NAME from AccountDataBase where FATHER='{database[1]}' and DOB='{database[2]}'"
            f" and MOBILE= {database[3]} ").fetchall()

    @staticmethod
    def idChecking(userId):
        DB, pointer, _ = DATABASE.DataBase()
        return pointer.execute(f"select UNAME from AccountDataBase where UNAME= '{userId}' ").fetchone()

    @staticmethod
    def LogIn(userId, password):
        try:
            DB, pointer, _ = DATABASE.DataBase()
            return pointer.execute(f'''select NAME, FATHER, DOB, MOBILE, GMAIL, ADDRESS , ACCOUNT_TYPE, UNAME,
                     PASSWORD from AccountDataBase where UNAME='{userId}' and PASSWORD='{password}' ''').fetchone()
        except Exception:
            pass

    @staticmethod
    def QuestionInsert(QNO, Quiz, PMark, sign):
        try:
            DB, pointer, _ = DATABASE.DataBase()
            pointer.execute(
                f'''INSERT INTO QuestionPaper(QNO, QuestionPaper, PMark, INCHARGE) VALUES("TEST {QNO}", "{Quiz}", {PMark}, "{sign}" )
        ''')
            DB.commit()
            return True
        except Exception:
            pass

    @staticmethod
    def Incharge(Quiz):
        DB, pointer, _ = DATABASE.DataBase()
        DBMS = pointer.execute(f'SELECT INCHARGE FROM QuestionPaper WHERE QNO="{Quiz}" ').fetchone()
        return DBMS[0]

    @staticmethod
    def CreateDataBase():
        try:
            DB, pointer, _ = DATABASE.DataBase()
            # ==================  Create QuestionPaper table =========================================================
            pointer.execute('''CREATE TABLE IF NOT EXISTS QuestionPaper(
                    SNO INTEGER PRIMARY KEY AUTOINCREMENT,
                    QNO VARCHAR NOT NULL UNIQUE,
                    QuestionPaper TEXT NOT NULL,
                    PMark INTEGER NOT NULL DEFAULT 25,
                    STATUS BOOLEAN CHECK( STATUS IN ("LOCK", "UNLOCK") ) NOT NULL DEFAULT "LOCK",
                    INCHARGE VARCHAR NOT NULL DEFAULT "SYSTEM"
                    )''')

            # ==================  Create Marksheet table =========================================================

            pointer.execute('''CREATE TABLE IF NOT EXISTS MarkSheet(
                    SNO INTEGER PRIMARY KEY AUTOINCREMENT,
                    QNO VARCHAR NOT NULL,
                    ExamMark VARCHAR NOT NULL DEFAULT "NOT SUBMITTED",
                    WrongAns VARCHAR NOT NULL DEFAULT "NOT SUBMITTED",
                    Speed VARCHAR NOT NULL DEFAULT "NOT SUBMITTED",
                    ExamStart VARCHAR NOT NULL,
                    ExamComplete VARCHAR NOT NULL DEFAULT "INCOMPLETE",
                    ExamDate VARCHAR NOT NULL
                    )''')

            # ==================  Create AccountDAtaBase Table =========================================================

            pointer.execute('''CREATE TABLE IF NOT EXISTS AccountDataBase(
                    NAME VARCHAR NOT NULL,
                    FATHER VARCHAR NOT NULL,
                    GENDER BOOLEAN CHECK(GENDER IN ("MALE", "FEMALE", "OTHER" ) ) NOT NULL DEFAULT "OTHER",
                    DOB VARCHAR NOT NULL,
                    MOBILE INTEGER NOT NULL,
                    GMAIL VARCHAR NOT NULL UNIQUE,
                    ADDRESS VARCHAR NOT NULL,
                    UNAME VARCHAR NOT NULL UNIQUE,
                    PASSWORD PASSWORD NOT NULL,
                    ACCOUNT_TYPE BOOLEAN CHECK( ACCOUNT_TYPE IN ("STANDARD ACCOUNT", "NORMAL ACCOUNT") ) NOT NULL,
                    PERMISSIONS VARCHAR
                     )''')

            # ==================  Create Default Questions =========================================================

            Quiz1 = '''The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog. The Quick Brown Fox Jumps Over the Lazy Dog.'''
            Quiz2 = '''The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs. The Quick Brown Fox Jumped Over The Lazy Dogs.'''
            Quiz3 = '''Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog. Quick Brown Fox Jumps Over The Lazy Dog.'''
            Quiz4 = '''Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard. Quick Fox Jumps Nightly Above Wizard.'''
            Quiz5 = '''Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job. Fox Dwarves Chop My Talking Quiz Job.'''
            Quiz6 = '''How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex. How Quickly Daft Jumping Zebras Vex.'''
            Quiz7 = '''Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip. Hick Dwarves Jam Blitzing Foxy Quip.'''
            Quiz8 = '''Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz. Both Fickle Dwarves Jinx My Pig Quiz.'''
            Quiz9 = '''Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz. Sex Charged Fop Blew My Junk TV Quiz.'''
            Quiz = '''The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly. The Five Boxing Wizards Jump Quickly.'''

            # ==================  Create Default Questions Entry =========================================================

            pointer.execute(
                f'INSERT INTO QuestionPaper(QNO, QuestionPaper, STATUS) VALUES("TEST 1", "{Quiz1.lower()}", "UNLOCK")')

            pointer.execute('SELECT MAX(SNO) FROM QuestionPaper')
            SNO = pointer.fetchone()[0]
            # print(SNO)


            pointer.execute(
                f'''INSERT INTO QuestionPaper(QNO, QuestionPaper) VALUES("TEST {SNO + 1}","{Quiz1.upper()}"),
                    ("TEST {SNO + 2}","{Quiz1}"), ("TEST {SNO + 3}","{Quiz2.lower()}"), ("TEST {SNO + 4}","{Quiz2.upper()}"), ("TEST {SNO + 5}","{Quiz2}")
                    , ("TEST {SNO + 6}","{Quiz3.lower()}"), ("TEST {SNO + 7}","{Quiz3.upper()}"), ("TEST {SNO + 8}","{Quiz3}")
                    , ("TEST {SNO + 9}","{Quiz4.lower()}"), ("TEST {SNO + 10}","{Quiz4.upper()}"), ("TEST {SNO + 11}","{Quiz4}")
                    , ("TEST {SNO + 12}","{Quiz5.lower()}"), ("TEST {SNO + 13}","{Quiz5.upper()}"), ("TEST {SNO + 14}","{Quiz5}")
                    , ("TEST {SNO + 15}","{Quiz6.lower()}"), ("TEST {SNO + 16}","{Quiz6.upper()}"), ("TEST {SNO + 17}","{Quiz6}")
                    , ("TEST {SNO + 18}","{Quiz7.lower()}"), ("TEST {SNO + 19}","{Quiz7.upper()}"), ("TEST {SNO + 20}","{Quiz7}")
                    , ("TEST {SNO + 21}","{Quiz8.lower()}"), ("TEST {SNO + 22}","{Quiz8.upper()}"), ("TEST {SNO + 23}","{Quiz8}")
                    , ("TEST {SNO + 24}","{Quiz9.lower()}"), ("TEST {SNO + 25}","{Quiz9.upper()}"), ("TEST {SNO + 26}","{Quiz9}")
                    , ("TEST {SNO + 27}","{Quiz.lower()}"), ("TEST {SNO + 28}","{Quiz.upper()}"), ("TEST {SNO + 29}","{Quiz}")
                    ''')
            DB.commit()
            return "successful"
        except sqlite3.IntegrityError:
            return 'overwrite'
        # except Exception as error:
        #     return str(f'{type(error)} : error')