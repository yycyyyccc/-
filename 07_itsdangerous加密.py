
 pip install itsdangerous

 from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


 Serializer() 创建对象，可以产生过期时间

 serializer = Serializer('密钥', 过期时间)

info = {'confirm':1}

res = serializer.dumps(info) # 加密

                .loads()  # 解密


