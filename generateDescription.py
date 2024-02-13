#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

if __name__ == "__main__":
    data = {
            "metadata":{
                "dc:title":"倪海厦病案合集(952例)",
                "dc:creator":"恩典之家",
                "dc:language":"en-US",
                "dc:identifier":"mark2epub-sample",
                "dc:source":"",
                "meta":"",
                "dc:date":"2023-01-01",
                "dc:publisher":"",
                "dc:contributor":"",
                "dc:rights":"",
                "dc:description":"",
                "dc:subject":""
                },
            "cover_image":"",
            "default_css":["code_styles.css","general.css"],
            "chapters":[
                ]
            }


    for index in range(1, 953):
        data["chapters"].append({"markdown":"倪医师病案纪录_{0:04d}.md".format(index),"css":""})

    str_json = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    with open("./md/description.json", "w") as description:
        description.write(str_json)
