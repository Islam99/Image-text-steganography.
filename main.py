import cv2


def char_generator(message):
  for c in message:
    yield ord(c)

def get_image(image_location):
  img = cv2.imread(image_location)
  return img

def gcd(x, y):
  while(y):
    x, y = y, x % y

  return x

def encode_image(image_location, msg):
  img = cv2.imread(image_location,  cv2.IMREAD_COLOR)
  height, width,x = img.shape
  msg_gen = char_generator(msg)
  pattern = gcd(height, width)
  pattern = 5
  for i in range(height):
    for j in range(width):
      if (i+1 * j+1) % pattern == 0:
        try:
          print(i,j)
          img[i-1][j-1][0] = next(msg_gen)
        except StopIteration:
          img[i-1][j-1][0] = 0
          return img

def decode_image(img_loc):
  img = cv2.imread(img_loc,  cv2.IMREAD_COLOR)
  height, width,x = img.shape
  pattern = gcd(height, width)
  pattern = 5
  message = ''
  for i in range(height):
    for j in range(width):
      if (i-1 * j-1) % pattern == 0:
        if img[i-1][j-1][0] != 0:
          message = message + chr(img[i-1][j-1][0])
        else:
          return message
x = encode_image('COLQD5bU8AEpVIp.png','aaaaaaaaaaaaa')
cv2.imwrite('encode.png',x)
print(decode_image('encode.png'))