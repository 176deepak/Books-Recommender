import sys
import numpy as np
from src.books_recommender.constants import *
from src.books_recommender.exception import CustomException
from src.books_recommender.utils.common import pickled_loader, read_yaml


def recommender(book_name):
    config = read_yaml(CONFIG_YAML_FILE)
        
    data_path = config.model_trainer.data_path
    data = pickled_loader(data_path)

    model_path = config.model_trainer.model_path
    model = pickled_loader(model_path)

    score_path = config.model_trainer.similarity_score
    scores = pickled_loader(score_path)

    index = np.where(model.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    books = []
    for i in similar_items:
        item = []
        temp_df = data[data['Book-Title'] == model.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-L'].values))
        
        books.append(item)
    
    return books
