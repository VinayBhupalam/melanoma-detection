from flask import render_template
from flask import Flask ,request
import os
import tensorflow as tf
import numpy as np
import skimage.io as sk
from skimage.transform import rescale, resize
import efficientnet.tfkeras

MODEL_DIR = "models"
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), "static")
DIMENSIONS = (224, 224)
# base_model = efn.EfficientNetB4(weights='imagenet', include_top=False,
#                                 input_shape=(*DIMENSIONS, 3))
#
# input_dim = (*DIMENSIONS, 3)
# input_tensor = L.Input(input_dim)
# curr_output = base_model(input_tensor)
# curr_output = L.GlobalAveragePooling2D()(curr_output)
# output = L.Dense(1, activation='sigmoid')(curr_output)
# model = Model(input_tensor, output)
# opt = tf.keras.optimizers.Adam(learning_rate=0.00001)
# model.compile(
#     optimizer=opt,
#     loss=tf.keras.losses.binary_crossentropy,
#     metrics=[tf.metrics.AUC()]
# )
#
#
# model.save("MODEL.h5")




@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        image_file = request.files['image']
        image_location = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_location)
        pred = predict(image_location, DIMENSIONS)
        print(pred)
        return render_template("index.html", prediction=pred[0], image_loc=image_file.filename)
    return render_template("index.html", image_loc=None)


def predict(image_path, dimensions):
    final_pred = 0
    # img = cv2.imread(image_path)
    # img = cv2.resize(img, dimensions)

    img = sk.imread(image_path, True)
    img = resize(img, (*dimensions, 3))
    img = np.expand_dims(img, axis=0)
    print("Shape of the image is")
    print(img.shape)
    img = tf.cast(img, tf.float32)
    MODEL = tf.keras.models.load_model('MODEL.h5')
    # model = get_model(dimensions)
    files = os.listdir(MODEL_DIR)
    num_models = len(files)
    for file in files:
        MODEL.load_weights(os.path.join(MODEL_DIR, file))
        predictions = MODEL.predict(img, verbose=1)
        final_pred = final_pred + predictions

    final_pred = final_pred/num_models
    return final_pred


if __name__ == '__main__':
    app.run()
