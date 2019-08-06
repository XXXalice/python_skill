# python_skill
pythonの小技・テク

## 競プロ関連
[これ](./fast_input.py)

* 標準入力のイロハ

```open().readline```を関数オブジェクトとして用いることで高速で沢山の行数のinputが行える



## ソフト開発関連

### 削除関連

* shutil.rmtree()

* * ワイルドカード

  脳死でディレクトリのパス投げればいい

  投げたディレクトリ自体も消えるから

  ```python
  import shutil, os
  shutil.rmtree(path=ぱす)
  os.makedirs(ぱす)
  ```

  

  こんなかんじがスマート

  

  * 消したくない例外がある

  ```python
  import shutil, os, sys
  ぱす = './rm_target'
  れーがい = './rm_target/極秘エロ画像.png'
  ひなんじょ = '.'
  shutil.copy(れーがい, ひなんじょ)
  runaway = os.path.join(ひなんじょ, れーがい.split('/')[-1])
  try:![os_path_join](/Users/umemiya/Desktop/python_skill/src/os_path_join.png)
    shutil.rmtree(path=ぱす)
    os.makedirs(ぱす)
    shutil.copy(runaway, ぱす)
  except:
    sys.stderr.write('失敗した失敗した失敗した\n')
  finally:
    os.remove(runaway)
  ```

  例外の疎開先を提示して一時コピー

  ↓

  フォルダごとバニッシュからのmkdir

  ↓

  バニッシュにエラっても避難所にいる例外デコイは消えて終了  

    

  もっと安全でスマートな書き方があるかも



### パス関連

* os.path.join()

空stringを突っ込むと無視される　これが意外と役に立つ

![os_path_join](/Users/umemiya/Desktop/python_skill/src/os_path_join.png)

