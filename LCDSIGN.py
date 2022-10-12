import sys
import bpy

ob = bpy.context.object
me = ob.data

letter_count = 15
desiredtext= "8TH AVE EXP"
linesign= "A"

parsedtext = []

for letter in desiredtext:
    parsedtext.append(letter)

midcount=len(parsedtext)
whitespace=letter_count-midcount

text_edge=0

if whitespace % 2 == 0:
 text_edge=whitespace/2
else:
 text_edge=whitespace/2
 text_edge=round(text_edge)

for i in range(text_edge):
 parsedtext.insert(0, "Blank")
 

while len(parsedtext)<= letter_count:
 parsedtext.append("Blank")

for i in range(letter_count):
 if parsedtext[i]==" ":
  parsedtext[i]="Blank"
 if parsedtext[i]=="0":
  parsedtext[i]="O"
 mat = bpy.data.materials.get("LCD_Sign_{}".format(i))
 tex = bpy.data.images.get('R46_{}.png'.format(parsedtext[i]))
 if not tex:
  tex = bpy.data.images.get('R46_Blank.png')
 image_node = mat.node_tree.nodes["Image Texture"]
 image_node.image = tex

mat = bpy.data.materials.get("LCD_Sign_Line")
tex = bpy.data.images.get('R64Line_{}.png'.format(linesign))
if not tex:
 tex = bpy.data.images.get('R64Line_Blank.png')

image_node = mat.node_tree.nodes["Image Texture"]
image_node.image = tex