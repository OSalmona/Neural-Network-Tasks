import numpy as np
from sklearn.model_selection import train_test_split


class InputHelper:
    def __init__(self):
        self.feature1 = -1
        self.feature2 = -1
        self.class1 = -1
        self.class2 = -1
        self.dataset = []
        self.read_file()
        self.training_input = []
        self.training_output = []
        self.testing_input = []
        self.testing_output = []

    def read_file(self):
        file = open("IrisData.txt", "r")
        content = file.readlines()

        temp_dataset = []
        for x in content:
            temp_dataset.append(x.split(','))
        self.dataset = np.array(temp_dataset)

    def set_data(self, feature1, feature2, class1, class2):
        self.feature1 = feature1
        self.feature2 = feature2
        self.class1 = class1
        self.class2 = class2

        c1start = self.class1 * 50 + 1
        c1end = c1start + 50

        c2start = self.class2 * 50 + 1
        c2end = c2start + 50

        x1_c1 = self.dataset[c1start:c1end, self.feature1]
        x2_c1 = self.dataset[c1start:c1end, self.feature2]
        x_c1 = np.array((x1_c1, x2_c1), dtype=float)
        x_c1 = np.transpose(x_c1)

        x1_c2 = self.dataset[c2start:c2end, self.feature1]
        x2_c2 = self.dataset[c2start:c2end, self.feature2]
        x_c2 = np.array((x1_c2, x2_c2), dtype=float)
        x_c2 = np.transpose(x_c2)

        y_c1 = np.full(50, 1)
        y_c2 = np.full(50, -1)

        x1_train, x1_test, y1_train, y1_test = train_test_split(x_c1, y_c1, test_size=0.40, shuffle=True)
        x2_train, x2_test, y2_train, y2_test = train_test_split(x_c2, y_c2, test_size=0.40, shuffle=True)

        self.training_input = np.concatenate((x1_train, x2_train))
        self.training_output = np.concatenate((y1_train, y2_train))
        self.testing_input = np.concatenate((x1_test, x2_test))
        self.testing_output = np.concatenate((y1_test, y2_test))
