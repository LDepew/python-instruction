from ast import Import
import webbrowser

try:
    from googlesearch import search
except ImportError:
    print("No module named google")

selection = input("Youtube or Google: ")

if selection == "Google" or selection == "google":
    query = input("Enter keyword(s) to search: ")

    option = input("Open Google or View List: ")
    if option == "Open Google" or option == "open google":
        webbrowser.open("https://www.google.com/search?q=" + query + "&sxsrf=ALiCzsZNnUtCuzheJ4w8C5qjGrcmyqUd9w%3A1666993162019&ei=CkxcY9dUiNnk2g-e9KOABA&ved=0ahUKEwjXgY-68YP7AhWILFkFHR76CEAQ4dUDCBA&uact=5&oq=" + query + "&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCC4QsQMQgwEQkQIyBAgAEEMyCAgAELEDEJECMgQIABBDMgQILhBDMgsILhCxAxCDARDUAjIECC4QQzIECAAQQzIECC4QQzIOCC4QgAQQsQMQgwEQ1AI6BAgjECc6BQgAEJECOhEILhCABBCxAxCDARDHARDRAzoFCAAQgAQ6CwguEIAEELEDEIMBOgsILhCABBDHARCvAToFCC4QgAQ6CgguELEDEIMBEEM6CAguELEDEIMBOgsIABCABBCxAxCDAToICAAQsQMQgwE6DgguELEDEIMBEMcBENEDOgoILhDHARDRAxBDOgsILhCABBCxAxDUAjoICC4QgAQQsQNKBAhNGAFKBAhBGABKBAhGGABQAFj-A2DbCGgAcAF4AIABVYgBiQOSAQE1mAEAoAEBwAEB&sclient=gws-wiz-serp")

    elif option == "View List" or option == "view list":
        for j in search(query, tld="co.uk", num=10, stop=10, pause=2):
            print(j)

    

elif selection == "Youtube" or selection == "youtube":
    query = input("Enter keyword(s) to search: ")

    webbrowser.open("https://www.youtube.com/results?search_query=" + query)