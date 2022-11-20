

import gensim
import gensim.downloader as download_api
russian_model = download_api.load('word2vec-ruscorpora-300')

from gensim.models.doc2vec import Doc2Vec, LabeledSentence
