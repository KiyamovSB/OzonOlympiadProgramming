-- this is not correct decision
def read_unical_pages():
    page_count = int(input())
    rare_pages = input().split(',')
    pages = []
    for rare_page in rare_pages:
        if rare_page.find('-') == -1:
            pages.append(int(rare_page))
        else:
            page_start, page_end = rare_page.split('-')
            page_range = list(range(int(page_start), int(page_end)+1))
            pages += page_range
    pages.append(int(page_count))
    unical_pages = set(pages)

    return(unical_pages)



unical_pages = list(read_unical_pages())

print_pages = []
for i in range(len(unical_pages)-1):
    if unical_pages[i] == unical_pages[i+1]-2:
        print_pages.append(unical_pages[i]+1)
    if unical_pages[i] == unical_pages[i+1]-3:
        print_pages.append(unical_pages[i]+1)
        print_pages.append(unical_pages[i] + 2)
    if unical_pages[i] < unical_pages[i+1]-3:
        print_pages.append(str(unical_pages[i]+1) + '-' + str(unical_pages[i+1]-1))

print(print_pages)
