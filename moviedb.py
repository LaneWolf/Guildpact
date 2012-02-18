import os
import sqlite3

class MovieDB:
    def __init__(self,dbname):
        self.mLastId = 0
        self.mData = {}
        self.mFilename = dbname

        self.load()


    def load(self):
        if os.access(self.mFilename,os.R_OK) == True:
            con = sqlite3.connect(self.mFilename)
            curs = con.cursor()

            curs.execute("Select * from filmdb ORDER by id")
            for rec1 in curs.fetchall():
                fr = {}
                fr['id'] = rec1[0]
                fr['name'] = rec1[1]
                fr['year'] = rec1[2]
                fr['location'] = rec1[3]

                curs.execute("Select * from valuedb WHERE fid = ?",(fr['id'],))
                for rec2 in curs.fetchall():
                    fr[rec2[1]] = rec2[2]

                self.mData[fr['id']] = fr
                if self.mLastId < fr['id']:
                    self.mLastId = fr['id']
            con.close()


    def initDB(self):
        con = sqlite3.connect(self.mFilename)
        curs = con.cursor()

        curs.execute("""CREATE TABLE filmdb ( 
                            id INTEGER PRIMARY KEY, 
                            name TEXT NOT NULL, 
                            year INTEGER CHECK (year > 1900), 
                            location TEXT NOT NULL)""")
        curs.execute("""CREATE TABLE valuedb ( 
                            fid INTEGER REFERENCES filmdb(id), 
                            name TEXT NOT NULL, 
                            value TEXT)""")

        con.commit()
        return con


    def save(self):
        if os.access(self.mFilename,os.F_OK) == True:
            bckname = "%s.bck" % self.mFilename
            os.rename(self.mFilename,bckname)

        try:
            con = self.initDB()
            curs = con.cursor()

            for rid,rec in self.mData.items():
                curs.execute("""INSERT INTO filmdb (id,name,year,location) 
                    VALUES (?,?,?,?)""",
                    (rid,rec.get("name"),rec.get("year"),rec.get("location")))

                for key,val in rec.items():
                    if key in ["name","year","location","id"]:
                        continue
                    curs.execute("""INSERT INTO valuedb (fid, name, value) 
                        VALUES (?,?,?)""",(rid,key,val))

                con.commit()
            con.close()
        except:
            if con is not None:
                con.close()
            if os.access(bckname,os.F_OK) == True:
                if os.access(self.mFilename,os.F_OK) == True:
                    os.unlink(self.mFilename)
                os.rename(bckname,self.mFilename)


    def addFilm(self,name,year,location,attr):
        nf = {}
        self.mLastId = self.mLastId + 1
        nf['id'] = self.mLastId

        nf['name'] = name
        nf['year'] = year
        nf['location'] = location
        for (key,val) in attr:
            nf[key] = val

        self.mData[nf['id']] = nf
        return nf['id']

    
    def setFilmAttr(self,fid,key,val):
        f = self.mData.get(fid)
        if f is not None:
            f[key] = val
