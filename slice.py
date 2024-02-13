#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
import pickle

if __name__ == "__main__":
    doc = Document('./倪海厦1500医案合集.docx')

    for index, table in enumerate(doc.tables):
        data = []
        for row in table.rows:
            ele = []
            for cell in row.cells:
                if cell.text not in ele:
                    ele.append(cell.text)   # 去重
            data.append(ele)


        with open("./db/{}.txt".format(index+1), "w") as handler:
            handler.write(str(data))

        with open("./db/{}.bin".format(index+1), "ab") as pickle_handle:
            pickle.dump(data, pickle_handle)


        print("write {}".format(index+1))

