# Quplot
PyQtによるmatplotlibのGUIアプリ
![DEMO](https://github.com/yoshizawa56/Quplot/blob/master/screen.gif)

# インストール方法
実行可能ファイルとしてビルドされたプログラムを利用します。
## MAC
[https://github.com/yoshizawa56/Quplot/releases](https://github.com/yoshizawa56/Quplot/releases) からQuplot.app.zipをダウンロード・解凍して、できた.appファイルをAppricationに追加して使用してください。

## Windows
未対応（対応予定）



# 使い方
## プロットの作成
必要項目を入力して、「Plot!!」ボタンを押すか、[Enter]キーを入力するとプロットが作成されます。

## プロットするデータの選択
ファイルからデータを取得する方法と、関数を入力する方法があります。
データは複数個指定することもできます。

### ファイルから取得
「Data source」の項目で、「File」を選択すると使えます。
読み込みたいパスを絶対パスで入力します。「Reference」ボタンでファイルを参照して入力することもできます。
ファイルのデータ形式については後述の「データ形式」を参照

### 関数を入力
「Data source」の項目で、「Function」を選択すると使えます。
数式やnumpyの関数などを入力することができます。

例）
```
2 * np.sin(x/2) + 1
```

関数をプロットする際には、定義域を決めるために「Range」にプロットしたい範囲を入力してください。
（「Data Source」と「X-Axis」のどちらの「Range」でも構いません。）

## プロットのエクスポート、インポート
プロットの設定をjson形式でエクスポート、インポートできます。

### エクスポート
現在の入力状態をjson形式のファイルに出力します。右上の「Export」ボタンを押して、出力先を指定すると保存できます。（拡張子は任意ですが、.jsonを推奨）

### インポート
エクスポートしたjsonファイルを読み込んで、入力領域に反映します。右上の「Import」ボタンを押して、エクスポートファイルを選択すると行えます。

また、右上の「Import last plot」ボタンを押すと、最新のプロットを行った際の状態にすることができます。

## プロットの保存
右下の「Save」ボタンを押すことで、現在のプロットを指定した保存先に画像ファイルとして保存できます。保存するファイル名の拡張子を変更することで、画像形式を変更できます。（.pdf, .eps, .pngなど）

また、保存先を指定しないで「Save」ボタンを押すと、デフォルト保存先のディレクトリに「yyyy_mm_dd_HH_MM_SS.pdf」のファイル名で保存されます。デフォルト保存先ディレクトリは後述のデフォルト値設定画面から指定することができます。

## 設定の変更
プロットの際のデフォルト値や使える色などを変更することができます。

### デフォルト値の変更
メニューから「Default value config」を選択するとデフォルト値設定画面が表示されます。変更したい項目を入力した上で「Apply」ボタンを押すと、デフォルト設定が変更されます。

### 色やマーカーの追加
メニューから「Colors and markers」を選択すると、色とマーカーを追加・変更する画面が表示されます。追加・削除・並び替えを行った上で、「Apply」ボタンを押すと、設定が反映されます。

# データ形式
テキスト形式とCSV形式に対応しています。

## コメント
- テキスト、CSVともに共通。
- 「#」がコメントとして認識されます。
- ファイルの1行目が「##」から始まる場合は、列名と認識します。
- ファイルの2行目が「##」から始まる場合は、プロットの際に表示する列のラベル（LaTeX表式）と認識します。
- 「##」行では「カンマ」を区切り文字として、各列を認識します。
- 識別文字「##」は設定で任意の値に変更できます。

例）
```
##x,sin_x,cos_x,log_x
##x,\sin x,\cos x,\log x
```

## テキスト形式
区切り文字はスペースまたはタブ

## CSV形式
区切り文字はカンマ
