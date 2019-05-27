# Shimeji

## Install
python3.6 ぐらいで作ってます。多分３系なら動く。２系でも動くかも。
webフレームワークとしてflaskを使ってます。インストールしてください。
```
pip3 install flask
```

## How to use
サーバー立ち上げ app.py を実行
```
python3 app.py
```

あとは 127.0.0.1:5000　にブラウザでアクセスしてください。
`template/index.html` の内容が表示されるはず。

## 開発者むけ情報
### スマホ操作画面
スマホから操作する画面は `template/index.html` を編集してください。
index.phpにしたい場合はapp.py の`index.html` の部分を編集してください。

### shimeji API
まだ、あんまりちゃんと決めてないですが
`127.0.0.1:5000/action` に動きの種類とパラメータをjson形式でPOSTするようにしようかと思います。

example ４秒間霧を吐く場合
```angular2
{
    "type": "blow_mist",
    "param": {
        "sec": 4
    }
}
```


example  10秒光る場合
```angular2
{
    "type": "light_up",
    "param": {
        "sec": 10
    }
}
```

shimejiの状態は `127.0.0.1:5000/action` にGETすると見れます。
ブラウザでも見れます。
```angular2
{"is_blowing_mist": false, "is_open": false, "is_lighting_up": false}
```
