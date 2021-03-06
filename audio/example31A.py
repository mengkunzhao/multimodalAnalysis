"""! 
@brief Example 31A
@details: Train a speech-music classifier
@author Theodoros Giannakopoulos {tyiannak@gmail.com}
"""
from pyAudioAnalysis.audioTrainTest import featureAndTrain

if __name__ == '__main__':
    mt = 1.0
    st = 0.05
    dir_paths = ["../data/speech_music/speech", "../data/speech_music/music"]
    featureAndTrain(dir_paths, mt, mt, st, st, "svm_rbf", "svm_speech_music")
