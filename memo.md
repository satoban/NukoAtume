# 開発作業メモ

- Djangoの基本的流れ  
    [1] アプリ内のvies.pyでロジックを作成する  
    [2] アプリ内のurls.pyでURLを作成する  

- Middlewareとは？  
   「Djangoのリクエスト/レスポンス処理の前後でフックを加える仕組み」  
   「フックとは、プログラムの特定箇所にユーザーが作成した処理を追加して実行する仕組みのこと」  
   'https://office54.net/python/django/django-middleware-about'  
   DjangoにおけるMiddlewareは、各ビュー関数で共通して行いたい処理を記述するものです。

- Djangoのマイグレーションとは？  
   マイグレーションは、Djangoでモデルに対して行った変更（フィールドの追加やモデルの削除など）をデータベーススキーマに反映させる方法  
   マイグレーションに関する操作  
  'https://zenn.dev/wtkn25/articles/django-migration'  

- renderメソッドとは  
   レンダリングは、あるデータを加工して表現（表示）すること。  
   Djangoにおけるrenderメソッドとは、多くの情報（request,template_name, context等）の情報を加工してhtmlファイルに上手に表現する仕組み。  
   'https://codor.co.jp/django/about-rendering'  

   request ・・・ セッションの情報やrequestの種類(get,post)の情報  
   template_name ・・・ 表示するhtmlファイルの情報  
   context ・・・ データベースに入っているデータの情報  

- views.pyでビュー関数を記述する
   記述のポイントとしては
   1. 関数では必ず引数「requestを受け取る」こと  
   2. ファイル名の記述は、templatesフォルダ以下のパスとすること  
   'https://itc.tokyo/django/html/'
