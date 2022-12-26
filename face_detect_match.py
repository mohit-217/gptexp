import face_recognition
import argparse
import time
import cv2
class facematch:
    def __init__(self,sample_document_path,sample_image):
        self.sample_doc= face_recognition.load_image_file(sample_document_path)
        self.sample_img= face_recognition.load_image_file(sample_image)
    def face_match(self):
        sample_doc_encoding = face_recognition.face_encodings(self.sample_doc)[0]
        sampler_img_encoding= face_recognition.face_encodings(self.sample_img)[0]
        sample_doc=[sample_doc_encoding]
        results = face_recognition.compare_faces(sample_doc, sampler_img_encoding)
        return results

# if __name__=="__main__":
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--sample_document',type=str,required=True)
#     parser.add_argument('--sample_img',type=str,required=True)
#     args=parser.parse_args()
#     obj=facematch()
#     s_t=time.time()
#     obj.face_match()
    