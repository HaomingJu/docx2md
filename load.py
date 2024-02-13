#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
from markdowngenerator import MarkdownGenerator
import re

# [0, 960]

if __name__ == "__main__":

    for index in range(1, 953):

        db = None
        with open("./db/{}.bin".format(index), "rb") as f:
            db = pickle.load(f)

        try:
            assert len(db[0]) == 1
            assert len(db[1]) == 4
            assert len(db[2]) == 4
        except:
            print("open db file: {0:04d}".format(index))

        tmp_item_first = db[0][0]
        tmp_item_first = tmp_item_first.replace("倪医师病案纪录", "").replace("初诊日期:", "").strip()

        item_first = "**初诊日期:** {}".format(tmp_item_first)
        item_name = "**姓名:** {}".format(db[2][0])
        item_sex = "**性别:** {}".format(db[2][1])
        item_age = "**年龄及体型:** {}".format(db[2][2])
        item_date = "**来诊日期:** {}".format(db[2][3])

        tmp_item_reason = db[3][0].replace("来诊原因:", "")
        item_reason = "**来诊原因:** {}".format(tmp_item_reason)

        tmp_item_ask = db[4][0].replace("问诊:", "")
        item_ask = "**问诊:** {}".format(tmp_item_ask)

        with MarkdownGenerator(filename="./md/倪医师病案纪录_{0:04d}.md".format(index), enable_write=False, enable_TOC=False) as doc:
            doc.addHeader(1, "倪医师病案纪录_{0:04d}".format(index))
            doc.writeTextLine(item_first)
            doc.writeTextLine(item_name)
            doc.writeTextLine(item_sex)
            doc.writeTextLine(item_age)
            doc.writeTextLine(item_date)
            doc.writeTextLine(item_reason)
            doc.addHorizontalRule()
            doc.writeTextLine(item_ask)

            for item in db[5:]:
                text_data = item[0]

                key_1 = text_data[0:2]
                if key_1 == "脉诊":
                    doc.writeTextLine("\n**脉诊:**\n{}".format(text_data[3:]))
                    continue
                elif key_1 == "望诊":
                    doc.writeTextLine("\n**望诊:**\n{}".format(text_data[3:]))
                    continue
                elif key_1 == "耳诊":
                    doc.writeTextLine("\n**耳诊:**\n{}".format(text_data[3:]))
                    continue
                elif key_1 == "诊断":
                    doc.writeTextLine("\n**诊断:**\n{}".format(text_data[3:]))
                    continue
                elif key_1 == "解说":
                    doc.writeTextLine("\n**解说:**\n{}".format(text_data[3:]))
                    continue
                elif key_1 == "备注":
                    doc.writeTextLine("\n**备注:**\n{}".format(text_data[3:]))
                    continue
                else:
                    pass


                key_2 = text_data[0:4]
                if key_2 == "特殊诊断":
                    doc.writeTextLine("\n**特殊诊断:**\n{}".format(text_data[5:]))
                    continue
                elif key_2 == "针灸处方":
                    doc.writeTextLine("\n**针灸处方:**\n{}".format(text_data[5:]))
                    continue
                elif key_2 == "中药处方":
                    doc.writeTextLine("\n**中药处方:**\n{}".format(text_data[5:]))
                    continue
                else:
                    pass

