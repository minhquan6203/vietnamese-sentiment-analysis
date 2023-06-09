from model.svm_model import createSVM_Model,SVM_Model
from model.transformer_model import createTrans_Model,Trans_Model
from model.transformer_svm_model import createTrans_SVM_Model,Trans_SVM_Model
from model.roberta_seq_classify import createRoberta_Model,Roberta_Model
from model.bert_cnn import createTextCNN_Model,TextCNN_Model

def build_model(config, answer_space):
    if config['model']['type_model']=='svm':
        return createSVM_Model(config, answer_space)
    if config['model']['type_model']=='trans':
        return createTrans_Model(config, answer_space)
    if config['model']['type_model']=='trans_svm':
        return createTrans_SVM_Model(config, answer_space)
    if config['model']['type_model']=='roberta':
        return createRoberta_Model(config, answer_space)
    if config['model']['type_model']=='bert_cnn':
        return createTextCNN_Model(config,answer_space)
    
def get_model(config, num_labels):
    if config['model']['type_model']=='svm':
        return SVM_Model(config, num_labels)
    if config['model']['type_model']=='trans':
        return Trans_Model(config, num_labels)
    if config['model']['type_model']=='trans_svm':
        return Trans_SVM_Model(config, num_labels)
    if config['model']['type_model']=='roberta':
        return Roberta_Model(config, num_labels)
    if config['model']['type_model']=='bert_cnn':
        return TextCNN_Model(config,num_labels)
