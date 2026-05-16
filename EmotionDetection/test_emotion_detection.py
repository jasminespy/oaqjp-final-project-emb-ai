from EmotionDetection.EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        print('Joy test:', result_1)

        # Test case for anger
        result_2 = emotion_detector('I am really mad about this')
        print('Anger test:', result_2)

        # Test case for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        print('Disgust test:', result_3)

        # Test case for sadness
        result_4 = emotion_detector('I am so sad about this')
        print('Sadness test:', result_4)

        # Test case for fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        print('Fear test:', result_5)

if __name__ == '__main__':
    unittest.main()
    