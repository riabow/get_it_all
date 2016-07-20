import time
import urllib2





gh_url = 'https://api.github.com'
gh_user= 'riabow'
gh_pass = 'Keertimc24'

req = urllib2.Request(gh_url)

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, gh_user, gh_pass)

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(req)

print handler.getcode()
print handler.headers.getheader('content-type')


n=0


while True:
    time.sleep(1) # delays for 5 seconds
    print ("aaa"+str(n))
    n+=1
    if n==3 :
        break

