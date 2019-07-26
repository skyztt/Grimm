from flask import Flask,request
import urllib3
import json
import config

app = Flask(__name__)

wx_appid = config.wx_appid
wx_secret = config.wx_appid

# http://127.0.0.1:5000/jscode2session?js_code=011WwOZv1HNcai08OB1w1bOVZv1WwOZm
# https://api.weixin.qq.com/sns/jscode2session?appid=wx4344453f7ef4347b&secret=24bab6cdf0b842d5f91978dd40d1cbea&js_code=011WwOZv1HNcai08OB1w1bOVZv1WwOZm&grant_type=authorization_code
@app.route('/jscode2session')
def wx_jscode2session():
	js_code = request.args.get("js_code")
	
	url = f'https://api.weixin.qq.com/sns/jscode2session?appid={wx_appid}&secret={wx_secret}&js_code={js_code}&grant_type=authorization_code'
	print('request url:', url)
	http = urllib3.PoolManager()
	response = http.request('GET', url)
	
	if response.status == 200:		
		response_data = response.data
		
		json_data = json.loads(response_data)
		json_data['server_errcode'] = 0
		
		# json_data['is_register'] = False
		json_data['is_register'] = False
		
		ret_data_str = json.dumps(json_data)
		print('response_data: ', ret_data_str)
	else:
		json_data = json.loads('{"server_errcode": -1}')
		ret_data_str = json.dumps(json_data)
	return ret_data_str
	
if __name__ == '__main__':
	app.run()