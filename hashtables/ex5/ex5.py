# Your code here


def finder(files, queries):
    result = []
    filesDic = {}
    files2Dic = {}
    queriesDic = {i: i for i in queries}

    # for file in filesDic:
    #     for query in queriesDic:
    #         if query in file and file not in result:
    #             result.append(file)
    # for file in files:
    #     if file.split("/")[-1] not in filesDic:
    #         filesDic[file.split("/")[-1]] = file
    #     else:
    #         files2Dic[file.split("/")[-1]] = file
    #     print(filesDic, files2Dic)
    #     for query in queriesDic:
    #         if query in filesDic[query]:
    #             print(query, filesDic[query])
    #             result.append(file)
    #             break
    #         elif query in files2Dic[query]:
    #             # and (filesDic[query] not in result):
    #             print(query, files2Dic[query])
    #             result.append(file)
    #             break

    # for query in queries:
    #     for file in files:
    #         if query in file:
    #             result.append(file)
    #             break
    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/bar',
        '/bin/foo',
        '/usr/bin/baz',
        '/usr/bin2/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
