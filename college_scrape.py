import requests
from lxml import html
import re



url_list = ["http://talk.collegeconfidential.com/stanford-university/1977925-stanford-class-of-2021-rd-results-thread.html",
       "http://talk.collegeconfidential.com/stanford-university/1977925-stanford-class-of-2021-rd-results-thread-p2.html",
       "http://talk.collegeconfidential.com/stanford-university/1833324-stanford-class-of-2020-rea-results-thread.html",
       "http://talk.collegeconfidential.com/stanford-university/1833324-stanford-class-of-2020-rea-results-thread-p2.html",
       "http://talk.collegeconfidential.com/stanford-university/1833324-stanford-class-of-2020-rea-results-thread-p3.html",
       "http://talk.collegeconfidential.com/stanford-university/1833324-stanford-class-of-2020-rea-results-thread-p4.html",
       "http://talk.collegeconfidential.com/stanford-university/1833324-stanford-class-of-2020-rea-results-thread-p5.html",
       "http://talk.collegeconfidential.com/stanford-university/1833324-stanford-class-of-2020-rea-results-thread-p6.html",
       "http://talk.collegeconfidential.com/stanford-university/1757051-official-stanford-class-of-2019-rd-results-only-thread.html",
       "http://talk.collegeconfidential.com/stanford-university/1757051-official-stanford-class-of-2019-rd-results-only-thread-p2.html",
       "http://talk.collegeconfidential.com/stanford-university/1757051-official-stanford-class-of-2019-rd-results-only-thread-p3.html",
       "http://talk.collegeconfidential.com/stanford-university/1630186-official-stanford-2018-rd-results-only-thread.html",
       "http://talk.collegeconfidential.com/stanford-university/1630186-official-stanford-2018-rd-results-only-thread-p2.html",
       "http://talk.collegeconfidential.com/stanford-university/1630186-official-stanford-2018-rd-results-only-thread-p3.html",
       ]
# for i in range(2010, 2019):
#     url.append("http://talk.collegeconfidential.com/rice-university/1754474-rice-university-class-of-" + str(i) +
#                "-results-decisions.html")
#     for j in range(2,4):
#         url.append("http://talk.collegeconfidential.com/rice-university/1754474-rice-university-class-of-" + str(i) +
#                    "-results-decisions-p" + str(j) + ".html")

def crawl_site(url):
    f = open("stanford_fixed.txt", "w")
    for u in url:
        page = requests.get(u)  # Make GET Request
        tree = html.fromstring(page.content)  # Read HTML from webpage
        begin_path = "//li[contains(@class, 'ItemComment')]"
        postings = tree.xpath(begin_path)
        id_list = []
        for posting in postings:
            id_list.append(posting.get("id"))
        for id in id_list:
            reg_path = "//li[@id='" + id + "']/div/div/div/div/text()"
            colr_text = "//li[@id='" + id + "']/div/div/div/div" + "/span/b/text()"
            colr_text2 = "//li[@id='" + id + "']/div/div/div/div" + "/b/span/text()"
            if tree.xpath(colr_text):
                print_str = ' '.join([' '.join(x.split()) for x in tree.xpath(colr_text)]) + "\n"
            elif tree.xpath(colr_text2):
                print_str = ' '.join([' '.join(x.split()) for x in tree.xpath(colr_text2)]) + "\n"
            else:
                print_str = ""
            #extra = ' '.join([' '.join(x.split()) for x in tree.xpath(reg_path)])
            extra = ' '.join(tree.xpath(reg_path))
            print_str += extra
            print(print_str)
            f.write(print_str.encode('utf8') + "\n~~~~~\n")
    f.close()

crawl_site(url_list)