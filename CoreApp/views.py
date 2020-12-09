
from django.shortcuts import render,HttpResponse
# Create your views here.
from CoreApp.models import Image
from CoreApp.fomrs import ImageForm
from PIL import Image as PILIMG
from os import path
from PIL import ImageDraw
import easyocr
from gtts import gTTS

def index(request):
    contex={}
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            tem = Image.objects.all().order_by('-id')[:1]
            contex['image_url']= tem
    form =ImageForm()
    contex['form']=form
    return render(request,'index.html',contex)

def extractImage(request):
    if request.method == 'POST':
        return index(request)
    contex = {}
    if request.method == 'GET':
        record_id=request.GET.get("id")
        # rec = Image.objects.get(id=record_id)
        rec=Image.objects.filter(id=record_id)
        rec_vals=rec.values()
        print(rec_vals)
        img_path=rec_vals[0]['imgs']
        img_name=img_path.split("/")[1]
        img_full_path = "./media/" + img_path
        img_lang=rec_vals[0]['language']
        if rec_vals[0]['content'] == "":
            if path.exists(img_full_path):
                content, res_img, res_audio = processImage(img_name, img_lang)  # [st, res_file_nm, audio_file]
                rec.update(title=img_name)
                rec.update(content=content)
                rec.update(res_img=res_img)
                rec.update(songfile=res_audio)
                rec.update()
                print("result values: ", rec.values())
                contex["result_rec"] = rec
            else:
                print("erro occurs")
                contex['file_error'] = "uploaded file may be damaged pls try again with other file....."
        else:
            print("record already exists")
            contex["result_rec"] = rec
        form = ImageForm()
        contex['form'] = form
        return render(request, 'index.html', contex)


def processImage(filename,language):
    lang = ['en']
    if language!='en':
        lang.append(language)
    print(filename,lang)
    img_full_path = "./media/Images/" + filename
    im=PILIMG.open(img_full_path)
    reader=easyocr.Reader(lang)
    result = reader.readtext(img_full_path)
    print(result)
    st = ""
    for i in result:
        st += i[1] + " "
    print(st)
    audio_file=convertAudio(st,language,filename.split(".")[0])
    res_img = draw_boxes(im, result)
    res_file_nm='/res_img/'+filename
    res_file_path='./media/res_img/'+filename
    res_img.save(res_file_path)
    return [st,res_file_nm,audio_file]

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def convertAudio(content,language,filename):
    myobj = gTTS(text=content, lang=language, slow=False)
    file=filename+".mp3"
    new_path="./media/"+file
    myobj.save(new_path)
    return file

def PDFPage(request):

    return render(request,"PDFextraction.html",None)
def audioList(request):
    all_result=Image.objects.all().values()
    return render(request,"Audio_list.html",{'aud_list':all_result})
