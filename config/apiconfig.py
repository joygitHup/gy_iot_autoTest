host='http://192.168.20.212:5500'
'''初始header'''
header = '{"Content-Type":"application/json;charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}'
'''通过租户获取ID'''
getidbynameurl='/api/system/tenant/get-id-by-name'
'''通过id获取租户ID'''
tenantIdurl='/api/system/auth-rule/get/captcha'
'''通过租户ID和用户名'''
usernametendiD='/api/system/auth/login-failures'
'''登录接口'''
userlogiapi='/api/system/auth/login'