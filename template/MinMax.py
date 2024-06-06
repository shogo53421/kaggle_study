from sklearn.preprocessing impoer MinMaxScaler
#学習データに基づいて複数列のMin-Maxスケーリングを定義
scaler = MinMaxScaler()
scaler.fir(train_x[cols])

#変換後のデータで各列を置換
train_x[cols] = scaler.transform(train_x[cols])
test_x[cols] = scaler.transform(test_x[cols])