import requests
import os

def GetSubString(body, str1, str2):
    if str1 in body:
        bg = body.find(str1)
        if str2 in body:
            en = body.find(str2, bg )
            if en>0:
                #print bg
                #print en
                return ( body[bg+len(str1):en])
            else:
                return ('en<0')
        else:
            return('No str2 in body')
    else:
        return('No str1 in body')




class a53s():

    session =""
    passdata = {'login': 'NosovE',
                 'pass': '12345',}



    def f(self):
        return 'hello world'
    def login(self):
        URL_login = "http://a53s.ru/login.php"
        self.session = requests.session()
        r = self.session.post(URL_login, data=self.passdata)
        #print self.session.

    def GetReport(self):
        URL = "http://a53s.ru/sort/poraskl3.php"
        r = self.session.post(URL,data=self.passdata)
        #print "code:"+str( r.status_code)

        #print "headers:"+str(r.headers)
        TMPfilepath = 'file_name.html'
        f = open(TMPfilepath, 'wb')
        f.write(r.content)
        f.close()
        os.startfile(TMPfilepath)

        return( r.content)

ll = a53s()
ll.login()
body =ll.GetReport()
MyD = GetSubString(body, 'Array','<table cellpadding="0" cellspacing="0" border="0" id="table" class="sortable" style="padding: 2px;">')
sql = GetSubString(body, '''<BR><BR><BR><br />''','''<BR><BR><BR>				<tr>''')



'''<BR><BR><BR>				<tr>
             <td class="brd">'''

# print(body)
print MyD
print sql



exit(0)


p = requests.get("http://google.com")
passdata = {'login': 'NosovE',
            'pass': '12345'}


payload1 = {
    'barcode': 'your user name/login',
    'telephone_primary': 'your password',
    'persistent': '1'  # remember me
}

URL_login = "http://a53s.ru/login.php"
session = requests.session()
r = session.post(URL_login, data=passdata)
print session.cookies
#print r.content

#exit(0)

print "*"
print "*"
print "*"
print "*"
URL = "http://a53s.ru/sort/poraskl3.php"
r = session.post(URL,data=passdata)
#This is quite easy. Then you can do like this:
print "code:"+str( r.status_code)

print "headers:"+str(r.headers)
print "content:"+ r.content