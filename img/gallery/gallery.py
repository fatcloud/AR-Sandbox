
import cv2
from os import listdir, makedirs
from os.path import isdir
import importlib
import sys
import shutil


# make directories
if 'display' in listdir('.'):
	shutil.rmtree('display')
makedirs('display')

if 'thumbnails' in listdir('.'):
	shutil.rmtree('thumbnails')
makedirs('thumbnails')


# define output image size (ad-hoc here)

thumbnail_shape = (650,366)
display_height  = 600.0

# prepare the html section to be paste in index.html

gallery_html = '	<section class=\"no-padding\" id=\"portfolio\">\n' + \
			   '        <div class=\"container-fluid\">\n' + \
               '			<div class=\"row no-gutter\">\n'

# process every jpg file in img/gallery folder

pic_names = [filename for filename in listdir('.') if '.jpg' in filename.lower()]

for pic_name in pic_names:
	print 'processing', pic_name, '...'

	image = cv2.imread(pic_name)

	# generate and save images be displayed in real size

	display_ratio = display_height/image.shape[0]
	display_image = cv2.resize(image, (0,0), fx=display_ratio, fy=display_ratio)
	cv2.imwrite('display/'+ pic_name, display_image, (cv2.IMWRITE_JPEG_QUALITY, 70))

	# generate and save thumbnails

	#thumbnail_ratio = max(thumbnail_shape[1]/image.shape[1], thumbnail_shape[0]/image.shape[0])
	thumbnail_image = cv2.resize(image, thumbnail_shape)
	cv2.imwrite('thumbnails/'+ pic_name, thumbnail_image, (cv2.IMWRITE_JPEG_QUALITY, 70))

	# generate the html code to be paste in index.html

	gallery_html += '                <div class=\"col-lg-4 col-sm-6\">\n' +\
					'                    <a href=\"#\" class=\"portfolio-box\">\n' +\
					'                        <img src=\"img/gallery/thumbnails/' + pic_name + '\" class=\"img-responsive\" alt=\"\">\n' +\
					'                        <div class=\"portfolio-box-caption\">\n' +\
					'                            <div class=\"portfolio-box-caption-content\">\n' +\
					'                                <div class=\"project-category text-faded\">\n' +\
					'                                    Category\n' +\
					'                                </div>\n' +\
					'                                <div class=\"project-name\">\n' +\
					'                                    Project Name\n' +\
					'                                </div>\n' +\
					'                            </div>\n' +\
					'                        </div>\n' +\
					'                    </a>\n' +\
					'                </div>\n'

# end the section in html code, save it to a txt file for further operation

gallery_html += '            </div>\n' +\
				'        </div>\n' +\
				'    </section>'

with open("gallery_code.txt", 'w') as f:
	f.write( gallery_html )

