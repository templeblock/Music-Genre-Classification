import Feature
import numpy as np
#from scikits.audiolab import wavread
import struct
import tools

class Feature_FreqDom(Feature.Feature):

    """
    Implementation of Feature.

    USES: amplitude vs time data.
    """

    def __init__(self, data, useInitialize=True):
        Feature.Feature.__init__(self, data, useInitialize)

    def initialize(self, data):
        self.freqData = tools.intoFrequencyDomain(tools.intoMono(data))
         
    def serialize(self):
        """
        Format:
        <length>:::<packed data>
        """

        return tools.packSongArray(self.freqData)

    @staticmethod
    def unserialize(serialized):
        newFeature = Feature_FreqDom(None, False)
        newFeature.freqData = tools.unpackSongArray(serialized)
        return newFeature

class Feature_Centroid(Feature.Feature):

    """
    Implementation of Feature Centroid function.

    USES: amplitude vs time data.
    """

    def __init__(self, data, useInitialize=True):
        Feature.Feature.__init__(self, data, useInitialize)

    def initialize(self, data):
        self.freqData = tools.intoFrequencyDomain(tools.intoMono(data))

        

        #for bin in self.freqData:

         
    def serialize(self):
        """
        Format:
        <length>:::<packed data>
        """

        return tools.packSongArray(self.freqData)

    @staticmethod
    def unserialize(serialized):
        newFeature = Feature_FreqDom(None, False)
        newFeature.freqData = tools.unpackSongArray(serialized)
        return newFeature



import sys
def main(argv):

    # ampData, fs, enc = wavread("/home/damian/Music-Genre-Classification/FingerprintGenerator/TestSongs/Rap/Eminem-Stan.wav")

    # feature1 = Feature_FreqDom(ampData[800000:800010])



    # print feature1.freqData
    # print ""
    # print feature1.unserialize(feature1.serialize()).freqData


    actualData = [[0.0426635742188, 0.0431213378906],[0.0339965820312, 0.034423828125],[0.0144653320312, 0.014892578125],[-0.00677490234375, -0.00634765625],[-0.0119018554688, -0.011474609375],[0.00283813476562, 0.0032958984375],[0.0173645019531, 0.0177917480469],[0.0170288085938, 0.0174560546875],[0.0120849609375, 0.0125122070312],[0.00521850585938, 0.00567626953125]] 


    TEH_Feature = Feature_FreqDom(actualData)
    print TEH_Feature.freqData


if __name__ == "__main__":
    main(sys.argv[1:])

