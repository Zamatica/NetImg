import png


class ImageWriter:
    def __init__(self, image_config):
        self.set_constants(image_config)

        self.reset_frame()

        self.current_image = 0


    def set_constants(self, image_config):
        self.FRAME_SIZE_X = image_config['FRAME_SIZE_X']
        self.FRAME_SIZE_Y = image_config['FRAME_SIZE_Y']
        self.PIXEL_STYLE = image_config['PIXEL_STYLE']
        self.PIXELS_IN_FRAME = self.FRAME_SIZE_X * 3 if self.PIXEL_STYLE == 'RGB' else self.FRAME_SIZE_X


    def reset_frame(self):
        self.frame = []

        self.current_row = 0

        for _ in range(self.FRAME_SIZE_Y):
            self.frame.append([])


    def callback(self, bytedata):
        pixels = [b for b in bytedata[0]]

        for x in pixels:
            if (len(self.frame[self.current_row]) < self.PIXELS_IN_FRAME):
                self.frame[self.current_row].append(x)
            else:
                self.current_row += 1

                if (self.current_row >= self.FRAME_SIZE_Y):
                    self.write_image()
                    self.current_row = 0
                    self.reset_frame()


    def write_image(self):
        filename = 'output/out-' + str(self.current_image) + '.png'
        png.from_array(self.frame, self.PIXEL_STYLE).save(filename)
        self.current_image += 1

