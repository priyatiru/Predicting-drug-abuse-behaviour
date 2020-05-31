import gensim
import logging

# for gensim to output some progress information while it's training
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
for f in range(1,405):
    corpus = gensim.corpora.textcorpus.TextCorpus("sample/csp1.txt")

    model = gensim.models.LdaModel(corpus, id2word=corpus.dictionary,
                                   alpha='auto',
                                   num_topics=10,
                                   passes=50)
 
    #file = open("ldatimeline/tweets"+str(f)+".txt","a")
    txt = ""
    for i in model.show_topic(5):
        txt = txt+"('"+i[0]+"', "+str(i[1])+"), "
    txt = txt.rstrip(", ")
    txt = "["+txt+"]\n"
    file.write(txt)
    list1 = []
    for topic_id in range(model.num_topics):
        topk = model.show_topic(topic_id, 15)
        topk_words = [ w for w, _ in topk ]
        list1.append(" ".join(topk_words))
     #   file.write('{}: {}'.format(topic_id, ' '.join(topk_words)))
      #  file.write('\n')
    #file.close()

