===================
モデルとスキーマ
===================

`tinycms` では、ドキュメントと画像ファイルを取扱います。
それぞれを ``Document`` クラス, ``PersistentImage`` クラスで定義します。

.. note::

   `tinycms` はストレージに :term:`ZODB` を利用します。
   :term:`ZODB` は、Pythonオブジェクトをそのまま保存できます。
   しかし、そのまま保存すると、そのオブジェクトが参照しているオブジェクトまでまるごと保存することになります。
   `persistent` を利用すると、参照しているオブジェクトを別々に保存して、必要なときに取り出されるようrになります。


Document
------------------------------

``Document`` は単純なオブジェクトです。
``title`` と ``contents`` の２つの属性を持ちます。
この２つの属性は、コンストラクタで受け取った内容をそのまま保存します。

.. literalinclude:: ../src/tinycms/models.py
   :pyobject: Document


PersistentImage
-------------------------------

``PersistentImage`` は、画像ファイルを取り扱います。
画像ファイルの内容は ``data`` という属性で保存します。
:term:``ZODB`` では、画像ファイルなどのような大きなデータを ``Blob`` というオブジェクトで保存します。

.. literalinclude:: ../src/tinycms/models.py
   :pyobject: PersistentImage


スキーマ
-----------------------------

:term:`Colander` は、フォームや、設定ファイル、 :term:`JSON` など様々な用途に使えるスキーマライブラリです。
手始めに、先ほど定義した ``Document``, ``PersistentImage`` のスキーマ定義をしてみましょう。

.. literalinclude:: ../src/tinycms/models.py
   :pyobject: DocumentSchema

.. literalinclude:: ../src/tinycms/models.py
   :pyobject: PersistentImageSchema

``PersistentImageSchema`` では、 画像ファイルだけを取り扱います。
そのために、アップロードされたファイルが画像ファイルであるか確認するために、 ``image`` バリデータを定義しています。

.. literalinclude:: ../src/tinycms/validators.py
   :pyobject: image





