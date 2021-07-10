import json,time,os
from requests import Session
s = Session()
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
'X-CSRFToken':'klMtcv9FbwmJ2O1VRrQSDYoqbiKAUpRf',
'Cookie':'g_cb=1; ig_did=7C6F65B9-9D23-470F-B8E3-D2F3AFF47C98; csrftoken=klMtcv9FbwmJ2O1VRrQSDYoqbiKAUpRf; mid=X4MymwAEAAHgt_F9tnHQS9uwxPV_; ig_nrcb=1'
id="UserName" #
data = {'email_or_username':id,'recaptcha_challenge_field':'','flow':'','app_id':'','source_account_id':	""}
r=s.get("https://www.instagram.com/accounts/password/reset/",headers=head)
cookies={"csrftoken":s.cookies.get_dict().get('csrftoken'),"ig_cb":"1","ig_did":"7C6F65B9-9D23-470F-B8E3-D2F3AFF47C98",
"ig_nrcb":"1",'mid':"X4MymwAEAAHgt_F9tnHQS9uwxPV_"
}
head["csrftoken"]=s.cookies.get_dict().get('csrftoken')
r=s.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",headers=head,data=data,cookies=cookies)
print (r.status_code)
