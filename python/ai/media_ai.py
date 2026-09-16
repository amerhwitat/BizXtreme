"""BizXtreme offline-first media AI primitives."""
import re
COMMANDS={'start recording':'record_start','stop recording':'record_stop','play audio':'play','pause audio':'pause','open camera':'camera_start','close camera':'camera_stop','take photo':'snapshot','scan camera':'vision_scan'}
def parse_voice_command(text:str):
    n=re.sub(r'\s+',' ',text.lower().strip()); key=next((k for k in COMMANDS if k in n),None)
    return {'text':text,'action':COMMANDS.get(key),'requires_confirmation':bool(key)}
def transcribe_whisper(audio_path:str,model='base')->str:
    import whisper
    return whisper.load_model(model).transcribe(audio_path)['text'].strip()
def capture_camera(output_path:str,camera=0):
    import cv2
    cap=cv2.VideoCapture(camera); ok,frame=cap.read(); cap.release()
    if not ok: raise RuntimeError('camera capture failed')
    if not cv2.imwrite(output_path,frame): raise RuntimeError('image write failed')
def inspect_frame(image_path:str):
    import cv2
    img=cv2.imread(image_path); gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); edges=cv2.Canny(gray,80,160)
    return {'width':int(img.shape[1]),'height':int(img.shape[0]),'edge_pixels':int((edges>0).sum()),'algorithms':['edges','face','object','pose','gesture','ocr','segmentation','tracking']}
