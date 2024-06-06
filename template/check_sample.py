filename = '' #コンテスト名
# sample_submission.csvの読み込み
submission_df = pd.read_csv('/kaggle/input/' + filename + '/sample_submission.csv')
# sample_submission.csvの形式を確認するために先頭五行を見てみる。
submission_df.head()