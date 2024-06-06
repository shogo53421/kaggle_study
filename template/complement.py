repair = '' #補完するデータの名前

train_x[repair].fillna(train_x[repair].mode()[0], inplace = True)
test_x[repair].fillna(test_x[repair].mode()[0], inplace = True)