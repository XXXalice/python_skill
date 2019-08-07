import inspect

# カレントから見て何層下か（ex:3）
hierarchy = 3

# pythonが実行されている起点に関係なくアクセスしたいパスの位置を入手する
nowpath = '/'.join(inspect.stack()[0][1].split('/')[:-hierarchy])

# そこから任意の直下フォルダにアクセスしたい場合
target_path = os.path.join(nowpath, 任意)
