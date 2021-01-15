import tensorflow as tf
import numpy as np

class inference:
    def __init__(self):
        self.model_name = "cnn3layers_full.h5"
        self.model = tf.keras.models.load_model(self.model_name)

    def label_prob(self,ds):
        pred_logits = self.model.predict(ds)
        probas = tf.sigmoid(pred_logits)
        labels=tf.argsort(probas,axis=-1,direction='DESCENDING')
        probas=tf.sort(probas,axis=-1,direction='DESCENDING')
        #print(probas)
        problist=[]
        labellist=[]
        for i in range(4):
            a=np.round(probas[0][i].numpy()*100,1)
            b=labels[0][i].numpy()
            problist.append(a)
            labellist.append(b)
        return (labellist,problist)
    
