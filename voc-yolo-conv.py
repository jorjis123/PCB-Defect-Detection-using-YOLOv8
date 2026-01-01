import os, random, shutil
import xml.etree.ElementTree as ET

voc_img_dir = "/content/VOC_PCB/JPEGImages"
voc_ann_dir = "/content/VOC_PCB/Annotations"

imgs = [f for f in os.listdir(voc_img_dir) if f.endswith(".jpg")]
random.shuffle(imgs)

split = int(0.8 * len(imgs))
train_imgs = imgs[:split]
val_imgs = imgs[split:]

def convert(w, h, box):
    return (
        ((box[0]+box[1])/2)/w,
        ((box[2]+box[3])/2)/h,
        (box[1]-box[0])/w,
        (box[3]-box[2])/h
    )

def process(images, split_name):
    for img in images:
        xml = os.path.join(voc_ann_dir, img.replace(".jpg",".xml"))
        tree = ET.parse(xml)
        root = tree.getroot()

        size = root.find("size")
        w = int(size.find("width").text)
        h = int(size.find("height").text)

        label_path = f"/content/pcb_yolo/labels/{split_name}/{img.replace('.jpg','.txt')}"
        with open(label_path,"w") as f:
            for obj in root.findall("object"):
                cls = obj.find("name").text
                if cls not in classes: continue
                cls_id = classes.index(cls)
                b = obj.find("bndbox")
                box = (
                    float(b.find("xmin").text),
                    float(b.find("xmax").text),
                    float(b.find("ymin").text),
                    float(b.find("ymax").text)
                )
                bb = convert(w,h,box)
                f.write(f"{cls_id} {' '.join(map(str,bb))}\n")

        shutil.copy(
            os.path.join(voc_img_dir,img),
            f"/content/pcb_yolo/images/{split_name}/{img}"
        )

process(train_imgs,"train")
process(val_imgs,"val")

print("✅ VOC → YOLO conversion completed")