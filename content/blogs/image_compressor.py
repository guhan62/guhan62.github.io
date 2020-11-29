import os
import argparse
from PIL import Image

argp = argparse.ArgumentParser()
argp.add_argument("-d", "--directory", required=False,
	help="Give the absolute path of the Image directory | Default = '.'", default='.')
argp.add_argument("-f", "--file", required=False,
	help="Give the Absolute Path to Image file | Default = None", default=None)
argp.add_argument("-q", "--quality", required=False,
	help="Quality of Image | Default = 100", default=100)
argp.add_argument("-s", "--size", required=False,
	help="Size to scale image | Default = None", default=None)
args = argp.parse_args()

if args.size != None:
	args.size = args.size.split('x')

def compressor(root,file, args):
	if file.rsplit('.',1)[1] in ['jpg', 'jpeg', 'png']:
		'''if file.rsplit('.',1)[0].endswith('_proc'):
									im = Image.open(os.path.join(root, file))
									if args.size != None:
										im = im.resize(tuple(map(lambda hw: int(hw), args.size)), Image.ANTIALIAS)
									im.save(os.path.join(root,file.rsplit('.',1)[0]) + '.jpeg', quality=args.quality, format='jpeg',optimize=True)'''
		if not(file.rsplit('.',1)[0].endswith('_proc')):
			im = Image.open(os.path.join(root, file))
			if im.mode != 'RGB':
				im = im.convert('RGB')
			if args.size != None:
				im = im.resize(tuple(map(lambda hw: int(hw), args.size)), Image.ANTIALIAS)
			im.save(os.path.join(root,file.rsplit('.',1)[0]) + '_proc.jpeg', quality=int(args.quality), format='jpeg',optimize=True)

try:
	if args.file == None:
		for root,dirs, files in os.walk(args.directory):
			for file in files:
				compressor(root,file, args)
	else:
		compressor(root,args.file, args)

			
except Exception as e:
	print(e)
