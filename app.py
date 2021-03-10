import streamlit as st
from PIL import Image,ImageFilter,ImageEnhance
import pandas as pd
import os
from datetime import datetime
# 깃 연동 되었습니다!!

def save_uploaded_file(directory,img):
    # 1. 디렉토리가 있는지 확인하여 ,없으면 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 이제는 디렉토리가 있으니까 ,파일을 저장.

    filename=datetime.now().isoformat().replace(':','-').replace('.','-')
    img.save(directory+'/'+filename+'a.jpg')
    return st.success('Saved file : {} in {}'.format(filename+'.jpg',directory))    


def load_image(image_file):
    img=Image.open(image_file)
    return img




def main():
    st.title('이미지 업로드하는 앱')
    

    image_file_list=st.file_uploader('이미지 파일 업로드',
    type=['png','jpeg','jpg'],accept_multiple_files=True)
    print(image_file_list)

    if image_file_list is not None:
    
    # 2.각 파일을 이미지로 바꿔줘야 한다.
        image_list=[]
    
    # 2-1.모든 파일이, image_list 에 이미지로 저장됨.
        for file in image_file_list:
            img=load_image(file)
            image_list.append(img)

    # 3.이미지를 화면에 확인해 본다.
        # for img in image_list:
        #     st.image(img)
        

        option_list=[
            'Show Image',
            'Rotate Image',
            'Create Thumbnail',
            'Crop Image',
            'Merge Images',
            'Flip Image',
            'Black & White',
            'Filters-Sharpen',
            'Filters-Edge Enhance',
            'Contrast Image',]
        option=st.selectbox('옵션을 선택하세요.',option_list)

        if option =='Show Image':
            for img in image_list:
                st.image(img)

            directory=st.text_input('파일 경로 입력')
            if st.button('파일 저장'):
                for img in image_list:
                    save_uploaded_file(directory,img)




        elif option =='Rotate Image':
            
            # 1.유저가 입력
            degree=st.number_input('각도입력',0,360)
            
            # 2.모든 이미지를 돌린다.
            transformed_img_list=[]
            for img in image_list:
                rotated_img=img.rotate(degree)
                # rotated_img.save('data/rot.jpg')
                st.image(rotated_img)
                transformed_img_list.append(rotated_img)
            directory=st.text_input('파일 경로 입력')
            if st.button('파일 저장'):
                # 3.파일 저장
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)


                    
            
        elif option =='Create Thumbnail':
#  이미지의 사이즈를 알아야겠다.



            print(img.size)
            width=st.number_input('width 입력',1,100)
            height=st.number_input('height 입력',1,100)
            size=(width,height)
            transformed_img_list=[]
            for img in image_list:
                thumb_img=img.thumbnail(size)
                st.image(img)
                transformed_img_list.append(img)

            #저장은 여기서
            directory=st.text_input('파일 경로 입력')
            if st.button('파일 저장'):
                # 3.파일 저장
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)
 


        # elif option =='Crop Image':
        #     # 왼쪽 위부분 부터 시작해서, 너비와 깊이만큼 잘라라
        #     # 왼쪽 위부분 좌표 (50,100)
        #     # 너비 X축으로 ,깊이 y축으로 (200,200) 
        #     start_x=st.number_input('시작 x 좌표',0,img.size[0]-1)
        #     start_y=st.number_input('시작 y 좌표',0,img.size[1]-1)
            
        #     max_width=img.size[0]-start_x
        #     max_height=img.size[1]-start_y

        #     width=st.number_input('width 입력',1,max_width)
        #     height=st.number_input('height 입력',1,max_height)
            
        #     st.image(img)
        #     box =(start_x,start_y,start_x+width,start_y+height)
        #     cropped_img=img.crop(box)
        #     st.image(cropped_img)



        # elif option =='Merge Images':
        #     merge_file=st.file_uploader('uploaded_file',
        #     type=['png','jpg','jpeg'],key='merge')

        #     if merge_file is not None:
        #         merge_img=load_image(merge_file)

        #         start_x=st.number_input('시작 x 좌표',0,img.size[0]-1)
        #         start_y=st.number_input('시작 y 좌표',0,img.size[1]-1)     
        #         position=(start_x,start_y)
        #         img.paste(merge_img,position)
        #         st.image(img)



        elif option =='Flip Image':
            flip=st.radio('반전을 선택하시오',['상하반전','좌우반전'])
            if flip=='상하반전':
                transformed_img_list=[]
                for img in image_list:
                    flipped_img =img.transpose(Image.FLIP_TOP_BOTTOM)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
            elif flip=='좌우반전':
                transformed_img_list=[]
                for img in image_list:
                    flipped_img =img.transpose(Image.FLIP_LEFT_RIGHT)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)

            directory=st.text_input('파일 경로 입력')
            if st.button('파일 저장'):
                # 3.파일 저장
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)



            


        elif option =='Black & White':
            status=st.radio('색 변경',['Color','Gray Scale','Black & White'])
            if status=='Color':
                transformed_img_list=[]
                for img in image_list:
                    color_img=img.convert('RGB')
                    st.image(color_img)
                    transformed_img_list.append(color_img)
            elif status=='Gray Scale':
                transformed_img_list=[]
                for img in image_list:
                    color_img=img.convert('L')
                    st.image(color_img)
                    transformed_img_list.append(color_img)
            elif status=='Black & White':
                transformed_img_list=[]
                for img in image_list:
                    color_img=img.convert('1')
                    st.image(color_img)
                    transformed_img_list.append(color_img)
            
            directory=st.text_input('파일 경로 입력')
            if st.button('파일 저장'):
                # 3.파일 저장
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)


    




        elif option =='Filters-Sharpen':
            transformed_img_list=[]
            for img in image_list:
                sharp_img=img.filter(ImageFilter.SHARPEN)
                st.image(sharp_img)
                transformed_img_list.append(sharp_img)

            directory=st.text_input('파일 경로 입력')
            if st.button('파일 저장'):
                 # 3.파일 저장
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)

        # elif option =='Filters-Edge Enhance':
        #     edge_img=img.filter(ImageFilter.EDGE_ENHANCE)
        #     st.image(edge_img)

        # elif option =='Contrast Image':
        #     contrast_img=ImageEnhance.Contrast(img).enhance(2)
        #     st.image(contrast_img)
        
        # 1. 이미지를 내가 마음대로 올릴 수 있어야 한다.
        # (이미지는 1장)

        # 2.하드코딩된 코드를 유저한테 입력받아서 처리할수 있도록 바꾼다.





if __name__=='__main__':
    main()
