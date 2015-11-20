from flask import Flask
from flask import request

app = Flask(__name__)


def deg2HMS(ra='', dec='', round=False):
  RA, DEC, rs, ds = '', '', '', ''
  if dec:
    if str(dec)[0] == '-':
      ds, dec = '-', abs(dec)
    deg = int(dec)
    decM = abs(int((dec-deg)*60))
    if round:
      decS = int((abs((dec-deg)*60)-decM)*60)
    else:
      decS = (abs((dec-deg)*60)-decM)*60
    DEC = '{0}{1} {2} {3}'.format(ds, deg, decM, decS)
  
  if ra:
    if str(ra)[0] == '-':
      rs, ra = '-', abs(ra)
    raH = int(ra/15)
    raM = int(((ra/15)-raH)*60)
    if round:
      raS = int(((((ra/15)-raH)*60)-raM)*60)
    else:
      raS = ((((ra/15)-raH)*60)-raM)*60
    RA = '{0}{1} {2} {3}'.format(rs, raH, raM, raS)
  
  if ra and dec:
    return (RA, DEC)
  else:
    return RA or DEC


@app.route("/")
def hello():
  if request.args.get('ra', ''):
    ra = float(request.args.get('ra', ''))
    de = float(request.args.get('de', ''))
    posi = deg2HMS(ra,de)
    return "<h1>Welcome to FlandersFinder</h1> <h3>RA=" + str(ra) + " DE=" + str(de) + " HMS=" + str(posi) + "</h3>"
  else:
    return "<h1>Welcome to FlandersFinder</h1> <h3>Use me to get HMS like this:<h3><ul><li>http://flandersfinder.herokuapp.com?ra=53.084&de=-27.873</li></ul>"    
if __name__ == "__main__":
    app.run()