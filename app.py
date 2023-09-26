from flask import *
import sqlite3

conn = sqlite3.connect('music.db')

c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS songs (
   id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   author TEXT NOT NULL,
   duration TEXT NOT NULL
);''')
# (c.execute('''INSERT INTO songs (id, name, author, duration)
# VALUES (1, 'perfect', 'ed', '1:00');'''))



conn.commit()

c.close()
conn.close()

def saveData(data):
    lis=data.split(';')
    id=lis[0]
    name=lis[1]
    dur=lis[2]
    if len(id) == 2:
        artNum=int(id[0])
    elif len(id) == 3:
        artNum=int(id[0]+id[1])
    artNum-=1
    artNum=artNum//5
    artDic={0:"Ed Sheeran",1:"One Direction",2:"Taylor Swift",3:"Back Street Boys",4:"Imagine Dragons"}
    author=artDic[artNum]
    # print(author,name,dur,id)
    conn = sqlite3.connect('music.db')
    c = conn.cursor()

    (c.execute("SELECT * FROM songs WHERE id="+id+";"))
    rows = c.fetchall()
    if len(rows)==0:
       (c.execute('INSERT INTO songs (id, name, author, duration) VALUES ("'+id+'", "'+name+'", "'+author+'", "'+dur+'");')) 

    (c.execute("SELECT * FROM songs;"))
    rows = c.fetchall()
    print(rows)

    conn.commit()
    c.close()
    conn.close()

def remData(id):
        
    conn = sqlite3.connect('music.db')
    c = conn.cursor()

    c.execute("DELETE FROM songs WHERE id="+id+";")

    conn.commit()
    c.close()
    conn.close()

def getData():
    conn = sqlite3.connect('music.db')
    c = conn.cursor()

    (c.execute("SELECT * FROM songs;"))
    data = c.fetchall()

    conn.commit()
    c.close()
    conn.close()

    return data

app = Flask(__name__)
    
@app.route("/")
def home() -> str:
    return render_template("home.html")
    
    
@app.route("/home.html")
def hoe() -> str:
    return render_template("home.html")
    
    
@app.route("/about.html")
def about() -> str:
    return render_template("about.html")
    
    
@app.route("/album.html")
def album() -> str:
    return render_template("album.html")
    
    
@app.route("/album2.html")
def album2() -> str:
    return render_template("album2.html")
    
    
@app.route("/album3.html")
def album3() -> str:
    return render_template("album3.html")
    
    
@app.route("/album4.html")
def album4() -> str:
    return render_template("album4.html")
    
    
@app.route("/album5.html")
def album5() -> str:
    return render_template("album5.html")
    
@app.route("/artists.html")
def artst() -> str:
    return render_template("artists.html")
    
@app.route("/search.html")
def search() -> str:
    return render_template("search.html")
    
@app.route("/spotlight.html")
def spot() -> str:
    return render_template("spotlight.html")

@app.route("/playlist.html", methods=['GET','POST'])
def play() -> str:
    if request.method == 'POST':
        id = request.form['butt']
        remData(id)
    data=getData()
    print(".........",data)
    ids=[]
    authors=[]
    names=[]
    durs=[]
    for dat in data:
        ids.append(dat[0])
        authors.append(dat[2]) 
        names.append(dat[1]) 
        durs.append(dat[3]) 
    print(authors,durs,names,ids)
    return render_template("playlist.html",ids=ids,authors=authors,names=names,durs=durs)
    
    
    
    
@app.route("/music01.html", methods=['GET','POST'])
def mu1() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music01.html")
    
@app.route("/music02.html", methods=['GET','POST'])
def mu2() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music02.html")
    
@app.route("/music03.html", methods=['GET','POST'])
def mu3() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music03.html")
    
@app.route("/music04.html", methods=['GET','POST'])
def mu4() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music04.html")
    
@app.route("/music05.html", methods=['GET','POST'])
def mu5() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music05.html")
    
@app.route("/music06.html", methods=['GET','POST'])
def mu6() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music06.html")
    
@app.route("/music07.html", methods=['GET','POST'])
def mu7() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music07.html")
    
@app.route("/music08.html", methods=['GET','POST'])
def mu8() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music08.html")
    
@app.route("/music09.html", methods=['GET','POST'])
def mu9() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music09.html")
    
@app.route("/music10.html", methods=['GET','POST'])
def mu10() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music10.html")
    
@app.route("/music11.html", methods=['GET','POST'])
def mu11() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music11.html")
    
@app.route("/music12.html", methods=['GET','POST'])
def mu12() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music12.html")
    
@app.route("/music13.html", methods=['GET','POST'])
def mu13() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music13.html")
    
@app.route("/music14.html", methods=['GET','POST'])
def mu14() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music14.html")
    
@app.route("/music15.html", methods=['GET','POST'])
def mu15() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music15.html")
    
@app.route("/music16.html", methods=['GET','POST'])
def mu16() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music16.html")
    
@app.route("/music17.html", methods=['GET','POST'])
def mu17() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music17.html")
    
@app.route("/music18.html", methods=['GET','POST'])
def mu18() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music18.html")
    
@app.route("/music19.html", methods=['GET','POST'])
def mu19() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music19.html")
    
@app.route("/music20.html", methods=['GET','POST'])
def mu20() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music20.html")
    
@app.route("/music21.html", methods=['GET','POST'])
def mu21() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music21.html")
    
@app.route("/music22.html", methods=['GET','POST'])
def mu22() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music22.html")
    
@app.route("/music23.html", methods=['GET','POST'])
def mu23() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music23.html")
    
@app.route("/music24.html", methods=['GET','POST'])
def mu24() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music24.html")
    
@app.route("/music25.html", methods=['GET','POST'])
def mu25() -> str:
    if request.method == 'POST':
        data = request.form['butt']
        saveData(data)
    return render_template("music25.html")
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
